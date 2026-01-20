# Anonymous Employee Feedback Platform

A Django-based platform that allows employees to submit anonymous feedback, concerns, questions, or suggestions using a company access code, and enables HR to manage and respond to submissions through a secure admin dashboard.

## Features

- **Anonymous Submissions**: Employees can submit feedback without logging in
- **Company Access Code**: Shared code for employee access
- **Receipt Codes**: Unique tracking codes for employees to check submission status
- **HR Dashboard**: Secure admin interface for managing submissions
- **Email Notifications**: HR receives email alerts for new submissions
- **Rate Limiting**: Protection against abuse
- **Modern UI**: Dark theme with responsive design

## Quick Start (Local Development)

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd project
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (for HR admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Employee site: http://127.0.0.1:8000/
   - HR Admin: http://127.0.0.1:8000/admin/

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions to make your app publicly accessible.

**Quick deploy options**:
- **Railway** (easiest): Connect GitHub repo, add env vars, deploy
- **Heroku**: Use Procfile, add PostgreSQL, deploy
- **DigitalOcean**: App Platform with automatic deployment
- **PythonAnywhere**: Free tier available

## Environment Variables

Required environment variables (see `env.example`):

- `DJANGO_SECRET_KEY`: Django secret key (generate a strong random string)
- `DJANGO_DEBUG`: Set to `0` for production
- `DJANGO_ALLOWED_HOSTS`: Your domain name(s), comma-separated
- `COMPANY_ACCESS_CODE`: Code shared with employees
- `HR_NOTIFY_EMAILS`: Comma-separated list of HR email addresses
- `DJANGO_DEFAULT_FROM_EMAIL`: Email address for sending notifications
- `DATABASE_URL`: PostgreSQL connection string (auto-set by most platforms)

## Usage

### For Employees

1. Visit the homepage
2. Enter the company access code
3. Submit feedback (Issue, Concern, Question, or Suggestion)
4. Save your receipt code to check status later
5. Use receipt code lookup to view HR responses

### For HR

1. Log in at `/admin/`
2. View dashboard with statistics
3. Click on submissions to view details
4. Add HR responses in the inline form
5. Update submission status
6. Use bulk actions for multiple submissions

## Project Structure

```
project/
├── anonplatform/          # Main Django project
│   ├── settings.py        # Settings (supports .env)
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
├── submissions/          # Main app
│   ├── models.py         # Submission and HrResponse models
│   ├── views.py          # Employee-facing views
│   ├── admin.py          # HR admin customization
│   ├── middleware.py     # Rate limiting
│   └── templates/       # Employee templates
├── templates/            # Admin templates
│   └── admin/           # Custom admin UI
├── requirements.txt     # Python dependencies
├── Procfile            # Deployment config
└── DEPLOYMENT.md       # Deployment guide
```

## Security Features

- Rate limiting on anonymous endpoints
- CSRF protection
- XSS protection headers
- Secure cookie settings
- Input validation and sanitization
- Anonymous submissions (no user tracking)

## License

MIT License - feel free to use for your organization.

## Support

For deployment help, see [DEPLOYMENT.md](DEPLOYMENT.md).
