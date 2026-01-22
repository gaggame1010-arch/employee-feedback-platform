# Complete Guide: Deploy to Railway from Scratch

Follow these steps **in order**. Don't skip any step!

---

## Part 1: Verify Your Code is on GitHub ✅

### Step 1.1: Check Your GitHub Repository

1. Open: https://github.com/gaggame1010-arch/employee-feedback-platform
2. Make sure you can see your files:
   - ✅ `requirements.txt`
   - ✅ `Procfile`
   - ✅ `manage.py`
   - ✅ `anonplatform/` folder
   - ✅ `submissions/` folder

**If files are missing:** Push them to GitHub first.

---

## Part 2: Set Up Railway Account 🔧

### Step 2.1: Create Railway Account

1. Go to: https://railway.app
2. Click **"Start a New Project"** or **"Login"**
3. Choose **"Login with GitHub"** (easiest option)
4. Authorize Railway to access your GitHub

### Step 2.2: Grant Repository Access

**Important:** Railway needs permission to access your repositories.

1. After logging in, Railway may ask for GitHub permissions
2. Click **"Authorize"** or **"Grant Access"**
3. Select **"All repositories"** OR select **`employee-feedback-platform`**
4. Click **"Install"** or **"Authorize"**

**If Railway didn't ask:**
1. Railway → Click your **profile icon** (top right)
2. Click **"Settings"**
3. Go to **"GitHub"** section
4. Click **"Connect GitHub"** or **"Manage Access"**
5. Grant access to your repositories

---

## Part 3: Create Project on Railway 🚀

### Step 3.1: Create New Project

1. Railway Dashboard → Click **"+ New Project"**
2. Select **"Deploy from GitHub repo"**
3. You should see a list of your GitHub repositories
4. Find and click **`employee-feedback-platform`**
5. Railway will create a project and start deploying

**If you don't see your repository:**
- Go back to Part 2.2 and grant access again
- Or try "Login with GitHub" again to refresh permissions

### Step 3.2: Wait for Initial Deployment

Railway will:
- Detect it's a Django app
- Install dependencies
- Try to start (will fail without database/variables - that's OK!)

Wait until you see a service created (even if deployment fails).

---

## Part 4: Add PostgreSQL Database 🗄️

### Step 4.1: Add Database Service

1. In your Railway project, click **"+ New"** (or **"+ Add Service"**)
2. Select **"Database"**
3. Click **"Add PostgreSQL"**
4. Wait 1-2 minutes for provisioning

### Step 4.2: Verify Database

1. You should see a new **PostgreSQL** service in your project
2. Railway automatically sets `DATABASE_URL` environment variable
3. You don't need to do anything else!

---

## Part 5: Set Environment Variables 🔐

### Step 5.1: Open Variables Section

1. Click on your **web service** (not PostgreSQL)
2. Go to **"Variables"** tab
3. Click **"+ New Variable"** or **"+ Add Variable"**

### Step 5.2: Add Required Variables

Add each variable **one by one**:

#### 1. DJANGO_SECRET_KEY
```
Variable Name: DJANGO_SECRET_KEY
Value: 28zHulFLQSNy01jXkl-PyWiFxHFO8BzQWRwiAgnR8xxTalilg8mSlcReVjjwrjd3ubM
```

#### 2. DJANGO_DEBUG
```
Variable Name: DJANGO_DEBUG
Value: 0
```

#### 3. DJANGO_ALLOWED_HOSTS
```
Variable Name: DJANGO_ALLOWED_HOSTS
Value: *.up.railway.app
```

#### 4. COMPANY_ACCESS_CODE
```
Variable Name: COMPANY_ACCESS_CODE
Value: 123456
```
*(Change to your actual company code)*

#### 5. HR_NOTIFY_EMAILS
```
Variable Name: HR_NOTIFY_EMAILS
Value: hr@company.com
```
*(Change to your HR email)*

#### 6. DJANGO_DEFAULT_FROM_EMAIL
```
Variable Name: DJANGO_DEFAULT_FROM_EMAIL
Value: no-reply@company.com
```

#### 7. CSRF_TRUSTED_ORIGINS
```
Variable Name: CSRF_TRUSTED_ORIGINS
Value: https://*.up.railway.app
```

### Step 5.3: Verify Variables

After adding all variables, Railway will **automatically redeploy**. Wait for it to finish.

---

## Part 6: Check Deployment Status 📊

### Step 6.1: View Deployments

1. Click on your **web service**
2. Go to **"Deployments"** tab
3. Click on the **latest deployment**
4. Check the **logs**

### Step 6.2: What to Look For

**Good signs:**
- ✅ "Building..." → Installing dependencies
- ✅ "Installing collected packages: django..."
- ✅ "Starting..."
- ✅ "Application started"

**If you see errors:**
- Note the exact error message
- Common: "No module named django" → Dependencies not installing
- Common: "DisallowedHost" → Need to update ALLOWED_HOSTS

---

## Part 7: Run Database Migrations 🗃️

### Step 7.1: Open Railway Shell

1. Click on your **web service**
2. Click **"Shell"** tab (or "Settings" → "Shell")
3. A terminal will open

### Step 7.2: Run Migrations

In the terminal, type:
```bash
python manage.py migrate
```

You should see:
```
Operations to perform:
  Apply all migrations: ...
Running migrations:
  Applying migrations... OK
```

### Step 7.3: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

You should see:
```
Collecting static files...
...
static files copied
```

---

## Part 8: Create Admin User 👤

### Step 8.1: Create Superuser

Still in Railway Shell, run:
```bash
python manage.py createsuperuser
```

### Step 8.2: Enter Details

Follow the prompts:
- **Username:** `hr_admin` (or your choice)
- **Email:** your HR email address
- **Password:** Create a strong password (save this!)

When it says "Superuser created successfully", you're done!

---

## Part 9: Get Your Public URL 🌐

### Step 9.1: Generate Domain

1. Click on your **web service**
2. Go to **"Settings"** tab
3. Scroll to **"Domains"** section
4. Click **"Generate Domain"** (if no domain exists)
5. Railway will create a domain like: `your-app-name.up.railway.app`

### Step 9.2: Copy Your URL

Copy your public URL. It will look like:
```
https://your-app-name.up.railway.app
```

---

## Part 10: Test Your App ✅

### Step 10.1: Test Homepage

1. Open your URL: `https://your-app-name.up.railway.app`
2. You should see the homepage
3. Try submitting a test submission (use your company access code)

### Step 10.2: Test Admin Panel

1. Go to: `https://your-app-name.up.railway.app/admin/`
2. Log in with your superuser credentials
3. You should see the HR Dashboard!

---

## Troubleshooting 🐛

### Problem: "GitHub repo not found"
**Solution:** Go back to Part 2.2 - Grant repository access

### Problem: "No deployments"
**Solution:** 
- Check GitHub connection in Railway Settings
- Try clicking "Redeploy" in service settings

### Problem: "No module named django"
**Solution:**
- Check Railway build logs
- Verify `requirements.txt` is in GitHub
- Check `railway.json` is in GitHub

### Problem: "DisallowedHost"
**Solution:**
- Update `DJANGO_ALLOWED_HOSTS` to include your exact domain
- Add: `your-app-name.up.railway.app`

### Problem: "Database connection failed"
**Solution:**
- Make sure PostgreSQL is added and running
- Wait 2-3 minutes after adding database
- Check `DATABASE_URL` is automatically set

---

## Complete Checklist ✅

Use this to track your progress:

- [ ] Code is on GitHub
- [ ] Railway account created
- [ ] GitHub connected to Railway
- [ ] Repository access granted
- [ ] Project created on Railway
- [ ] PostgreSQL database added
- [ ] All environment variables set
- [ ] Deployment successful
- [ ] Migrations run
- [ ] Admin user created
- [ ] Public URL obtained
- [ ] Homepage works
- [ ] Admin panel works
- [ ] Can submit test submission

---

## Need Help?

If you get stuck at any step:
1. Note the exact error message
2. Check which part you're on
3. Share the error and I'll help!

**Let's start with Part 1 - verify your code is on GitHub!**
