# Email Sent But Not Received - Troubleshooting Guide

## Problem
Railway logs show "Email sent successfully" but you're not receiving emails at `sales@kyrex.co`.

## Possible Causes

### 1. Email Going to Spam (Most Common)

**Check:**
1. **Gmail Spam Folder**:
   - Go to: https://mail.google.com/
   - Log in with: `sales@kyrex.co`
   - Click "Spam" folder (left sidebar)
   - Look for emails with subject: "Contact Form Submission from [Company Name]"

2. **Search Gmail**:
   - In Gmail, search for: `from:sales@kyrex.co` OR `subject:"Contact Form Submission"`
   - This will find emails even if they're in spam

3. **If Found in Spam**:
   - Open the email
   - Click "Not spam" button
   - Future emails should go to inbox

### 2. Wrong Email Address

**Check:**
1. **Verify Email Address**:
   - Railway → Your Service → Variables tab
   - Check `CONTACT_EMAIL` variable
   - Should be: `sales@kyrex.co`
   - Make sure there are no typos

2. **Verify Gmail Account**:
   - Make sure `sales@kyrex.co` is a valid Gmail/Google Workspace account
   - Try logging in to confirm the account exists

### 3. Gmail App Password Issue

**Check:**
1. **Verify App Password**:
   - Railway → Your Service → Variables tab
   - Check `EMAIL_HOST_PASSWORD`
   - Should be 16 characters, no spaces
   - Example: `abcdefghijklmnop`

2. **Verify Email User**:
   - Railway → Variables tab
   - Check `EMAIL_HOST_USER`
   - Should be: `sales@kyrex.co` (or the Gmail account you're using)

3. **Recreate App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Delete old App Password
   - Create new App Password
   - Update `EMAIL_HOST_PASSWORD` in Railway

### 4. Gmail Blocking Emails

**Check:**
1. **Gmail Security Settings**:
   - Go to: https://myaccount.google.com/security
   - Check "Less secure app access" (if using regular Gmail)
   - For Google Workspace, check admin settings

2. **Check Gmail Activity**:
   - Go to: https://myaccount.google.com/security
   - Click "Recent security activity"
   - Look for blocked login attempts

### 5. Email Actually Failing Silently

**Check Railway Logs:**
- Look for any error messages after "Email sent successfully"
- Check for SMTP errors
- Look for authentication errors

## Step-by-Step Troubleshooting

### Step 1: Check Spam Folder

1. **Go to Gmail**: https://mail.google.com/
2. **Log in**: `sales@kyrex.co`
3. **Click "Spam"** folder
4. **Search**: `from:sales@kyrex.co`
5. **If found**: Mark as "Not spam"

### Step 2: Verify Email Configuration

1. **Go to Railway**:
   - Railway → Your Service → Variables tab

2. **Check these variables**:
   ```
   CONTACT_EMAIL=sales@kyrex.co
   EMAIL_HOST_USER=sales@kyrex.co
   EMAIL_HOST_PASSWORD=your-16-character-app-password
   DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
   ```

3. **Verify all are correct** (no typos, correct App Password)

### Step 3: Test Email Configuration

1. **Submit contact form again**
2. **Check Railway logs** for:
   - "Email send result: 1" (means sent successfully)
   - Any error messages
   - SMTP errors

### Step 4: Try Sending to Different Email

**Temporary test:**
1. **Change `CONTACT_EMAIL`** in Railway Variables:
   - Set to a different email you control (like your personal Gmail)
   - Submit contact form
   - Check if you receive it at the different email

2. **If you receive it at different email**:
   - The issue is with `sales@kyrex.co` account
   - Check spam, account settings, etc.

3. **If you don't receive it anywhere**:
   - SMTP configuration issue
   - Check App Password, credentials, etc.

## Quick Checklist

- [ ] Checked spam folder in Gmail
- [ ] Searched Gmail for "Contact Form Submission"
- [ ] Verified `CONTACT_EMAIL` is correct in Railway
- [ ] Verified `EMAIL_HOST_USER` is correct
- [ ] Verified `EMAIL_HOST_PASSWORD` is correct (16 chars, no spaces)
- [ ] Checked Railway logs for errors
- [ ] Tried sending to different email address
- [ ] Checked Gmail security settings

## Common Solutions

### Solution 1: Mark as Not Spam
- Found email in spam → Mark as "Not spam"
- Future emails should go to inbox

### Solution 2: Fix App Password
- Wrong App Password → Create new one
- Update `EMAIL_HOST_PASSWORD` in Railway

### Solution 3: Check Email Address
- Wrong email address → Fix `CONTACT_EMAIL` in Railway
- Make sure account exists and is accessible

## Still Not Working?

If you've tried everything above:

1. **Check Railway logs** for detailed error messages
2. **Try sending to a different email** to test if SMTP works
3. **Verify Gmail account** is active and accessible
4. **Check Gmail admin settings** (if using Google Workspace)

---

## Summary

If logs show "Email sent successfully" but you're not receiving:
1. **Check spam folder** (most common)
2. **Verify email address** is correct
3. **Check App Password** is correct
4. **Try different email** to test SMTP

The email is likely in spam or there's a configuration issue! 🚀
