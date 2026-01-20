# How to Create Admin User (HR Login)

## 🏠 Option 1: Create Admin User Locally (On Your Computer)

If you want to test the admin panel on your local server:

### Step 1: Make sure your server is NOT running
Press `Ctrl+C` in the terminal where your server is running to stop it.

### Step 2: Open PowerShell in your project folder
```
cd c:\project
```

### Step 3: Activate virtual environment (if using one)
```
.\.venv\Scripts\Activate.ps1
```

### Step 4: Create admin user
Run this command:
```bash
python manage.py createsuperuser
```

### Step 5: Follow the prompts
You'll be asked to enter:
1. **Username**: Type a username (e.g., `hr_admin` or `admin`)
2. **Email address**: Type your email (e.g., `hr@company.com`)
3. **Password**: Type a strong password (you'll type it twice)
   - Password won't show on screen (that's normal)
   - Make it secure!

**Example:**
```
Username: hr_admin
Email address: hr@company.com
Password: [type your password - won't show]
Password (again): [type again]
```

### Step 6: Start your server again
```bash
python manage.py runserver
```

### Step 7: Login to admin
Go to: **http://127.0.0.1:8000/admin/**

Use the username and password you just created!

---

## ☁️ Option 2: Create Admin User on Railway (After Deployment)

After your app is deployed on Railway:

### Method A: Using Railway Shell (Recommended)

1. **Go to Railway Dashboard**
   - Visit https://railway.app
   - Click on your project
   - Click on your web service

2. **Open Shell**
   - Click on **"Deployments"** tab
   - Click on the **"..."** (three dots) next to your latest deployment
   - Select **"Open Shell"** (or look for "Shell" or "Terminal" tab)

3. **Run migrations** (if not done automatically)
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Follow the prompts** (same as local):
   - Username: `hr_admin`
   - Email: Your HR email
   - Password: Strong password (type twice)

6. **Done!** Login at: `https://your-app.railway.app/admin/`

### Method B: Using Railway CLI (Alternative)

If you have Railway CLI installed:

1. **Login to Railway**
   ```bash
   railway login
   ```

2. **Link to your project**
   ```bash
   railway link
   ```

3. **Run commands**
   ```bash
   railway run python manage.py migrate
   railway run python manage.py createsuperuser
   ```

---

## 🔐 Example Admin User Setup

Here's a complete example:

**Username Options:**
- `hr_admin`
- `admin`
- `hr`
- `yourname`

**Email:**
- `hr@yourcompany.com`
- `your.email@gmail.com` (for testing)

**Password:**
- Use a **strong password**
- At least 8 characters
- Mix of letters, numbers, symbols
- Example: `Hr@2024Secure!`

---

## ✅ Verify Admin User Was Created

### Local:
1. Go to http://127.0.0.1:8000/admin/
2. Try logging in with your username/password
3. You should see the HR Dashboard!

### Railway:
1. Go to `https://your-app.railway.app/admin/`
2. Try logging in with your username/password
3. You should see the HR Dashboard!

---

## 🆘 Troubleshooting

### "Error: That username is already taken"
- Someone already created that username
- Try a different username (e.g., `hr_admin2`)

### "Command not found: python"
- Try `python3` instead of `python`
- Or activate your virtual environment first

### "No such table: auth_user"
- You need to run migrations first:
  ```bash
  python manage.py migrate
  ```

### Can't access admin on Railway
- Make sure your app is deployed successfully
- Check Railway logs for errors
- Verify `DJANGO_DEBUG=0` and `ALLOWED_HOSTS` includes your Railway domain

---

## 📝 Quick Command Summary

**Local Development:**
```bash
cd c:\project
.\.venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Railway (in Shell):**
```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 💡 Tips

1. **Remember your credentials!** Write them down securely
2. **Use a strong password** - you'll handle employee data
3. **Test locally first** before deploying to Railway
4. **Create multiple admin users** if needed (just run `createsuperuser` again)

Need help with any step? Let me know!
