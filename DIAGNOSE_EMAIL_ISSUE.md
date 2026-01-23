# Diagnose Email Issue - Step by Step

## Problem
You see "Message sent. We'll get back to you soon." but haven't received any email.

## Step 1: Check Railway Logs (Most Important!)

1. **Go to Railway**:
   - Railway → Your Service → **Deployments** tab
   - Click on the **latest deployment**
   - Click **"Logs"** or **"View Logs"**

2. **Submit the contact form again**:
   - Go to: https://kyrex.co/contact/
   - Fill out and submit the form
   - Keep Railway logs open

3. **Look for these messages in Railway logs**:

   **If you see this:**
   ```
   Attempting to send contact form email to sales@kyrex.co
   Email backend: django.core.mail.backends.console.EmailBackend
   ```
   → **This means emails are NOT being sent!** They're only printed to logs.
   → **Solution:** Configure SMTP (see Step 2)

   **If you see this:**
   ```
   Attempting to send contact form email to sales@kyrex.co
   Email backend: django.core.mail.backends.smtp.EmailBackend
   Contact form email sent successfully to sales@kyrex.co
   ```
   → **This means email was sent successfully!**
   → **Check:** Your email inbox and spam folder

   **If you see this:**
   ```
   ERROR: Error sending contact form email to sales@kyrex.co: ...
   ```
   → **This means there's an email sending error**
   → **Solution:** Check the error message and fix it (see Step 3)

## Step 2: Configure SMTP (If Not Already Done)

If logs show `console.EmailBackend`, you need to configure SMTP:

### 2.1 Create Gmail App Password

1. **Go to**: https://myaccount.google.com/apppasswords
2. **Select app**: "Mail"
3. **Select device**: "Other (Custom name)" → Enter "Railway"
4. **Click "Generate"**
5. **Copy the 16-character password** (remove spaces)
   - Example: `abcd efgh ijkl mnop` → `abcdefghijklmnop`

### 2.2 Add Variables to Railway

1. **Go to Railway**:
   - Railway → Your Service → **Variables** tab
   - Click "New Variable" for each:

**Add these 6 variables:**

```
DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=sales@kyrex.co
EMAIL_HOST_PASSWORD=your-16-character-app-password
```

**Important:** Replace `your-16-character-app-password` with your actual App Password (no spaces).

2. **Save all variables**
   - Railway will automatically redeploy

### 2.3 Test Again

1. **Wait for Railway to redeploy** (2-5 minutes)
2. **Submit contact form again**
3. **Check Railway logs** - should now show `smtp.EmailBackend`
4. **Check your email** - should receive it!

## Step 3: Check for Email Errors

If logs show email errors, check the error message:

### Error: "Authentication failed"
- **Cause:** Wrong password or App Password not created
- **Fix:** 
  - Make sure you're using App Password (not regular password)
  - Verify App Password has no spaces
  - Check `EMAIL_HOST_USER` is correct email address

### Error: "SMTP server connection failed"
- **Cause:** Wrong SMTP settings
- **Fix:**
  - Verify `EMAIL_HOST` = `smtp.gmail.com`
  - Verify `EMAIL_PORT` = `587`
  - Verify `EMAIL_USE_TLS` = `True`

### Error: "Username and Password not accepted"
- **Cause:** 2-Step Verification not enabled or App Password incorrect
- **Fix:**
  - Enable 2-Step Verification in Google Account
  - Create new App Password
  - Update `EMAIL_HOST_PASSWORD` in Railway

## Step 4: Check Email Inbox

Even if email was sent successfully, check:

1. **Inbox**: Check your `sales@kyrex.co` inbox
2. **Spam folder**: Emails might go to spam initially
3. **Search**: Search for "Contact Form Submission" in Gmail
4. **Wait**: Sometimes emails take a few minutes to arrive

## Quick Checklist

- [ ] Checked Railway logs for email backend type
- [ ] If `console.EmailBackend` → Configure SMTP (Step 2)
- [ ] If `smtp.EmailBackend` → Check email inbox and spam
- [ ] If errors in logs → Fix error (Step 3)
- [ ] Checked spam folder
- [ ] Waited a few minutes for email to arrive

## What to Share

If you need help, share:
1. **Railway logs** (especially the email-related lines)
2. **What email backend you see** (`console` or `smtp`)
3. **Any error messages** from Railway logs

---

## Summary

The success message means the form worked, but emails aren't being sent because:
1. Email backend is `console` (prints to logs) - **Most common**
2. SMTP is configured but there's an error
3. Emails are being sent but going to spam

**Check Railway logs first** - that will tell you exactly what's happening! 🚀
