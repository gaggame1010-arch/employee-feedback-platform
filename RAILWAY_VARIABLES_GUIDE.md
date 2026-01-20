# How to Access Railway Variables Tab + Your Current Settings

## 🎯 How to Open Railway Variables Tab

### Step 1: Go to Your Railway Project
1. Visit **https://railway.app**
2. Log in with your GitHub account
3. Click on your project (the one you created from GitHub)

### Step 2: Select Your Service
- You'll see your web service listed (it might be named something like "employee-feedback-platform" or "web")
- **Click on your web service** (not the database, the web service)

### Step 3: Open Variables Tab
- You'll see tabs at the top: **"Deployments"**, **"Settings"**, **"Variables"**, **"Metrics"**, etc.
- **Click on the "Variables" tab**
- This is where you add/edit environment variables

### Visual Guide:
```
Railway Dashboard
  └── Your Project
      └── Your Web Service
          ├── Deployments
          ├── Settings
          ├── Variables  ← CLICK HERE
          ├── Metrics
          └── Logs
```

---

## 📋 Your Current Configuration

Based on your `env.example` file:

### Current Company Access Code:
```
123456
```
This is what employees use to submit anonymous issues.

### Current HR Email:
```
hr@company.com
```
⚠️ **This is just a placeholder!** You need to replace this with your **actual HR email address**.

---

## ✅ Variables You Need to Set in Railway

Go to **Variables** tab and add these (click "New Variable" for each):

### 1. Company Access Code
```
Key: COMPANY_ACCESS_CODE
Value: 123456
```
(Or change it to something more secure like `COMPANY2024` or `secure123`)

### 2. HR Email Address
```
Key: HR_NOTIFY_EMAILS
Value: your-actual-email@example.com
```
Replace `your-actual-email@example.com` with your real email address.

**Example:** If your HR email is `hr@mycompany.com`, set it to:
```
Key: HR_NOTIFY_EMAILS
Value: hr@mycompany.com
```

### 3. Django Secret Key
```
Key: DJANGO_SECRET_KEY
Value: X1iO1h4dlwrMDicvPS28n29d1vKVWwRT7WfBbq3SwsaOddcXx75f87YoMPtvw11NmFw
```

### 4. Debug Mode (Production)
```
Key: DJANGO_DEBUG
Value: 0
```

### 5. Allowed Hosts
```
Key: DJANGO_ALLOWED_HOSTS
Value: *.railway.app
```

### 6. Email Settings
```
Key: DJANGO_DEFAULT_FROM_EMAIL
Value: noreply@yourcompany.com
```

```
Key: DJANGO_EMAIL_BACKEND
Value: django.core.mail.backends.console.EmailBackend
```

---

## 🔐 What Should I Set for Company Access Code?

The current code is `123456`, which is easy but not very secure. You can:

**Option 1: Keep it simple** (for testing)
```
123456
```

**Option 2: Make it more secure** (recommended for production)
```
COMPANY2024
```
or
```
HR2024SECURE
```

**Option 3: Use a random code**
```
839271
```

**Important:** 
- Share this code **only** with employees
- Change it periodically for security
- Make it something employees can remember

---

## 📧 What Should I Set for HR Email?

Use your **actual email address** where you want to receive notifications about new submissions.

**Examples:**
- `hr@mycompany.com`
- `humanresources@company.com`
- `your.name@company.com`

You can set **multiple emails** by separating with commas:
```
Key: HR_NOTIFY_EMAILS
Value: hr@company.com,manager@company.com
```

---

## ⚠️ Important Notes

1. **Railway automatically provides `DATABASE_URL`** when you add a PostgreSQL database - you don't need to set this manually.

2. **After adding/changing variables**, Railway will **automatically redeploy** your app.

3. **Never commit secrets to GitHub** - always use environment variables.

4. **Variables are case-sensitive** - make sure spelling matches exactly.

---

## ✅ Quick Checklist

- [ ] Found Variables tab in Railway
- [ ] Added `COMPANY_ACCESS_CODE` (decided on a value)
- [ ] Added `HR_NOTIFY_EMAILS` (your real email)
- [ ] Added `DJANGO_SECRET_KEY`
- [ ] Added `DJANGO_DEBUG=0`
- [ ] Added `DJANGO_ALLOWED_HOSTS=*.railway.app`
- [ ] Added `DJANGO_DEFAULT_FROM_EMAIL`
- [ ] Added `DJANGO_EMAIL_BACKEND`

---

## 🆘 Still Can't Find It?

If you can't find the Variables tab:
1. Make sure you're logged into Railway
2. Make sure you've created a project from your GitHub repo
3. Make sure you've created a web service (not just a database)
4. Click on the web service, not the project root
5. Look for tabs at the top of the service page

Let me know if you need help finding it!
