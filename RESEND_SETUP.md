# Resend Email Setup Guide for Railway

## Quick Setup (5 minutes)

### Step 1: Create Resend Account

1. Go to [https://resend.com](https://resend.com)
2. Click **Sign Up** (you can use Google/GitHub to sign up faster)
3. Verify your email address

### Step 2: Get Your API Key

1. Once logged in, go to **API Keys** in the sidebar
2. Click **Create API Key**
3. Name it (e.g., "Railway Production")
4. Click **Add**
5. **Copy the API key immediately** - it starts with `re_` and you won't see it again!

### Step 3: Verify Your Domain (or Use Test Domain)

**Option A: Use Resend's Test Domain (Quick Testing)**
- Resend provides a test domain for quick testing
- You can send emails from `onboarding@resend.dev` for testing
- Check your Resend dashboard for the test domain details

**Option B: Verify Your Own Domain (Production)**
1. Go to **Domains** in the sidebar
2. Click **Add Domain**
3. Enter `kyrex.co`
4. Resend will show you DNS records to add:
   - Go to your domain registrar (Namecheap)
   - Add the DNS records they provide (usually TXT and CNAME records)
   - Wait for DNS propagation (5-30 minutes)
   - Resend will verify automatically

### Step 4: Add Environment Variables to Railway

In your Railway project dashboard:

1. Go to your **web service** (not the database)
2. Click on **Variables** tab
3. Add these three variables:

```
DJANGO_EMAIL_BACKEND=anonplatform.email_backends.ResendEmailBackend
RESEND_API_KEY=re_your-actual-api-key-here
DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
```

**Important**: 
- Replace `re_your-actual-api-key-here` with the API key you copied in Step 2
- If you're using Resend's test domain, use `onboarding@resend.dev` instead of `sales@kyrex.co`

### Step 5: Redeploy

Railway will automatically redeploy when you add environment variables. Or you can:
- Go to **Deployments** tab
- Click **Redeploy** on the latest deployment

### Step 6: Test

1. Go to `https://kyrex.co/contact/`
2. Fill out the contact form with a test message
3. Submit the form
4. Check your `sales@kyrex.co` inbox (and spam folder)
5. Check Railway logs to see if email was sent successfully

## Troubleshooting

### "Resend API returned unexpected response"
- Check that your `RESEND_API_KEY` is correct (starts with `re_`)
- Make sure there are no extra spaces in the Railway environment variable

### "Email sent successfully but not received"
- Check spam folder
- If using test domain, make sure you're using `onboarding@resend.dev` as the sender
- If using your own domain, make sure DNS records are verified in Resend dashboard

### "RESEND_API_KEY not set"
- Make sure you added the variable to the **web service** (not database)
- Check for typos: `RESEND_API_KEY` (all caps, with underscores)
- Redeploy after adding the variable

### Still having issues?
- Check Railway logs for detailed error messages
- Verify your API key in Resend dashboard → API Keys
- Make sure your domain is verified (if using custom domain)

## Resend Free Tier

- ✅ **100 emails per day**
- ✅ **3,000 emails per month**
- ✅ Perfect for your use case (contact forms + HR notifications)

## Next Steps

Once everything is working:
1. ✅ Contact form emails will be sent to `sales@kyrex.co`
2. ✅ HR notification emails will work for employee submissions
3. ✅ All emails will be sent via Resend API (works on Railway!)

---

**Need Help?** 
- Resend Docs: [https://resend.com/docs](https://resend.com/docs)
- Resend Dashboard: [https://resend.com/emails](https://resend.com/emails)
