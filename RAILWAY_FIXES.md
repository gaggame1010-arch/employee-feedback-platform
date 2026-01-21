# Railway Deployment Fixes

## Common Railway Deployment Errors & Fixes

### 1. **"ModuleNotFoundError: No module named 'whitenoise'"**
**Fix:** Already in `requirements.txt`. Make sure Railway installs dependencies:
- Railway → Settings → Build Command: Leave empty (auto-detects `requirements.txt`)

### 2. **"DisallowedHost" Error**
**Fix:** Set `DJANGO_ALLOWED_HOSTS` in Railway Variables:
```
DJANGO_ALLOWED_HOSTS=yourapp.up.railway.app,*.railway.app
```
Replace `yourapp` with your actual Railway domain.

### 3. **"CSRF verification failed"**
**Fix:** Set `CSRF_TRUSTED_ORIGINS` in Railway Variables:
```
CSRF_TRUSTED_ORIGINS=https://yourapp.up.railway.app
```

### 4. **"No such file or directory: 'staticfiles'"**
**Fix:** Already fixed in `Procfile` - it now runs `collectstatic` automatically.

### 5. **"Database connection failed"**
**Fix:** Railway auto-provisions PostgreSQL. Make sure:
- Railway → Service → Variables → `DATABASE_URL` is set (auto-set by Railway)
- Or add PostgreSQL plugin in Railway dashboard

### 6. **"Port binding failed"**
**Fix:** Already fixed in `Procfile` - uses `$PORT` environment variable.

### 7. **"Secret key not set"**
**Fix:** Set `DJANGO_SECRET_KEY` in Railway Variables:
```
DJANGO_SECRET_KEY=your-long-random-secret-key-here
```
Generate one: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

### 8. **"Static files not loading"**
**Fix:** Already configured with WhiteNoise. Make sure `STATIC_ROOT` is set (it is: `staticfiles/`).

## Required Railway Variables

Set these in Railway → Your Service → Variables:

### Required:
```
DJANGO_SECRET_KEY=<generate-random-key>
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=yourapp.up.railway.app,*.railway.app
COMPANY_ACCESS_CODE=123456
HR_NOTIFY_EMAILS=hr@company.com
DJANGO_DEFAULT_FROM_EMAIL=no-reply@company.com
CSRF_TRUSTED_ORIGINS=https://yourapp.up.railway.app
```

### Optional (for email):
```
DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Steps to Fix Deployment

1. **Check Railway Logs:**
   - Railway → Your Service → Deployments → Click latest deployment → View Logs
   - Look for error messages

2. **Verify Variables:**
   - Railway → Your Service → Variables
   - Make sure all required variables are set

3. **Check Build:**
   - Railway → Your Service → Settings → Build Command
   - Should be empty (auto-detects)

4. **Check Start Command:**
   - Railway → Your Service → Settings → Start Command
   - Should be empty (uses `Procfile`)

5. **Redeploy:**
   - Railway → Your Service → Deployments → Redeploy

## Quick Test Commands

Run these in Railway Shell (Railway → Your Service → Shell):

```bash
# Check if all dependencies installed
pip list

# Check Django settings
python manage.py check --deploy

# Test database connection
python manage.py dbshell

# Check static files
python manage.py collectstatic --dry-run
```

## Still Having Issues?

Share the exact error message from Railway logs, and I'll help fix it!
