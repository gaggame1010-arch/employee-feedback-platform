# How to Push Code to GitHub - Step by Step

Follow these steps to push your project to GitHub so you can deploy it on Railway.

## Prerequisites

1. **GitHub Account**: If you don't have one, sign up at https://github.com (it's free)

2. **Git Installed**: Check if you have git installed:
   ```bash
   git --version
   ```
   
   If not installed, download from: https://git-scm.com/download/win

---

## Step 1: Create a GitHub Repository

1. **Go to GitHub**: https://github.com

2. **Sign in** to your account

3. **Create a new repository**:
   - Click the **"+"** icon in the top right corner
   - Select **"New repository"**

4. **Fill in the repository details**:
   - **Repository name**: `employee-feedback-platform` (or any name you like)
   - **Description**: "Anonymous Employee Feedback Platform" (optional)
   - **Visibility**: Choose **Public** (free, and required for Railway free tier)
     - Or **Private** if you prefer (you can always change this later)
   - **DO NOT** check:
     - ❌ "Add a README file" (you already have one)
     - ❌ "Add .gitignore" (you already have one)
     - ❌ "Choose a license" (optional, you can add later)

5. **Click "Create repository"**

6. **Copy the repository URL** - you'll see it on the next page:
   - It will look like: `https://github.com/YOUR_USERNAME/employee-feedback-platform.git`
   - Or SSH: `git@github.com:YOUR_USERNAME/employee-feedback-platform.git`
   - **Save this URL** - you'll need it in Step 3!

---

## Step 2: Initialize Git (if not already done)

Open PowerShell or Command Prompt in your project folder (`c:\project`):

```bash
cd c:\project
```

Check if git is already initialized:
```bash
git status
```

### If you see "not a git repository" error:

Initialize git:
```bash
git init
```

### If git is already initialized:

You can skip to Step 3!

---

## Step 3: Add Your Files to Git

Add all files to git:
```bash
git add .
```

This adds all files (respecting your `.gitignore` file).

**Verify what's being added**:
```bash
git status
```

You should see your files listed in green.

---

## Step 4: Create Your First Commit

Commit your files:
```bash
git commit -m "Initial commit - Employee Feedback Platform ready for deployment"
```

This saves your code with a message describing what you're committing.

---

## Step 5: Connect to GitHub

Add your GitHub repository as the remote:

**Replace `YOUR_USERNAME` and `REPOSITORY_NAME` with your actual GitHub username and repo name:**

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
```

For example, if your username is `john` and repo is `employee-feedback-platform`:
```bash
git remote add origin https://github.com/john/employee-feedback-platform.git
```

**Verify the remote was added**:
```bash
git remote -v
```

You should see:
```
origin  https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git (fetch)
origin  https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git (push)
```

---

## Step 6: Push to GitHub

Set the default branch name (if needed):
```bash
git branch -M main
```

Push your code to GitHub:
```bash
git push -u origin main
```

**You'll be prompted to login:**
- GitHub may ask for your username and password
- **For password**: Use a **Personal Access Token** (not your GitHub password)
  - See "Troubleshooting" below for how to create one

**If successful**, you'll see:
```
Enumerating objects: XX, done.
Counting objects: 100% (XX/XX), done.
Writing objects: 100% (XX/XX), done.
To https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

## Step 7: Verify on GitHub

1. Go back to your GitHub repository page
2. Refresh the page
3. You should see all your files!

---

## Troubleshooting

### Problem: "Authentication failed" when pushing

**Solution**: Use a Personal Access Token instead of password

1. **Create a Personal Access Token**:
   - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Click "Generate new token (classic)"
   - Name it: "Railway Deployment"
   - Check "repo" scope (full control)
   - Click "Generate token"
   - **COPY THE TOKEN** - you won't see it again!

2. **When prompted for password**, paste the token instead

### Problem: "Remote origin already exists"

**Solution**: Remove and re-add the remote
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
```

### Problem: "Permission denied"

**Solution**: Make sure:
- You're using the correct repository URL
- Your GitHub username is correct
- You have access to the repository (you're the owner)

### Problem: "Failed to push some refs"

**Solution**: If GitHub created a README, you need to pull first:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Problem: "Branch 'master' instead of 'main'"

**Solution**: Use your actual branch name:
```bash
git branch  # See current branch name
git push -u origin master  # If your branch is 'master'
```

---

## Quick Copy-Paste Commands

**Replace YOUR_USERNAME and REPOSITORY_NAME:**

```bash
cd c:\project
git init
git add .
git commit -m "Initial commit - Ready for deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
git push -u origin main
```

---

## Next Steps After Pushing

Once your code is on GitHub:

1. ✅ **Go to Railway**: https://railway.app
2. ✅ **Login with GitHub**
3. ✅ **Deploy from GitHub repo**
4. ✅ **Follow the Railway deployment guide**

See `RAILWAY_DEPLOY.md` for the next steps!

---

## Need Help?

- GitHub Docs: https://docs.github.com
- Git Documentation: https://git-scm.com/doc
- Check if your files are visible on GitHub repository page
