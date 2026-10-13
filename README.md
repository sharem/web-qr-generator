# Web QR Generator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge)

**A web application for generating QR codes instantly**

</div>

## About

A responsive Flask web application that creates QR codes from text, URLs, emails, and phone numbers. Features dark/light themes, instant generation, and downloadable SVG output.

## Features

- ⚡ **Instant QR Generation** - Real-time creation with SVG output
- 🌓 **Theme Support** - Dark/light mode with preference saving
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 💾 **Download Support** - Save as high-quality SVG files
- 🚀 **Quick Examples** - Pre-built templates for common use cases
- 📊 **Usage Counter** - Track generated QR codes locally

## Quick Start

### Prerequisites
- **Python 3.10+**
- pip (included with Python)

### Installation

```bash
# Clone the repository
git clone https://github.com/sharem/web-qr-generator.git
cd web-qr-generator

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## Testing

### Running Tests

```bash
# Install development dependencies (pytest, ruff, bandit, pip-audit)
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=xml

# Run with HTML formatted coverage report
pytest --cov=app --cov-report=html

# Run specific test class
pytest test_app.py::TestApp -v

# Run with detailed output
pytest -v --tb=long
```

### Lint and Security Checks

These run in CI on every pull request:

```bash
ruff check .                              # Lint
bandit -q -r . -x ./test_app.py           # Static security analysis
pip-audit -r requirements.txt             # Known vulnerabilities in dependencies
```

Optionally, install the git hooks with `pre-commit install` to run ruff, bandit and gitleaks before each commit.

### Test Coverage

The test suite includes:
- ✅ **Route Testing** - All endpoints and error handlers
- ✅ **QR Generation** - Valid inputs, edge cases, and error handling
- ✅ **Integration Tests** - Complete workflow testing
- ✅ **Error Scenarios** - Exception handling and validation

View the coverage report by opening `htmlcov/index.html` after running tests with coverage.

## Usage

1. **Enter content** in the text field (URLs, emails, phone numbers, or any text)
2. **Click "Generate QR Code"** or press Enter
3. **Download** the QR code as an SVG file

### Quick Examples
- 🔗 **GitHub Profile** - `https://github.com/username`
- 📧 **Email** - `mailto:contact@example.com`
- 📞 **Phone** - `tel:+1-234-567-8900`
- 📶 **WiFi** - `WIFI:T:WPA;S:NetworkName;P:Password;;`

## Development

### Project Structure
```
web-qr-generator/
├── app.py                 # Flask application
├── test_app.py           # Test suite
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
├── pytest.ini           # Pytest configuration
├── static/              # CSS, JS, favicons
└── templates/           # HTML templates
```

### Tech Stack
- **Backend**: Python 3.10+, Flask 3.1.3
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **QR Generation**: qrcode library (SVG output)
- **Testing**: pytest, pytest-cov
- **Quality & Security**: ruff, bandit, pip-audit

### Python Version Support
| Version | Status | Notes |
|---------|--------|-------|
| 3.13+ | ✅ Recommended | Latest features and best performance |
| 3.12 | ✅ Excellent | Great performance and features |
| 3.11 | ✅ Great | Excellent performance improvements |
| 3.10 | ✅ Minimum Required | Union types, match statements |
| <3.10 | ❌ Not supported | Please upgrade Python |

### API Endpoints
- `GET /` - Main application page
- `POST /generate` - Generate QR code from form data

### Development Setup
```bash
# Clone and install (see Quick Start)
# Debug mode is disabled by default; enable it only for local development
FLASK_DEBUG=1 python app.py  # Server auto-reloads on changes
```

## Configuration

### Customization
Modify CSS variables in `static/css/styles.css` for theming, or adjust QR settings in `app.py`.

## License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- [qrcode](https://github.com/lincolnloop/python-qrcode) - QR code generation
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Font Awesome](https://fontawesome.com/) - Icons

---

<div align="center">

**Made with ❤️ by [sharem](https://github.com/sharem)**

</div>
