# Enable Debug Mode Temporarily to See Errors

## Quick Fix: See the Actual Error

To see what's causing the 500 error:

### Step 1: Enable Debug Mode

1. **Railway → Your Service → Variables**
2. **Find or add:** `DJANGO_DEBUG`
3. **Set value to:** `1`
4. **Save** (Railway will redeploy)

### Step 2: Try Submitting Again

1. Wait for Railway to redeploy (2-3 minutes)
2. Go to: https://kyrex.co/submit/
3. Submit a form
4. **You'll see the actual error** on the page (instead of generic message)

### Step 3: Share the Error

1. Copy the error message from the page
2. Share it with me
3. I'll fix it!

### Step 4: Disable Debug Mode (IMPORTANT!)

After we fix the error:

1. **Railway → Variables**
2. **Set:** `DJANGO_DEBUG` = `0`
3. **Save**

**Important:** Debug mode shows sensitive information. Only enable temporarily!

---

## Alternative: Check Railway Logs

After submitting, immediately check Railway logs:

1. Railway → Deployments → Latest deployment → Logs
2. Look for "ERROR:" messages
3. Share the error with me

---

## Most Likely Issue

The database migration hasn't run yet. The `hr_access_code` field doesn't exist in the database table.

**Fix:** Migrations need to run. Check Railway logs to see if migrations ran.
