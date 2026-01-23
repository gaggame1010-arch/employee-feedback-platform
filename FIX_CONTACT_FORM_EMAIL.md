# Fix: Contact Form Not Sending Emails

## Problem
You submitted the contact form but didn't receive an email at `sales@kyrex.co`.

## Why This Happens
The contact form needs SMTP email configuration to actually send emails. By default, Django just prints emails to the console (logs).

## Solution: Configure Gmail SMTP in Railway

### Step 1: Check Current Email Configuration

1. **Go to Railway**:
   - Railway → Your Service → **Variables** tab
   - Look for these variables:
     - `DJANGO_EMAIL_BACKEND`
     - `EMAIL_HOST`
     - `EMAIL_PORT`
     - `EMAIL_USE_TLS`
     - `EMAIL_HOST_USER`
     - `EMAIL_HOST_PASSWORD`

2. **If these are missing or incorrect**, proceed to Step 2.

### Step 2: Set Up Gmail App Password

**Important:** You can't use your regular Gmail password. You need an **App Password**.

1. **Enable 2-Step Verification** (if not already enabled):
   - Go to: https://myaccount.google.com/security
   - Click "2-Step Verification"
   - Follow the setup process

2. **Create App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Select app: "Mail"
   - Select device: "Other (Custom name)" → Enter "Railway"
   - Click "Generate"
   - **Copy the 16-character password** (remove spaces)
   - Example: `abcd efgh ijkl mnop` → `abcdefghijklmnop`

### Step 3: Add Email Variables to Railway

1. **Go to Railway**:
   - Railway → Your Service → **Variables** tab
   - Click "New Variable" for each one below

2. **Add these variables**:

   **Variable 1: Email Backend**
   - **Name:** `DJANGO_EMAIL_BACKEND`
   - **Value:** `django.core.mail.backends.smtp.EmailBackend`

   **Variable 2: Email Host**
   - **Name:** `EMAIL_HOST`
   - **Value:** `smtp.gmail.com`

   **Variable 3: Email Port**
   - **Name:** `EMAIL_PORT`
   - **Value:** `587`

   **Variable 4: Use TLS**
   - **Name:** `EMAIL_USE_TLS`
   - **Value:** `True`

   **Variable 5: Email Username**
   - **Name:** `EMAIL_HOST_USER`
   - **Value:** `sales@kyrex.co` (or your Gmail address)

   **Variable 6: Email Password**
   - **Name:** `EMAIL_HOST_PASSWORD`
   - **Value:** `abcdefghijklmnop` (your 16-character App Password, no spaces)

3. **Save all variables**
   - Railway will automatically redeploy

### Step 4: Verify Configuration

1. **Check Railway Logs**:
   - Railway → Your Service → Deployments → Latest deployment → Logs
   - Look for email-related errors
   - After deployment, you should see no email errors

2. **Test the Contact Form**:
   - Go to: https://kyrex.co/contact/
   - Fill out the form
   - Submit it
   - Check Railway logs for:
     - "Attempting to send contact form email to sales@kyrex.co"
     - "Contact form email sent successfully"
     - Or any error messages

3. **Check Your Email**:
   - Go to: https://mail.google.com/
   - Log in with: `sales@kyrex.co`
   - Check inbox (and spam folder)
   - You should receive an email with subject: "Contact Form Submission from [Name]"

## Common Issues

### Issue 1: "Authentication failed"

**Cause:** Wrong password or App Password not created

**Fix:**
- Make sure you're using **App Password** (not regular password)
- Verify App Password has no spaces
- Check `EMAIL_HOST_USER` is correct email address

### Issue 2: "SMTP server connection failed"

**Cause:** Wrong SMTP settings

**Fix:**
- Verify `EMAIL_HOST` = `smtp.gmail.com`
- Verify `EMAIL_PORT` = `587`
- Verify `EMAIL_USE_TLS` = `True`

### Issue 3: Emails going to spam

**Fix:**
- Check spam folder
- Mark as "Not spam" if found
- Gmail will learn to deliver to inbox

### Issue 4: Still not receiving emails

**Check:**
1. Railway logs for errors (see Step 4)
2. Gmail account is active (`sales@kyrex.co`)
3. App Password is correct
4. All environment variables are set correctly
5. Railway redeployed after adding variables

## Quick Checklist

- [ ] 2-Step Verification enabled in Google Account
- [ ] App Password created (16 characters, no spaces)
- [ ] Railway variables added:
  - [ ] `DJANGO_EMAIL_BACKEND` = `django.core.mail.backends.smtp.EmailBackend`
  - [ ] `EMAIL_HOST` = `smtp.gmail.com`
  - [ ] `EMAIL_PORT` = `587`
  - [ ] `EMAIL_USE_TLS` = `True`
  - [ ] `EMAIL_HOST_USER` = `sales@kyrex.co`
  - [ ] `EMAIL_HOST_PASSWORD` = (your App Password)
- [ ] Railway redeployed
- [ ] Tested contact form
- [ ] Checked Railway logs for email messages
- [ ] Checked Gmail inbox (and spam)

## Railway Variables Summary

Copy-paste these into Railway → Variables:

```
DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=sales@kyrex.co
EMAIL_HOST_PASSWORD=your-16-character-app-password
```

**Important:** Replace `your-16-character-app-password` with your actual App Password (no spaces).

## After Configuration

Once configured:
- ✅ Contact form emails will be sent to `sales@kyrex.co`
- ✅ You'll receive emails when someone submits the contact form
- ✅ All emails sent from `sales@kyrex.co`

## Need Help?

If emails still aren't working:
1. Check Railway logs for detailed error messages
2. Verify App Password is correct
3. Test email sending via Railway shell (see CONFIGURE_GMAIL_FOR_DJANGO.md)
4. Check Gmail inbox and spam folder

Let me know what errors you see in Railway logs! 🚀
