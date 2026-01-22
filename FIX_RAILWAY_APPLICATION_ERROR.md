# Fix "Application failed to respond" Error on Railway

## Step 1: Check Deploy Logs

**This is the most important step!** The logs will tell us exactly what's wrong.

### How to Check Logs:

1. **Go to Railway Dashboard**
   - Visit: https://railway.app
   - Log in to your account

2. **Open Your Service**
   - Click on your web service (the one with the error)

3. **View Deploy Logs**
   - Click on the **"Deployments"** tab (or "Deploys" tab)
   - Click on the **most recent deployment** (the one that failed)
   - Scroll through the logs to find error messages

4. **Look for Error Messages**
   - Red text or error messages
   - Python tracebacks
   - Import errors
   - Database connection errors
   - Missing environment variable errors

---

## Common Errors and Fixes

### Error 1: Missing DJANGO_SECRET_KEY

**Error message:**
```
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty
```

**Fix:**
1. Railway → Your Service → **Variables** tab
2. Add variable:
   - **Name**: `DJANGO_SECRET_KEY`
   - **Value**: Generate a secret key (see below)

**Generate Secret Key:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Or use this online tool: https://djecrety.ir/

---

### Error 2: Database Connection Error

**Error message:**
```
django.db.utils.OperationalError: could not connect to server
```

**Fix:**
1. Make sure you have a **PostgreSQL database** added to your Railway project
2. Railway automatically creates `DATABASE_URL` when you add a database
3. If missing, add PostgreSQL database:
   - Railway → Your Project → **New** → **Database** → **Add PostgreSQL**

---

### Error 3: Missing Environment Variables

**Error message:**
```
KeyError: 'DJANGO_ALLOWED_HOSTS'
```

**Fix:**
Add all required environment variables in Railway → Variables:

**Required Variables:**
```
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=kyrex.co,www.kyrex.co,*.up.railway.app
CSRF_TRUSTED_ORIGINS=https://kyrex.co,https://www.kyrex.co,https://*.up.railway.app
HR_NOTIFY_EMAILS=sales@kyrex.co
DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
COMPANY_ACCESS_CODE=your-access-code
```

---

### Error 4: Import Error / Missing Package

**Error message:**
```
ModuleNotFoundError: No module named 'gunicorn'
```

**Fix:**
1. Check `requirements.txt` includes all packages
2. Make sure `gunicorn` is in `requirements.txt`
3. Redeploy (Railway will reinstall packages)

---

### Error 5: Migration Error

**Error message:**
```
django.db.migrations.exceptions.MigrationError
```

**Fix:**
1. Check if migrations are running in `Procfile`
2. Your `Procfile` should have:
   ```
   release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py create_admin || true
   ```

---

### Error 6: Port Binding Error

**Error message:**
```
Address already in use
```

**Fix:**
- Railway handles ports automatically
- Make sure your `Procfile` doesn't specify a port:
  ```
  web: gunicorn anonplatform.wsgi:application
  ```
  (NOT: `gunicorn anonplatform.wsgi:application --bind 0.0.0.0:$PORT`)

---

## Quick Fix Checklist

1. **Check Deploy Logs** ← Do this first!
   - Railway → Deployments → Latest deployment → View logs

2. **Verify Environment Variables**
   - Railway → Variables tab
   - Make sure all required variables are set

3. **Check Database**
   - Railway → Your Project
   - Make sure PostgreSQL database is added

4. **Verify Procfile**
   - Should be in root of project
   - Should have `release:` and `web:` commands

5. **Check requirements.txt**
   - Should include: `django`, `gunicorn`, `whitenoise`, `psycopg2-binary`, `dj-database-url`

---

## Step-by-Step Debugging

### 1. Check What Error You're Getting

**Share the error message from Railway logs**, and I'll help you fix it!

### 2. Common Missing Variables

Make sure these are set in Railway → Variables:

```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=kyrex.co,www.kyrex.co,*.up.railway.app
CSRF_TRUSTED_ORIGINS=https://kyrex.co,https://www.kyrex.co,https://*.up.railway.app
HR_NOTIFY_EMAILS=sales@kyrex.co
DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
COMPANY_ACCESS_CODE=123456
```

### 3. Verify Database

1. Railway → Your Project
2. Check if you have a PostgreSQL database service
3. If not, add one: **New** → **Database** → **Add PostgreSQL**

### 4. Redeploy

After fixing issues:
1. Railway will auto-redeploy when you save variables
2. Or manually trigger: **Deployments** → **Redeploy**

---

## Still Not Working?

**Share with me:**
1. The error message from Railway deploy logs
2. Screenshot of your Railway Variables tab
3. Screenshot of your Deployments tab

I'll help you fix it! 🚀
