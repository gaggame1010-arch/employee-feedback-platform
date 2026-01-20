# How to Share Your Error

## 📋 What I Need to Help You

Please share:

1. **The exact error message** (copy/paste from terminal)
2. **What command you ran** (e.g., `python manage.py runserver`)
3. **What you were trying to do** (e.g., start the server, create admin user)

---

## 🔍 How to Copy Error Message

### In PowerShell:
1. Right-click in the terminal
2. Select "Mark"
3. Drag to select the error text
4. Press Enter to copy
5. Paste it here

### Or:
1. Select the text with your mouse
2. Right-click → Copy
3. Paste it in your message

---

## ✅ Quick Test Commands

Run these and share the output:

**Test 1: Check Django**
```powershell
cd c:\project
.\.venv\Scripts\python.exe -c "import django; print('OK')"
```

**Test 2: Check if in right directory**
```powershell
cd c:\project
ls manage.py
```

**Test 3: Try starting server with full path**
```powershell
cd c:\project
.\.venv\Scripts\python.exe manage.py runserver
```

---

## 🆘 Common Error Patterns

**If you see:**
- `ModuleNotFoundError` → Virtual environment not activated
- `Permission denied` → Need to run as Administrator or use different port
- `Port already in use` → Use port 8001 instead
- `Execution of scripts is disabled` → Need to change PowerShell policy
- `No such table` → Need to run migrations

---

**Please share your exact error message and I'll fix it!**
