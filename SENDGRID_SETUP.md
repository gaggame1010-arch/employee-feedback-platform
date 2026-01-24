# SendGrid Email Setup Guide

Railway blocks outbound SMTP connections (ports 25, 587, 465) to prevent spam. This means Gmail SMTP won't work on Railway. Instead, we use **SendGrid API** which works perfectly on Railway.

## Quick Setup Steps

### 1. Create a SendGrid Account

1. Go to [https://sendgrid.com](https://sendgrid.com)
2. Sign up for a free account (100 emails/day free forever)
3. Verify your email address

### 2. Create a SendGrid API Key

1. Log in to SendGrid dashboard
2. Go to **Settings** → **API Keys**
3. Click **Create API Key**
4. Name it (e.g., "Railway Production")
5. Select **Full Access** (or "Mail Send" permissions)
6. Click **Create & View**
7. **Copy the API key immediately** (you won't see it again!)

### 3. Verify Your Sender Email

1. Go to **Settings** → **Sender Authentication**
2. Click **Verify a Single Sender**
3. Fill in your details:
   - **From Email**: `sales@kyrex.co` (or your sending email)
   - **From Name**: Your company name
   - **Reply To**: `sales@kyrex.co`
   - Complete the form and submit
4. Check your email inbox and click the verification link

### 4. Add Environment Variables to Railway

In your Railway project, add these environment variables:

```
DJANGO_EMAIL_BACKEND=anonplatform.email_backends.SendGridEmailBackend
SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
```

**Important**: Replace `SG.xxxxxxxx...` with your actual SendGrid API key from step 2.

### 5. Redeploy

After adding the environment variables, Railway will automatically redeploy. Or you can trigger a manual redeploy.

## Testing

1. Submit a test message via the contact form at `https://kyrex.co/contact/`
2. Check your `sales@kyrex.co` inbox (and spam folder)
3. Check Railway logs to see if the email was sent successfully

## Troubleshooting

### "SendGrid API returned status 403"
- Your API key might not have "Mail Send" permissions
- Create a new API key with full access

### "SendGrid API returned status 400"
- Your sender email (`DJANGO_DEFAULT_FROM_EMAIL`) might not be verified
- Go to SendGrid → Settings → Sender Authentication and verify the email

### "SENDGRID_API_KEY not set"
- Make sure you added `SENDGRID_API_KEY` to Railway environment variables
- Check for typos in the variable name
- Redeploy after adding the variable

### Still not receiving emails?
- Check spam folder
- Verify the recipient email address is correct
- Check Railway logs for error messages
- Make sure `DJANGO_EMAIL_BACKEND` is set to `anonplatform.email_backends.SendGridEmailBackend`

## SendGrid Free Tier Limits

- **100 emails per day** (free forever)
- Perfect for small to medium businesses
- Upgrade to paid plans for more volume

## Alternative: Use Your Own Domain

If you want to send from `@kyrex.co` instead of a verified single sender:

1. Go to **Settings** → **Sender Authentication**
2. Click **Authenticate Your Domain**
3. Follow the DNS setup instructions
4. This allows sending from any email address on your domain

---

**Need Help?** Check SendGrid documentation: https://docs.sendgrid.com
