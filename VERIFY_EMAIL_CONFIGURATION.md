# Verify Email Configuration - Step by Step

## Problem
You changed the email address but still not receiving emails.

## Step 1: Verify Railway Variables Are Set

1. **Go to Railway**:
   - Railway → Your Service → **Variables** tab

2. **Check these variables exist and are correct**:

   ```
   CONTACT_EMAIL=your-new-email@example.com
   EMAIL_HOST_USER=your-gmail@gmail.com (or sales@kyrex.co)
   EMAIL_HOST_PASSWORD=your-16-character-app-password
   DJANGO_DEFAULT_FROM_EMAIL=your-gmail@gmail.com (or sales@kyrex.co)
   DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   ```

3. **Important**:
   - `EMAIL_HOST_USER` should be the Gmail account you're sending FROM
   - `CONTACT_EMAIL` should be where you want to receive emails
   - `EMAIL_HOST_PASSWORD` should be the App Password for `EMAIL_HOST_USER`

## Step 2: Wait for Railway to Redeploy

1. **After changing variables**:
   - Railway automatically redeploys (usually 2-5 minutes)
   - Check Railway → Deployments → Latest deployment
   - Wait until it shows "Active"

2. **If it hasn't redeployed**:
   - Make a small change to trigger deployment
   - Or manually redeploy

## Step 3: Check Railway Logs After Deployment

1. **Submit contact form**:
   - Go to: https://kyrex.co/contact/
   - Fill out and submit

2. **Check Railway logs**:
   - Railway → Deployments → Latest → Logs
   - Look for these lines:

   ```
   CONTACT FORM: Recipient: [your-new-email]
   CONTACT FORM: Email user: [your-gmail]
   CONTACT FORM: Email password set: Yes
   CONTACT FORM: Email send result: 1
   ```

3. **If you see errors**:
   - Look for "SMTP Error" or "Authentication failed"
   - Share the error message

## Step 4: Common Issues

### Issue 1: Wrong Email Configuration

**Problem**: `EMAIL_HOST_USER` and `CONTACT_EMAIL` are different, but App Password is for wrong account.

**Fix**:
- `EMAIL_HOST_USER` = Gmail account you're sending FROM
- `EMAIL_HOST_PASSWORD` = App Password for that Gmail account
- `CONTACT_EMAIL` = Where you want to receive emails (can be different)

### Issue 2: App Password Not Working

**Problem**: App Password is incorrect or expired.

**Fix**:
1. Go to: https://myaccount.google.com/apppasswords
2. Delete old App Password
3. Create new App Password
4. Update `EMAIL_HOST_PASSWORD` in Railway

### Issue 3: Email Going to Spam

**Problem**: Email is sent but goes to spam.

**Fix**:
- Check spam folder
- Mark as "Not spam"
- Check if `FROM` email matches your Gmail account

### Issue 4: Railway Not Redeployed

**Problem**: Changes haven't taken effect yet.

**Fix**:
- Wait 2-5 minutes for auto-deploy
- Or trigger manual redeploy

## Step 5: Test Configuration

1. **Set up test**:
   - `CONTACT_EMAIL` = Your personal Gmail (that you can check)
   - `EMAIL_HOST_USER` = Same Gmail (or different Gmail with App Password)
   - `EMAIL_HOST_PASSWORD` = App Password for `EMAIL_HOST_USER`

2. **Submit form**:
   - Submit contact form
   - Check your personal Gmail inbox and spam

3. **If you receive it**:
   - SMTP is working!
   - Issue is with the original email address

4. **If you don't receive it**:
   - SMTP configuration issue
   - Check App Password, credentials, etc.

## Quick Checklist

- [ ] Verified all email variables are set in Railway
- [ ] `EMAIL_HOST_USER` matches the Gmail account with App Password
- [ ] `EMAIL_HOST_PASSWORD` is correct (16 chars, no spaces)
- [ ] `CONTACT_EMAIL` is the email where you want to receive
- [ ] Waited for Railway to redeploy (2-5 minutes)
- [ ] Checked Railway logs for email configuration
- [ ] Checked spam folder
- [ ] Tried sending to personal Gmail to test

## What to Share

If still not working, share:
1. **Railway logs** (especially the email configuration lines)
2. **What email addresses** you're using (`EMAIL_HOST_USER` and `CONTACT_EMAIL`)
3. **Any error messages** from Railway logs

---

## Summary

After changing email:
1. **Verify variables** are set correctly in Railway
2. **Wait for redeploy** (2-5 minutes)
3. **Check logs** to see what email addresses are being used
4. **Test with personal Gmail** to verify SMTP works

The issue is likely configuration or the email is going to spam! 🚀
