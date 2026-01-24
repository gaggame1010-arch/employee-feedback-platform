# Email Service Alternatives for Railway

Railway blocks outbound SMTP connections, so you need to use API-based email services. Here are three great alternatives, all with free tiers:

## 🚀 Option 1: Resend (Recommended - Easiest)

**Why Resend?**
- ✅ Simplest setup (just one API key)
- ✅ Modern, developer-friendly API
- ✅ 100 emails/day free (3,000/month)
- ✅ Great documentation

### Setup Steps:

1. **Sign up** at [https://resend.com](https://resend.com)
2. **Get API key**: Dashboard → API Keys → Create API Key
3. **Verify domain** (or use their test domain for testing):
   - Go to Domains → Add Domain
   - Add DNS records they provide
   - Or use their test domain for quick testing

4. **Add to Railway**:
   ```
   DJANGO_EMAIL_BACKEND=anonplatform.email_backends.ResendEmailBackend
   RESEND_API_KEY=re_your-api-key-here
   DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
   ```

**Free Tier**: 100 emails/day, 3,000/month

---

## 📧 Option 2: SendGrid

**Why SendGrid?**
- ✅ Very popular, well-established
- ✅ 100 emails/day free forever
- ✅ Good for high volume later

### Setup Steps:

1. **Sign up** at [https://sendgrid.com](https://sendgrid.com)
2. **Create API Key**: Settings → API Keys → Create API Key
3. **Verify sender**: Settings → Sender Authentication → Verify a Single Sender

4. **Add to Railway**:
   ```
   DJANGO_EMAIL_BACKEND=anonplatform.email_backends.SendGridEmailBackend
   SENDGRID_API_KEY=SG.your-api-key-here
   DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
   ```

**Free Tier**: 100 emails/day forever

---

## 📮 Option 3: Mailgun

**Why Mailgun?**
- ✅ Generous free tier initially
- ✅ Good for testing
- ✅ 5,000 emails/month free for first 3 months

### Setup Steps:

1. **Sign up** at [https://www.mailgun.com](https://www.mailgun.com)
2. **Get API key**: Dashboard → Settings → API Keys
3. **Get domain**: Dashboard → Sending → Domains (they provide a sandbox domain for testing)
4. **Verify domain** (or use sandbox domain)

5. **Add to Railway**:
   ```
   DJANGO_EMAIL_BACKEND=anonplatform.email_backends.MailgunEmailBackend
   MAILGUN_API_KEY=your-api-key-here
   MAILGUN_DOMAIN=mg.yourdomain.com
   DJANGO_DEFAULT_FROM_EMAIL=sales@kyrex.co
   ```

**Free Tier**: 
- First 3 months: 5,000 emails/month
- After that: 1,000 emails/month

---

## Comparison Table

| Service | Free Tier | Setup Difficulty | Best For |
|---------|-----------|------------------|----------|
| **Resend** | 100/day (3K/month) | ⭐ Easiest | Quick setup, modern API |
| **SendGrid** | 100/day forever | ⭐⭐ Medium | Long-term, high volume later |
| **Mailgun** | 5K/month (3 months), then 1K/month | ⭐⭐ Medium | Testing, initial high volume |

---

## Quick Recommendation

**For most users**: Start with **Resend** - it's the easiest to set up and has a good free tier.

**If you need more emails**: Use **Mailgun** for the first 3 months (5,000/month), then switch to **SendGrid** or upgrade to a paid plan.

---

## Testing

After setting up any service:

1. Add the environment variables to Railway
2. Redeploy your app
3. Test the contact form at `https://kyrex.co/contact/`
4. Check your inbox (and spam folder)
5. Check Railway logs for any errors

---

## Need Help?

- **Resend**: [https://resend.com/docs](https://resend.com/docs)
- **SendGrid**: [https://docs.sendgrid.com](https://docs.sendgrid.com)
- **Mailgun**: [https://documentation.mailgun.com](https://documentation.mailgun.com)
