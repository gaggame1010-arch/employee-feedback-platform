# Quick Guide: Push to GitHub (Copy-Paste Commands)

## Step 1: Create GitHub Repository (Do This First!)

1. Go to https://github.com and sign in
2. Click the **"+"** icon → **"New repository"**
3. Repository name: `employee-feedback-platform` (or any name)
4. Choose **Public** (free, needed for Railway)
5. **DO NOT check** "Add a README" or ".gitignore" (you already have them)
6. Click **"Create repository"**
7. **Copy the repository URL** - it looks like:
   ```
   https://github.com/YOUR_USERNAME/employee-feedback-platform.git
   ```

## Step 2: Run These Commands

Open PowerShell or Command Prompt in your project folder and run:

**Replace YOUR_USERNAME and REPOSITORY_NAME with your actual GitHub info:**

```bash
# Navigate to your project (if not already there)
cd c:\project

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit - Employee Feedback Platform"

# Set branch name to main
git branch -M main

# Add GitHub as remote (REPLACE with your actual GitHub URL)
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git

# Push to GitHub
git push -u origin main
```

**When prompted:**
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (see below)

---

## Creating a Personal Access Token

GitHub requires a token instead of your password:

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token (classic)"**
3. Name: `Railway Deployment`
4. Check **"repo"** (full control of repositories)
5. Click **"Generate token"**
6. **COPY THE TOKEN** - you won't see it again!
7. Use this token as your password when pushing

---

## Quick Example

If your GitHub username is `johnsmith` and repo name is `employee-feedback-platform`:

```bash
cd c:\project
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/johnsmith/employee-feedback-platform.git
git push -u origin main
```

---

## Troubleshooting

**"Authentication failed"?**
- Use Personal Access Token as password (see above)

**"Remote origin already exists"?**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
```

**"Permission denied"?**
- Check your GitHub username is correct
- Make sure you own the repository

---

For detailed instructions, see `GITHUB_SETUP.md`
