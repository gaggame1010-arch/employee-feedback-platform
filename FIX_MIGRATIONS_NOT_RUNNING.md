# Fix: Migrations Not Running on Railway

## Problem
The error `relation "submissions_submission" does not exist` means database migrations haven't run on Railway.

## Why This Happens
Railway should automatically run migrations via the `release` command in `Procfile`, but sometimes:
- The release command fails silently
- Railway doesn't detect the Procfile correctly
- Database connection isn't available during release phase

## Solution 1: Check Railway Deployment Logs

1. **Go to Railway Dashboard**:
   - https://railway.app
   - Log in to your account
   - Click on your project
   - Click on your web service

2. **Check Deployment Logs**:
   - Click "Deployments" tab
   - Click on the latest deployment
   - Look for "Release" phase logs
   - Search for "Running migrations..." or "Operations to perform"

3. **What to Look For**:
   ```
   Running migrations...
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions, submissions
   Running migrations:
     Applying submissions.0001_initial... OK
     Applying submissions.0002_hraccesscode... OK
   ```

4. **If You Don't See Migration Messages**:
   - Migrations didn't run
   - Proceed to Solution 2

## Solution 2: Manually Run Migrations via Railway Web Interface

### Option A: Use Railway's "Run Command" Feature

1. **Go to Railway Dashboard**:
   - Railway → Your Project → Your Web Service

2. **Look for "Run Command" or "Shell"**:
   - Some Railway interfaces have a "Run Command" button
   - Or look for a "Shell" tab/button

3. **Run Migration Command**:
   ```bash
   python manage.py migrate
   ```

4. **Check Output**:
   - You should see "Operations to perform..." and "Applying migrations..."
   - If you see "OK" for all migrations, they're applied

### Option B: Trigger a New Deployment

1. **Make a Small Change**:
   - Add a comment to any file (e.g., `README.md`)
   - Commit and push:
     ```bash
     git add .
     git commit -m "Trigger deployment"
     git push origin main
     ```

2. **Watch Deployment Logs**:
   - Railway will automatically deploy
   - Watch the "Release" phase logs
   - Look for migration messages

## Solution 3: Verify Database Connection

1. **Check Railway Variables**:
   - Railway → Your Service → Variables tab
   - Ensure `DATABASE_URL` is set
   - Railway should auto-set this if you added a PostgreSQL database

2. **If `DATABASE_URL` is Missing**:
   - Railway → Your Project → Add PostgreSQL database
   - Railway will automatically set `DATABASE_URL`

## Solution 4: Add Startup Migration Check (Temporary Fix)

If migrations still don't run automatically, we can add a startup check. But first, try Solutions 1-3.

## After Migrations Run

1. **Verify Tables Exist**:
   - Go to: https://kyrex.co/submit/
   - Try submitting a form
   - It should work now

2. **Check Admin Panel**:
   - Go to: https://kyrex.co/admin/
   - Log in
   - You should see submissions

## Quick Checklist

- [ ] Checked Railway deployment logs for migration messages
- [ ] Verified `DATABASE_URL` is set in Railway Variables
- [ ] Tried manually running `python manage.py migrate` via Railway interface
- [ ] Triggered a new deployment to run migrations
- [ ] Tested submission form after migrations ran

## Still Not Working?

If migrations still don't run:
1. Share Railway deployment logs (especially the "Release" phase)
2. Share Railway Variables (hide sensitive values)
3. Check if PostgreSQL database is properly connected
