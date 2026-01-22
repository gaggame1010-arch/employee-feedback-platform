# Complete DNS Setup Guide for kyrex.co

## Quick Start Checklist

- [ ] Get DNS records from Railway
- [ ] Add CNAME/A record at domain registrar
- [ ] Add www subdomain record
- [ ] Add Google site verification TXT record
- [ ] Update Railway environment variables
- [ ] Wait for DNS propagation (15-30 minutes)
- [ ] Verify domain works

---

## Step 1: Get DNS Records from Railway

### 1.1 Go to Railway Dashboard

1. Open your browser and go to: https://railway.app
2. Log in to your Railway account
3. Click on your **web service** (the one running your Django app)

### 1.2 Add Custom Domain

1. In your service, click on the **Settings** tab
2. Scroll down to **Domains** section
3. Click **"Custom Domain"** or **"Add Domain"** button
4. Enter: `kyrex.co`
5. Click **"Add"** or **"Save"**

### 1.3 Copy DNS Records

Railway will show you DNS records that look like this:

```
Type: CNAME
Name: @
Value: web-production-XXXXX.up.railway.app
```

**OR** it might show:

```
Type: A
Name: @
Value: [IP address]
```

**📝 IMPORTANT:** Copy these exact values! You'll need them in the next step.

**Example:** If Railway shows:
- Type: `CNAME`
- Name: `@`
- Value: `web-production-593fc.up.railway.app`

Write this down or keep the Railway page open.

---

## Step 2: Add DNS Records at Your Domain Registrar

**First, tell me which registrar you're using:**
- Cloudflare
- Namecheap
- GoDaddy
- Google Domains / Squarespace
- Other (specify)

I'll provide specific instructions based on your registrar. Below are instructions for the most common ones:

---

### Option A: Cloudflare (Recommended)

#### 2.1 Log in to Cloudflare

1. Go to: https://dash.cloudflare.com/
2. Log in to your account
3. Click on **`kyrex.co`** domain

#### 2.2 Go to DNS Settings

1. In the left sidebar, click **"DNS"**
2. You'll see a list of existing DNS records

#### 2.3 Add Main Domain Record (CNAME or A)

1. Click **"Add record"** button
2. **If Railway gave you a CNAME:**
   - **Type**: Select `CNAME`
   - **Name**: Enter `@` (or leave blank if Cloudflare doesn't accept @)
   - **Target**: Paste Railway's value (e.g., `web-production-593fc.up.railway.app`)
   - **Proxy status**: Click the **orange cloud** 🟠 to turn it **gray** ⚪ (DISABLE proxy - this is important!)
   - **TTL**: Select `Auto`
   - Click **"Save"**

3. **If Railway gave you an A record:**
   - **Type**: Select `A`
   - **Name**: Enter `@` (or leave blank)
   - **IPv4 address**: Paste Railway's IP address
   - **Proxy status**: Click to **disable proxy** (gray cloud ⚪)
   - **TTL**: Select `Auto`
   - Click **"Save"**

#### 2.4 Add www Subdomain

1. Click **"Add record"** again
2. **Type**: Select `CNAME`
3. **Name**: Enter `www`
4. **Target**: Paste the same Railway value (e.g., `web-production-593fc.up.railway.app`)
5. **Proxy status**: **Disable proxy** (gray cloud ⚪)
6. **TTL**: Select `Auto`
7. Click **"Save"**

#### 2.5 Add Google Site Verification

1. Click **"Add record"** again
2. **Type**: Select `TXT`
3. **Name**: Enter `@` (or leave blank)
4. **Content**: Enter `google-site-verification=ra9ZCbxVLoy5PHsAR0N9ScnmiObzzPZlA9MCN32clPc`
5. **TTL**: Select `Auto`
6. Click **"Save"**

#### 2.6 Verify Records

Your DNS records should look like:

```
Type    Name    Content/Target                              Proxy
CNAME   @       web-production-593fc.up.railway.app         DNS only (gray ⚪)
CNAME   www     web-production-593fc.up.railway.app         DNS only (gray ⚪)
TXT     @       google-site-verification=ra9ZCbxVLoy5...    DNS only (gray ⚪)
```

**⚠️ CRITICAL:** Make sure proxy is **disabled** (gray cloud) for Railway records!

---

### Option B: Namecheap

#### 2.1 Log in to Namecheap

1. Go to: https://www.namecheap.com/
2. Log in to your account
3. Go to **Domain List**

#### 2.2 Access DNS Settings

1. Find `kyrex.co` in your domain list
2. Click **"Manage"** next to it
3. Go to **"Advanced DNS"** tab

#### 2.3 Add Main Domain Record

1. Click **"Add New Record"**
2. **If Railway gave you a CNAME:**
   - **Type**: Select `CNAME Record`
   - **Host**: Enter `@` (or leave blank)
   - **Value**: Paste Railway's value (e.g., `web-production-593fc.up.railway.app`)
   - **TTL**: Select `Automatic` or `3600`
   - Click **"Save"** (green checkmark)

3. **If Railway gave you an A record:**
   - **Type**: Select `A Record`
   - **Host**: Enter `@` (or leave blank)
   - **Value**: Paste Railway's IP address
   - **TTL**: Select `Automatic` or `3600`
   - Click **"Save"**

#### 2.4 Add www Subdomain

1. Click **"Add New Record"**
2. **Type**: Select `CNAME Record`
3. **Host**: Enter `www`
4. **Value**: Paste the same Railway value
5. **TTL**: Select `Automatic` or `3600`
6. Click **"Save"**

#### 2.5 Add Google Site Verification

1. Click **"Add New Record"**
2. **Type**: Select `TXT Record`
3. **Host**: Enter `@` (or leave blank)
4. **Value**: Enter `google-site-verification=ra9ZCbxVLoy5PHsAR0N9ScnmiObzzPZlA9MCN32clPc`
5. **TTL**: Select `Automatic` or `3600`
6. Click **"Save"**

---

### Option C: GoDaddy

#### 2.1 Log in to GoDaddy

1. Go to: https://www.godaddy.com/
2. Log in to your account
3. Go to **"My Products"** → **"Domains"**

#### 2.2 Access DNS Settings

1. Find `kyrex.co` in your domain list
2. Click on `kyrex.co`
3. Click **"DNS"** or **"Manage DNS"**

#### 2.3 Add Records

1. Click **"Add"** or **"Add Record"**
2. Follow the same pattern as Namecheap:
   - Add CNAME/A record for main domain
   - Add CNAME record for www
   - Add TXT record for Google verification

---

### Option D: Google Domains / Squarespace

1. Log in to your registrar
2. Go to **DNS Settings** or **DNS Management**
3. Click **"Add Record"** or **"Create Record"**
4. Add the same three records:
   - Main domain (CNAME or A)
   - www subdomain (CNAME)
   - Google verification (TXT)

---

## Step 3: Update Railway Environment Variables

After adding DNS records, update Railway's environment variables:

### 3.1 Go to Railway Variables

1. Railway → Your Service → **Variables** tab

### 3.2 Add/Update Variables

Add or update these variables:

#### Variable 1: DJANGO_ALLOWED_HOSTS
- **Name**: `DJANGO_ALLOWED_HOSTS`
- **Value**: `kyrex.co,www.kyrex.co,*.up.railway.app`

#### Variable 2: CSRF_TRUSTED_ORIGINS
- **Name**: `CSRF_TRUSTED_ORIGINS`
- **Value**: `https://kyrex.co,https://www.kyrex.co,https://*.up.railway.app`

#### Variable 3: HR_NOTIFY_EMAILS
- **Name**: `HR_NOTIFY_EMAILS`
- **Value**: `sales@kyrex.co`

#### Variable 4: DJANGO_DEFAULT_FROM_EMAIL
- **Name**: `DJANGO_DEFAULT_FROM_EMAIL`
- **Value**: `sales@kyrex.co`

#### Variable 5: DJANGO_SUPERUSER_EMAIL
- **Name**: `DJANGO_SUPERUSER_EMAIL`
- **Value**: `sales@kyrex.co`

### 3.3 Save Changes

- Railway will automatically redeploy after you save variables
- Wait for deployment to complete

---

## Step 4: Wait for DNS Propagation

### 4.1 How Long Does It Take?

- **Usually**: 15-30 minutes
- **Can take**: Up to 48 hours (rare)
- **Most registrars**: 5-30 minutes

### 4.2 Check DNS Propagation

1. Visit: https://dnschecker.org/
2. Enter: `kyrex.co`
3. Select record type: `CNAME` (or `A` if you used that)
4. Click **"Search"**
5. Wait for green checkmarks across the globe

### 4.3 Check Railway Domain Status

1. Railway → Settings → Domains
2. `kyrex.co` should show:
   - **Status**: "Active" or "Verified"
   - **SSL**: "Active" or "Valid" (takes 5-15 minutes after DNS is verified)

---

## Step 5: Verify Everything Works

### 5.1 Test Your Domain

1. Wait 15-30 minutes after adding DNS records
2. Open your browser
3. Visit: `https://kyrex.co`
4. Your site should load! 🎉

### 5.2 Test www Subdomain

1. Visit: `https://www.kyrex.co`
2. Should also work

### 5.3 Check SSL Certificate

- Browser should show a lock icon 🔒
- URL should start with `https://`
- No SSL warnings

---

## Troubleshooting

### Problem: DNS Not Working After 30 Minutes

**Solutions:**
1. **Check DNS Propagation**
   - Visit https://dnschecker.org
   - Verify records are visible globally
   - If not, wait longer (up to 48 hours)

2. **Verify Records at Registrar**
   - Double-check values are correct
   - No typos in Railway's domain value
   - TTL is set (not 0)

3. **Check Railway Domain Status**
   - Railway → Settings → Domains
   - Look for error messages
   - Domain should show "Active"

### Problem: SSL Certificate Not Working

**Solutions:**
1. **Wait Longer**
   - SSL takes 5-15 minutes after DNS is verified
   - Railway automatically creates certificates

2. **Check Railway Status**
   - Railway → Settings → Domains
   - SSL should show "Active"

3. **Use HTTPS**
   - Make sure you're using `https://kyrex.co` (not `http://`)

### Problem: Cloudflare Proxy Issues

**Solution:**
- **Disable Cloudflare Proxy** for Railway records
- In Cloudflare DNS, click orange cloud 🟠 → turn to gray cloud ⚪
- This is required for Railway to work correctly

### Problem: "DisallowedHost" Error

**Solution:**
- Make sure `DJANGO_ALLOWED_HOSTS` includes `kyrex.co,www.kyrex.co`
- Update in Railway → Variables
- Redeploy if needed

---

## Quick Reference: DNS Records Summary

You need to add these **3 DNS records** at your registrar:

### Record 1: Main Domain
```
Type: CNAME (or A)
Name: @ (or leave blank)
Value: [Railway's value from Step 1]
TTL: Auto or 3600
```

### Record 2: www Subdomain
```
Type: CNAME
Name: www
Value: [Same as Record 1]
TTL: Auto or 3600
```

### Record 3: Google Verification
```
Type: TXT
Name: @ (or leave blank)
Value: google-site-verification=ra9ZCbxVLoy5PHsAR0N9ScnmiObzzPZlA9MCN32clPc
TTL: Auto or 3600
```

---

## Need Help?

**If you get stuck:**
1. Share which registrar you're using
2. Share the DNS records Railway gave you
3. Share any error messages you see
4. I'll help you troubleshoot!

**Common Questions:**
- **Q:** What if my registrar doesn't accept `@` for Name?
  - **A:** Leave it blank or enter the domain name (`kyrex.co`)

- **Q:** What if Railway shows an A record instead of CNAME?
  - **A:** Use the A record exactly as Railway shows it

- **Q:** How do I know if DNS is working?
  - **A:** Check https://dnschecker.org and Railway's domain status

---

## Success Checklist

- [ ] Got DNS records from Railway
- [ ] Added main domain record (CNAME/A) at registrar
- [ ] Added www subdomain record at registrar
- [ ] Added Google site verification TXT record
- [ ] Updated `DJANGO_ALLOWED_HOSTS` in Railway
- [ ] Updated `CSRF_TRUSTED_ORIGINS` in Railway
- [ ] Updated email variables in Railway
- [ ] Waited 15-30 minutes for DNS propagation
- [ ] Verified DNS at dnschecker.org
- [ ] Checked Railway domain status (Active)
- [ ] Tested `https://kyrex.co` in browser
- [ ] Tested `https://www.kyrex.co` in browser
- [ ] SSL certificate is active (lock icon)

**Once all checked, your domain is fully configured! 🎉**
