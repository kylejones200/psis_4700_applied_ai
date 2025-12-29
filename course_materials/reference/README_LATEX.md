# Reference Materials - LaTeX PDFs

Professional reference sheets for students in the Applied AI course.

## Available Reference Materials

1. **ai_terms_plain_english.pdf** - Glossary of key AI terms with plain language definitions
2. **model_family_map.pdf** - Quick reference for matching problems to model families
3. **problem_to_model_examples.pdf** - Concrete examples of problem-to-model matching
4. **prompt_patterns_workbook.pdf** - Interactive workbook for practicing prompt engineering patterns
5. **simple_sample_dataset.pdf** - Sample CSV dataset for practice exercises
6. **tidy_data_one_pager.pdf** - Principles of clean data structure
7. **what_is_ai.pdf** - Foundational overview of AI concepts

## File Structure

```
reference/
├── pdfs/                          # Compiled PDF files (created by script)
│   ├── ai_terms_plain_english.pdf
│   ├── model_family_map.pdf
│   └── ... (all 7 reference PDFs)
├── *.tex                          # LaTeX source files
├── *.md                           # Original markdown versions
├── compile_all_references.sh      # Batch compilation script
└── README_LATEX.md                # This file
```

## Compiling to PDF

### Option 1: Compile All Reference Materials (Recommended)

```bash
./compile_all_references.sh
```

This script will:
- Compile all .tex files to PDF
- Save all PDFs to the `pdfs/` folder
- Show progress and results
- Clean up auxiliary files
- Create a summary of success/failures

### Option 2: Compile Individual Files

```bash
pdflatex filename.tex
mv filename.pdf pdfs/
```

## Requirements

- LaTeX distribution (TeX Live, MacTeX, or MiKTeX)
- `pdflatex` command available in PATH
- Packages used: geometry, fancyhdr, xcolor, tcolorbox, tabularx, booktabs, titlesec, multicol, listings

## Design Features

### Color Scheme
- **Primary Blue** (RGB: 33, 150, 243) - Headers and main elements
- **Light Gray** (RGB: 245, 245, 245) - Fill boxes and backgrounds
- **Accent Colors** - Green for special emphasis, Orange for pattern boxes

### Layout
- Letter-size (8.5" x 11") paper
- Professional headers with PSIS 4700 branding
- Clean section formatting with colored titles
- Generous spacing for readability

### Special Elements
- **Glossary format** for term definitions (ai_terms_plain_english)
- **Tables** for model mapping references
- **Fill-in boxes** for interactive elements (workbook, practice sheets)
- **Code listings** for CSV data display
- **Two-column layout** for efficient space use (where appropriate)

## Usage

### For Instructors
- Compile PDFs using the provided script
- Distribute PDFs to students for reference
- Source .tex files can be customized for your course
- Update content as needed and recompile

### For Students
- Print and keep handy during coursework
- Use as quick reference during projects
- Complete fill-in sections where provided
- Refer back throughout the course

## Customization

To modify content:
1. Edit the corresponding .tex file
2. Run `./compile_all_references.sh` to regenerate all PDFs
3. Or compile individual files with `pdflatex filename.tex`

## Troubleshooting

### Missing Packages
If compilation fails due to missing LaTeX packages, install them:
- **macOS**: Use TeX Live Utility or `tlmgr install package-name`
- **Linux**: Use your package manager (e.g., `apt install texlive-full`)
- **Windows**: Use MiKTeX Package Manager

### Common Issues
- **Headheight warnings**: Safe to ignore; PDFs still compile correctly
- **Font warnings**: LaTeX will substitute available fonts automatically
- **Overfull hbox**: Usually cosmetic; check PDF output to verify layout

## Notes

- PDFs are optimized for printing and digital reading
- All materials use consistent branding and design
- Source markdown files preserved for easy editing
- LaTeX provides professional typography and layout control
