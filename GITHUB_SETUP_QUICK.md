# Quick GitHub Setup for Railway

## Step 1: Initialize Git (if not done)

```powershell
cd C:\project
git init
```

## Step 2: Create GitHub Repository

1. **Go to GitHub.com** and sign in
2. Click **"+"** → **"New repository"**
3. **Name it:** `anonymous-employee-platform` (or any name)
4. Make it **Public** (Railway needs access)
5. **Don't** check "Initialize with README" (you already have code)
6. Click **"Create repository"**

## Step 3: Add All Files and Commit

```powershell
cd C:\project
git add .
git commit -m "Initial commit - ready for Railway"
```

## Step 4: Connect to GitHub and Push

GitHub will show you commands after creating the repo. They'll look like:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

**Replace:**
- `YOUR_USERNAME` with your GitHub username
- `YOUR_REPO_NAME` with your repository name

## Step 5: Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository
5. Railway will auto-detect and deploy!

---

## Complete Commands (Copy-Paste Ready)

```powershell
# Navigate to project
cd C:\project

# Initialize git (if needed)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - ready for Railway deployment"

# Create branch (if needed)
git branch -M main

# Add GitHub remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

---

## After Pushing to GitHub

1. **Railway will see your code**
2. **Railway will auto-deploy**
3. **Add PostgreSQL database** in Railway
4. **Set environment variables** in Railway
5. **Your app will be live!**

See `RAILWAY_QUICK_START.md` for next steps after GitHub push!
