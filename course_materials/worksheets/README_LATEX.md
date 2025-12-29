# LaTeX Worksheets for PSIS 4700: Applied AI

This directory contains professionally formatted LaTeX worksheets for students.

## Worksheets Available

1. **ai_workflow_quick_guide.tex** - Step-by-step AI workflow practice
2. **applied_ai_planning_pack.tex** - Project planning templates and idea bank
3. **applied_ethics_case_review.tex** - Ethics case analysis framework
4. **dataset_checklist_and_quality_comparison.tex** - Data quality assessment tools
5. **ethics_incident_case_summaries.tex** - Real-world AI failure cases
6. **genai_practice_pack.tex** - Generative AI task planning and refinement
7. **prompt_troubleshooting_guide.tex** - Fixing common prompt problems
8. **responsible_ai_checklist.tex** - Pre-deployment responsibility checklist
9. **risk_and_mitigation_worksheet.tex** - Risk identification and management
10. **weak_dataset_case_walkthrough.tex** - Data cleaning case study
11. **when_to_use_ai_vs_not_use_ai.tex** - AI adoption decision framework

## Compiling to PDF

### Option 1: Compile All Worksheets (Recommended)

```bash
./compile_all_worksheets.sh
```

This script will:
- Compile all .tex files to PDF
- Save all PDFs to the `pdfs/` folder
- Show progress and results
- Clean up auxiliary files
- Create a summary of success/failures

### Option 2: Compile Individual Worksheet

```bash
pdflatex worksheet_name.tex
pdflatex worksheet_name.tex  # Run twice for proper formatting
```

### Requirements

- **LaTeX Distribution**:
  - **macOS**: MacTeX (install via `brew install --cask mactex`)
  - **Linux**: TeX Live (`sudo apt-get install texlive-full`)
  - **Windows**: MiKTeX or TeX Live

- **Required Packages** (included in full distributions):
  - `geometry`, `fancyhdr`, `xcolor`, `tikz`
  - `enumitem`, `tcolorbox`, `tabularx`
  - `array`, `booktabs`, `titlesec`, `longtable`

## Features

All worksheets include:

- **Professional Header**: Course branding on every page
- **Color-Coded Sections**: Green for main headings, contextual colors for special boxes
- **Fill-in Boxes**: Gray boxes with proper spacing for student responses
- **Clean Typography**: Easy-to-read fonts and proper spacing
- **Print-Ready**: Optimized for letter-size paper (8.5" x 11")
- **Tables**: Professional tables with alternating row colors
- **Checkboxes**: For checklist-style worksheets

## Design Philosophy

1. **Generous Spacing**: Plenty of room for handwritten responses
2. **Visual Hierarchy**: Clear distinction between instructions and fill-in areas
3. **Professional Appearance**: Suitable for coursework submission
4. **Accessibility**: High contrast, clear fonts, organized layouts
5. **Consistency**: All worksheets follow the same design language

## Customization

To modify the appearance, edit these settings at the top of any .tex file:

```latex
% Change main color (default: green #66BB6A)
\definecolor{maincolor}{RGB}{102,187,106}

% Change fill box background (default: light gray)
\definecolor{lightgray}{RGB}{245,245,245}

% Adjust margins (default: 1 inch)
\usepackage[margin=1in]{geometry}
```

## Troubleshooting

### PDFs Don't Generate
- Ensure LaTeX is properly installed: `pdflatex --version`
- Check that all required packages are installed
- Review error logs (`.log` files) for specific issues

### Tables Overflow Page
- Some complex tables may need margin adjustments
- Edit geometry settings: `\usepackage[margin=0.75in]{geometry}`

### Missing Fonts
- Install the full LaTeX distribution (not minimal)
- Ensure standard fonts are available

## File Structure

```
worksheets/
├── pdfs/                          # Compiled PDF files (created by script)
│   ├── ai_workflow_quick_guide.pdf
│   ├── applied_ai_planning_pack.pdf
│   └── ... (all 11 worksheet PDFs)
├── *.tex                          # LaTeX source files
├── *.md                           # Original markdown versions
├── compile_all_worksheets.sh      # Batch compilation script
└── README_LATEX.md                # This file
```

## Distribution

### For Students
- Distribute only the PDF files from the `pdfs/` folder
- Students can print and fill out by hand
- Or students can fill out digitally using PDF editors

### For Instructors
- Keep .tex files for customization
- Modify content, spacing, or design as needed
- Recompile after changes

## Tips for Best Results

1. **Print Quality**: Use laser printer for best results
2. **Digital Filling**: Adobe Acrobat or Preview (macOS) work well for digital completion
3. **Batch Printing**: All worksheets are formatted consistently for easy batch printing
4. **Two-Sided Printing**: Most worksheets span 2-4 pages, perfect for double-sided printing

---

**Created**: December 29, 2025  
**Course**: PSIS 4700 Applied Artificial Intelligence  
**Format**: LaTeX with TikZ and tcolorbox styling
