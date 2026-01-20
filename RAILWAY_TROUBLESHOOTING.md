# Railway Troubleshooting Guide

## Common Issues and Solutions

### Issue 1: "Build Failed" or "Deployment Failed"

**Check the logs:**
1. Go to your Railway project
2. Click on the deployment that failed
3. Check the "Build Logs" or "Deploy Logs"
4. Look for error messages

**Common causes:**
- Missing dependencies in `requirements.txt`
- Python version mismatch
- Procfile syntax error

**Solution:** Check if you see errors like:
```
ModuleNotFoundError: No module named 'X'
```
Add missing packages to `requirements.txt`

---

### Issue 2: "Application Error" or 500 Error

**Possible causes:**
1. **Missing environment variables**
   - Go to Variables tab
   - Make sure all required variables are set:
     - `DJANGO_SECRET_KEY`
     - `DJANGO_DEBUG=0`
     - `DJANGO_ALLOWED_HOSTS=*.railway.app`
     - `COMPANY_ACCESS_CODE`
     - `HR_NOTIFY_EMAILS`

2. **Database not connected**
   - Make sure PostgreSQL database is added
   - Check that `DATABASE_URL` is automatically set (Railway does this)

**Solution:** Check deployment logs for specific error messages

---

### Issue 3: "Port already in use" or Connection Issues

**Railway automatically handles ports** - make sure your Procfile uses `$PORT`:

```
web: gunicorn anonplatform.wsgi --bind 0.0.0.0:$PORT
```

---

### Issue 4: Static Files Not Loading

**Railway should handle this automatically** via the Procfile, but if issues persist:

1. Check deployment logs
2. Make sure `collectstatic` runs (it should in the `release` command)
3. Verify WhiteNoise is in `requirements.txt`

---

### Issue 5: "Cannot connect to database"

**Solution:**
1. Make sure PostgreSQL database is added:
   - Click "+ New" → "Database" → "PostgreSQL"
2. Check that database is linked to your web service
3. Railway automatically sets `DATABASE_URL`
4. In shell, run: `python manage.py migrate`

---

### Issue 6: Railway Website Won't Load or Timeout

**Possible issues:**
- Railway service might be down (check status.railway.app)
- Your account might have hit usage limits
- Try a different browser or clear cache

---

## Quick Diagnostic Commands

Open Railway shell and run:

```bash
# Check if Python works
python --version

# Check if Django is installed
python -c "import django; print(django.get_version())"

# Check environment variables
env | grep DJANGO

# Try to connect to database
python manage.py dbshell
```

---

## If Railway Still Doesn't Work

Try these alternative platforms (all easier than traditional hosting):

1. **Render** - Very similar to Railway, free tier available
2. **Fly.io** - Great free tier, fast deployments
3. **PythonAnywhere** - Free tier, beginner-friendly
4. **Heroku** - Classic option, still works (paid)

See `ALTERNATIVE_DEPLOY.md` for instructions on these platforms.

---

## Get Help

- Railway Discord: https://discord.gg/railway
- Railway Docs: https://docs.railway.app
- Check Railway status: https://status.railway.app
