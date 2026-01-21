# Complete Cloudflare Tutorial: Register kanvo.io & Connect to Railway

## Step-by-Step Guide

---

## Part 1: Register Domain on Cloudflare

### Step 1: Create Cloudflare Account

1. **Go to Cloudflare**
   - Visit: https://www.cloudflare.com/
   - Click **"Sign Up"** (top right)

2. **Sign Up**
   - Enter your email address
   - Create a password
   - Click **"Create Account"**
   - Verify your email (check inbox)

---

### Step 2: Register kanvo.io Domain

1. **Access Domain Registration**
   - Once logged in, look for **"Domain Registration"** or **"Register Domains"**
   - Or go directly to: https://www.cloudflare.com/products/registrar/

2. **Search for Domain**
   - In the search box, type: `kanvo.io`
   - Click **"Search"** or press Enter

3. **Check Availability**
   - Cloudflare will show if `kanvo.io` is available
   - If available, you'll see the price
   - If taken, try variations like `kanvo-app.io` or `getkanvo.io`

4. **Add to Cart**
   - Click **"Add to Cart"** next to `kanvo.io`
   - You might see options for additional services (optional):
     - ❌ Skip "WHOIS Privacy" (it's free anyway)
     - ❌ Skip any premium features (not needed)

5. **Complete Purchase**
   - Click **"Checkout"** or **"Continue"**
   - Review your order
   - Enter payment information
   - Complete purchase

---

## Part 2: Configure DNS for Railway

### Step 3: Access DNS Settings

After purchasing:

1. **Go to Dashboard**
   - Cloudflare will redirect you to your dashboard
   - Or go to: https://dash.cloudflare.com/

2. **Find Your Domain**
   - Look for `kanvo.io` in your domain list
   - Click on `kanvo.io` to open it

3. **Go to DNS**
   - In the left sidebar, click **"DNS"**
   - Or use the top navigation tabs and click **"DNS"**

---

### Step 4: Get DNS Records from Railway

**Before adding DNS records, get them from Railway:**

1. **Go to Railway**
   - Railway → Your Service → **Settings** → **Domains**
   - Click **"Custom Domain"** or **"Add Domain"**

2. **Enter Domain**
   - Type: `kanvo.io`
   - Click **"Add"** or **"Save"**

3. **Copy DNS Records**
   - Railway will show DNS records to add
   - Usually looks like:
     ```
     Type: CNAME
     Name: @
     Value: web-production-593fc.up.railway.app
     ```

4. **Keep this page open** (you'll need it in the next step)

---

### Step 5: Add DNS Records in Cloudflare

1. **Add Main Domain Record**

   - In Cloudflare DNS page, click **"Add record"**

   - **If Railway shows CNAME:**
     - **Type**: Select `CNAME`
     - **Name**: Enter `@` (or `kanvo.io`, or leave blank - depends on Cloudflare's interface)
     - **Target**: Paste Railway's value (e.g., `web-production-593fc.up.railway.app`)
     - **Proxy status**: Click the **orange cloud** icon (🟠) to turn it **gray** (⚪) - **disable proxy** for Railway
     - **TTL**: Select `Auto`
     - Click **"Save"**

   - **If Railway shows A record:**
     - **Type**: Select `A`
     - **Name**: Enter `@` (or leave blank)
     - **IPv4 address**: Paste Railway's IP address
     - **Proxy status**: Click to **disable proxy** (gray cloud ⚪)
     - **TTL**: Select `Auto`
     - Click **"Save"**

2. **Add www Subdomain (Recommended)**

   - Click **"Add record"** again
   - **Type**: Select `CNAME`
   - **Name**: Enter `www`
   - **Target**: Paste the same Railway value (e.g., `web-production-593fc.up.railway.app`)
   - **Proxy status**: **Disable proxy** (gray cloud ⚪)
   - **TTL**: Select `Auto`
   - Click **"Save"**

3. **Verify Records**

   Your DNS records should look like:
   ```
   Type    Name    Content                                    Proxy
   CNAME   @       web-production-593fc.up.railway.app        DNS only (gray)
   CNAME   www     web-production-593fc.up.railway.app        DNS only (gray)
   ```

   ⚠️ **Important**: Make sure proxy is **disabled** (gray cloud) for Railway!

---

## Part 3: Update Railway Configuration

### Step 6: Update Railway Environment Variables

1. **Go to Railway**
   - Railway → Your Service → **Variables**

2. **Update ALLOWED_HOSTS**
   - Find or add: `DJANGO_ALLOWED_HOSTS`
   - Set value to:
     ```
     kanvo.io,www.kanvo.io,*.up.railway.app
     ```

3. **Update CSRF_TRUSTED_ORIGINS**
   - Find or add: `CSRF_TRUSTED_ORIGINS`
   - Set value to:
     ```
     https://kanvo.io,https://www.kanvo.io,https://*.up.railway.app
     ```

4. **Save Changes**
   - Railway will automatically redeploy

---

## Part 4: Wait for DNS Propagation

### Step 7: Verify DNS Propagation

1. **Check DNS Propagation**
   - Visit: https://dnschecker.org/
   - Enter: `kanvo.io`
   - Select record type: `CNAME` (or `A` if you used that)
   - Click **"Search"**
   - Wait for green checkmarks across the globe (usually 5-30 minutes)

2. **Check in Cloudflare**
   - Go back to Cloudflare → DNS
   - Records should show as active
   - Status should be "Proxied: DNS only" (gray cloud)

3. **Check in Railway**
   - Railway → Settings → Domains
   - `kanvo.io` should show as "Active" or "Verified"
   - SSL certificate will be automatically provisioned (takes 5-15 minutes)

---

## Part 5: Test Your Domain

### Step 8: Access Your Site

1. **Wait 15-30 Minutes**
   - DNS needs time to propagate
   - SSL certificate needs to be issued

2. **Visit Your Site**
   - Open browser
   - Go to: `https://kanvo.io`
   - Should load your application! 🎉

3. **Test www Subdomain**
   - Also test: `https://www.kanvo.io`
   - Should redirect or load the same site

---

## Troubleshooting

### DNS Not Working?

**Problem**: Site doesn't load after 30 minutes

**Solutions:**
1. **Check DNS Records**
   - Cloudflare → DNS → Verify records are correct
   - Make sure proxy is **disabled** (gray cloud)

2. **Verify Propagation**
   - https://dnschecker.org - Check if DNS is propagated
   - If not showing, wait longer (up to 48 hours, but usually 15-30 min)

3. **Check Railway Domain Status**
   - Railway → Settings → Domains
   - Look for error messages
   - Domain should show "Active"

4. **Clear Browser Cache**
   - Try incognito/private window
   - Or clear browser cache

---

### SSL Certificate Not Working?

**Problem**: Getting SSL errors or "Not Secure" warning

**Solutions:**
1. **Wait Longer**
   - SSL certificate provisioning takes 5-15 minutes after DNS is verified
   - Railway automatically creates certificates via Let's Encrypt

2. **Check Railway Status**
   - Railway → Settings → Domains
   - Should show SSL as "Active" or "Valid"

3. **Verify HTTPS**
   - Make sure you're using `https://kanvo.io` (not `http://`)
   - Railway automatically redirects HTTP to HTTPS

---

### Proxy Issues

**Problem**: Site shows Cloudflare error or doesn't connect to Railway

**Solution:**
- **Disable Cloudflare Proxy** for Railway DNS records
- In Cloudflare DNS, click the **orange cloud** → turn to **gray cloud**
- This is required for Railway to work correctly

---

## Visual Guide: Cloudflare DNS Settings

### Correct DNS Setup:

```
┌─────────────────────────────────────────────────────┐
│  Cloudflare DNS Records                             │
├──────────┬──────────┬───────────────────────────────┤
│ Type     │ Name     │ Target/Content                │
├──────────┼──────────┼───────────────────────────────┤
│ CNAME    │ @        │ web-prod-593fc.up.railway.app │
│          │          │ ⚪ DNS only (gray cloud)      │
├──────────┼──────────┼───────────────────────────────┤
│ CNAME    │ www      │ web-prod-593fc.up.railway.app │
│          │          │ ⚪ DNS only (gray cloud)      │
└──────────┴──────────┴───────────────────────────────┘
```

### ⚠️ Important: Disable Proxy!

- **Orange cloud 🟠** = Proxy enabled (NOT for Railway)
- **Gray cloud ⚪** = DNS only (CORRECT for Railway)

---

## Quick Checklist

- [ ] Created Cloudflare account
- [ ] Registered `kanvo.io` domain
- [ ] Got DNS records from Railway
- [ ] Added CNAME record in Cloudflare (proxy disabled)
- [ ] Added www CNAME record (proxy disabled)
- [ ] Updated `DJANGO_ALLOWED_HOSTS` in Railway
- [ ] Updated `CSRF_TRUSTED_ORIGINS` in Railway
- [ ] Waited for DNS propagation (15-30 min)
- [ ] Verified DNS at dnschecker.org
- [ ] Tested `https://kanvo.io` in browser
- [ ] SSL certificate active

---

## Summary

1. ✅ **Register** `kanvo.io` on Cloudflare
2. ✅ **Get DNS records** from Railway
3. ✅ **Add DNS records** in Cloudflare (disable proxy!)
4. ✅ **Update Railway** environment variables
5. ✅ **Wait** for DNS propagation
6. ✅ **Test** your site at `https://kanvo.io`

**Total Time**: ~30-45 minutes (mostly waiting for DNS)

---

## Need Help?

If you get stuck at any step, share:
1. What step you're on
2. Any error messages you see
3. Screenshot of your Cloudflare DNS records (optional)

I'll help you troubleshoot! 🚀
