# Fix "An error occurred while submitting" Error

## Step 1: Check Railway Deploy Logs (MOST IMPORTANT!)

The logs will show the actual error. This is the first thing to check.

### How to Check Logs:

1. **Go to Railway**
   - Railway → Your Service → **Deployments** tab
   - Click on the **most recent deployment**
   - Scroll through the logs

2. **Look for errors:**
   - Red text
   - "Error", "Exception", "Traceback"
   - Python error messages
   - Email-related errors
   - Database errors

3. **Copy the error message**
   - Especially the last 20-30 lines
   - Share it with me!

---

## Common Errors and Fixes

### Error 1: Email Configuration Error

**Error message:**
```
SMTPAuthenticationError
SMTP server connection failed
Username and Password not accepted
```

**Fix:**
1. Check Railway Variables:
   - `EMAIL_HOST_PASSWORD` = Your App Password (16 characters, no spaces)
   - `EMAIL_HOST_USER` = `sales@kyrex.co`
   - `EMAIL_HOST` = `smtp.gmail.com`
   - `EMAIL_PORT` = `587`
   - `EMAIL_USE_TLS` = `True`

2. Verify App Password is correct
3. Make sure 2-Step Verification is enabled

---

### Error 2: CSRF Token Error

**Error message:**
```
CSRF verification failed
Forbidden (403)
```

**Fix:**
1. Check Railway Variables:
   - `CSRF_TRUSTED_ORIGINS` = `https://kyrex.co,https://www.kyrex.co,https://*.up.railway.app`

2. Make sure you're accessing via HTTPS: `https://kyrex.co`

3. Clear browser cache and try again

---

### Error 3: Database Error

**Error message:**
```
OperationalError
could not connect to server
database connection failed
```

**Fix:**
1. Check if PostgreSQL database is running in Railway
2. Check `DATABASE_URL` is set (Railway sets this automatically)
3. Verify database service is active

---

### Error 4: Missing Environment Variable

**Error message:**
```
KeyError
Environment variable not found
```

**Fix:**
1. Check Railway Variables:
   - `HR_NOTIFY_EMAILS` = `sales@kyrex.co`
   - `DJANGO_DEFAULT_FROM_EMAIL` = `sales@kyrex.co`
   - `COMPANY_ACCESS_CODE` = (your access code)

---

### Error 5: Email Backend Error

**Error message:**
```
SMTPException
Connection refused
```

**Fix:**
1. Check Railway Variables:
   - `DJANGO_EMAIL_BACKEND` = `django.core.mail.backends.smtp.EmailBackend`
   - `EMAIL_HOST` = `smtp.gmail.com`
   - `EMAIL_PORT` = `587`

2. If email keeps failing, temporarily use console backend:
   - `DJANGO_EMAIL_BACKEND` = `django.core.mail.backends.console.EmailBackend`
   - This will print emails to logs instead of sending

---

## Step 2: Check Railway Variables

Make sure all required variables are set:

### Required Variables:

```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=kyrex.co,www.kyrex.co,*.up.railway.app
CSRF_TRUSTED_ORIGINS=https://kyrex.co,https://www.kyrex.co,https://*.up.railway.app
HR_NOTIFY_EMAILS=sales@kyrex.co
DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
COMPANY_ACCESS_CODE=your-access-code
```

### Email Variables (if using Gmail):

```
DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=sales@kyrex.co
EMAIL_HOST_PASSWORD=your-app-password
```

---

## Step 3: Temporary Fix - Use Console Email Backend

If email is causing the error, temporarily disable email sending:

1. **Railway → Variables**
2. **Update:**
   - `DJANGO_EMAIL_BACKEND` = `django.core.mail.backends.console.EmailBackend`
3. **Save** (Railway will redeploy)
4. **Try submitting again**

This will print emails to Railway logs instead of sending them, so you can test if the form works.

---

## Step 4: Check Browser Console

1. **Open your browser**
2. **Press F12** (or right-click → Inspect)
3. **Go to "Console" tab**
4. **Try submitting the form**
5. **Look for JavaScript errors**

---

## What to Share With Me

To help you fix this, I need:

1. **The error from Railway logs**
   - Railway → Deployments → Latest deployment → Logs
   - Copy the error (especially last 20-30 lines)

2. **Railway Variables**
   - Which variables are set?
   - Are email variables set?

3. **When does the error happen?**
   - Immediately on submit?
   - After form validation?
   - After email sending?

---

## Quick Action Items

1. ✅ **Check Railway logs** (most important!)
2. ✅ **Verify all Railway variables are set**
3. ✅ **Try temporary console email backend** (to test if email is the issue)
4. ✅ **Check browser console for JavaScript errors**

---

## Most Likely Causes

1. **Email configuration error** (most common)
   - Wrong App Password
   - Missing email variables
   - SMTP connection failed

2. **CSRF token error**
   - `CSRF_TRUSTED_ORIGINS` not set correctly

3. **Database error**
   - Database connection failed

**Check Railway logs first** - that will tell us exactly what's wrong!
