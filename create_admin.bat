@echo off
echo Activating virtual environment...
call .venv\Scripts\activate.bat
echo.
echo Creating admin user...
python manage.py createsuperuser
pause
