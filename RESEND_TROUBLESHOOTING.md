# Resend Email Troubleshooting Guide

If you're not receiving emails, follow these steps to diagnose the issue:

## Step 1: Check Railway Logs

1. Go to your Railway project dashboard
2. Click on your **web service** (not the database)
3. Click on **Deployments** tab
4. Click on the latest deployment
5. Click **View Logs** or look at the **Logs** tab

**Look for these messages:**
- `*** RESEND: Starting email send ***` - Email attempt started
- `*** RESEND: API Response ***` - What Resend API returned
- `RESEND SUCCESS` - Email was sent successfully
- `RESEND ERROR` or `RESEND EXCEPTION` - Something went wrong

**Copy and share the logs** - especially any lines with "RESEND" in them.

## Step 2: Verify Environment Variables

In Railway dashboard:

1. Go to your **web service** (not database)
2. Click **Variables** tab
3. Verify you have these **exact** variable names (case-sensitive):

```
DJANGO_EMAIL_BACKEND=anonplatform.email_backends.ResendEmailBackend
RESEND_API_KEY=re_your-actual-key-here
DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
```

**Common mistakes:**
- ❌ `resend_api_key` (should be `RESEND_API_KEY` - all caps)
- ❌ Extra spaces: `RESEND_API_KEY = re_...` (should be `RESEND_API_KEY=re_...`)
- ❌ Missing `re_` prefix in the API key
- ❌ Variable added to database service instead of web service

## Step 3: Verify Resend API Key

1. Go to [Resend Dashboard](https://resend.com/api-keys)
2. Check that your API key exists and is active
3. Make sure you copied the **full** key (starts with `re_` and is quite long)

## Step 4: Verify Domain/Email in Resend

**If using test domain:**
- Use `onboarding@resend.dev` as `DJANGO_DEFAULT_FROM_EMAIL`
- This works immediately without verification

**If using your own domain (`sales@kyrex.co`):**
1. Go to [Resend Domains](https://resend.com/domains)
2. Check if `kyrex.co` is verified (should show green checkmark)
3. If not verified:
   - Click on the domain
   - Add the DNS records they show to your Namecheap DNS
   - Wait 5-30 minutes for DNS propagation
   - Resend will verify automatically

## Step 5: Check Spam Folder

- Emails might be going to spam
- Check your spam/junk folder
- If using test domain, emails might be marked as spam more often

## Step 6: Test with Resend Dashboard

1. Go to [Resend Dashboard → Emails](https://resend.com/emails)
2. Try sending a test email from there
3. If that works, the issue is with the code configuration
4. If that doesn't work, the issue is with your Resend account/domain

## Common Error Messages

### "Resend not configured. Set RESEND_API_KEY environment variable"
- **Fix**: Add `RESEND_API_KEY` to Railway environment variables
- Make sure it's in the **web service**, not database

### "Resend API returned unexpected response"
- **Fix**: Check Railway logs for the actual response
- Might be an API key issue or domain verification issue

### "Error sending email via Resend: ..."
- **Fix**: Check the full error message in Railway logs
- Common causes:
  - Invalid API key
  - Domain not verified
  - Invalid email address format

### Email shows as "sent" in logs but not received
- **Possible causes:**
  1. Email went to spam (check spam folder)
  2. Domain not verified (emails might be blocked)
  3. Wrong recipient email address
  4. Email provider blocking Resend emails

## Quick Test

After fixing any issues:

1. **Redeploy** your Railway app (or wait for auto-redeploy)
2. Go to `https://kyrex.co/contact/`
3. Submit a test message
4. **Immediately check Railway logs** (within 10 seconds)
5. Look for `RESEND` messages in the logs
6. Check your inbox (and spam folder)

## Still Not Working?

Share these details:
1. **Railway logs** (especially lines with "RESEND")
2. **Environment variables** you have set (hide the actual API key, just show the variable names)
3. **Resend dashboard status** - is your domain verified?
4. **What you see** when submitting the contact form (any error messages?)

---

**Quick Checklist:**
- [ ] `RESEND_API_KEY` is set in Railway (web service, not database)
- [ ] API key starts with `re_` and is the full key
- [ ] `DJANGO_EMAIL_BACKEND=anonplatform.email_backends.ResendEmailBackend`
- [ ] `DJANGO_DEFAULT_FROM_EMAIL` is set correctly
- [ ] Domain is verified in Resend (or using test domain)
- [ ] Checked spam folder
- [ ] Checked Railway logs for RESEND messages
- [ ] Redeployed after adding/changing variables
