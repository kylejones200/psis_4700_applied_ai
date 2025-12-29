# AAI Webslides Viewer

A lightweight, browser-based presentation viewer for all AAI course slides.

## Usage

### Option 1: Local File (Simple)
1. Open `index.html` in your browser
2. Select a slide deck from the sidebar
3. Navigate with arrow keys (← →) or buttons

### Option 2: Local Server (Recommended for large files)
```bash
# Navigate to webslides directory
cd /Users/k.jones/Downloads/AAI/webslides

# Python 3
python3 -m http.server 8000

# Or Python 2
python -m SimpleHTTPServer 8000

# Then open browser to:
# http://localhost:8000
```

### Navigation
- **Arrow Keys**: ← Previous slide | → Next slide
- **Buttons**: Use Previous/Next buttons in the header
- **Sidebar**: Click any file to load that slide deck

## Features
- Lightweight (single HTML file + CDN markdown parser)
- Dark mode for comfortable viewing
- Keyboard navigation
- Organized sidebar with all slide decks
- Slide counter
- Clean, professional presentation view

## Slide Organization
- **Intro Course**: 8 weeks of introductory material
- **Advanced Course**: 8 weeks of technical content
- **Lectures**: 5 detailed lecture files
- **Reference**: Key terms and definitions

## Troubleshooting
If slides don't load when opening `index.html` directly:
- Use a local server (see Option 2 above)
- Some browsers block local file access for security
- A simple HTTP server resolves this issue

