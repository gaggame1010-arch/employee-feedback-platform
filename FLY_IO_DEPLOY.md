# Deploy to Fly.io - Step by Step Guide

## Prerequisites

1. **Sign up** at [fly.io](https://fly.io) (free tier available)
2. **Install Fly CLI**:
   - **Windows**: Download from [fly.io/docs/hands-on/install-flyctl/](https://fly.io/docs/hands-on/install-flyctl/)
   - **Mac**: `brew install flyctl`
   - **Linux**: `curl -L https://fly.io/install.sh | sh`

## Quick Deploy Steps

### 1. Login to Fly.io

```powershell
fly auth login
```

This will open your browser to authenticate.

### 2. Create PostgreSQL Database

```powershell
fly postgres create --name anonymous-platform-db
```

Choose:
- **Region**: Pick closest to you (e.g., `iad` for Washington DC, `ord` for Chicago)
- **VM Size**: `shared-cpu-1x` (256MB) is free tier sufficient
- **Volume size**: 1GB is fine to start

**Save the connection details** that Fly.io shows you!

### 3. Create Fly.io App

```powershell
fly launch --no-deploy
```

This will:
- Create a `fly.toml` file (already created for you, but Fly will update it)
- Ask for app name (or use existing `fly.toml`)
- Ask for region (pick same as database)

### 4. Attach Database to App

```powershell
fly postgres attach anonymous-platform-db
```

This automatically sets `DATABASE_URL` environment variable.

### 5. Set Environment Variables

```powershell
# Set secret key (generate one first)
fly secrets set DJANGO_SECRET_KEY="your-secret-key-here"

# Set other required variables
fly secrets set DJANGO_DEBUG="0"
fly secrets set DJANGO_ALLOWED_HOSTS="anonymous-employee-platform.fly.dev"
fly secrets set COMPANY_ACCESS_CODE="123456"
fly secrets set HR_NOTIFY_EMAILS="hr@company.com"
fly secrets set DJANGO_DEFAULT_FROM_EMAIL="no-reply@company.com"
fly secrets set CSRF_TRUSTED_ORIGINS="https://anonymous-employee-platform.fly.dev"
```

**Or set them all at once:**
```powershell
fly secrets set ^
  DJANGO_SECRET_KEY="your-secret-key-here" ^
  DJANGO_DEBUG="0" ^
  DJANGO_ALLOWED_HOSTS="anonymous-employee-platform.fly.dev" ^
  COMPANY_ACCESS_CODE="123456" ^
  HR_NOTIFY_EMAILS="hr@company.com" ^
  DJANGO_DEFAULT_FROM_EMAIL="no-reply@company.com" ^
  CSRF_TRUSTED_ORIGINS="https://anonymous-employee-platform.fly.dev"
```

**Generate secret key:**
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 6. Deploy!

```powershell
fly deploy
```

This will:
- Build Docker image
- Deploy to Fly.io
- Run migrations automatically (if configured)

### 7. Run Migrations

```powershell
fly ssh console -C "python manage.py migrate"
```

### 8. Create Admin User

```powershell
fly ssh console -C "python manage.py createsuperuser"
```

Follow prompts to create HR admin account.

### 9. Your App is Live!

Visit: `https://anonymous-employee-platform.fly.dev`

## View Logs

```powershell
fly logs
```

## Scale Your App

```powershell
# View current status
fly status

# Scale up (if needed)
fly scale count 2

# Scale memory
fly scale vm shared-cpu-2x --memory 512
```

## Update Environment Variables

```powershell
fly secrets set VARIABLE_NAME="new-value"
```

## View Secrets (without values)

```powershell
fly secrets list
```

## SSH into App

```powershell
fly ssh console
```

## Troubleshooting

### Build Fails
```powershell
# Check logs
fly logs

# Test build locally
docker build -t test-build .
```

### Database Connection Issues
```powershell
# Check database status
fly postgres status anonymous-platform-db

# Check connection string
fly ssh console -C "echo \$DATABASE_URL"
```

### App Won't Start
```powershell
# Check logs
fly logs

# Check app status
fly status

# Restart app
fly apps restart anonymous-employee-platform
```

### Static Files Not Loading
```powershell
# Recollect static files
fly ssh console -C "python manage.py collectstatic --noinput"
```

### Port Issues
Make sure `PORT` environment variable is set (Fly.io sets this automatically).

## Database Backups

Fly.io PostgreSQL has automatic daily backups. To restore:

```powershell
fly postgres backups list -a anonymous-platform-db
fly postgres restore <backup-id>
```

## Free Tier Limits

- **3 shared-cpu-1x VMs** (256MB RAM)
- **3GB persistent volume storage**
- **160GB outbound data transfer per month**

This is usually enough for a small-to-medium application!

## Custom Domain

1. **Add domain in Fly.io dashboard:**
   - App → Settings → Domains → Add domain

2. **Update environment variables:**
   ```powershell
   fly secrets set DJANGO_ALLOWED_HOSTS="yourdomain.com,www.yourdomain.com"
   fly secrets set CSRF_TRUSTED_ORIGINS="https://yourdomain.com,https://www.yourdomain.com"
   ```

3. **Configure DNS** (Fly.io will show you what to add)

## Monitoring

View metrics:
```powershell
fly metrics
```

## Cost Estimate

**Free tier** covers:
- Small app (<256MB RAM)
- PostgreSQL database (small)
- Limited traffic

**Paid tier** starts at ~$5-10/month for:
- More memory
- More database storage
- Higher traffic limits

## Need Help?

- Fly.io Docs: [fly.io/docs](https://fly.io/docs)
- Community: [community.fly.io](https://community.fly.io)
