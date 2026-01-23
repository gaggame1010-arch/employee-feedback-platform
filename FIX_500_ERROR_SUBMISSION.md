# Fix 500 Error When Submitting

## Common Causes

### 1. Database Migration Not Run (Most Likely)

The `hr_access_code` field was added to the `Submission` model, but the migration might not have run yet.

**Check Railway Logs:**
1. Railway → Your Service → Deployments → Latest deployment → Logs
2. Look for migration messages:
   - "Running migrations..."
   - "Applying submissions.0002_hraccesscode..."
   - Any migration errors

**Fix:**
- Migrations should run automatically via `Procfile` release command
- If not, wait for Railway to redeploy
- Or manually run: `python manage.py migrate` in Railway shell

---

### 2. Database Field Missing

If migration didn't run, the `hr_access_code` field doesn't exist in the database.

**Fix:**
- Wait for migrations to run
- Or manually run migrations

---

### 3. Code Error

There might be an error in the submission creation code.

**Check Railway Logs:**
- Look for the actual error message
- Should show: "Error creating submission: [error]"
- Share the error with me to fix it

---

## Quick Fix Steps

### Step 1: Check Railway Logs

1. Railway → Your Service → Deployments → Latest deployment
2. Scroll through logs
3. Look for:
   - Migration errors
   - "Error creating submission" messages
   - Python tracebacks

### Step 2: Verify Migrations Ran

Look for these messages in logs:
```
Running migrations...
Applying submissions.0002_hraccesscode... OK
```

### Step 3: Check Database

If migrations didn't run:
- Wait for Railway to redeploy (migrations run automatically)
- Or manually trigger: Railway → Deployments → Redeploy

---

## What to Share

To help fix this, share:

1. **The error from Railway logs:**
   - Railway → Deployments → Latest deployment → Logs
   - Look for "Error creating submission" or traceback
   - Copy the error message

2. **Migration status:**
   - Do you see migration messages in logs?
   - Did migrations run successfully?

---

## Temporary Fix (If Needed)

If you need to test while fixing:

1. **Railway → Variables**
2. **Set:** `DJANGO_DEBUG=1` (temporarily)
3. **Save** (Railway will redeploy)
4. **Try submitting again**
5. **You'll see the actual error** on the page
6. **Share the error** with me

**Remember to set `DJANGO_DEBUG=0` back after!**

---

## Most Likely Fix

**Wait for migrations to run:**
- Railway should run migrations automatically
- Check deployment logs to confirm
- If migrations failed, share the error

The 500 error is likely because the database doesn't have the new `hr_access_code` field yet. Once migrations run, it should work!
