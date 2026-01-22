# Check Database Setup - Quick Guide

## Good News! ✅

Your `Procfile` already has migrations configured to run automatically:
```
release: python manage.py migrate --noinput
```

This means migrations **should** run automatically on every deployment.

---

## Step 1: Verify PostgreSQL Database Exists

1. **Go to Railway**
   - Railway → Your **Project** (not service)
   - Look for a service called "Postgres" or "PostgreSQL"

2. **If you DON'T see a database:**
   - Click **"New"** button
   - Select **"Database"**
   - Select **"Add PostgreSQL"**
   - Railway will automatically create `DATABASE_URL` environment variable

3. **If you DO see a database:**
   - Good! Move to Step 2

---

## Step 2: Check if Migrations Ran

1. **Go to Railway → Your Service → Deployments**
2. **Click on the most recent deployment**
3. **Look for these messages in the logs:**
   - "Running migrations..."
   - "Operations to perform:"
   - "Applying migrations..."
   - "OK" after each migration

4. **If you see errors:**
   - Copy the error message
   - Share it with me

---

## Step 3: Check Database Connection

1. **Railway → Your Service → Variables**
2. **Check if `DATABASE_URL` exists:**
   - If you have PostgreSQL, Railway should auto-create this
   - If it's missing, the database might not be connected

---

## Step 4: Force Redeploy (If Needed)

If migrations didn't run:

1. **Railway → Your Service → Deployments**
2. **Click "Redeploy"** or **"Deploy"**
3. **Watch the logs** to see if migrations run
4. **Look for migration messages**

---

## Quick Checklist

- [ ] PostgreSQL database exists in Railway project
- [ ] `DATABASE_URL` environment variable exists (auto-created by Railway)
- [ ] Migrations ran in deployment logs
- [ ] No migration errors in logs

---

## What to Check Now

1. **Do you have a PostgreSQL database in Railway?**
   - Railway → Your Project
   - Look for "Postgres" service

2. **Check deployment logs for migration messages**
   - Railway → Deployments → Latest deployment → Logs
   - Look for "migrate" or "migrations" messages

3. **Share what you find:**
   - Do you see a database?
   - Do you see migration messages in logs?
   - Any errors?

---

## If Database Doesn't Exist

**Add PostgreSQL database:**
1. Railway → Your Project
2. Click **"New"** → **"Database"** → **"Add PostgreSQL"**
3. Railway will automatically:
   - Create the database
   - Set `DATABASE_URL` environment variable
   - Your next deployment will run migrations automatically

---

## Summary

Your migrations are **already configured** to run automatically! You just need to:
1. Make sure you have a PostgreSQL database
2. Check that migrations ran in the deployment logs
3. If not, add the database and redeploy

Let me know what you find! 🚀
