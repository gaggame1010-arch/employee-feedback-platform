# How to Find Railway Logs - Step by Step

## Where to Find Logs in Railway

### Method 1: Deployment Logs (Recommended)

1. **Go to Railway Dashboard**:
   - https://railway.app
   - Log in to your account

2. **Select Your Project**:
   - Click on your project name

3. **Select Your Web Service**:
   - Click on your web service (the one running Django)

4. **Go to Deployments Tab**:
   - Click "Deployments" tab at the top
   - You should see a list of deployments

5. **Click on Latest Deployment**:
   - Click on the most recent deployment (usually at the top)
   - It should show status like "Active" or "Building"

6. **View Logs**:
   - Look for a "Logs" button or tab
   - OR scroll down to see the logs
   - OR click "View Logs" or "Open Logs"

7. **Submit Contact Form**:
   - Keep the logs page open
   - Go to: https://kyrex.co/contact/
   - Fill out and submit the form
   - **Watch the logs page** - you should see messages appear!

### Method 2: Service Logs

1. **Go to Railway Dashboard**:
   - Railway → Your Project → Your Web Service

2. **Look for "Logs" Tab**:
   - Some Railway interfaces have a "Logs" tab directly in the service
   - Click on it

3. **View Real-time Logs**:
   - You should see real-time logs from your service
   - Submit the contact form and watch for new messages

### Method 3: Service Metrics/Activity

1. **Go to Railway Dashboard**:
   - Railway → Your Project → Your Web Service

2. **Look for "Metrics" or "Activity"**:
   - Some interfaces show logs in these sections
   - Check both tabs

## What to Look For in Logs

After submitting the contact form, you should see messages like:

```
============================================================
CONTACT FORM: Form submitted successfully
CONTACT FORM: Company: [Company Name]
CONTACT FORM: Email: [Email]
CONTACT FORM: Starting email send in background thread
============================================================
============================================================
CONTACT FORM: Starting email send process
CONTACT FORM: Recipient: sales@kyrex.co
CONTACT FORM: Email backend: django.core.mail.backends.console.EmailBackend
CONTACT FORM: Email host: Not set
CONTACT FORM: From email: sales@kyrex.co
============================================================
```

**Key things to check:**
- `Email backend: django.core.mail.backends.console.EmailBackend` → **Emails NOT being sent!**
- `Email backend: django.core.mail.backends.smtp.EmailBackend` → **SMTP configured!**
- `Email host: Not set` → **SMTP not configured!**
- `Email host: smtp.gmail.com` → **SMTP configured!**

## If You Still Don't See Logs

### Option 1: Check Different Time Range

1. **In Railway logs**, look for a time filter
2. **Select "Last hour"** or "Last 24 hours"
3. **Refresh the page**

### Option 2: Check if Deployment Happened

1. **Go to Deployments tab**
2. **Check if there's a recent deployment**
3. **If not, trigger a new deployment:**
   - Make a small change to any file
   - Commit and push to GitHub
   - Railway will auto-deploy

### Option 3: Use Railway CLI

If web interface doesn't show logs:

1. **Install Railway CLI** (if not installed):
   ```bash
   npm install -g @railway/cli
   ```

2. **Login**:
   ```bash
   railway login
   ```

3. **Link project**:
   ```bash
   railway link
   ```

4. **View logs**:
   ```bash
   railway logs
   ```

## Quick Checklist

- [ ] Opened Railway → Your Project → Your Web Service
- [ ] Clicked "Deployments" tab
- [ ] Clicked on latest deployment
- [ ] Found "Logs" button/tab
- [ ] Submitted contact form while logs page is open
- [ ] Looked for "CONTACT FORM:" messages
- [ ] Checked email backend type in logs

## Still Can't Find Logs?

If you still can't see any logs:

1. **Share a screenshot** of what you see in Railway
2. **Tell me which tabs/buttons you see** in your Railway interface
3. **Check if the deployment is still building** (might need to wait)

---

## Summary

Railway logs are usually found in:
- **Deployments tab** → Latest deployment → Logs
- **Service dashboard** → Logs tab
- **Service dashboard** → Metrics/Activity

After submitting the contact form, you should see "CONTACT FORM:" messages in the logs that tell you exactly what's happening with email sending! 🚀
