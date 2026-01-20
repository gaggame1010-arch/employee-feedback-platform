# 🚀 Quick Start: Deploy to Railway (5 Minutes)

## What You'll Need
- GitHub account (free)
- Railway account (free)

## The 5-Step Process

### 1️⃣ Push to GitHub
```bash
git init
git add .
git commit -m "Ready for deployment"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2️⃣ Deploy on Railway
- Go to https://railway.app
- Click "Login with GitHub"
- Click "New Project" → "Deploy from GitHub repo"
- Select your repository

### 3️⃣ Add Database
- Click "+ New" → "Database" → "PostgreSQL"
- Railway handles everything automatically!

### 4️⃣ Set Environment Variables
In Railway → Your Service → Variables, add:

```bash
# Generate this locally first:
python -c "import secrets; print(secrets.token_urlsafe(50))"
# Copy the output and paste it below:

DJANGO_SECRET_KEY=paste-generated-key-here
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=*.railway.app
COMPANY_ACCESS_CODE=your-secure-code
HR_NOTIFY_EMAILS=your-hr@email.com
DJANGO_DEFAULT_FROM_EMAIL=noreply@yourcompany.com
DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### 5️⃣ Create Admin User
- Railway → Your Service → Deployments → (...) → "Open Shell"
- Run:
```bash
python manage.py migrate
python manage.py createsuperuser
```

**Done!** Your app is live at `https://your-app.up.railway.app` 🎉

---

For detailed instructions, see **RAILWAY_DEPLOY.md**
