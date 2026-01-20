# Step-by-Step Railway Deployment Guide

Follow these steps to deploy your app on Railway - the easiest and safest option.

## Prerequisites

1. GitHub account (free) - https://github.com
2. Railway account (free tier available) - https://railway.app

---

## Step 1: Push Your Code to GitHub

1. **Go to GitHub** and create a new repository:
   - Click "+" → "New repository"
   - Name it: `employee-feedback-platform` (or any name you like)
   - Make it **Public** (Railway can access it)
   - **Don't** initialize with README (your code already has one)

2. **Push your code**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

   Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repo name.

---

## Step 2: Deploy on Railway

1. **Go to Railway**: https://railway.app

2. **Sign up** (use "Login with GitHub" - easiest option)

3. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect it's a Django app

4. **Railway will start deploying** automatically - wait for it to finish

---

## Step 3: Add PostgreSQL Database

1. In your Railway project, click **"+ New"**

2. Select **"Database"** → **"Add PostgreSQL"**

3. Railway will automatically:
   - Create a PostgreSQL database
   - Set the `DATABASE_URL` environment variable
   - Your app will connect automatically!

---

## Step 4: Configure Environment Variables

1. In your Railway project, click on your **web service**

2. Go to **"Variables"** tab

3. Click **"+ New Variable"** and add these one by one:

   ```
   Variable Name: DJANGO_SECRET_KEY
   Value: [Generate a strong key - see below]
   ```

   **Generate Secret Key** (run this locally):
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(50))"
   ```
   Copy the output and paste it as the value.

4. **Add all these variables**:
   
   ```
   DJANGO_DEBUG=0
   DJANGO_ALLOWED_HOSTS=*.railway.app
   COMPANY_ACCESS_CODE=your-secure-code-12345
   HR_NOTIFY_EMAILS=hr@yourcompany.com
   DJANGO_DEFAULT_FROM_EMAIL=noreply@yourcompany.com
   DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
   ```

   ⚠️ **Important**: Replace:
   - `your-secure-code-12345` with your actual company access code
   - `hr@yourcompany.com` with your HR email address
   - `noreply@yourcompany.com` with your preferred sender email

---

## Step 5: Run Database Migrations

1. In Railway, go to your **web service**

2. Click on the **"Deployments"** tab

3. Click the **three dots** (...) on the latest deployment

4. Select **"Open Shell"**

5. Run these commands:
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser
   ```
   
   When creating superuser, enter:
   - Username: `hr_admin` (or your choice)
   - Email: Your HR email
   - Password: Create a strong password (you'll need this to log in)

6. **Close the shell** - your app will redeploy automatically

---

## Step 6: Get Your Public URL

1. In Railway, go to your **web service**

2. Click on the **"Settings"** tab

3. Scroll down to **"Domains"**

4. Railway gives you a free domain like: `your-app-production.up.railway.app`

5. **Copy this URL** - this is your public website!

---

## Step 7: Test Your Deployment

1. **Visit your public URL**: `https://your-app-production.up.railway.app`

2. **Test Employee Side**:
   - Go to homepage
   - Enter your company access code
   - Submit a test submission
   - Save the receipt code

3. **Test HR Admin**:
   - Go to: `https://your-app-production.up.railway.app/admin/`
   - Log in with your superuser credentials
   - You should see the HR dashboard!

---

## Step 8: Set Up Custom Domain (Optional)

If you want your own domain (like `feedback.yourcompany.com`):

1. In Railway, go to **Settings** → **Domains**
2. Click **"Generate Domain"** or **"Custom Domain"**
3. Follow Railway's instructions to add DNS records

---

## Railway Free Tier Limits

- **$5 free credit monthly** - More than enough for small apps
- **500 hours** of runtime per month
- PostgreSQL database included
- Automatic HTTPS
- Unlimited deployments

---

## Security Checklist ✅

After deployment, verify:

- [ ] `DJANGO_DEBUG=0` (production mode)
- [ ] Strong `DJANGO_SECRET_KEY` set
- [ ] `ALLOWED_HOSTS` includes `*.railway.app`
- [ ] HTTPS is working (check the padlock icon)
- [ ] Company access code is set
- [ ] HR email notifications configured
- [ ] Superuser created for HR access

---

## Troubleshooting

**App won't deploy?**
- Check the "Deployments" tab for error logs
- Make sure all environment variables are set
- Verify `requirements.txt` is correct

**Database errors?**
- Make sure PostgreSQL database is added
- Check that `DATABASE_URL` is automatically set by Railway
- Run migrations in the shell: `python manage.py migrate`

**Can't access admin?**
- Make sure you created a superuser: `python manage.py createsuperuser`
- Use HTTPS URL (not HTTP)
- Check you're using the correct username/password

**Static files not loading?**
- Railway automatically runs `collectstatic` from the Procfile
- Check the deployment logs for any errors

---

## Need Help?

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Check deployment logs in Railway dashboard

---

## Next Steps After Deployment

1. **Share the company access code** with your employees
2. **Share the admin URL** with HR team
3. **Set up email notifications** (see DEPLOYMENT.md for email setup)
4. **Monitor submissions** in the HR dashboard

**Your app is now live and accessible to the public! 🎉**
