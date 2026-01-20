# Alternative Deployment Options

If Railway isn't working, here are other easy options:

## Option 1: Render (Recommended Alternative) ⭐

**Why Render?**
- Free tier available
- Similar to Railway
- Automatic HTTPS
- Built-in PostgreSQL

### Steps:

1. **Sign up** at https://render.com (use GitHub login)

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select: `employee-feedback-platform`

3. **Configure**:
   - **Name**: `employee-feedback-platform`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn anonplatform.wsgi --bind 0.0.0.0:$PORT`

4. **Add PostgreSQL Database**:
   - Click "New +" → "PostgreSQL"
   - Name it: `feedback-db`
   - Render will automatically set `DATABASE_URL`

5. **Add Environment Variables**:
   Go to "Environment" tab and add:
   ```
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=0
   DJANGO_ALLOWED_HOSTS=your-app.onrender.com
   COMPANY_ACCESS_CODE=your-code
   HR_NOTIFY_EMAILS=hr@email.com
   DJANGO_DEFAULT_FROM_EMAIL=noreply@email.com
   DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
   ```

6. **Deploy** - Click "Create Web Service"

7. **After deployment**, open shell and run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

✅ **Your app will be live at**: `https://your-app.onrender.com`

---

## Option 2: Fly.io (Great Free Tier)

### Steps:

1. **Install Fly CLI**:
   ```bash
   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Sign up** at https://fly.io

3. **Login**:
   ```bash
   fly auth login
   ```

4. **Launch your app**:
   ```bash
   cd c:\project
   fly launch
   ```
   - Follow prompts
   - Create PostgreSQL database when asked

5. **Set secrets**:
   ```bash
   fly secrets set DJANGO_SECRET_KEY=your-key
   fly secrets set DJANGO_DEBUG=0
   fly secrets set COMPANY_ACCESS_CODE=your-code
   # ... etc
   ```

6. **Deploy**:
   ```bash
   fly deploy
   ```

✅ **Your app will be live at**: `https://your-app.fly.dev`

---

## Option 3: PythonAnywhere (Free Tier Available)

### Steps:

1. **Sign up** at https://www.pythonanywhere.com

2. **Upload files**:
   - Go to "Files" tab
   - Upload your project files (or use Git)

3. **Open Bash console**

4. **Set up virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```

5. **Create Web App**:
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python version: 3.10

6. **Configure WSGI file**:
   - Click on the WSGI file link
   - Replace content with:
   ```python
   import os
   import sys
   
   path = '/home/YOUR_USERNAME/employee-feedback-platform'
   if path not in sys.path:
       sys.path.insert(0, path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'anonplatform.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

7. **Set environment variables** in Web app settings

8. **Reload** the web app

---

## Option 4: Heroku (Classic, Still Works)

### Steps:

1. **Install Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli

2. **Login**:
   ```bash
   heroku login
   ```

3. **Create app**:
   ```bash
   heroku create your-app-name
   ```

4. **Add PostgreSQL**:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

5. **Set config vars**:
   ```bash
   heroku config:set DJANGO_SECRET_KEY=your-key
   heroku config:set DJANGO_DEBUG=0
   heroku config:set DJANGO_ALLOWED_HOSTS=your-app.herokuapp.com
   # ... etc
   ```

6. **Deploy**:
   ```bash
   git push heroku main
   ```

7. **Run migrations**:
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

---

## Quick Comparison

| Platform | Free Tier | Ease | Recommended |
|----------|-----------|------|-------------|
| **Render** | ✅ Yes | ⭐⭐⭐⭐⭐ | **Best alternative** |
| **Fly.io** | ✅ Yes | ⭐⭐⭐⭐ | Great option |
| **PythonAnywhere** | ✅ Yes | ⭐⭐⭐ | Good for learning |
| **Heroku** | ❌ Paid | ⭐⭐⭐⭐ | Classic but paid |

---

## My Recommendation

If Railway isn't working, try **Render** first - it's the most similar and easiest to use!

1. Go to https://render.com
2. Sign up with GitHub
3. Deploy from GitHub repo (same as Railway)
4. Follow the steps above

Let me know which one you want to try!
