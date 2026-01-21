# Railway Deployment - Quick Start Guide

## 🚀 Deploy in 5 Minutes!

### Step 1: Sign Up & Create Project

1. **Sign up** at [railway.app](https://railway.app)
   - Sign up with GitHub (recommended for easy deployment)
   - Or use email

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your GitHub account
   - Select your repository

### Step 2: Add PostgreSQL Database

1. In your Railway project, click **"+ New"**
2. Select **"Database"** → **"Add PostgreSQL"**
3. Wait 1-2 minutes for it to provision
4. Railway automatically sets `DATABASE_URL` environment variable ✨

### Step 3: Set Environment Variables

1. Click on your **web service** (the one from GitHub)
2. Go to **"Variables"** tab
3. Add these variables:

#### Required Variables:

```
DJANGO_SECRET_KEY=<generate-a-secret-key>
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=*.up.railway.app,your-app-name.up.railway.app
COMPANY_ACCESS_CODE=123456
HR_NOTIFY_EMAILS=hr@company.com
DJANGO_DEFAULT_FROM_EMAIL=no-reply@company.com
CSRF_TRUSTED_ORIGINS=https://*.up.railway.app
```

#### How to Generate Secret Key:

Run this locally:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and paste as `DJANGO_SECRET_KEY` value.

### Step 4: Deploy!

Railway automatically deploys when you:
- Push to GitHub (if connected)
- Or click "Deploy" button

**Your app will be live at:** `https://your-app-name.up.railway.app`

### Step 5: Run Migrations & Create Admin

1. **Open Railway Shell:**
   - Click on your web service
   - Click **"Shell"** tab

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Create admin user:**
   ```bash
   python manage.py createsuperuser
   ```
   - Username: `hr_admin` (or your choice)
   - Email: your HR email
   - Password: strong password

### Step 6: Get Your Public URL

1. Click on your **web service**
2. Go to **"Settings"** tab
3. Click **"Generate Domain"** (if not auto-generated)
4. Copy your public URL

---

## ✅ That's It!

Your app is now live at:
- **Public URL**: `https://your-app-name.up.railway.app`
- **Admin**: `https://your-app-name.up.railway.app/admin/`

---

## 🔧 Important Railway Settings

### Railway Auto-Detects:
- ✅ `Procfile` (runs migrations + starts server)
- ✅ `requirements.txt` (installs dependencies)
- ✅ `runtime.txt` (Python version)
- ✅ Database connection (via `DATABASE_URL`)

### No Configuration Needed!
Railway automatically:
- Builds your app
- Runs `python manage.py migrate` (from Procfile)
- Runs `python manage.py collectstatic` (from Procfile)
- Starts Gunicorn server
- Provides HTTPS/SSL

---

## 📋 Environment Variables Checklist

Make sure these are set in Railway → Variables:

- [x] `DJANGO_SECRET_KEY` (required)
- [x] `DJANGO_DEBUG=0` (required)
- [x] `DJANGO_ALLOWED_HOSTS` (required)
- [x] `COMPANY_ACCESS_CODE` (required)
- [x] `HR_NOTIFY_EMAILS` (required)
- [x] `DJANGO_DEFAULT_FROM_EMAIL` (required)
- [x] `CSRF_TRUSTED_ORIGINS` (required)
- [x] `DATABASE_URL` (auto-set by Railway PostgreSQL)

---

## 🐛 Troubleshooting

### "DisallowedHost" Error
**Fix:** Set `DJANGO_ALLOWED_HOSTS` to:
```
*.up.railway.app,your-app-name.up.railway.app
```

### "CSRF verification failed"
**Fix:** Set `CSRF_TRUSTED_ORIGINS` to:
```
https://*.up.railway.app
```

### "Database connection failed"
**Fix:** 
1. Make sure PostgreSQL is added
2. Make sure PostgreSQL is running (green status)
3. Wait 2-3 minutes after creating database

### "Module not found"
**Fix:** Make sure `requirements.txt` has all dependencies (it does!)

### Build fails
**Fix:** Check Railway logs:
- Railway → Your Service → Deployments → Latest → View Logs

---

## 💰 Railway Pricing

### Free Tier:
- **$5 credit per month** free
- Requires payment method (won't charge unless you exceed)
- Enough for small-to-medium apps

### Cost Estimate:
- Web service: ~$5/month
- PostgreSQL: ~$5/month
- **Total: ~$10/month** (after free credits)

---

## 🔐 Security Features

Railway automatically provides:
- ✅ HTTPS/SSL certificates
- ✅ Auto-renewal of certificates
- ✅ DDoS protection
- ✅ Global CDN

Your Django app enforces:
- ✅ HTTPS redirects
- ✅ HSTS headers
- ✅ Secure cookies
- ✅ CSRF protection

---

## 📊 Monitoring

### View Logs:
- Railway → Your Service → Deployments → Latest → View Logs

### View Metrics:
- Railway → Your Service → Metrics

### Restart Service:
- Railway → Your Service → Settings → Restart

---

## 🔄 Updating Your App

1. **Push to GitHub:**
   ```powershell
   git add .
   git commit -m "Update app"
   git push origin main
   ```

2. **Railway auto-deploys** ✨

That's it! Railway detects the push and redeploys automatically.

---

## 📝 Custom Domain (Optional)

1. Railway → Your Service → Settings → Domains
2. Add custom domain
3. Update `DJANGO_ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`
4. Configure DNS (Railway will show you what to add)

---

## 🆘 Need Help?

1. **Check logs** in Railway dashboard
2. **Use Railway Shell** to debug:
   ```bash
   python manage.py check --deploy
   python manage.py dbshell
   ```
3. See `RAILWAY_TROUBLESHOOTING.md` for common issues

---

## ✅ Success Checklist

- [ ] Project created in Railway
- [ ] GitHub repo connected
- [ ] PostgreSQL database added
- [ ] All environment variables set
- [ ] First deployment successful
- [ ] Migrations run
- [ ] Admin user created
- [ ] App accessible at public URL
- [ ] HTTPS working (padlock in browser)
- [ ] Can submit test submission
- [ ] Can access admin panel

**You're all set! 🎉**
