# Setup Gmail for kyrex.co (Google Workspace)

## Overview

You're setting up Gmail for your custom domain `kyrex.co` using Google Workspace. This requires adding MX (Mail Exchange) records to your Namecheap DNS settings.

---

## Step 1: Go to Namecheap DNS Settings

1. **Log in to Namecheap**
   - Visit: https://www.namecheap.com/
   - Log in to your account

2. **Access DNS Management**
   - Go to **Domain List**
   - Find `kyrex.co`
   - Click **"Manage"** next to it
   - Click **"Advanced DNS"** tab

---

## Step 2: Delete Existing MX Records (If Any)

**Important:** Google says to delete any existing MX records first.

1. **In Advanced DNS tab**, scroll to **"Mail Settings"** or **"MX Records"** section
2. **Look for any existing MX records**
3. **Delete them** (click trash icon or delete button)
4. **Save changes**

---

## Step 3: Add Google MX Record

1. **In Advanced DNS tab**, scroll to **"Mail Settings"** section
2. **Click "Add New Record"**
3. **Select "MX Record"** from the dropdown
4. **Enter the values:**

   **Host:**
   - Enter `@` (or leave blank - depends on Namecheap's interface)
   - Some registrars use `@`, others use blank

   **Priority:**
   - Enter: `1`

   **Value:**
   - Enter: `SMTP.GOOGLE.COM`
   - **Important:** Some registrars require a period at the end: `SMTP.GOOGLE.COM.`
   - Check Namecheap's format - it might auto-add the period

   **TTL:**
   - Select "Automatic" or "30 min" (lowest value)

5. **Click "Save"** (green checkmark)

---

## Step 4: Verify MX Record

Your MX record should look like:

```
Type: MX Record
Host: @ (or blank)
Priority: 1
Value: SMTP.GOOGLE.COM (or SMTP.GOOGLE.COM.)
TTL: Automatic
```

---

## Step 5: Wait for DNS Propagation

- **Wait 15-30 minutes** for DNS to propagate
- MX records can take longer than other DNS records
- Can take up to 48 hours (but usually 15-30 minutes)

---

## Step 6: Confirm in Google Workspace

1. **Go back to Google Workspace**
   - Return to the "Activate Gmail" page
   - Check the box: "Come back here and confirm once you have updated the code on your domain host"
   - Click **"Confirm"** button

2. **Google will verify the MX record**
   - This may take a few minutes
   - Google will check if the MX record is correct

---

## Troubleshooting

### Issue 1: MX Record Not Saving

**Solution:**
- Make sure you're in the "Advanced DNS" tab
- Check if there's a "Mail Settings" section
- Try refreshing the page and adding again

---

### Issue 2: Google Can't Verify MX Record

**Solution:**
1. **Check DNS Propagation**
   - Visit: https://mxtoolbox.com/
   - Enter: `kyrex.co`
   - Select "MX Lookup"
   - Should show `SMTP.GOOGLE.COM`

2. **Verify Record Format**
   - Make sure value is exactly: `SMTP.GOOGLE.COM` or `SMTP.GOOGLE.COM.`
   - Check priority is `1`
   - Check TTL is set

3. **Wait Longer**
   - MX records can take 30-60 minutes to propagate
   - Wait and try again

---

### Issue 3: Period at End of Value

**Solution:**
- Some registrars require: `SMTP.GOOGLE.COM.` (with period)
- Some don't: `SMTP.GOOGLE.COM` (without period)
- Check Namecheap's format - it might auto-format it
- If Google verification fails, try adding/removing the period

---

## Important Notes

### ⚠️ Don't Delete Your Other DNS Records!

**Keep these records:**
- ✅ CNAME records for Railway (your website)
- ✅ TXT record for Google site verification
- ✅ Any other DNS records you need

**Only delete:**
- ❌ Old MX records (if any)

---

### 📧 Email vs Website

- **MX records** = For email (Gmail)
- **CNAME records** = For website (Railway)

**You need BOTH:**
- MX records for Gmail to work
- CNAME records for your website to work

**They don't conflict!** You can have both.

---

## Quick Checklist

- [ ] Logged into Namecheap
- [ ] Opened Advanced DNS for `kyrex.co`
- [ ] Deleted any existing MX records
- [ ] Added new MX record:
  - [ ] Host: `@` (or blank)
  - [ ] Priority: `1`
  - [ ] Value: `SMTP.GOOGLE.COM` (or `SMTP.GOOGLE.COM.`)
  - [ ] TTL: Automatic
- [ ] Saved the record
- [ ] Waited 15-30 minutes
- [ ] Verified MX record at mxtoolbox.com
- [ ] Confirmed in Google Workspace

---

## After Setup

Once Gmail is activated:

1. **Create email accounts** in Google Workspace
   - Example: `sales@kyrex.co`
   - Example: `hr@kyrex.co`

2. **Update Railway Variables** (if needed)
   - Your Django app already uses `sales@kyrex.co`
   - Once Gmail is set up, you can configure email sending

3. **Test Email**
   - Send a test email to `sales@kyrex.co`
   - Should receive in Gmail

---

## Need Help?

**If MX record isn't working:**
1. Check mxtoolbox.com to verify MX record
2. Wait longer (up to 48 hours)
3. Verify record format matches Google's requirements
4. Check Namecheap's documentation for MX record format

**If Google verification fails:**
1. Double-check the MX record value
2. Make sure priority is `1`
3. Wait for DNS propagation
4. Try removing/adding period at end of value

---

## Summary

1. **Namecheap** → Domain List → Manage → Advanced DNS
2. **Delete** old MX records (if any)
3. **Add** new MX record:
   - Host: `@`
   - Priority: `1`
   - Value: `SMTP.GOOGLE.COM`
   - TTL: Automatic
4. **Save** and wait 15-30 minutes
5. **Confirm** in Google Workspace

That's it! 🚀
