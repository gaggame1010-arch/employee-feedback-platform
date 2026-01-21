# Fix "No Module Called Django" Error on Railway

## Quick Fixes

### Solution 1: Verify Requirements.txt Format

Make sure `requirements.txt` has NO blank lines and NO trailing spaces:

```
django>=6.0.1
python-dotenv==1.0.1
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
dj-database-url==2.1.0
```

### Solution 2: Check Railway Build Logs

1. **Railway Dashboard** → Your Service → **Deployments**
2. Click on the **latest deployment**
3. Check the **Build Logs** (not Runtime Logs)

Look for:
- ✅ `Collecting django...` (should see this)
- ✅ `Successfully installed django...` (should see this)
- ❌ If you see errors, note them down

### Solution 3: Force Railway to Rebuild

1. **Railway Dashboard** → Your Service → **Settings**
2. Scroll to **"Build"** section
3. Check **"Build Command"** - should be empty (Railway auto-detects)
4. If empty, try adding: `pip install -r requirements.txt`

Or click **"Redeploy"** button to rebuild.

### Solution 4: Check Python Version

Make sure `runtime.txt` contains exactly:
```
python-3.12
```

**No spaces, no quotes, just:** `python-3.12`

### Solution 5: Railway Configuration File

I've created `railway.json` for you. This helps Railway detect your app correctly.

**After adding this file:**
1. Commit and push to GitHub:
   ```powershell
   git add railway.json
   git commit -m "Add Railway configuration"
   git push origin main
   ```
2. Railway will auto-redeploy

### Solution 6: Manual Build Check

If still not working, check Railway is detecting Python:

1. **Railway Dashboard** → Your Service → **Settings**
2. Look for **"Buildpack"** or **"Builder"**
3. Should show **"Python"** or **"Nixpacks"**

If it shows something else (like "Node.js"), Railway didn't detect Python correctly.

**Fix:**
- Make sure `manage.py` is in the root directory ✅ (it is)
- Make sure `requirements.txt` is in root ✅ (it is)
- Add `railway.json` I created ✅ (done)

### Solution 7: Check Procfile

Make sure `Procfile` (no extension) exists in root:

```
release: python manage.py migrate --noinput; python manage.py collectstatic --noinput
web: gunicorn anonplatform.wsgi:application --bind 0.0.0.0:$PORT
```

**No `.txt` extension!** Just `Procfile`

## Most Common Issues

### Issue 1: Build Command Not Running
**Symptom:** No "Collecting django" in build logs

**Fix:** 
- Railway → Settings → Build → Add build command:
  ```
  pip install -r requirements.txt
  ```

### Issue 2: Wrong Python Version
**Symptom:** Build succeeds but runtime fails

**Fix:**
- Make sure `runtime.txt` has `python-3.12`
- Railway should auto-detect from `runtime.txt`

### Issue 3: Dependencies Not Found
**Symptom:** "ModuleNotFoundError" for other packages too

**Fix:**
- Check `requirements.txt` is being read
- Verify file is in root directory
- Check file has no encoding issues

## Debugging Steps

### Step 1: Check Build Logs
```
Railway → Service → Deployments → Latest → Build Logs
```

Look for:
- `Installing dependencies from requirements.txt`
- `Collecting django>=6.0.1`
- `Successfully installed django-6.x.x`

### Step 2: Check Runtime Logs
```
Railway → Service → Deployments → Latest → Runtime Logs
```

Look for:
- Startup errors
- ModuleNotFoundError details

### Step 3: Test Locally
```powershell
# Make sure your local environment works
python manage.py check
```

### Step 4: Verify Files Are Pushed
Make sure these files are in your GitHub repo:
- ✅ `requirements.txt`
- ✅ `runtime.txt`
- ✅ `Procfile`
- ✅ `manage.py`
- ✅ `railway.json` (I just created this)

## Still Not Working?

**Share the exact error from Railway logs:**

1. Railway → Service → Deployments → Latest
2. Click "View Logs"
3. Copy the **exact error message**
4. Share it with me

Common error messages and fixes:

- **"No such file or directory: requirements.txt"** → File not pushed to GitHub
- **"Command 'pip' not found"** → Python not detected
- **"invalid syntax"** → requirements.txt has formatting issues
- **"No module named 'django'"** → Dependencies not installed (current issue)

## Quick Checklist

- [ ] `requirements.txt` exists in root
- [ ] `runtime.txt` exists with `python-3.12`
- [ ] `Procfile` exists (no extension)
- [ ] `manage.py` exists in root
- [ ] `railway.json` exists (I created it)
- [ ] All files pushed to GitHub
- [ ] Railway detected Python correctly
- [ ] Build logs show Django installation
- [ ] No errors in build process

Try these fixes in order, and let me know which one works!
