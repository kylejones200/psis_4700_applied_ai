#!/bin/bash

# Compile All Worksheets to PDF
# This script compiles all .tex files in the worksheets directory to PDF format

# Color output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}PSIS 4700: Applied AI Worksheet Compiler${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Check if pdflatex is installed
if ! command -v pdflatex &> /dev/null; then
    echo -e "${RED}Error: pdflatex is not installed.${NC}"
    echo "Please install LaTeX (e.g., MacTeX on macOS, TeX Live on Linux)"
    exit 1
fi

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Count worksheets
TOTAL=$(ls -1 *.tex 2>/dev/null | wc -l)
SUCCESS=0
FAILED=0

echo -e "Found ${YELLOW}${TOTAL}${NC} worksheet(s) to compile"
echo ""

# Compile each .tex file
for texfile in *.tex; do
    if [ -f "$texfile" ]; then
        echo -e "Compiling: ${YELLOW}${texfile}${NC}"
        
        # Run pdflatex twice (for proper references and page numbers)
        # Redirect output to log file
        pdflatex -interaction=nonstopmode "$texfile" > "${texfile%.tex}.log" 2>&1
        
        # Check if PDF was created
        pdffile="${texfile%.tex}.pdf"
        if [ -f "$pdffile" ]; then
            echo -e "${GREEN}✓ Success:${NC} $pdffile created"
            SUCCESS=$((SUCCESS + 1))
            
            # Clean up auxiliary files
            rm -f "${texfile%.tex}.aux"
            rm -f "${texfile%.tex}.log"
            rm -f "${texfile%.tex}.out"
            rm -f "${texfile%.tex}.toc"
        else
            echo -e "${RED}✗ Failed:${NC} $pdffile not created"
            echo -e "  Check ${texfile%.tex}.log for errors"
            FAILED=$((FAILED + 1))
        fi
        echo ""
    fi
done

# Summary
echo -e "${GREEN}========================================${NC}"
echo -e "Compilation Summary:"
echo -e "${GREEN}  Success: ${SUCCESS}${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${RED}  Failed:  ${FAILED}${NC}"
fi
echo -e "${GREEN}========================================${NC}"

if [ $SUCCESS -eq $TOTAL ]; then
    echo -e "${GREEN}All worksheets compiled successfully!${NC}"
    exit 0
else
    echo -e "${YELLOW}Some worksheets failed to compile. Check log files for details.${NC}"
    exit 1
fi
