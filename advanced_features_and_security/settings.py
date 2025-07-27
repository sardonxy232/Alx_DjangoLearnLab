# ============================
# HTTPS and Security Settings
# ============================

# Force HTTPS redirect
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include subdomains
SECURE_HSTS_PRELOAD = True  # Allow HSTS preloading by browsers

# Secure cookies
SESSION_COOKIE_SECURE = True  # Session cookies over HTTPS only
CSRF_COOKIE_SECURE = True  # CSRF cookies over HTTPS only

# Security headers
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME-sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS filter

# Optional: Use this to manually add headers if needed in middleware
# Use with caution or if your deployment platform doesn't support automatic headers
# Example for XSS and NOSNIFF:
# from django.middleware.security import SecurityMiddleware
