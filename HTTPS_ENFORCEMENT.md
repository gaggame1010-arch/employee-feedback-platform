# HTTPS Enforcement & Data Encryption

This application is configured to **enforce HTTPS on all pages** and **encrypt all data in transit**.

## HTTPS Enforcement Settings

### 1. Automatic HTTP to HTTPS Redirect
- **`SECURE_SSL_REDIRECT = True`** (in production)
  - Automatically redirects all HTTP requests to HTTPS
  - Prevents any unencrypted connections

### 2. HTTP Strict Transport Security (HSTS)
- **`SECURE_HSTS_SECONDS = 31536000`** (1 year)
  - Tells browsers to always use HTTPS for this domain
  - Prevents man-in-the-middle attacks
  - Applied for 1 year after first visit

- **`SECURE_HSTS_INCLUDE_SUBDOMAINS = True`**
  - Applies HSTS to all subdomains

- **`SECURE_HSTS_PRELOAD = True`**
  - Allows inclusion in browser HSTS preload lists

### 3. Proxy SSL Header
- **`SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')`**
  - Required for Railway, Heroku, and other platforms behind a proxy
  - Ensures Django recognizes HTTPS connections from the proxy

## Data Encryption in Transit

### All Traffic Encrypted
- **HTTPS/TLS 1.2+** encryption for all HTTP traffic
- Browser-to-server encryption
- Server-to-database encryption (if using external database)

### Cookie Security
- **`SESSION_COOKIE_SECURE = True`** (production)
  - Session cookies only sent over HTTPS
  
- **`CSRF_COOKIE_SECURE = True`** (production)
  - CSRF tokens only sent over HTTPS

- **`SESSION_COOKIE_HTTPONLY = True`**
  - Prevents JavaScript access to session cookies

- **`CSRF_COOKIE_HTTPONLY = True`**
  - Prevents JavaScript access to CSRF tokens

## Security Headers

### Content Security Policy (CSP)
- Restricts resource loading to prevent XSS attacks
- Only allows resources from trusted sources

### Other Security Headers
- **X-Frame-Options: DENY** - Prevents clickjacking
- **X-Content-Type-Options: nosniff** - Prevents MIME sniffing
- **X-XSS-Protection: 1; mode=block** - Browser XSS protection
- **Referrer-Policy** - Controls referrer information
- **Cross-Origin-Opener-Policy** - Prevents cross-origin attacks

## Platform-Specific Configuration

### Railway
Railway automatically provides HTTPS with valid SSL certificates. The settings above ensure Django:
1. Recognizes HTTPS connections (via proxy header)
2. Redirects HTTP to HTTPS
3. Sets proper security headers

### Heroku
Heroku also provides HTTPS automatically. Same configuration applies.

### Custom Domain
If using a custom domain:
1. Configure SSL certificate (Let's Encrypt recommended)
2. Set `DJANGO_ALLOWED_HOSTS` to your domain
3. Set `CSRF_TRUSTED_ORIGINS` to `https://yourdomain.com`
4. Django will automatically enforce HTTPS

## Testing HTTPS

### In Production
1. Visit your site via HTTP: `http://yourdomain.com`
2. Should automatically redirect to: `https://yourdomain.com`
3. Check browser address bar for padlock icon (🔒)
4. Verify "Secure" or "HTTPS" indicator

### Using Browser DevTools
1. Open DevTools (F12)
2. Go to Network tab
3. Check that all requests use `https://`
4. Check Response Headers for:
   - `Strict-Transport-Security`
   - `X-Frame-Options: DENY`
   - `Content-Security-Policy`

## Verification Checklist

- [x] `SECURE_SSL_REDIRECT = True` (in production)
- [x] `SECURE_HSTS_SECONDS` set (1 year)
- [x] `SECURE_PROXY_SSL_HEADER` configured
- [x] All cookies marked as secure
- [x] Security headers configured
- [x] CSP policy set
- [x] HTTP redirects to HTTPS automatically

## Environment Variables

Make sure these are set in production:

```env
DJANGO_DEBUG=0
CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

## Important Notes

1. **Development vs Production**: HTTPS enforcement is **disabled** when `DEBUG=True` for local development
2. **Proxy Required**: The `SECURE_PROXY_SSL_HEADER` setting is required for Railway/Heroku
3. **First Visit**: HSTS only activates after the first HTTPS visit
4. **Mixed Content**: All resources (CSS, JS, images) must also use HTTPS or relative URLs

## Troubleshooting

### "Too Many Redirects" Error
- Check `SECURE_PROXY_SSL_HEADER` is set correctly
- Verify your platform sets `X-Forwarded-Proto` header
- Disable `SECURE_SSL_REDIRECT` temporarily to test

### Mixed Content Warnings
- Ensure all external resources use HTTPS URLs
- Check browser console for HTTP resources
- Update any hardcoded HTTP URLs to HTTPS

### SSL Certificate Errors
- Verify your platform provides valid SSL certificates
- Check certificate expiration
- Ensure certificate covers all subdomains if needed
