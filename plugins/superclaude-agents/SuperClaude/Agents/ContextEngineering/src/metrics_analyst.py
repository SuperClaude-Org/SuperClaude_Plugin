"""
Metrics Analyst Agent Implementation

Handles performance evaluation, optimization, and metrics tracking.
Implements Context Engineering "Write Context" and "Compress Context" strategies.
"""

import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, List, Optional
import json


class MetricsAnalyst:
    """
    Performance evaluation and optimization specialist.
    
    Responsibilities:
    - Track command execution metrics
    - Generate performance reports
    - Run A/B tests
    - Provide optimization recommendations
    """
    
    def __init__(self, db_path: Optional[Path] = None):
        """
        Initialize Metrics Analyst.
        
        Args:
            db_path: Path to metrics database. Defaults to ~/.claude/metrics/metrics.db
        """
        if db_path is None:
            self.db_path = Path.home() / ".claude" / "metrics" / "metrics.db"
        else:
            self.db_path = Path(db_path)
        
        # Create directory if it doesn't exist
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize database
        self._init_database()
        
        # Session tracking
        self.session_id = f"sess_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.session_metrics = {
            "commands_executed": 0,
            "cumulative_tokens": 0,
            "cumulative_latency_ms": 0,
            "quality_scores": [],
            "agent_activations": {}
        }
    
    def _init_database(self):
        """Initialize SQLite database with schema"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Command metrics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS command_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME NOT NULL,
                command VARCHAR(50) NOT NULL,
                tokens_used INTEGER NOT NULL,
                latency_ms INTEGER NOT NULL,
                quality_score REAL CHECK(quality_score >= 0 AND quality_score <= 1),
                agent_activated VARCHAR(100),
                user_rating INTEGER CHECK(user_rating >= 1 AND user_rating <= 5),
                session_id VARCHAR(50),
                cost_usd REAL,
                context_size INTEGER,
                compression_ratio REAL
            )
        """)
        
        # Add indexes
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_timestamp 
            ON command_metrics(timestamp)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_command 
            ON command_metrics(command)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_session 
            ON command_metrics(session_id)
        """)
        
        # Agent performance table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agent_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_name VARCHAR(50) NOT NULL UNIQUE,
                activation_count INTEGER DEFAULT 0,
                avg_quality REAL,
                avg_tokens INTEGER,
                success_rate REAL,
                last_activated DATETIME,
                total_cost_usd REAL
            )
        """)
        
        # Optimization experiments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS optimization_experiments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                experiment_name VARCHAR(100) NOT NULL,
                variant_a TEXT,
                variant_b TEXT,
                start_date DATETIME,
                end_date DATETIME,
                winner VARCHAR(10),
                improvement_pct REAL,
                statistical_significance REAL,
                p_value REAL
            )
        """)
        
        conn.commit()
        conn.close()
    
    def record_execution(self, metrics: Dict[str, Any]) -> None:
        """
        Record command execution metrics.
        
        Args:
            metrics: Dictionary with execution data:
                - command (str): Command name
                - tokens_used (int): Number of tokens consumed
                - latency_ms (int): Execution time in milliseconds
                - quality_score (float): Quality assessment (0-1)
                - agent_activated (str, optional): Agent name
                - user_rating (int, optional): User rating (1-5)
                - cost_usd (float, optional): Estimated cost
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO command_metrics 
            (timestamp, command, tokens_used, latency_ms, quality_score,
             agent_activated, user_rating, session_id, cost_usd)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().isoformat(),
            metrics['command'],
            metrics['tokens_used'],
            metrics['latency_ms'],
            metrics.get('quality_score', 0.0),
            metrics.get('agent_activated'),
            metrics.get('user_rating'),
            self.session_id,
            metrics.get('cost_usd', metrics['tokens_used'] * 0.000005)  # Estimate
        ))
        
        conn.commit()
        conn.close()
        
        # Update session metrics
        self.session_metrics['commands_executed'] += 1
        self.session_metrics['cumulative_tokens'] += metrics['tokens_used']
        self.session_metrics['cumulative_latency_ms'] += metrics['latency_ms']
        if 'quality_score' in metrics:
            self.session_metrics['quality_scores'].append(metrics['quality_score'])
        
        # Update agent activation count
        if 'agent_activated' in metrics:
            agent = metrics['agent_activated']
            self.session_metrics['agent_activations'][agent] = \
                self.session_metrics['agent_activations'].get(agent, 0) + 1
    
    def generate_report(
        self,
        timeframe: str = "week",
        compare_previous: bool = False
    ) -> Dict[str, Any]:
        """
        Generate performance report.
        
        Args:
            timeframe: One of 'session', 'today', 'week', 'month', 'all'
            compare_previous: Include comparison with previous period
        
        Returns:
            Dictionary with report data
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Calculate time range
        now = datetime.now()
        if timeframe == "session":
            start_date = None  # Use session_id filter
        elif timeframe == "today":
            start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif timeframe == "week":
            start_date = now - timedelta(days=7)
        elif timeframe == "month":
            start_date = now - timedelta(days=30)
        else:  # all
            start_date = datetime(1970, 1, 1)
        
        # Build query
        if timeframe == "session":
            query = """
                SELECT 
                    COUNT(*) as total_commands,
                    AVG(tokens_used) as avg_tokens,
                    AVG(latency_ms) as avg_latency,
                    AVG(quality_score) as avg_quality,
                    SUM(cost_usd) as total_cost
                FROM command_metrics
                WHERE session_id = ?
            """
            cursor.execute(query, (self.session_id,))
        else:
            query = """
                SELECT 
                    COUNT(*) as total_commands,
                    AVG(tokens_used) as avg_tokens,
                    AVG(latency_ms) as avg_latency,
                    AVG(quality_score) as avg_quality,
                    SUM(cost_usd) as total_cost
                FROM command_metrics
                WHERE timestamp >= ?
            """
            cursor.execute(query, (start_date.isoformat(),))
        
        row = cursor.fetchone()
        
        report = {
            "timeframe": timeframe,
            "period": {
                "start": start_date.isoformat() if start_date else self.session_id,
                "end": now.isoformat()
            },
            "metrics": {
                "total_commands": row[0] or 0,
                "avg_tokens_per_command": round(row[1] or 0, 2),
                "avg_latency_ms": round(row[2] or 0, 2),
                "avg_quality_score": round(row[3] or 0, 3),
                "total_cost_usd": round(row[4] or 0, 4)
            }
        }
        
        # Get top performing commands
        if timeframe == "session":
            cursor.execute("""
                SELECT command, AVG(quality_score) as avg_quality, AVG(tokens_used) as avg_tokens
                FROM command_metrics
                WHERE session_id = ?
                GROUP BY command
                ORDER BY avg_quality DESC
                LIMIT 5
            """, (self.session_id,))
        else:
            cursor.execute("""
                SELECT command, AVG(quality_score) as avg_quality, AVG(tokens_used) as avg_tokens
                FROM command_metrics
                WHERE timestamp >= ?
                GROUP BY command
                ORDER BY avg_quality DESC
                LIMIT 5
            """, (start_date.isoformat(),))
        
        report["top_commands"] = [
            {
                "command": row[0],
                "avg_quality": round(row[1], 3),
                "avg_tokens": round(row[2], 0)
            }
            for row in cursor.fetchall()
        ]
        
        conn.close()
        
        return report
    
    def get_optimization_opportunities(self) -> List[Dict[str, Any]]:
        """
        Identify optimization opportunities based on data.
        
        Returns:
            List of optimization suggestions
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        opportunities = []
        
        # Find commands with high token usage but low quality
        cursor.execute("""
            SELECT command, AVG(tokens_used) as avg_tokens, AVG(quality_score) as avg_quality
            FROM command_metrics
            WHERE timestamp >= datetime('now', '-7 days')
            GROUP BY command
            HAVING avg_tokens > 3000 AND avg_quality < 0.8
            ORDER BY avg_tokens DESC
            LIMIT 3
        """)
        
        for row in cursor.fetchall():
            opportunities.append({
                "impact": "high",
                "type": "token_optimization",
                "command": row[0],
                "current_tokens": round(row[1], 0),
                "current_quality": round(row[2], 3),
                "recommendation": f"Compress {row[0]} output to reduce tokens while maintaining quality"
            })
        
        # Find commands with high latency
        cursor.execute("""
            SELECT command, AVG(latency_ms) as avg_latency
            FROM command_metrics
            WHERE timestamp >= datetime('now', '-7 days')
            GROUP BY command
            HAVING avg_latency > 3000
            ORDER BY avg_latency DESC
            LIMIT 3
        """)
        
        for row in cursor.fetchall():
            opportunities.append({
                "impact": "medium",
                "type": "latency_optimization",
                "command": row[0],
                "current_latency_ms": round(row[1], 0),
                "recommendation": f"Cache common patterns in {row[0]} to reduce latency"
            })
        
        conn.close()
        
        return opportunities
    
    def export_data(self, format: str = "json", output_path: Optional[Path] = None) -> str:
        """
        Export metrics data.
        
        Args:
            format: Export format ('json' or 'csv')
            output_path: Output file path (optional)
        
        Returns:
            Exported data as string or file path
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT timestamp, command, tokens_used, latency_ms, quality_score, 
                   agent_activated, session_id, cost_usd
            FROM command_metrics
            ORDER BY timestamp DESC
            LIMIT 1000
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        if format == "json":
            data = [
                {
                    "timestamp": row[0],
                    "command": row[1],
                    "tokens_used": row[2],
                    "latency_ms": row[3],
                    "quality_score": row[4],
                    "agent_activated": row[5],
                    "session_id": row[6],
                    "cost_usd": row[7]
                }
                for row in rows
            ]
            
            result = json.dumps(data, indent=2)
            
            if output_path:
                output_path.write_text(result)
                return str(output_path)
            
            return result
        
        elif format == "csv":
            import csv
            import io
            
            output = io.StringIO()
            writer = csv.writer(output)
            
            # Write header
            writer.writerow([
                "timestamp", "command", "tokens_used", "latency_ms",
                "quality_score", "agent_activated", "session_id", "cost_usd"
            ])
            
            # Write data
            writer.writerows(rows)
            
            result = output.getvalue()
            output.close()
            
            if output_path:
                output_path.write_text(result)
                return str(output_path)
            
            return result
        
        raise ValueError(f"Unsupported format: {format}")


# Example usage
if __name__ == "__main__":
    analyst = MetricsAnalyst()
    
    # Record a command execution
    analyst.record_execution({
        "command": "/sc:implement",
        "tokens_used": 3421,
        "latency_ms": 2100,
        "quality_score": 0.92,
        "agent_activated": "backend-engineer"
    })
    
    # Generate report
    report = analyst.generate_report(timeframe="week")
    print(json.dumps(report, indent=2))
    
    # Get optimization opportunities
    opportunities = analyst.get_optimization_opportunities()
    for opp in opportunities:
        print(f"[{opp['impact'].upper()}] {opp['recommendation']}")
