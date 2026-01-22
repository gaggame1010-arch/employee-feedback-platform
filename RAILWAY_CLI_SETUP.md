# Railway CLI Setup - Step by Step

## Where to Run Railway CLI Commands

Run these commands in **PowerShell on your local computer** (not in Railway).

---

## Step 1: Check if Node.js/npm is Installed

Open PowerShell and run:
```powershell
npm --version
```

### If you see a version number (like `10.0.0`):
✅ npm is installed! Go to **Step 2**.

### If you see an error:
❌ You need to install Node.js first.

**Install Node.js:**
1. Go to: https://nodejs.org
2. Download the **LTS version** (recommended)
3. Install it (default settings are fine)
4. Restart PowerShell
5. Run `npm --version` again to verify

---

## Step 2: Install Railway CLI

In PowerShell, run:
```powershell
npm install -g @railway/cli
```

Wait for installation to complete. You should see "added X packages".

---

## Step 3: Login to Railway

In PowerShell, run:
```powershell
railway login
```

This will:
- Open your browser
- Ask you to authorize Railway CLI
- Redirect you back
- Show "Logged in successfully"

---

## Step 4: Navigate to Your Project

In PowerShell, run:
```powershell
cd C:\project
```

Make sure you're in your project directory.

---

## Step 5: Link Railway to Your Project

In PowerShell, run:
```powershell
railway link
```

You'll see a list of your Railway projects. Select the one that matches your app.

---

## Step 6: Run Commands

Now you can run Django commands through Railway:

### Run Migrations:
```powershell
railway run python manage.py migrate
```

### Create Admin User:
```powershell
railway run python manage.py createsuperuser
```

Follow the prompts:
- Username: `hr_admin`
- Email: your HR email
- Password: create a strong password

---

## Complete Example

Here's what your PowerShell session should look like:

```powershell
# 1. Navigate to project
cd C:\project

# 2. Login (first time only)
railway login

# 3. Link to project (first time only)
railway link

# 4. Run migrations
railway run python manage.py migrate

# 5. Create admin user
railway run python manage.py createsuperuser
```

---

## Quick Start (Copy-Paste)

If you already have npm installed, copy-paste these commands in PowerShell:

```powershell
npm install -g @railway/cli
railway login
cd C:\project
railway link
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

---

## Troubleshooting

### "npm is not recognized"
→ Install Node.js from nodejs.org

### "railway: command not found"
→ Make sure Railway CLI installed successfully
→ Try: `npm install -g @railway/cli` again

### "Not linked to a project"
→ Run `railway link` first
→ Select your Railway project from the list

### "Authentication failed"
→ Run `railway login` again
→ Make sure you authorize in the browser

---

## Where Are You Now?

**Open PowerShell and run:**
```powershell
npm --version
```

Then tell me what you see, and I'll guide you from there!
