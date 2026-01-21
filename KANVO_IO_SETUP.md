# Kanvo.io Domain Setup

Your application is now configured to use **kanvo.io** as the domain.

## Updated Files

✅ `env.example` - Updated default emails to use `kanvo.io`
✅ `submissions/management/commands/create_admin.py` - Updated default admin email

## Railway Environment Variables

Update these in **Railway → Your Service → Variables**:

### Required Variables

1. **HR_NOTIFY_EMAILS**
   ```
   hr@kanvo.io
   ```
   (Or multiple emails: `hr@kanvo.io,admin@kanvo.io`)

2. **DJANGO_DEFAULT_FROM_EMAIL**
   ```
   no-reply@kanvo.io
   ```

3. **DJANGO_SUPERUSER_EMAIL** (for auto-creating admin)
   ```
   hr@kanvo.io
   ```

## Custom Domain Setup (Future)

When you're ready to use `kanvo.io` as your actual domain:

### Step 1: Point Domain to Railway

1. Go to Railway → Your Service → Settings → Domains
2. Click "Custom Domain" or "Add Domain"
3. Enter: `kanvo.io` and `www.kanvo.io`
4. Railway will give you DNS records to add to your domain registrar

### Step 2: Update ALLOWED_HOSTS

In Railway → Variables, update:

```
DJANGO_ALLOWED_HOSTS=kanvo.io,www.kanvo.io,*.up.railway.app
```

### Step 3: Update CSRF_TRUSTED_ORIGINS

```
CSRF_TRUSTED_ORIGINS=https://kanvo.io,https://www.kanvo.io,https://*.up.railway.app
```

### Step 4: Email Setup

Make sure your email is configured:
- Either use your domain's email service (if `kanvo.io` has email)
- Or use a third-party service like:
  - SendGrid
  - Mailgun
  - AWS SES
  - Google Workspace

Then update Railway variables:
- `EMAIL_HOST` = your SMTP server
- `EMAIL_HOST_USER` = your email username
- `EMAIL_HOST_PASSWORD` = your email password
- `EMAIL_PORT` = usually 587 or 465
- `EMAIL_USE_TLS` = True (for port 587) or `EMAIL_USE_SSL` = True (for port 465)

## Current Status

✅ Code updated to use `kanvo.io` by default
⚠️ Need to update Railway environment variables to match
⚠️ Domain DNS not yet configured (still using Railway's default domain)

## Next Steps

1. **Update Railway Variables** - Change email addresses to `@kanvo.io`
2. **Verify Domain Ownership** - Make sure you own `kanvo.io`
3. **Configure DNS** - Point `kanvo.io` to Railway when ready
4. **Setup Email** - Configure email sending for `@kanvo.io` addresses
