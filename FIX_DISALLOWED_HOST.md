# Fix DisallowedHost Error on Railway

## Your Railway Domain
```
web-production-593fc.up.railway.app
```

## Quick Fix: Update Environment Variables

Go to Railway → Your Service → Variables and update:

### 1. DJANGO_ALLOWED_HOSTS
**Current value:** `*.up.railway.app`

**Change to:**
```
web-production-593fc.up.railway.app,*.up.railway.app
```

Or just:
```
*.up.railway.app,web-production-593fc.up.railway.app
```

### 2. CSRF_TRUSTED_ORIGINS
**Current value:** `https://*.up.railway.app`

**Change to:**
```
https://web-production-593fc.up.railway.app,https://*.up.railway.app
```

### 3. DJANGO_DEBUG
**Current value:** `1` (True)

**Change to:**
```
0
```

**Important:** DEBUG should be `0` in production!

---

## After Updating Variables

1. Railway will automatically redeploy
2. Wait for deployment to complete
3. Visit your URL again: `https://web-production-593fc.up.railway.app`
4. Should work now!

---

## Also Noticed: Database Issue

Your error shows:
```
DATABASE_URL: None
DATABASES: {'default': {'ENGINE': 'django.db.backends.sqlite3'...
```

This means PostgreSQL isn't connected. Make sure:
1. PostgreSQL service is added in Railway
2. PostgreSQL is running (green status)
3. `DATABASE_URL` is automatically set (Railway does this)

---

## Complete Variable Checklist

Make sure ALL these are set correctly:

- [x] `DJANGO_SECRET_KEY` = (your secret key)
- [ ] `DJANGO_DEBUG` = `0` ← **Change this!**
- [ ] `DJANGO_ALLOWED_HOSTS` = `web-production-593fc.up.railway.app,*.up.railway.app` ← **Update this!**
- [ ] `CSRF_TRUSTED_ORIGINS` = `https://web-production-593fc.up.railway.app,https://*.up.railway.app` ← **Update this!**
- [x] `COMPANY_ACCESS_CODE` = (your code)
- [x] `HR_NOTIFY_EMAILS` = (your email)
- [x] `DJANGO_DEFAULT_FROM_EMAIL` = (your email)
- [ ] `DATABASE_URL` = (should be auto-set by Railway PostgreSQL)

---

## Quick Action Items

1. **Update ALLOWED_HOSTS** to include your specific domain
2. **Set DEBUG=0** (important for security!)
3. **Update CSRF_TRUSTED_ORIGINS** with your domain
4. **Check PostgreSQL** is connected

After updating, Railway will redeploy and your site should work!
