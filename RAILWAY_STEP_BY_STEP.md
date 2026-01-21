# Railway Deployment - Step by Step Guide

## ✅ Step 1: Code is Ready!

Your code is committed and ready to deploy.

---

## 🚀 Step 2: Go to Railway

1. **Open your browser** and go to: **https://railway.app**

2. **Click "Login"** (top right)

3. **Select "Login with GitHub"**
   - This is the easiest option
   - Authorize Railway to access your GitHub account

---

## 🆕 Step 3: Create New Project

1. **In Railway dashboard**, click the **"+ New Project"** button (or "Start a New Project")

2. **Select "Deploy from GitHub repo"**
   - You'll see a list of your GitHub repositories
   - Find and click on: **`employee-feedback-platform`** (or your repo name)
   - Click **"Deploy Now"**

3. **Railway will automatically:**
   - Detect it's a Django/Python app
   - Read your `Procfile` and `requirements.txt`
   - Start building your app

4. **Wait for deployment** - This takes 2-5 minutes
   - Watch the logs to see it build
   - You'll see messages like "Installing dependencies..."

---

## 🗄️ Step 4: Add PostgreSQL Database

1. **In your Railway project**, click the **"+ New"** button

2. **Select "Database"** → **"Add PostgreSQL"**

3. **Railway will automatically:**
   - Create a PostgreSQL database
   - Set the `DATABASE_URL` environment variable
   - Link it to your web service

**That's it!** Railway handles everything automatically.

---

## ⚙️ Step 5: Set Environment Variables

1. **Click on your Web Service** (not the database, the web app)

2. **Click on the "Variables" tab** (top navigation)

3. **Add these environment variables** (click "New Variable" for each):

   ```
   DJANGO_SECRET_KEY=X1iO1h4dlwrMDicvPS28n29d1vKVWwRT7WfBbq3SwsaOddcXx75f87YoMPtvw11NmFw
   ```

   ```
   DJANGO_DEBUG=0
   ```

   ```
   DJANGO_ALLOWED_HOSTS=*.railway.app
   ```

   ```
   COMPANY_ACCESS_CODE=123456
   ```
   *(Change this to your actual company code if needed)*

   ```
   HR_NOTIFY_EMAILS=your-email@example.com
   ```
   *(Replace with your actual HR email address)*

   ```
   DJANGO_DEFAULT_FROM_EMAIL=noreply@yourcompany.com
   ```

   ```
   DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
   ```

4. **Important**: Railway automatically sets `DATABASE_URL` - you don't need to add it!

5. **After adding variables**, Railway will automatically redeploy

---

## 🔗 Step 6: Get Your Public URL

1. **Click on your Web Service**

2. **Go to "Settings" tab**

3. **Find "Domains" section**

4. **Click "Generate Domain"** (or it may be auto-generated)

5. **You'll get a URL like**: `https://your-app-production.up.railway.app`

6. **Copy this URL** - This is your public website!

---

## 🗃️ Step 7: Run Migrations

1. **In Railway dashboard**, click on your **Web Service**

2. **Go to "Deployments" tab**

3. **Find your latest deployment**

4. **Click the "..." (three dots)** next to it

5. **Select "Open Shell"** (or "View Logs")

6. **In the shell, run:**
   ```bash
   python manage.py migrate
   ```

7. **You should see:**
   ```
   Operations to perform:
     Apply all migrations: ...
   Running migrations:
     ...
   OK
   ```

---

## 👤 Step 8: Create Admin User

1. **Still in the Railway shell**, run:
   ```bash
   python manage.py createsuperuser
   ```

2. **Follow the prompts:**
   - Username: `hr_admin` (or your choice)
   - Email: Your HR email
   - Password: Create a strong password (type it twice)

3. **Done!**

---

## ✅ Step 9: Test Your Live Site!

1. **Go to your Railway URL**: `https://your-app-production.up.railway.app`

2. **Test employee site:**
   - Homepage should load
   - Try submitting with company access code

3. **Test admin panel:**
   - Go to: `https://your-app-production.up.railway.app/admin/`
   - Login with your admin credentials

---

## 🆘 Troubleshooting

### If deployment fails:
- Check the **Deploy Logs** for errors
- Make sure all environment variables are set
- Verify `requirements.txt` is correct

### If site won't load:
- Check if deployment finished (green status)
- Verify `DJANGO_ALLOWED_HOSTS=*.railway.app`
- Check the logs for errors

### If database error:
- Make sure PostgreSQL is added
- Run migrations in the shell
- Check `DATABASE_URL` is set (should be automatic)

---

## 🎉 Success!

Your app is now **publicly accessible** on the internet!

**Share the URL with your team:**
- Employees can submit anonymously
- HR can login to the admin panel

---

**Need help with any step? Let me know!**
