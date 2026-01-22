# Configure Gmail (Google Workspace) for Django App

## Overview

This guide will help you configure your Django app to send emails via Gmail (Google Workspace) for `kyrex.co`.

---

## Step 1: Create Gmail App Password

**Important:** You can't use your regular Gmail password. You need to create an **App Password**.

### 1.1 Enable 2-Step Verification (If Not Already Enabled)

1. Go to: https://myaccount.google.com/security
2. Click "2-Step Verification"
3. Follow the setup process (if not already enabled)

### 1.2 Create App Password

1. Go to: https://myaccount.google.com/apppasswords
   - Or: Google Account → Security → 2-Step Verification → App passwords

2. **Select app:**
   - Choose "Mail" from dropdown

3. **Select device:**
   - Choose "Other (Custom name)"
   - Enter: "Django App" or "Railway"

4. **Click "Generate"**
   - Google will show you a 16-character password
   - **Copy this password immediately!** (You won't see it again)
   - Example: `abcd efgh ijkl mnop`

5. **Save the password:**
   - Remove spaces: `abcdefghijklmnop`
   - Save it somewhere safe (you'll need it for Railway)

---

## Step 2: Create Email Account in Google Workspace (If Not Done)

1. Go to: https://admin.google.com/
2. Click "Users" → "Add new user"
3. Create: `sales@kyrex.co`
4. Set a password
5. Save the credentials

---

## Step 3: Update Railway Environment Variables

1. **Go to Railway**
   - Railway → Your Service → **Variables** tab

2. **Add/Update these variables:**

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

   **Variable 6: Email Password (App Password)**
   - **Name:** `EMAIL_HOST_PASSWORD`
   - **Value:** `abcdefghijklmnop` (your 16-character App Password, no spaces)

3. **Save all variables**
   - Railway will automatically redeploy

---

## Step 4: Verify Django Settings

Your `settings.py` should already be configured correctly. It reads from environment variables:

```python
EMAIL_BACKEND = os.environ.get(
    "DJANGO_EMAIL_BACKEND",
    "django.core.mail.backends.console.EmailBackend",
)
```

This means:
- If `DJANGO_EMAIL_BACKEND` is set → Uses SMTP (Gmail)
- If not set → Uses console (prints to logs)

---

## Step 5: Test Email Configuration

### Option 1: Test via Railway Shell

1. **Railway → Your Service → Deployments → Latest deployment**
2. **Click "Shell" or "Open Shell"**
3. **Run:**
   ```bash
   python manage.py shell
   ```
4. **In Python shell, run:**
   ```python
   from django.core.mail import send_mail
   send_mail(
       'Test Email',
       'This is a test email from Django.',
       'sales@kyrex.co',
       ['sales@kyrex.co'],  # Send to yourself
       fail_silently=False,
   )
   ```
5. **Check your Gmail inbox** - you should receive the email!

### Option 2: Test via Admin Panel

1. Visit: https://kyrex.co/admin/
2. Log in
3. Create a test submission
4. Check if email notification is sent

---

## Step 6: Verify Email is Working

### Check Railway Logs

1. **Railway → Your Service → Deployments → Latest deployment → Logs**
2. **Look for:**
   - No email errors
   - Successful email sending messages

### Check Gmail Inbox

1. **Go to:** https://mail.google.com/
2. **Log in with:** `sales@kyrex.co`
3. **Check inbox** for test emails

---

## Troubleshooting

### Error: "Authentication failed"

**Cause:** Wrong password or App Password not created

**Fix:**
1. Make sure you're using **App Password** (not regular password)
2. Verify App Password has no spaces
3. Check `EMAIL_HOST_USER` is correct email address

---

### Error: "SMTP server connection failed"

**Cause:** Wrong SMTP settings

**Fix:**
1. Verify `EMAIL_HOST` = `smtp.gmail.com`
2. Verify `EMAIL_PORT` = `587`
3. Verify `EMAIL_USE_TLS` = `True`

---

### Error: "Username and Password not accepted"

**Cause:** 2-Step Verification not enabled or App Password incorrect

**Fix:**
1. Enable 2-Step Verification in Google Account
2. Create new App Password
3. Update `EMAIL_HOST_PASSWORD` in Railway

---

### Emails Not Sending

**Check:**
1. Railway logs for errors
2. Gmail account is active
3. App Password is correct
4. Environment variables are set correctly

---

## Quick Checklist

- [ ] 2-Step Verification enabled in Google Account
- [ ] App Password created (16 characters, no spaces)
- [ ] Email account created in Google Workspace (`sales@kyrex.co`)
- [ ] Railway variables updated:
  - [ ] `DJANGO_EMAIL_BACKEND` = `django.core.mail.backends.smtp.EmailBackend`
  - [ ] `EMAIL_HOST` = `smtp.gmail.com`
  - [ ] `EMAIL_PORT` = `587`
  - [ ] `EMAIL_USE_TLS` = `True`
  - [ ] `EMAIL_HOST_USER` = `sales@kyrex.co`
  - [ ] `EMAIL_HOST_PASSWORD` = (your App Password)
- [ ] Railway redeployed
- [ ] Test email sent successfully

---

## Railway Variables Summary

Add these to Railway → Variables:

```
DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=sales@kyrex.co
EMAIL_HOST_PASSWORD=your-16-character-app-password
```

**Important:** Replace `your-16-character-app-password` with your actual App Password (no spaces).

---

## After Configuration

Once configured:
- ✅ HR notifications will be sent to `sales@kyrex.co`
- ✅ Email notifications work for new submissions
- ✅ All emails sent from `sales@kyrex.co`

---

## Need Help?

If emails aren't working:
1. Check Railway logs for errors
2. Verify App Password is correct
3. Test email sending via Railway shell
4. Check Gmail inbox for received emails

Let me know if you need help with any step! 🚀
