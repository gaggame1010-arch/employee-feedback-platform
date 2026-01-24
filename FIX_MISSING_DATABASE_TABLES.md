# Fix "no such table" Error - Migrations Not Run

## The Problem

Error: `no such table: submissions_submission`

This means **migrations haven't run** - the database tables don't exist yet.

---

## Root Cause

Your `Procfile` has migrations configured:
```
release: python manage.py migrate --noinput && ...
```

But migrations might not be running because:
1. **No PostgreSQL database** - Railway might be using SQLite
2. **Migrations failing silently** - The `|| true` hides errors
3. **Database connection issue**

---

## Step 1: Check if You Have PostgreSQL Database

1. **Railway → Your Project** (not service)
2. **Look for a service called:**
   - "Postgres" or "PostgreSQL"
   - Database service

3. **If you DON'T see a database:**
   - Click **"New"** → **"Database"** → **"Add PostgreSQL"**
   - Railway will automatically create `DATABASE_URL` environment variable

4. **If you DO see a database:**
   - Good! Move to Step 2

---

## Step 2: Check Migration Logs

1. **Railway → Your Service → Deployments → Latest deployment → Logs**
2. **Look for:**
   - "Running migrations..."
   - "Operations to perform:"
   - "Applying migrations..."
   - "OK" after each migration
   - Any migration errors

3. **If you see migration errors:**
   - Copy the error
   - Share it with me

---

## Step 3: Verify Database Connection

1. **Railway → Your Service → Variables**
2. **Check if `DATABASE_URL` exists:**
   - If you have PostgreSQL, Railway should auto-create this
   - If missing, the database might not be connected

---

## Step 4: Force Migrations to Run

If migrations aren't running automatically:

### Option A: Check Procfile Release Command

Your `Procfile` should have:
```
release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py create_admin || true
```

The `|| true` means it won't fail the deployment if migrations fail, which hides errors!

### Option B: Manually Trigger Migrations

1. **Railway → Your Service → Deployments → Redeploy**
2. **Watch the logs** to see if migrations run
3. **Look for migration messages**

---

## Quick Fix: Add PostgreSQL Database

If you don't have a PostgreSQL database:

1. **Railway → Your Project**
2. **Click "New" → "Database" → "Add PostgreSQL"**
3. **Railway will:**
   - Create the database
   - Set `DATABASE_URL` automatically
   - Your next deployment will run migrations

---

## What to Check Now

1. **Do you have a PostgreSQL database in Railway?**
   - Railway → Your Project
   - Look for "Postgres" service

2. **Check deployment logs for migrations:**
   - Railway → Deployments → Latest deployment → Logs
   - Do you see "Running migrations..."?

3. **Check `DATABASE_URL` variable:**
   - Railway → Variables
   - Does `DATABASE_URL` exist?

---

## Most Likely Fix

**Add PostgreSQL database:**
1. Railway → Your Project → **New** → **Database** → **Add PostgreSQL**
2. Wait for Railway to set `DATABASE_URL`
3. Railway will automatically redeploy
4. Migrations will run automatically
5. Tables will be created

---

## Summary

- **Error:** Database tables don't exist (migrations not run)
- **Cause:** No PostgreSQL database or migrations not running
- **Fix:** Add PostgreSQL database in Railway

**Do you have a PostgreSQL database in your Railway project?** If not, add one and migrations will run automatically!
