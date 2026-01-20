# Fix "This site can't be reached" Error

## 🔴 The Problem
The error means **your Django server is not running**. You need to start it first!

---

## ✅ Solution: Start the Server

### Option 1: Double-Click the Batch File (Easiest!)

I've created `start_server.bat` for you. Just **double-click it** in your project folder!

This will:
- Activate the virtual environment
- Start the server
- Show you the URL

---

### Option 2: Manual Start (PowerShell)

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

4. **Start the server:**
   ```powershell
   python manage.py runserver
   ```

5. **You should see:**
   ```
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```

6. **Keep this window open!** The server must stay running.

---

### Option 3: Manual Start (Command Prompt)

1. **Open Command Prompt**
   - Press `Windows + R`
   - Type `cmd` and press Enter

2. **Navigate and start:**
   ```cmd
   cd c:\project
   .venv\Scripts\activate.bat
   python manage.py runserver
   ```

---

## 🌐 Access Your Site

Once the server is running, open your browser and go to:

- **Homepage:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Submit Form:** http://127.0.0.1:8000/submit/
- **Check Status:** http://127.0.0.1:8000/status/

---

## ⚠️ Important Notes

### Keep the Server Running!
- **Don't close** the PowerShell/Command Prompt window
- The server must stay running for the site to work
- To stop: Press `Ctrl + C` in the server window

### If Port 8000 is Busy

If you see "port already in use", use a different port:

```powershell
python manage.py runserver 8001
```

Then access: http://127.0.0.1:8001/

---

## 🔍 Troubleshooting

### Error: "No module named django"

**Fix:** Activate virtual environment first!
```powershell
.\.venv\Scripts\Activate.ps1
```

### Error: "Port already in use"

**Fix:** Use a different port:
```powershell
python manage.py runserver 8001
```

### Server starts but site still won't load

**Check:**
1. Is the server window still open?
2. Did you see "Starting development server..." message?
3. Try: http://127.0.0.1:8000/ (not localhost)
4. Check firewall isn't blocking it

### "This site can't be reached" after server starts

**Possible causes:**
- Server crashed (check the server window for errors)
- Wrong URL (must be http://127.0.0.1:8000/)
- Browser cache (try Ctrl+F5 to refresh)

---

## ✅ Quick Checklist

- [ ] Opened PowerShell/Command Prompt
- [ ] Navigated to `c:\project`
- [ ] Activated virtual environment (see `(.venv)` in prompt)
- [ ] Ran `python manage.py runserver`
- [ ] See "Starting development server..." message
- [ ] Server window is still open
- [ ] Opened browser to http://127.0.0.1:8000/

---

## 🎯 Quick Start Commands

**Copy and paste these:**

```powershell
cd c:\project
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

**Then open:** http://127.0.0.1:8000/

---

**Remember: The server must stay running! Keep that window open!**
