# Setting Up DNS Records for kyrex.co on Railway

## Overview

To use `kyrex.co` as your custom domain, you need to add DNS records at your domain registrar (where you bought `kyrex.co`).

## Step 1: Get DNS Records from Railway

1. Go to **Railway → Your Service → Settings → Domains**
2. Click **"Custom Domain"** or **"Add Domain"**
3. Enter: `kyrex.co`
4. Railway will show you the DNS records you need to add

## Step 2: Common DNS Records Railway Provides

Railway typically provides one of these:

### Option A: CNAME Record (Most Common)
```
Type: CNAME
Name: @ (or kyrex.co or leave blank)
Value: your-app-name.up.railway.app
TTL: 3600 (or Auto)
```

### Option B: A Record
```
Type: A
Name: @ (or kyrex.co or leave blank)
Value: [Railway's IP address]
TTL: 3600 (or Auto)
```

### Option C: ALIAS/ANAME Record
```
Type: ALIAS (or ANAME)
Name: @
Value: your-app-name.up.railway.app
TTL: 3600
```

## Step 3: Add DNS Records at Your Domain Registrar

### Popular Registrars:

#### **Namecheap**
1. Log in to Namecheap
2. Go to **Domain List** → Click **Manage** next to `kyrex.co`
3. Go to **Advanced DNS** tab
4. Click **Add New Record**
5. Select the record type Railway provided
6. Enter the values Railway gave you
7. Click **Save**

#### **GoDaddy**
1. Log in to GoDaddy
2. Go to **My Products** → **Domains** → Click `kyrex.co`
3. Click **DNS** or **Manage DNS**
4. Click **Add** or **Add Record**
5. Select the record type
6. Enter the values
7. Click **Save**

#### **Cloudflare**
1. Log in to Cloudflare
2. Select `kyrex.co` domain
3. Go to **DNS** → **Records**
4. Click **Add record**
5. Select the record type
6. Enter the values
7. Click **Save**

#### **Google Domains / Squarespace Domains**
1. Log in to your registrar
2. Go to **DNS Settings** or **DNS Management**
3. Click **Add Record** or **Create Record**
4. Enter the values Railway provided
5. Save

## Step 4: Add www Subdomain (Optional but Recommended)

For `www.kyrex.co`, add another record:

```
Type: CNAME
Name: www
Value: your-app-name.up.railway.app (same as main domain)
TTL: 3600
```

## Step 4.5: Add Google Site Verification (Required)

Add a TXT record for Google Search Console verification:

```
Type: TXT
Name: @ (or kyrex.co or leave blank)
Value: google-site-verification=ra9ZCbxVLoy5PHsAR0N9ScnmiObzzPZlA9MCN32clPc
TTL: 3600 (or Auto)
```

**Note:** This record is required for Google Search Console verification. Add it at the same place where you added the CNAME/A record.

## Step 5: Update Railway Environment Variables

After DNS is configured, update these in **Railway → Variables**:

### 1. DJANGO_ALLOWED_HOSTS
```
kyrex.co,www.kyrex.co,*.up.railway.app
```

### 2. CSRF_TRUSTED_ORIGINS
```
https://kyrex.co,https://www.kyrex.co,https://*.up.railway.app
```

## Step 6: Wait for DNS Propagation

- DNS changes can take **5 minutes to 48 hours** to propagate
- Usually takes **15-30 minutes** for most registrars
- You can check propagation at: https://dnschecker.org

## Step 7: Verify Setup

1. Wait for DNS to propagate
2. Railway will automatically detect the DNS records
3. Railway will provision SSL certificate (automatic, takes a few minutes)
4. Visit `https://kyrex.co` - should work!

## Troubleshooting

### DNS Not Working?

1. **Check DNS Propagation**
   - Visit: https://dnschecker.org
   - Enter: `kyrex.co`
   - Check if your DNS records are visible globally

2. **Verify Records at Registrar**
   - Make sure records are saved correctly
   - Check for typos in values
   - Ensure TTL is set (not 0)

3. **Check Railway Domain Status**
   - Railway → Settings → Domains
   - Should show "Active" or "Verified" status
   - If showing error, check the error message

4. **Common Issues**
   - **"DNS not found"**: Records haven't propagated yet (wait longer)
   - **"Invalid record"**: Check the exact values Railway provided
   - **"Already in use"**: Another service might be using the domain

## SSL Certificate

Railway automatically provisions SSL certificates via Let's Encrypt:
- ✅ Free
- ✅ Automatic renewal
- ✅ Works for both `kyrex.co` and `www.kyrex.co`
- ⏱️ Takes 5-15 minutes after DNS is verified

## What Railway Shows You

Railway will display something like:

```
To finish setting up your custom domain, add the following DNS records to kyrex.co:

Type: CNAME
Name: @
Value: web-production-593fc.up.railway.app
```

**Copy these exact values** and add them at your domain registrar!

---

## Quick Checklist

- [ ] Got DNS records from Railway
- [ ] Logged into domain registrar
- [ ] Added DNS record(s) Railway provided
- [ ] Added www subdomain (optional)
- [ ] Updated `DJANGO_ALLOWED_HOSTS` in Railway
- [ ] Updated `CSRF_TRUSTED_ORIGINS` in Railway
- [ ] Waited for DNS propagation (15-30 min)
- [ ] Verified domain in Railway dashboard
- [ ] Tested `https://kyrex.co` in browser

---

## Need Help?

If Railway shows specific DNS records, **share them with me** and I can help you add them correctly!
