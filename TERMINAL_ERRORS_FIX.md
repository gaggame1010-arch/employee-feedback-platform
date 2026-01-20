# Fix Common Terminal Errors

## 🔴 Common Errors and Solutions

### Error 1: "No module named django"

**What you see:**
```
ModuleNotFoundError: No module named 'django'
```

**Fix:**
```powershell
cd c:\project
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

**Make sure you see `(.venv)` in your prompt!**

---

### Error 2: "Execution of scripts is disabled"

**What you see:**
```
.\.venv\Scripts\Activate.ps1 : File cannot be loaded because running scripts is disabled on this system.
```

**Fix:**
1. Open PowerShell as **Administrator** (Right-click → Run as Administrator)
2. Run:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Type `Y` when asked
4. Try activating again

---

### Error 3: "Port 8000 is already in use"

**What you see:**
```
Error: That port is already in use.
```

**Fix Option A: Use different port**
```powershell
python manage.py runserver 8001
```
Then access: http://127.0.0.1:8001/

**Fix Option B: Kill the process using port 8000**
```powershell
netstat -ano | findstr :8000
# Note the PID number, then:
taskkill /PID <PID_NUMBER> /F
```

---

### Error 4: "No such table" or Database errors

**What you see:**
```
django.db.utils.OperationalError: no such table: ...
```

**Fix:**
```powershell
cd c:\project
.\.venv\Scripts\Activate.ps1
python manage.py migrate
```

---

### Error 5: "SyntaxError" or Python syntax errors

**What you see:**
```
SyntaxError: invalid syntax
```

**Fix:**
- Check if you're using the right Python version
- Make sure you activated the virtual environment
- Try: `.\.venv\Scripts\python.exe manage.py runserver`

---

### Error 6: "Permission denied" or Access errors

**What you see:**
```
PermissionError: [Errno 13] Permission denied
```

**Fix:**
- Run PowerShell as Administrator
- Or use a different port: `python manage.py runserver 8001`

---

### Error 7: "Command not found" or "python is not recognized"

**What you see:**
```
'python' is not recognized as an internal or external command
```

**Fix:**
Use the full path to Python:
```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

---

### Error 8: "Could not import settings"

**What you see:**
```
django.core.exceptions.ImproperlyConfigured: ...
```

**Fix:**
Make sure you're in the project directory:
```powershell
cd c:\project
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

---

## ✅ Correct Way to Start Server

**Step-by-step:**

1. **Open PowerShell**
   - Press `Windows + X`
   - Click "Windows PowerShell"

2. **Navigate to project:**
   ```powershell
   cd c:\project
   ```

3. **Activate virtual environment:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   **You should see `(.venv)` in your prompt!**

4. **Start server:**
   ```powershell
   python manage.py runserver
   ```

5. **You should see:**
   ```
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```

---

## 🔍 Alternative: Use Full Path (No Activation Needed)

If activation keeps failing, use the full path:

```powershell
cd c:\project
.\.venv\Scripts\python.exe manage.py runserver
```

---

## 📋 Quick Diagnostic Commands

**Test if Django works:**
```powershell
.\.venv\Scripts\python.exe -c "import django; print('Django version:', django.get_version())"
```

**Check if you're in the right directory:**
```powershell
pwd
# Should show: C:\project
```

**List files to verify:**
```powershell
ls manage.py
# Should show: manage.py
```

**Test Django configuration:**
```powershell
.\.venv\Scripts\python.exe manage.py check
```

---

## 🆘 Still Having Issues?

**Share the exact error message** and I'll help you fix it!

Common things to check:
- [ ] Are you in `c:\project` directory?
- [ ] Is virtual environment activated? (See `(.venv)` in prompt)
- [ ] Is Django installed? (Run diagnostic command above)
- [ ] Is port 8000 free? (Try port 8001 instead)

---

## 💡 Pro Tips

1. **Always activate virtual environment first**
   - Look for `(.venv)` in your prompt
   - If you don't see it, activation failed

2. **Use full path if activation fails**
   - `.\.venv\Scripts\python.exe` instead of `python`

3. **Keep server window open**
   - Don't close the terminal while server is running

4. **Check for typos**
   - `manage.py` not `mange.py`
   - `runserver` not `run server`

---

**What error message are you seeing? Share it and I'll help fix it!**
