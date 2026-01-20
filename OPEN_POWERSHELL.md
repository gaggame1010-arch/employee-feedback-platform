# How to Open PowerShell in Your Project Folder

## ✅ Easiest Method: Right-Click in File Explorer

1. **Open File Explorer** (Windows key + E)

2. **Navigate to your project**: 
   - Go to `C:\project`

3. **Right-click** in an empty area (not on a file)

4. **While holding Shift**, click **"Open PowerShell window here"**
   - Or **"Open in Terminal"** (Windows 11)

5. ✅ **PowerShell opens in your project folder!**

---

## Method 2: From Start Menu

1. **Press Windows key**

2. **Type**: `powershell`

3. **Press Enter**

4. **Navigate to your project**:
   ```powershell
   cd C:\project
   ```

---

## Method 3: From Current Folder Address Bar

1. **Open File Explorer** and go to `C:\project`

2. **Click in the address bar** (where it shows `C:\project`)

3. **Type**: `powershell`

4. **Press Enter**

5. ✅ PowerShell opens in that folder!

---

## Method 4: Windows 11 - Terminal

If you're on **Windows 11**:

1. **Right-click** in File Explorer (`C:\project`)

2. Click **"Open in Terminal"**

3. If it opens Command Prompt, click the **arrow** next to "Command Prompt"

4. Select **"PowerShell"**

---

## Visual Guide

**File Explorer → Right-Click → "Open PowerShell window here"**

That's it! You'll see a blue window with:
```
PS C:\project>
```

This means PowerShell is ready and you're in the right folder!

---

## Next Steps

Once PowerShell is open in `C:\project`, you can run:

```powershell
git init
git add .
git commit -m "Initial commit"
# ... etc
```

---

## Tip

If you see `PS C:\Users\YourName>` instead of `PS C:\project>`, just run:
```powershell
cd C:\project
```

Then you're ready to go! 🚀
