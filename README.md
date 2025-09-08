# unofficial-ai-twinkle-website

🌐 Twinkle AI "UnOfficial" Website

This repository contains a static HTML website showcasing the Twinkle AI community and their projects. The site serves as a landing page for the Taiwanese Traditional Chinese language model research community.

## Quick Start

Simply open the HTML file in a browser:

```bash
open index.html
```

Or use a local HTTP server for better development experience:

```bash
python -m http.server 8000
# Then visit http://localhost:8000
```

## Features

- **Terminal-themed UI** with dark background (#0a0a0a) and yellow accents (#ffd500)
- **Animated background particles** floating upward
- **Typing effect animations** for dynamic text
- **Responsive design** with mobile-first approach
- **Bilingual support** with Traditional Chinese / English language toggle
- **Language-specific typography** - Open Huninn Font for Traditional Chinese, Cabin for English
- **Custom SVG icons** replacing emoji throughout the interface
- **Mascot display** in terminal window format
- **Website favicon** using official Twinkle AI logo
- **Interactive terminal-style windows** with colored header dots

## Content Sections

1. **Hero Section**: Community introduction and branding with mascot display
2. **Mission**: Philosophy and goals of the Twinkle AI community with custom icons
3. **Core Projects**: LLM Lab and Twinkle Eval frameworks with custom SVG icons
4. **Models & Datasets**: Formosa-1 series and various datasets with custom icons
5. **Quick Start**: Getting started with repositories
6. **Community Links**: Discord, GitHub, and Hugging Face profiles

## Official Links

- [Discord Community](https://discord.gg/v3S9Ku2Y)
- [GitHub Organization](https://github.com/ai-twinkle)
- [Hugging Face](https://huggingface.co/twinkle-ai)
- [LinkedIn](https://www.linkedin.com/company/twinkle-ai/)

## Development

This is a completely self-contained static website with no build process required. All styling and JavaScript is inline in `index.html` for simplicity.

For notebook development and tutorials, see the [AGENTS.md](AGENTS.md) file for detailed setup instructions using `uv` and marimo notebooks.

## Community Guidelines

- Follow the [STYLEGUIDE.md](STYLEGUIDE.md) for notebook development and Traditional Chinese content standards
- Adhere to our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for respectful community interaction

## Repository Structure

- `index.html` - Main website file (static HTML with embedded CSS and JavaScript)
- `AGENTS.md` - Detailed development guidance and architecture documentation
- `STYLEGUIDE.md` - Development and content style guidelines
- `CODE_OF_CONDUCT.md` - Community behavior guidelines
- `assets/` - Custom SVG icons and mascot images
- `marimo_notebook/` - Marimo notebooks for Gemini API tutorials
- `jupyter_notebook/` - Original Jupyter notebooks
- `official_image/` - Official Twinkle AI logos and brand assets (includes favicon)
- `official_link/` - Official platform links and resources
- `faq/` - FAQ and community information in Traditional Chinese
