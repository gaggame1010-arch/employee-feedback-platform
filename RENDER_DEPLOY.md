# Deploy to Render (Easy Alternative to Railway)

Render is very similar to Railway and often works when Railway doesn't. Follow these steps:

## Step 1: Sign Up on Render

1. Go to **https://render.com**
2. Click **"Get Started for Free"**
3. Click **"Sign up with GitHub"**
4. Authorize Render to access your GitHub account

## Step 2: Create Web Service

1. In Render dashboard, click **"New +"** button
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - Click **"Connect account"** if not connected
   - Select **"employee-feedback-platform"** repository
   - Click **"Connect"**

## Step 3: Configure Web Service

Fill in these settings:

- **Name**: `employee-feedback-platform` (or any name)
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: Leave empty
- **Runtime**: `Python 3`
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```
  gunicorn anonplatform.wsgi --bind 0.0.0.0:$PORT
  ```
- **Plan**: Select **"Free"** (or paid if you prefer)

Click **"Create Web Service"**

## Step 4: Add PostgreSQL Database

1. Click **"New +"** → **"PostgreSQL"**
2. **Name**: `feedback-db` (or any name)
3. **Database**: Leave default
4. **User**: Leave default
5. **Region**: Same as your web service
6. **Plan**: Select **"Free"**
7. Click **"Create Database"**

**Important**: Note the connection details (you'll see a connection string)

## Step 5: Link Database to Web Service

1. Go back to your **Web Service**
2. Go to **"Environment"** tab
3. Scroll down to **"Environment Variables"**
4. Render automatically adds `DATABASE_URL` when you link the database
5. To link: Go to your database → **"Connections"** → Select your web service

## Step 6: Add Environment Variables

In your **Web Service** → **"Environment"** tab, add these variables:

Click **"Add Environment Variable"** for each:

```
Key: DJANGO_SECRET_KEY
Value: X1iO1h4dlwrMDicvPS28n29d1vKVWwRT7WfBbq3SwsaOddcXx75f87YoMPtvw11NmFw

Key: DJANGO_DEBUG
Value: 0

Key: DJANGO_ALLOWED_HOSTS
Value: your-app-name.onrender.com

Key: COMPANY_ACCESS_CODE
Value: your-secure-code-here

Key: HR_NOTIFY_EMAILS
Value: hr@yourcompany.com

Key: DJANGO_DEFAULT_FROM_EMAIL
Value: noreply@yourcompany.com

Key: DJANGO_EMAIL_BACKEND
Value: django.core.mail.backends.console.EmailBackend
```

⚠️ **Important**: Replace:
- `your-app-name.onrender.com` with your actual Render URL (you'll see it after deployment)
- `your-secure-code-here` with your company access code
- `hr@yourcompany.com` with your actual HR email

## Step 7: Update Procfile for Render

Render uses a slightly different Procfile. Update it:

**Create `render.yaml` file** (or just use the Procfile as-is):

Render will automatically use your Procfile. Make sure it has:
```
release: python manage.py migrate
web: gunicorn anonplatform.wsgi --bind 0.0.0.0:$PORT
```

## Step 8: Deploy and Create Admin User

1. **After deployment**, go to your web service
2. Click **"Shell"** tab (or "Logs" to see if it's running)
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
   - Enter username: `hr_admin`
   - Enter email: Your HR email
   - Enter password: Strong password

## Step 9: Access Your App

Your app will be live at:
```
https://your-app-name.onrender.com
```

**HR Admin**: 
```
https://your-app-name.onrender.com/admin/
```

---

## Troubleshooting Render

**Build fails?**
- Check "Logs" tab for errors
- Make sure all dependencies are in `requirements.txt`
- Check Python version (should be 3.10+)

**App won't start?**
- Check Start Command is correct
- Verify `$PORT` is used (Render automatically sets this)
- Check environment variables are set

**Database connection error?**
- Make sure PostgreSQL is linked to web service
- Check `DATABASE_URL` is in environment variables
- Run migrations in Shell: `python manage.py migrate`

---

## Render Free Tier

- **750 hours/month** - Enough for small apps
- **Free PostgreSQL** - 90 days, then $7/month (or use external DB)
- **Automatic HTTPS** - Included
- **Custom domains** - Supported
- **Auto-deploy from GitHub** - Included

---

## Success Checklist

- [ ] Web service created
- [ ] PostgreSQL database added and linked
- [ ] All environment variables set
- [ ] Deployment successful (green status)
- [ ] Migrations run
- [ ] Superuser created
- [ ] Can access homepage
- [ ] Can access admin panel

---

**Your app is now live on Render! 🎉**
