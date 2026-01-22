# Railway "Application failed to respond" - Step-by-Step Fix

## ⚠️ This Error Means Your App Crashed

"Application failed to respond" = Your Django app failed to start. We need to find WHY.

---

## Step 1: Check Railway Deploy Logs (MOST IMPORTANT!)

### How to View Logs:

1. **Go to Railway Dashboard**
   - Visit: https://railway.app
   - Log in

2. **Open Your Service**
   - Click on your **web service** (the one showing the error)

3. **View Deployments**
   - Click on **"Deployments"** tab (top menu)
   - You'll see a list of deployments

4. **Open Latest Deployment**
   - Click on the **most recent deployment** (usually at the top)
   - It might show "Failed" or have a red indicator

5. **View Logs**
   - Scroll down to see the deployment logs
   - Look for **red text** or **error messages**
   - Look for lines that say:
     - "Error"
     - "Failed"
     - "Exception"
     - "Traceback"
     - "ModuleNotFoundError"
     - "OperationalError"

6. **Copy the Error**
   - Scroll to find the actual error message
   - Copy the entire error (or at least the last few lines)
   - **Share it with me!**

---

## Step 2: Verify Required Environment Variables

Go to **Railway → Your Service → Variables** tab and check:

### ✅ Required Variables Checklist:

- [ ] **DJANGO_SECRET_KEY** 
  - Value: Should be a long random string (like: `QapZedqu2Thm47z82sEefiQytyFACJesvmX9hchOJTwMaJrq4P3kL_wD3VfCwpqz1tM`)
  - **If missing, add it now!**

- [ ] **DJANGO_DEBUG**
  - Value: `0` (for production)

- [ ] **DJANGO_ALLOWED_HOSTS**
  - Value: `kyrex.co,www.kyrex.co,*.up.railway.app`

- [ ] **CSRF_TRUSTED_ORIGINS**
  - Value: `https://kyrex.co,https://www.kyrex.co,https://*.up.railway.app`

- [ ] **HR_NOTIFY_EMAILS**
  - Value: `sales@kyrex.co`

- [ ] **DJANGO_DEFAULT_FROM_EMAIL**
  - Value: `sales@kyrex.co`

- [ ] **COMPANY_ACCESS_CODE**
  - Value: Your company access code (e.g., `123456`)

---

## Step 3: Verify Database

1. **Go to Railway Dashboard**
   - Railway → Your **Project** (not service)

2. **Check for PostgreSQL Database**
   - Look for a service called "Postgres" or "PostgreSQL"
   - If you don't see one, you need to add it!

3. **Add Database (if missing)**
   - Click **"New"** button
   - Select **"Database"**
   - Select **"Add PostgreSQL"**
   - Railway will automatically create `DATABASE_URL` environment variable

---

## Step 4: Common Errors and Quick Fixes

### Error: "The SECRET_KEY setting must not be empty"

**Fix:**
1. Railway → Variables
2. Add: `DJANGO_SECRET_KEY` = `QapZedqu2Thm47z82sEefiQytyFACJesvmX9hchOJTwMaJrq4P3kL_wD3VfCwpqz1tM`
3. Save (Railway will redeploy)

---

### Error: "could not connect to server" or "database connection failed"

**Fix:**
1. Add PostgreSQL database:
   - Railway → Your Project → **New** → **Database** → **Add PostgreSQL**
2. Railway automatically creates `DATABASE_URL`
3. Redeploy

---

### Error: "ModuleNotFoundError: No module named 'gunicorn'"

**Fix:**
1. Check `requirements.txt` includes:
   ```
   gunicorn
   whitenoise
   psycopg2-binary
   dj-database-url
   django>=6.0.1
   ```
2. If missing, add them
3. Commit and push to GitHub
4. Railway will redeploy

---

### Error: "DisallowedHost" or "Invalid HTTP_HOST header"

**Fix:**
1. Railway → Variables
2. Update `DJANGO_ALLOWED_HOSTS`:
   - Value: `kyrex.co,www.kyrex.co,*.up.railway.app`
3. Save

---

## Step 5: Manual Redeploy

After fixing issues:

1. **Railway → Your Service → Deployments**
2. Click **"Redeploy"** or **"Deploy"** button
3. Watch the logs to see if it succeeds

---

## What to Share With Me

To help you fix this, I need:

1. **The error message from Railway deploy logs**
   - Railway → Deployments → Latest deployment → Logs
   - Copy the error (especially the last 10-20 lines)

2. **Screenshot or list of your Railway Variables**
   - Railway → Variables tab
   - Just tell me which variables you have set

3. **Do you have a PostgreSQL database?**
   - Yes/No

---

## Quick Action Items

**Do these NOW:**

1. ✅ **Check Railway deploy logs** (Step 1 above)
2. ✅ **Verify DJANGO_SECRET_KEY is set** (Step 2)
3. ✅ **Verify PostgreSQL database exists** (Step 3)
4. ✅ **Share the error message** from logs

Once I see the actual error, I can give you the exact fix! 🚀
