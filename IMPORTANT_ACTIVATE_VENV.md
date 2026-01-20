# 🔴 CRITICAL: How to Fix "Couldn't import Django" Error

## The Problem
You're running Python **outside** the virtual environment. Django is installed **inside** `.venv`, so you must activate it first!

---

## ✅ SOLUTION 1: Use the Helper Scripts (Easiest!)

I've created helper scripts for you. Just double-click:

### For Windows:
**Double-click:** `create_admin.bat`

This will automatically:
1. Activate the virtual environment
2. Run the createsuperuser command
3. Wait for you to enter your details

---

### For PowerShell:
**Right-click** `create_admin.ps1` → **Run with PowerShell**

Or in PowerShell, run:
```powershell
.\create_admin.ps1
```

---

## ✅ SOLUTION 2: Manual Activation (Step-by-Step)

### Option A: Using Command Prompt (CMD)

1. Open **Command Prompt** (not PowerShell)
   - Press `Windows + R`
   - Type `cmd` and press Enter

2. Navigate to project:
   ```cmd
   cd c:\project
   ```

3. Activate virtual environment:
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   You should see `(.venv)` in your prompt:
   ```
   (.venv) C:\project>
   ```

4. Create admin user:
   ```cmd
   python manage.py createsuperuser
   ```

---

### Option B: Using PowerShell

1. Open **PowerShell**
   - Press `Windows + X`
   - Click "Windows PowerShell"

2. Navigate to project:
   ```powershell
   cd c:\project
   ```

3. Activate virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   If you get an execution policy error, run this first:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   Then try activating again.

4. You should see `(.venv)` in your prompt:
   ```
   (.venv) PS C:\project>
   ```

5. Create admin user:
   ```powershell
   python manage.py createsuperuser
   ```

---

## ✅ SOLUTION 3: Use Full Path to Python (No Activation Needed)

If activation doesn't work, use the full path:

### Windows Command Prompt:
```cmd
cd c:\project
.venv\Scripts\python.exe manage.py createsuperuser
```

### PowerShell:
```powershell
cd c:\project
.\.venv\Scripts\python.exe manage.py createsuperuser
```

---

## 🔍 How to Check if Virtual Environment is Activated

**Check your command prompt:**

✅ **ACTIVATED** - You'll see:
```
(.venv) PS C:\project>
(.venv) C:\project>
```

❌ **NOT ACTIVATED** - You'll see:
```
PS C:\project>
C:\project>
```

---

## 🆘 Troubleshooting

### Error: "Execution of scripts is disabled"

**Fix:**
1. Open PowerShell as **Administrator**
2. Run:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Type `Y` when asked
4. Try activating again

---

### Error: "Activate.ps1 not found"

**Check if virtual environment exists:**
```powershell
Test-Path .venv\Scripts\Activate.ps1
```

If it returns `False`, create the virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

---

### Still Getting "No module named django"

**Verify Django is installed:**
```powershell
.\.venv\Scripts\python.exe -c "import django; print(django.get_version())"
```

If this works, Django IS installed. The problem is you're not using the venv Python.

**Force use venv Python:**
```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

---

## 📝 Quick Reference

| Command | What It Does |
|---------|-------------|
| `.venv\Scripts\activate.bat` | Activates venv (CMD) |
| `.\.venv\Scripts\Activate.ps1` | Activates venv (PowerShell) |
| `.\.venv\Scripts\python.exe` | Uses venv Python directly (no activation needed) |
| `python manage.py createsuperuser` | Creates admin user (after activation) |

---

## ✅ Recommended: Use the Batch File

**Just double-click `create_admin.bat`** - it's the easiest way!

This will handle everything automatically.

---

**Remember: Django is installed, you just need to activate the virtual environment first!**
