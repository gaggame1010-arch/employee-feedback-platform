# Check Email Configuration - Quick Guide

## Step 1: Check Railway Logs

1. **Go to Railway**:
   - Railway → Your Service → Deployments → Latest deployment → Logs

2. **Submit the contact form** at https://kyrex.co/contact/

3. **Look for these messages in Railway logs**:
   - "Attempting to send contact form email to sales@kyrex.co"
   - "Email backend: django.core.mail.backends.console.EmailBackend" ← **This means emails are NOT being sent!**
   - OR "Email backend: django.core.mail.backends.smtp.EmailBackend" ← **This means SMTP is configured**

4. **If you see `console.EmailBackend`**:
   - Emails are being printed to logs, not actually sent
   - You need to configure SMTP (see Step 2)

## Step 2: Check Railway Variables

1. **Go to Railway**:
   - Railway → Your Service → **Variables** tab

2. **Check if these variables exist**:
   - `DJANGO_EMAIL_BACKEND` - Should be `django.core.mail.backends.smtp.EmailBackend`
   - `EMAIL_HOST` - Should be `smtp.gmail.com`
   - `EMAIL_PORT` - Should be `587`
   - `EMAIL_USE_TLS` - Should be `True`
   - `EMAIL_HOST_USER` - Should be `sales@kyrex.co` (or your Gmail)
   - `EMAIL_HOST_PASSWORD` - Should be your Gmail App Password (16 characters)

3. **If any are missing**, you need to set them up (see Step 3)

## Step 3: Set Up Gmail SMTP (If Not Already Done)

### 3.1 Create Gmail App Password

1. **Enable 2-Step Verification** (if not already):
   - Go to: https://myaccount.google.com/security
   - Click "2-Step Verification"
   - Follow setup

2. **Create App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Select app: "Mail"
   - Select device: "Other (Custom name)" → Enter "Railway"
   - Click "Generate"
   - **Copy the 16-character password** (remove spaces)
   - Example: `abcd efgh ijkl mnop` → `abcdefghijklmnop`

### 3.2 Add Variables to Railway

1. **Go to Railway**:
   - Railway → Your Service → **Variables** tab
   - Click "New Variable" for each:

**Variable 1:**
- **Name:** `DJANGO_EMAIL_BACKEND`
- **Value:** `django.core.mail.backends.smtp.EmailBackend`

**Variable 2:**
- **Name:** `EMAIL_HOST`
- **Value:** `smtp.gmail.com`

**Variable 3:**
- **Name:** `EMAIL_PORT`
- **Value:** `587`

**Variable 4:**
- **Name:** `EMAIL_USE_TLS`
- **Value:** `True`

**Variable 5:**
- **Name:** `EMAIL_HOST_USER`
- **Value:** `sales@kyrex.co` (or your Gmail address)

**Variable 6:**
- **Name:** `EMAIL_HOST_PASSWORD`
- **Value:** `abcdefghijklmnop` (your 16-character App Password, no spaces)

2. **Save all variables**
   - Railway will automatically redeploy

## Step 4: Test After Configuration

1. **Wait for Railway to redeploy** (2-5 minutes)

2. **Submit contact form again**:
   - Go to: https://kyrex.co/contact/
   - Fill out the form
   - Submit

3. **Check Railway logs**:
   - Should see: "Email backend: django.core.mail.backends.smtp.EmailBackend"
   - Should see: "Contact form email sent successfully"

4. **Check your email**:
   - Go to: https://mail.google.com/
   - Log in with: `sales@kyrex.co`
   - Check inbox (and spam folder)
   - You should receive the email!

## Quick Checklist

- [ ] Checked Railway logs for email backend type
- [ ] Verified `DJANGO_EMAIL_BACKEND` is set to `smtp.EmailBackend`
- [ ] Created Gmail App Password (16 characters)
- [ ] Added all 6 email variables to Railway
- [ ] Railway redeployed
- [ ] Tested contact form again
- [ ] Checked email inbox (and spam)

## Common Issues

### Issue: Still seeing `console.EmailBackend` in logs

**Fix:** Make sure `DJANGO_EMAIL_BACKEND` is set correctly in Railway Variables

### Issue: "Authentication failed" error

**Fix:** 
- Make sure you're using App Password (not regular password)
- Verify App Password has no spaces
- Check `EMAIL_HOST_USER` is correct email address

### Issue: Emails going to spam

**Fix:**
- Check spam folder
- Mark as "Not spam"
- Gmail will learn to deliver to inbox

---

## Summary

If you haven't received emails, it's almost certainly because:
1. Email backend is set to `console` (prints to logs)
2. SMTP variables are not configured in Railway

Follow Steps 1-3 above to configure email properly! 🚀
