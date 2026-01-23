# Fix: Worker Timeout on Railway

## Problem
Workers are timing out after 30-60 seconds, causing the app to crash repeatedly.

## Root Cause
The most common cause is a **database connection issue**:
- PostgreSQL database not connected to your Railway service
- `DATABASE_URL` environment variable not set
- Database connection hanging during startup

## Solution 1: Verify Database Connection

### Step 1: Check if PostgreSQL Database Exists

1. **Go to Railway Dashboard**:
   - Railway → Your Project
   - Look for a PostgreSQL database service

2. **If No Database Exists**:
   - Click "New" → "Database" → "Add PostgreSQL"
   - Railway will automatically create `DATABASE_URL` environment variable

3. **If Database Exists**:
   - Click on the PostgreSQL service
   - Check "Variables" tab
   - Verify `DATABASE_URL` is set

### Step 2: Verify DATABASE_URL is Set in Web Service

1. **Go to Railway**:
   - Railway → Your Project → Your Web Service
   - Click "Variables" tab

2. **Check for `DATABASE_URL`**:
   - Should look like: `postgresql://user:password@host:port/dbname`
   - If missing, Railway should auto-set it when you add PostgreSQL

3. **If Missing**:
   - Go to PostgreSQL service → "Variables" tab
   - Copy the `DATABASE_URL` value
   - Go to Web Service → "Variables" tab
   - Add `DATABASE_URL` with the copied value

## Solution 2: Temporarily Use SQLite (For Testing)

If you want to test if the app works without PostgreSQL:

1. **Go to Railway**:
   - Railway → Your Web Service → Variables tab
   - **Remove or rename** `DATABASE_URL` temporarily
   - The app will fall back to SQLite

2. **Redeploy**:
   - Railway will automatically redeploy
   - Check if workers start without timeout

3. **Note**: SQLite is fine for testing, but PostgreSQL is recommended for production

## Solution 3: Check Railway Logs for Database Errors

1. **Go to Railway**:
   - Railway → Your Web Service → Deployments → Latest deployment → Logs

2. **Look for**:
   - Database connection errors
   - "could not connect to server"
   - "timeout" errors
   - "connection refused" errors

3. **Common Errors**:
   ```
   django.db.utils.OperationalError: could not connect to server
   psycopg2.OperationalError: connection timeout
   ```

## Solution 4: Verify Database is Running

1. **Go to Railway**:
   - Railway → Your Project → PostgreSQL database service

2. **Check Status**:
   - Should show "Running" or "Active"
   - If stopped, click "Start" or "Restart"

3. **Check Logs**:
   - Click on PostgreSQL service → Logs
   - Look for any errors

## Quick Checklist

- [ ] PostgreSQL database exists in Railway project
- [ ] PostgreSQL database is running/active
- [ ] `DATABASE_URL` is set in Web Service Variables
- [ ] `DATABASE_URL` format is correct (`postgresql://...`)
- [ ] Checked Railway logs for database connection errors
- [ ] Tried temporarily removing `DATABASE_URL` to test with SQLite

## After Fixing Database Connection

1. **Redeploy**:
   - Railway will automatically redeploy when you fix the database connection
   - Or manually trigger redeploy

2. **Check Logs**:
   - Workers should start without timeout
   - No more "WORKER TIMEOUT" errors

3. **Test App**:
   - Go to: https://kyrex.co/
   - App should load without errors

## Still Not Working?

If workers still timeout after fixing database connection:

1. **Share Railway Logs**:
   - Copy the latest deployment logs
   - Look for any error messages

2. **Check Database Connection**:
   - Verify PostgreSQL is accessible
   - Test connection from Railway shell (if available)

3. **Contact Railway Support**:
   - If database is set up correctly but still timing out
   - Railway support can help diagnose connection issues

---

## Summary

The worker timeout is almost always caused by a database connection issue. Check:
1. PostgreSQL database exists and is running
2. `DATABASE_URL` is set correctly
3. Database connection is accessible

Once the database connection is fixed, workers should start without timeout! 🚀
