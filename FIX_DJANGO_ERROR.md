# Fix "No module named django" Error

## ✅ Solution: Activate Virtual Environment First!

The error happens because you're using Python **without** the virtual environment activated. Django is installed **inside** the virtual environment.

---

## 🔧 Quick Fix

### Step 1: Open PowerShell
Press `Windows + X` → Click "Windows PowerShell" or "Terminal"

### Step 2: Navigate to project
```powershell
cd c:\project
```

### Step 3: Activate virtual environment
```powershell
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the beginning of your command prompt:
```
(.venv) PS C:\project>
```

### Step 4: Now run your command
```powershell
python manage.py createsuperuser
```

---

## ✅ Verify Django is Installed

After activating the virtual environment, test it:
```powershell
python -c "import django; print(django.get_version())"
```

You should see: `5.1.5`

---

## 📝 Complete Commands (Copy/Paste)

**Always activate virtual environment first:**

```powershell
cd c:\project
.\.venv\Scripts\Activate.ps1
python manage.py createsuperuser
```

**Or for running the server:**

```powershell
cd c:\project
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

---

## ⚠️ Common Mistakes

### ❌ Wrong: Running without activation
```powershell
cd c:\project
python manage.py createsuperuser  # ERROR: No module named django
```

### ✅ Correct: Activate first
```powershell
cd c:\project
.\.venv\Scripts\Activate.ps1  # Activate virtual environment
python manage.py createsuperuser  # Works!
```

---

## 🆘 If Still Getting Errors

### Error: "cannot be loaded because running scripts is disabled"

PowerShell script execution is disabled. Fix it:

1. **Open PowerShell as Administrator**
2. Run:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Type `Y` when asked
4. Try activating again

### Error: "Activate.ps1 not found"

The virtual environment might not exist. Create it:

```powershell
cd c:\project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

---

## 💡 Pro Tip: Always Check Prompt

When virtual environment is activated, you'll see:
```
(.venv) PS C:\project>
```

If you don't see `(.venv)`, the virtual environment is **not activated**!

---

## 🎯 Quick Checklist

- [ ] Opened PowerShell in `c:\project`
- [ ] Ran `.\.venv\Scripts\Activate.ps1`
- [ ] See `(.venv)` in prompt
- [ ] Django command works

---

**Remember: Always activate the virtual environment before running Django commands!**
