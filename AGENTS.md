# AGENTS.md

This file provides guidance to AI agents (Claude Code and others) when working with code in this repository.

## Overview

This is the "unofficial-ai-twinkle-website" repository, which contains a static HTML website showcasing the Twinkle AI community and their projects. The repository serves as a landing page for the Taiwanese Traditional Chinese language model research community.

## Repository Structure

- `index.html` - Main website file (static HTML with embedded CSS and JavaScript)
- `README.md` - Comprehensive project overview and quick start guide
- `STYLEGUIDE.md` - Style guide for notebook development and Traditional Chinese content
- `CODE_OF_CONDUCT.md` - Community code of conduct and behavior guidelines
- `marimo_notebook/` - Contains marimo notebooks for Gemini API tutorials
- `jupyter_notebook/` - Contains original Jupyter notebooks for Gemini API tutorials  
- `notebook/` - Empty directory for additional notebooks
- `official_image/` - Contains official Twinkle AI logos and style guide
  - `twinkle-star-logo-circle-1024x1024.svg` - Circular logo (SVG format)
  - `twinkle-star-logo-round-1024x1024.svg` - Round logo (SVG format)
  - `twinkle-title-black-1920x.svg` - Title logo on black background (SVG format)
  - `twinkle-title-reverse-1920x.svg` - Title logo reversed (SVG format)
  - `twinkle-title-white-1920x.svg` - Title logo on white background (SVG format)
  - `style.md` - Brand style guide (primary color: #ffd500, font: Cabin)
- `official_link/` - Contains official links and resources
  - `README.md` - Official links to Twinkle AI platforms (Discord, GitHub, Hugging Face, LinkedIn)
  - `link.md` - Primary official links file with current platform URLs
- `faq/` - Contains frequently asked questions and community information
  - `faq.md` - Community FAQ in Traditional Chinese explaining Twinkle AI's mission and philosophy
- `unofficial-ai-twinkle-website/` - Python virtual environment directory (legacy)
- `.venv/` - Current Python virtual environment (managed by uv)
- `.env` - Environment variables (API keys, not tracked in git)
- `.env.example` - Template for environment variables
- `pyproject.toml` - Python project configuration for uv
- `uv.lock` - Locked dependency versions

## Development Setup

This is primarily a static HTML website that can be opened directly in a browser. No build process is required.

### For local development:

```bash
# Simply open the HTML file in a browser
open index.html

# Or use a simple HTTP server for better development experience
python -m http.server 8000
# Then visit http://localhost:8000
```

### For notebook development:

The project uses `uv` for Python dependency management:

```bash
# Initialize the project (already done)
uv init

# Add dependencies for notebook development
uv add marimo google-genai pillow python-dotenv openai

# Run marimo tutorial
uv run marimo tutorial intro

# Convert Jupyter notebooks to marimo format
uv run marimo convert jupyter_notebook/01-getting-your-api-key.ipynb -o 01-getting-your-api-key.py

# Run marimo notebooks
uv run marimo edit marimo_notebook/02-use-nano-banana.py

# Run individual notebook cells or full notebook
uv run marimo run marimo_notebook/02-use-nano-banana.py
```

### Environment Setup:

Create a `.env` file in the project root with your Google AI API key:

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
GOOGLE_API_KEY=your_api_key_here
```

Get your API key from: https://aistudio.google.com/apikey

## Website Architecture

The website is a single-page application built with vanilla HTML, CSS, and JavaScript:

- **Styling**: Custom CSS with terminal/developer theme using yellow accent color (#ffd500)
- **Layout**: Terminal-style windows with header dots and content sections
- **Animations**: CSS animations for particles, typing effects, and hover interactions
- **Responsive**: Mobile-first design with CSS Grid and Flexbox
- **JavaScript**: Vanilla JS for particle effects, typing animation, and smooth scrolling

## Content Structure

The website showcases:
1. **Hero Section**: Community introduction and branding
2. **Mission**: Philosophy and goals of the Twinkle AI community
3. **Core Projects**: LLM Lab and Twinkle Eval frameworks
4. **Models & Datasets**: Formosa-1 series and various datasets on Hugging Face
5. **Quick Start**: Getting started with their repositories
6. **Community Links**: Discord, GitHub, and Hugging Face profiles

## Key Features

- Terminal-themed UI design with dark background (#0a0a0a)
- Animated background particles floating upward
- Typing effect animations for dynamic text
- Responsive card layouts with hover effects
- Yellow accent color (#ffd500) throughout
- Traditional Chinese content focus
- Interactive terminal-style windows with colored dots
- Smooth scrolling and hover transforms

## External Links

The website links to:
- Discord community: https://discord.gg/v3S9Ku2Y
- GitHub organization: https://github.com/ai-twinkle
- Hugging Face organization: https://huggingface.co/twinkle-ai
- LinkedIn company page: https://www.linkedin.com/company/twinkle-ai/
- Specific model and dataset collections on Hugging Face

## Notes for Development

### Website Development
- The website is completely self-contained in `index.html`
- No external dependencies or build tools required
- Uses Google Fonts (Cabin and JetBrains Mono)
- All styling and scripting is inline for simplicity
- Color scheme: Dark theme (#0a0a0a) with yellow accents (#ffd500)
- Terminal aesthetics with red/yellow/green dots for window headers

### Notebook Development
- The marimo notebooks are separate educational content about Gemini API usage
- Notebooks use python-dotenv for secure API key management
- Script headers in notebooks define dependencies for isolated execution
- Marimo provides interactive Python notebooks with reactive execution
- Dependencies are specified in `# /// script` headers for standalone execution

## Troubleshooting

### Marimo Notebook Issues
- **API Key Errors**: Ensure `.env` file exists in project root with valid `GOOGLE_API_KEY`
- **Import Errors**: Dependencies are managed via script headers in notebooks
- **Session Errors**: AI completion errors in marimo can be safely ignored
- **Script Header Format**: All lines between `# /// script` and `# ///` must start with `#` and proper spacing

### Common Commands
```bash
# Check environment variables are loaded
uv run python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key loaded:', bool(os.getenv('GOOGLE_API_KEY')))"

# Validate API key format (should be ~39 chars starting with AIzaSy)
uv run python -c "import os; from dotenv import load_dotenv; load_dotenv(); key=os.getenv('GOOGLE_API_KEY'); print(f'Length: {len(key) if key else 0}, Starts with AIzaSy: {key.startswith(\"AIzaSy\") if key else False}')"

# Test marimo installation
uv run marimo --version

# List all project dependencies
uv tree
```

## Project Dependencies

The project uses these main dependencies:
- **marimo**: Interactive Python notebooks with reactive execution
- **google-genai**: Google's Generative AI SDK for Gemini models
- **pillow**: Python Imaging Library for image processing
- **python-dotenv**: Environment variable management from .env files
- **openai**: OpenAI API client (optional for additional AI features)

## Community Guidelines

### Style Guide
The repository follows specific style guidelines outlined in `STYLEGUIDE.md`:
- **Language**: Content and comments primarily in **Traditional Chinese**
- **Terminology**: Use "台灣" instead of "台灣地區"
- **Notebook Structure**: Include learning objectives, key points, implementation steps, exercises, and further reading
- **Code Style**: Prioritize teaching clarity, use meaningful variable names, follow PEP8 for Python
- **File Naming**: Use `00_`, `01_`, `02_` prefixes for notebooks, snake_case for dataset files

### Code of Conduct
The community follows the Contributor Covenant Code of Conduct as outlined in `CODE_OF_CONDUCT.md`:
- **Respectful Interaction**: Maintain respectful and inclusive attitudes
- **Constructive Feedback**: Provide constructive opinions, avoid personal attacks
- **Safe Environment**: Keep the community safe and friendly
- **Prohibited Behavior**: No discrimination, harassment, or malicious misinformation
- **Contact**: Use official Twinkle AI community channels for concerns

## File Organization

- Keep all website files in the root directory
- Store notebooks in `marimo_notebook/` for converted marimo files
- Store original Jupyter notebooks in `jupyter_notebook/`
- Place images and assets in `official_image/`
- Store official links and resources in `official_link/`
- Store FAQ and community information in `faq/`
- Follow the style guide in `STYLEGUIDE.md` for notebook development
- Adhere to the community standards in `CODE_OF_CONDUCT.md`
- Never commit the `.env` file (contains sensitive API keys)