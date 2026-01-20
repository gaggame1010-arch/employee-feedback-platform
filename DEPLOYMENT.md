# Deployment Guide

This guide will help you deploy the Anonymous Employee Feedback Platform to make it publicly accessible.

## Quick Deploy Options

### Option 1: Railway (Recommended - Easiest)

1. **Sign up** at [railway.app](https://railway.app)

2. **Create a new project** and connect your GitHub repository

3. **Add environment variables** in Railway dashboard:
   ```
   DJANGO_SECRET_KEY=your-secret-key-here (generate a strong random string)
   DJANGO_DEBUG=0
   DJANGO_ALLOWED_HOSTS=your-app-name.railway.app
   COMPANY_ACCESS_CODE=your-company-code
   HR_NOTIFY_EMAILS=hr@yourcompany.com
   DJANGO_DEFAULT_FROM_EMAIL=noreply@yourcompany.com
   DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   ```

4. **Add PostgreSQL database** (Railway will auto-create DATABASE_URL)

5. **Deploy** - Railway will automatically detect the Procfile and deploy

6. **Your app will be live** at `https://your-app-name.railway.app`

---

### Option 2: Heroku

1. **Install Heroku CLI** from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. **Login and create app**:
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Add PostgreSQL database**:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

4. **Set environment variables**:
   ```bash
   heroku config:set DJANGO_SECRET_KEY=your-secret-key-here
   heroku config:set DJANGO_DEBUG=0
   heroku config:set DJANGO_ALLOWED_HOSTS=your-app-name.herokuapp.com
   heroku config:set COMPANY_ACCESS_CODE=your-company-code
   heroku config:set HR_NOTIFY_EMAILS=hr@yourcompany.com
   heroku config:set DJANGO_DEFAULT_FROM_EMAIL=noreply@yourcompany.com
   ```

5. **Deploy**:
   ```bash
   git push heroku main
   ```

6. **Run migrations**:
   ```bash
   heroku run python manage.py migrate
   ```

7. **Create superuser** (for HR admin access):
   ```bash
   heroku run python manage.py createsuperuser
   ```

---

### Option 3: DigitalOcean App Platform

1. **Sign up** at [digitalocean.com](https://www.digitalocean.com)

2. **Create App** → Connect GitHub repository

3. **Configure**:
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `gunicorn anonplatform.wsgi --log-file -`
   - Environment Variables: (same as Railway above)

4. **Add PostgreSQL database** in Resources

5. **Deploy**

---

### Option 4: PythonAnywhere (Free tier available)

1. **Sign up** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload files** via Files tab or Git

3. **Create Web App** → Manual configuration

4. **Set up virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```

5. **Configure WSGI file** to point to `anonplatform.wsgi`

6. **Set environment variables** in Web app settings

7. **Reload** the web app

---

## Environment Variables Required

Create a `.env` file or set these in your hosting platform:

```env
# REQUIRED - Generate a strong secret key (use: python -c "import secrets; print(secrets.token_urlsafe(50))")
DJANGO_SECRET_KEY=your-secret-key-here

# Set to 0 for production
DJANGO_DEBUG=0

# Your domain name (comma-separated for multiple)
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Company access code (shared with employees)
COMPANY_ACCESS_CODE=your-secure-code-here

# HR notification emails (comma-separated)
HR_NOTIFY_EMAILS=hr@yourcompany.com,admin@yourcompany.com

# Email settings
DJANGO_DEFAULT_FROM_EMAIL=noreply@yourcompany.com
DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

# Email server settings (if using SMTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Database URL (auto-set by most platforms, or use PostgreSQL connection string)
DATABASE_URL=postgresql://user:password@host:port/dbname
```

---

## Post-Deployment Steps

1. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

2. **Collect static files**:
   ```bash
   python manage.py collectstatic --noinput
   ```

3. **Create HR admin user**:
   ```bash
   python manage.py createsuperuser
   ```
   Username: `hr_admin` (or your choice)
   Email: Your HR email
   Password: Strong password

4. **Test the application**:
   - Visit your public URL
   - Test employee submission form
   - Test HR admin login at `/admin/`

---

## Security Checklist

- [ ] `DJANGO_DEBUG=0` in production
- [ ] Strong `DJANGO_SECRET_KEY` set
- [ ] `ALLOWED_HOSTS` includes your domain
- [ ] HTTPS enabled (most platforms do this automatically)
- [ ] Strong `COMPANY_ACCESS_CODE` set
- [ ] HR admin password is strong
- [ ] Email notifications configured
- [ ] Database backups enabled (if using PostgreSQL)

---

## Email Configuration

For production email notifications, configure SMTP:

**Gmail example**:
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password  # Use App Password, not regular password
```

**SendGrid example**:
```env
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
```

---

## Troubleshooting

**Static files not loading?**
- Run `python manage.py collectstatic`
- Check `STATIC_ROOT` is set correctly
- Verify WhiteNoise middleware is in `MIDDLEWARE`

**Database errors?**
- Ensure migrations are run: `python manage.py migrate`
- Check `DATABASE_URL` is set correctly

**500 errors?**
- Check logs in your hosting platform
- Verify all environment variables are set
- Ensure `DEBUG=0` in production

**Can't access admin?**
- Create superuser: `python manage.py createsuperuser`
- Check you're using HTTPS URL

---

## Need Help?

- Check Django deployment docs: https://docs.djangoproject.com/en/5.1/howto/deployment/
- Platform-specific docs:
  - Railway: https://docs.railway.app
  - Heroku: https://devcenter.heroku.com/articles/django-app-configuration
  - DigitalOcean: https://docs.digitalocean.com/products/app-platform/
