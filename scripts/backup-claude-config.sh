#!/bin/bash
#
# SuperClaude Plugin - Automated Backup Script
#
# This script safely backs up your Claude Code configuration before
# installing the SuperClaude plugin.
#
# Usage:
#   ./backup-claude-config.sh [backup-directory]
#
# If no directory is specified, creates backup in ~/claude-backups/
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Emoji support
CHECKMARK="✅"
WARNING="⚠️ "
ERROR="❌"
INFO="ℹ️ "
PACKAGE="📦"
FOLDER="📂"
LOCK="🔒"

echo ""
echo "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo "${BLUE}  SuperClaude Plugin - Configuration Backup Tool${NC}"
echo "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo ""

# Function to print colored messages
print_success() {
    echo -e "${GREEN}${CHECKMARK} $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}${WARNING}$1${NC}"
}

print_error() {
    echo -e "${RED}${ERROR} $1${NC}"
}

print_info() {
    echo -e "${BLUE}${INFO}$1${NC}"
}

# Check if running in interactive mode
if [ -t 0 ]; then
    INTERACTIVE=true
else
    INTERACTIVE=false
fi

# Determine backup directory
if [ -n "$1" ]; then
    BACKUP_BASE_DIR="$1"
else
    BACKUP_BASE_DIR="$HOME/claude-backups"
fi

# Create timestamped backup directory
TIMESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
BACKUP_DIR="$BACKUP_BASE_DIR/backup-$TIMESTAMP"

# Create backup directory
mkdir -p "$BACKUP_DIR"
if [ $? -eq 0 ]; then
    print_success "Created backup directory: $BACKUP_DIR"
else
    print_error "Failed to create backup directory"
    exit 1
fi

echo ""
echo "${PACKAGE} Scanning for Claude Code configuration files..."
echo ""

# Track what we backed up
BACKED_UP_COUNT=0
TOTAL_SIZE=0

# Function to backup a file
backup_file() {
    local source_file="$1"
    local dest_name="$2"

    if [ -f "$source_file" ]; then
        cp "$source_file" "$BACKUP_DIR/$dest_name"
        if [ $? -eq 0 ]; then
            local size=$(stat -f%z "$source_file" 2>/dev/null || stat -c%s "$source_file" 2>/dev/null)
            local size_kb=$(( size / 1024 ))
            print_success "Backed up: $dest_name (${size_kb} KB)"
            BACKED_UP_COUNT=$((BACKED_UP_COUNT + 1))
            TOTAL_SIZE=$((TOTAL_SIZE + size))
        else
            print_warning "Failed to backup: $dest_name"
        fi
    else
        print_info "Not found: $source_file (skipping)"
    fi
}

# Function to backup a directory
backup_directory() {
    local source_dir="$1"
    local dest_name="$2"

    if [ -d "$source_dir" ]; then
        cp -r "$source_dir" "$BACKUP_DIR/$dest_name"
        if [ $? -eq 0 ]; then
            local size=$(du -sk "$source_dir" | cut -f1)
            print_success "Backed up: $dest_name/ (${size} KB)"
            BACKED_UP_COUNT=$((BACKED_UP_COUNT + 1))
            TOTAL_SIZE=$((TOTAL_SIZE + size * 1024))
        else
            print_warning "Failed to backup: $dest_name/"
        fi
    else
        print_info "Not found: $source_dir (skipping)"
    fi
}

# Backup global Claude Code settings
echo "${FOLDER} Global Settings:"
backup_file "$HOME/.claude/settings.local.json" "settings.local.json"
backup_file "$HOME/.claude/settings.json" "settings.json"
backup_file "$HOME/.claude/CLAUDE.md" "CLAUDE.md"
backup_file "$HOME/.claude/.credentials.json" ".credentials.json"

echo ""
echo "${FOLDER} Project-Specific Settings (current directory):"
backup_file "./.mcp.json" "project-mcp.json"
backup_file "./.claude.json" "project-claude.json"
backup_directory "./.claude" "project-dot-claude"

echo ""
echo "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo ""

# Calculate total size in human-readable format
if [ $TOTAL_SIZE -gt 1048576 ]; then
    SIZE_MB=$((TOTAL_SIZE / 1048576))
    SIZE_DISPLAY="${SIZE_MB} MB"
elif [ $TOTAL_SIZE -gt 1024 ]; then
    SIZE_KB=$((TOTAL_SIZE / 1024))
    SIZE_DISPLAY="${SIZE_KB} KB"
else
    SIZE_DISPLAY="${TOTAL_SIZE} bytes"
fi

# Create backup manifest
cat > "$BACKUP_DIR/BACKUP_MANIFEST.txt" << EOF
SuperClaude Plugin - Backup Manifest
=====================================

Backup Date: $(date '+%Y-%m-%d %H:%M:%S')
Backup Location: $BACKUP_DIR
Files Backed Up: $BACKED_UP_COUNT
Total Size: $SIZE_DISPLAY

Files:
$(ls -lh "$BACKUP_DIR" | tail -n +2)

Restore Instructions:
====================

To restore this backup:

# Global settings
cp "$BACKUP_DIR/settings.local.json" ~/.claude/
cp "$BACKUP_DIR/CLAUDE.md" ~/.claude/
cp "$BACKUP_DIR/.credentials.json" ~/.claude/

# Project settings (if exists)
cp "$BACKUP_DIR/project-mcp.json" ./.mcp.json
cp -r "$BACKUP_DIR/project-dot-claude" ./.claude

Then restart Claude Code.

EOF

print_success "Created backup manifest: BACKUP_MANIFEST.txt"

echo ""
echo "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo "${GREEN}${CHECKMARK} Backup Complete!${NC}"
echo "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo "${PACKAGE} Summary:"
echo "  ${CHECKMARK} Files backed up: $BACKED_UP_COUNT"
echo "  ${CHECKMARK} Total size: $SIZE_DISPLAY"
echo "  ${FOLDER} Location: $BACKUP_DIR"
echo ""
echo "${LOCK} Next Steps:"
echo ""
echo "  1. Verify backup:"
echo "     ${BLUE}ls -lh \"$BACKUP_DIR\"${NC}"
echo ""
echo "  2. Install SuperClaude plugin:"
echo "     ${BLUE}/plugin marketplace add SuperClaude-Org/SuperClaude_Plugin${NC}"
echo "     ${BLUE}/plugin install sc@superclaude-official${NC}"
echo ""
echo "  3. If you need to restore:"
echo "     ${BLUE}cat \"$BACKUP_DIR/BACKUP_MANIFEST.txt\"${NC}"
echo ""
echo "${INFO} Keep this backup for at least 1 week after installation."
echo ""

# Save backup location for easy access
echo "$BACKUP_DIR" > "$HOME/.claude-last-backup"
print_info "Backup location saved to ~/.claude-last-backup"

echo ""
echo "${GREEN}You're ready to install the plugin safely!${NC}"
echo ""

# If interactive, offer to open backup directory
if [ "$INTERACTIVE" = true ]; then
    echo -n "Would you like to open the backup directory? (y/N): "
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        if command -v open &> /dev/null; then
            open "$BACKUP_DIR"
        elif command -v xdg-open &> /dev/null; then
            xdg-open "$BACKUP_DIR"
        else
            print_info "Please manually open: $BACKUP_DIR"
        fi
    fi
fi

exit 0
