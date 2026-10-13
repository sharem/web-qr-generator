from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import qrcode
import qrcode.image.svg
import logging
import os
import sys

app = Flask(__name__)

# Rate limiting per client IP. In-memory storage is per process; use a shared
# backend (e.g. RATELIMIT_STORAGE_URI=redis://...) when running multiple workers.
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri=os.environ.get("RATELIMIT_STORAGE_URI", "memory://"),
)

CONTENT_SECURITY_POLICY = "; ".join([
    "default-src 'self'",
    "script-src 'self'",
    "style-src 'self' https://fonts.googleapis.com https://cdnjs.cloudflare.com",
    "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com",
    "img-src 'self' data: blob:",
    "connect-src 'self'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
])

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check Python version compatibility
if sys.version_info < (3, 10):
    logger.error("Python 3.10+ is required for this application")
    sys.exit(1)

# Log Python version for debugging
logger.info(f"Running on Python {sys.version}")


@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = CONTENT_SECURITY_POLICY
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=()'
    return response


@app.route('/')
def main():
    return render_template('index.html')


def generate_QR(text: str) -> tuple[str | None, str | None]:
    if not text:
        return None, "Please enter some text"
    if len(text) > 1000:
        return None, "Text is too long. Please keep it under 1000 characters."
    try:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
            image_factory=qrcode.image.svg.SvgFillImage,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image()
        return img.to_string(encoding='unicode'), None
    except Exception as e:
        logger.error(f"Error generating QR code: {str(e)}")
        return None, "An error occurred while generating the QR code"


@app.route('/generate', methods=['POST'])
@limiter.limit("30 per minute")
def generate():
    try:
        text = request.form.get('text', '').strip()
        result, error = generate_QR(text)
        if error:
            return error, 400
        return result
    except Exception as e:
        logger.error(f"Error in generate route: {str(e)}")
        return "An internal error occurred", 500


@app.errorhandler(404)
def not_found(error):
    return render_template('index.html'), 404


@app.errorhandler(429)
def rate_limited(error):
    return "Too many requests. Please wait a moment and try again.", 429


@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {str(error)}")
    return "Internal server error", 500


if __name__ == "__main__":
    # Never enable debug in production: the Werkzeug debugger allows arbitrary code execution
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=5000)
