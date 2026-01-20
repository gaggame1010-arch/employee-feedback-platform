# Safe server startup script with error handling
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Django Development Server" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in the right directory
if (-not (Test-Path "manage.py")) {
    Write-Host "ERROR: manage.py not found!" -ForegroundColor Red
    Write-Host "Please run this script from c:\project directory" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Current directory: $(Get-Location)" -ForegroundColor Yellow
    pause
    exit
}

# Check if virtual environment exists
if (-not (Test-Path ".venv\Scripts\python.exe")) {
    Write-Host "ERROR: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please create it first:" -ForegroundColor Yellow
    Write-Host "  python -m venv .venv" -ForegroundColor Yellow
    Write-Host "  .\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow
    Write-Host "  pip install -r requirements.txt" -ForegroundColor Yellow
    pause
    exit
}

# Try to activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
try {
    & .\.venv\Scripts\Activate.ps1
    Write-Host "✓ Virtual environment activated" -ForegroundColor Green
} catch {
    Write-Host "WARNING: Could not activate virtual environment" -ForegroundColor Yellow
    Write-Host "Will use full path to Python instead..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Checking Django installation..." -ForegroundColor Yellow
try {
    $djangoVersion = & .\.venv\Scripts\python.exe -c "import django; print(django.get_version())" 2>&1
    Write-Host "✓ Django $djangoVersion is installed" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Django is not installed!" -ForegroundColor Red
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    & .\.venv\Scripts\python.exe -m pip install -r requirements.txt
}

Write-Host ""
Write-Host "Running Django system check..." -ForegroundColor Yellow
try {
    & .\.venv\Scripts\python.exe manage.py check 2>&1 | Out-Null
    Write-Host "✓ System check passed" -ForegroundColor Green
} catch {
    Write-Host "WARNING: System check found issues" -ForegroundColor Yellow
    Write-Host "Continuing anyway..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting server at http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Start the server
try {
    & .\.venv\Scripts\python.exe manage.py runserver
} catch {
    Write-Host ""
    Write-Host "ERROR: Failed to start server" -ForegroundColor Red
    Write-Host "Error details:" -ForegroundColor Yellow
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "Trying alternative port 8001..." -ForegroundColor Yellow
    & .\.venv\Scripts\python.exe manage.py runserver 8001
}

Write-Host ""
Write-Host "Server stopped." -ForegroundColor Yellow
pause
