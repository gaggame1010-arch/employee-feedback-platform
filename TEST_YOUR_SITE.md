# 🎉 Server Started! Test Your Site

Your server is running! Here's what to do next:

---

## ✅ Step 1: Test Employee Site

### 1.1 Open Homepage
1. Open your browser
2. Go to: **http://127.0.0.1:8000/**
3. You should see the **Anonymous Employee Platform** homepage

### 1.2 Test Submission Form
1. Click **"Submit"** button or go to: **http://127.0.0.1:8000/submit/**
2. Fill out the form:
   - **Company Access Code:** `123456` (from env.example)
   - **Type:** Select Issue, Concern, Question, or Suggestion
   - **Title:** Test Submission
   - **Description:** This is a test submission
3. Click **"Submit"**
4. **Save your Receipt Code!** (e.g., `12345-67890`)

### 1.3 Test Status Check
1. Go to: **http://127.0.0.1:8000/status/**
2. Enter the receipt code you just received
3. You should see your submission status

---

## ✅ Step 2: Test HR Admin Panel

### 2.1 Login to Admin
1. Go to: **http://127.0.0.1:8000/admin/**
2. Login with your admin credentials:
   - Username: (what you created earlier)
   - Password: (what you set earlier)

### 2.2 Explore Dashboard
You should see:
- **Welcome banner** at the top
- **Statistics cards** (Total, New, In Review, Responded, Closed)
- **Type statistics** (Issues, Concerns, Questions, Suggestions)
- **Recent Submissions** section

### 2.3 View Your Test Submission
1. Click on **"Submissions"** in the left menu
2. You should see your test submission in the list
3. Click on it to view details

### 2.4 Respond to Submission
1. On the submission detail page, scroll down
2. Find the **"HR Responses"** section
3. Type a response in the text box
4. Click **"Save"** or **"Save and continue editing"**
5. The submission status should automatically change to "Responded"

### 2.5 Test Filters
1. Click on any statistics card on the dashboard
2. It should filter submissions by that type/status
3. Try clicking "Issues", "New", etc.

---

## ✅ Step 3: Update Your Settings (Optional)

### 3.1 Change Company Access Code
1. Edit `env.example` file (or create `.env`)
2. Change:
   ```env
   COMPANY_ACCESS_CODE=your-new-secure-code
   ```
3. Restart server (Ctrl+C, then start again)

### 3.2 Update HR Email
1. Edit `env.example` or `.env`
2. Change:
   ```env
   HR_NOTIFY_EMAILS=your-actual-email@example.com
   ```
3. Restart server

---

## ✅ Step 4: Deploy to Railway (Make It Public)

Once everything works locally:

### 4.1 Push to GitHub
```powershell
git add .
git commit -m "Ready for deployment"
git push origin main
```

### 4.2 Deploy on Railway
1. Go to **https://railway.app**
2. Login with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your repository

### 4.3 Configure Railway
- Add PostgreSQL database
- Set environment variables (see `RAILWAY_VARIABLES_GUIDE.md`)
- Create admin user in Railway shell

### 4.4 Your app will be live!
- Public URL: `https://your-app.railway.app`

---

## 📋 Testing Checklist

**Employee Side:**
- [ ] Can access homepage
- [ ] Can submit with company access code
- [ ] Receives receipt code after submission
- [ ] Can check status with receipt code

**HR Side:**
- [ ] Can login to admin panel
- [ ] Sees dashboard with statistics
- [ ] Can view submissions list
- [ ] Can view submission details
- [ ] Can respond to submissions
- [ ] Status updates automatically when responding
- [ ] Can filter by type/status
- [ ] Statistics cards are clickable

---

## 🎯 What to Do Right Now

1. **Open browser:** http://127.0.0.1:8000/
2. **Test submitting** an issue/concern/question/suggestion
3. **Login to admin:** http://127.0.0.1:8000/admin/
4. **Check your submission** appears
5. **Try responding** to it

---

## 🆘 Keep Server Running!

**Important:** Don't close the terminal window where the server is running!

- The server must stay running for the site to work
- To stop: Press `Ctrl + C` in the server terminal
- To start again: Run `python manage.py runserver`

---

**Have fun testing! Let me know if everything works or if you need help! 🚀**
