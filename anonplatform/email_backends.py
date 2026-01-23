"""
Custom email backends for Django.

This module provides email backends that work with Railway and other platforms
that block outbound SMTP connections.
"""

import logging
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import EmailMessage
from django.conf import settings

logger = logging.getLogger(__name__)


class SendGridEmailBackend(BaseEmailBackend):
    """
    Email backend using SendGrid API (not SMTP).
    
    This works on Railway and other platforms that block SMTP ports.
    
    Environment variables required:
    - SENDGRID_API_KEY: Your SendGrid API key
    - DJANGO_DEFAULT_FROM_EMAIL: The sender email address (must be verified in SendGrid)
    """
    
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        self.fail_silently = fail_silently
        self.api_key = None
        
        # Try to import sendgrid
        try:
            import sendgrid
            from sendgrid.helpers.mail import Mail, Email, Content
            self.sendgrid = sendgrid
            self.Mail = Mail
            self.Email = Email
            self.Content = Content
        except ImportError:
            if not fail_silently:
                raise ImportError(
                    "SendGrid package is not installed. "
                    "Install it with: pip install sendgrid"
                )
            self.sendgrid = None
        
        # Get API key from environment
        import os
        self.api_key = os.environ.get('SENDGRID_API_KEY', '')
        
        if not self.api_key and not fail_silently:
            logger.warning("SENDGRID_API_KEY not set. Emails will not be sent.")
    
    def send_messages(self, email_messages):
        """
        Send one or more EmailMessage objects and return the number of emails sent.
        """
        if not self.sendgrid or not self.api_key:
            if not self.fail_silently:
                raise ValueError("SendGrid not configured. Set SENDGRID_API_KEY environment variable.")
            return 0
        
        if not email_messages:
            return 0
        
        num_sent = 0
        sg = self.sendgrid.SendGridAPIClient(api_key=self.api_key)
        
        for message in email_messages:
            if not isinstance(message, EmailMessage):
                continue
            
            try:
                # Build SendGrid Mail object
                from_email = self.Email(message.from_email or settings.DEFAULT_FROM_EMAIL)
                
                # Handle multiple recipients
                to_emails = message.to
                if not to_emails:
                    continue
                
                # Create Mail object with first recipient
                # SendGrid requires at least one "to" email in the constructor
                mail = self.Mail(
                    from_email=from_email,
                    to_emails=self.Email(to_emails[0]),
                    subject=message.subject,
                    plain_text_content=message.body,
                )
                
                # Add additional recipients if any
                if len(to_emails) > 1:
                    for email in to_emails[1:]:
                        mail.add_to(self.Email(email))
                
                # Add CC recipients if any
                if message.cc:
                    for email in message.cc:
                        mail.add_cc(self.Email(email))
                
                # Add BCC recipients if any
                if message.bcc:
                    for email in message.bcc:
                        mail.add_bcc(self.Email(email))
                
                # Add reply-to if specified
                if message.reply_to:
                    mail.reply_to = self.Email(message.reply_to[0])
                
                # Send email via SendGrid API
                response = sg.send(mail)
                
                # Check response status
                if response.status_code in [200, 201, 202]:
                    num_sent += 1
                    logger.info(f"Email sent successfully via SendGrid to {to_emails}")
                else:
                    error_msg = f"SendGrid API returned status {response.status_code}: {response.body}"
                    logger.error(error_msg)
                    if not self.fail_silently:
                        raise Exception(error_msg)
                        
            except Exception as e:
                error_msg = f"Error sending email via SendGrid: {type(e).__name__}: {e}"
                logger.error(error_msg, exc_info=True)
                if not self.fail_silently:
                    raise
                # Continue to next message if fail_silently is True
        
        return num_sent


class ResendEmailBackend(BaseEmailBackend):
    """
    Email backend using Resend API.
    
    Resend is a modern email API service with a great free tier.
    Free tier: 100 emails/day, 3,000 emails/month
    
    Environment variables required:
    - RESEND_API_KEY: Your Resend API key
    - DJANGO_DEFAULT_FROM_EMAIL: The sender email address (must be verified in Resend)
    """
    
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        self.fail_silently = fail_silently
        self.api_key = None
        
        # Try to import resend
        try:
            import resend
            self.resend = resend
        except ImportError:
            if not fail_silently:
                raise ImportError(
                    "Resend package is not installed. "
                    "Install it with: pip install resend"
                )
            self.resend = None
        
        # Get API key from environment
        import os
        self.api_key = os.environ.get('RESEND_API_KEY', '')
        
        if not self.api_key and not fail_silently:
            logger.warning("RESEND_API_KEY not set. Emails will not be sent.")
    
    def send_messages(self, email_messages):
        """
        Send one or more EmailMessage objects and return the number of emails sent.
        """
        import sys
        import traceback
        from datetime import datetime
        
        if not self.resend or not self.api_key:
            error_msg = "Resend not configured. Set RESEND_API_KEY environment variable."
            print(f"\n{'='*80}", file=sys.stderr, flush=True)
            print(f"[{datetime.now()}] *** RESEND ERROR: {error_msg} ***", file=sys.stderr, flush=True)
            print(f"RESEND: API key set: {'Yes' if self.api_key else 'No'}", file=sys.stderr, flush=True)
            print(f"RESEND: Resend module loaded: {'Yes' if self.resend else 'No'}", file=sys.stderr, flush=True)
            print(f"{'='*80}\n", file=sys.stderr, flush=True)
            logger.error(error_msg)
            if not self.fail_silently:
                raise ValueError(error_msg)
            return 0
        
        if not email_messages:
            return 0
        
        num_sent = 0
        
        # Set API key at module level (Resend requires this)
        self.resend.api_key = self.api_key
        
        for message in email_messages:
            if not isinstance(message, EmailMessage):
                continue
            
            try:
                from_email = message.from_email or settings.DEFAULT_FROM_EMAIL
                to_emails = message.to
                if not to_emails:
                    continue
                
                # Log email attempt
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n{'='*80}", file=sys.stdout, flush=True)
                print(f"[{timestamp}] *** RESEND: Starting email send ***", file=sys.stdout, flush=True)
                print(f"RESEND: From: {from_email}", file=sys.stdout, flush=True)
                print(f"RESEND: To: {to_emails}", file=sys.stdout, flush=True)
                print(f"RESEND: Subject: {message.subject}", file=sys.stdout, flush=True)
                print(f"RESEND: API key prefix: {self.api_key[:10]}..." if len(self.api_key) > 10 else "RESEND: API key: (empty)", file=sys.stdout, flush=True)
                print(f"{'='*80}\n", file=sys.stdout, flush=True)
                
                # Resend supports multiple recipients
                params = {
                    "from": from_email,
                    "to": to_emails,
                    "subject": message.subject,
                    "text": message.body,
                }
                
                # Add CC if any
                if message.cc:
                    params["cc"] = message.cc
                
                # Add BCC if any
                if message.bcc:
                    params["bcc"] = message.bcc
                
                # Add reply-to if specified
                if message.reply_to:
                    params["reply_to"] = message.reply_to[0]
                
                # Send email via Resend API
                email = self.resend.Emails.send(params)
                
                # Log response
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n{'='*80}", file=sys.stdout, flush=True)
                print(f"[{timestamp}] *** RESEND: API Response ***", file=sys.stdout, flush=True)
                print(f"RESEND: Response type: {type(email)}", file=sys.stdout, flush=True)
                print(f"RESEND: Response value: {email}", file=sys.stdout, flush=True)
                print(f"{'='*80}\n", file=sys.stdout, flush=True)
                
                # Resend returns a dict with 'id' on success
                if email and isinstance(email, dict) and 'id' in email:
                    num_sent += 1
                    success_msg = f"Email sent successfully via Resend to {to_emails}, id: {email['id']}"
                    logger.info(success_msg)
                    print(f"[{timestamp}] RESEND SUCCESS: {success_msg}", file=sys.stdout, flush=True)
                elif email:  # Some versions might return different format
                    num_sent += 1
                    success_msg = f"Email sent successfully via Resend to {to_emails}"
                    logger.info(success_msg)
                    print(f"[{timestamp}] RESEND SUCCESS: {success_msg}", file=sys.stdout, flush=True)
                else:
                    error_msg = f"Resend API returned unexpected response: {email}"
                    logger.error(error_msg)
                    print(f"[{timestamp}] RESEND ERROR: {error_msg}", file=sys.stderr, flush=True)
                    if not self.fail_silently:
                        raise Exception(error_msg)
                        
            except Exception as e:
                error_msg = f"Error sending email via Resend: {type(e).__name__}: {e}"
                traceback_str = traceback.format_exc()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"\n{'='*80}", file=sys.stderr, flush=True)
                print(f"[{timestamp}] *** RESEND EXCEPTION ***", file=sys.stderr, flush=True)
                print(f"RESEND ERROR: {error_msg}", file=sys.stderr, flush=True)
                print(f"RESEND TRACEBACK:\n{traceback_str}", file=sys.stderr, flush=True)
                print(f"{'='*80}\n", file=sys.stderr, flush=True)
                
                logger.error(error_msg, exc_info=True)
                if not self.fail_silently:
                    raise
        
        return num_sent


class MailgunEmailBackend(BaseEmailBackend):
    """
    Email backend using Mailgun API.
    
    Mailgun is a popular email service with good free tier.
    Free tier: 5,000 emails/month for first 3 months, then 1,000/month
    
    Environment variables required:
    - MAILGUN_API_KEY: Your Mailgun API key
    - MAILGUN_DOMAIN: Your Mailgun domain (e.g., 'mg.yourdomain.com')
    - DJANGO_DEFAULT_FROM_EMAIL: The sender email address
    """
    
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        self.fail_silently = fail_silently
        self.api_key = None
        self.domain = None
        
        # Try to import requests (Mailgun uses HTTP API)
        try:
            import requests
            self.requests = requests
        except ImportError:
            if not fail_silently:
                raise ImportError(
                    "requests package is not installed. "
                    "Install it with: pip install requests"
                )
            self.requests = None
        
        # Get API key and domain from environment
        import os
        self.api_key = os.environ.get('MAILGUN_API_KEY', '')
        self.domain = os.environ.get('MAILGUN_DOMAIN', '')
        
        if not self.api_key and not fail_silently:
            logger.warning("MAILGUN_API_KEY not set. Emails will not be sent.")
        if not self.domain and not fail_silently:
            logger.warning("MAILGUN_DOMAIN not set. Emails will not be sent.")
    
    def send_messages(self, email_messages):
        """
        Send one or more EmailMessage objects and return the number of emails sent.
        """
        if not self.requests or not self.api_key or not self.domain:
            if not self.fail_silently:
                raise ValueError(
                    "Mailgun not configured. Set MAILGUN_API_KEY and MAILGUN_DOMAIN environment variables."
                )
            return 0
        
        if not email_messages:
            return 0
        
        num_sent = 0
        api_url = f"https://api.mailgun.net/v3/{self.domain}/messages"
        
        for message in email_messages:
            if not isinstance(message, EmailMessage):
                continue
            
            try:
                from_email = message.from_email or settings.DEFAULT_FROM_EMAIL
                to_emails = message.to
                if not to_emails:
                    continue
                
                # Mailgun API parameters
                data = {
                    "from": from_email,
                    "to": to_emails,  # Can be a list or comma-separated string
                    "subject": message.subject,
                    "text": message.body,
                }
                
                # Add CC if any
                if message.cc:
                    data["cc"] = message.cc if isinstance(message.cc, str) else ",".join(message.cc)
                
                # Add BCC if any
                if message.bcc:
                    data["bcc"] = message.bcc if isinstance(message.bcc, str) else ",".join(message.bcc)
                
                # Add reply-to if specified
                if message.reply_to:
                    data["h:Reply-To"] = message.reply_to[0]
                
                # Send email via Mailgun API
                response = self.requests.post(
                    api_url,
                    auth=("api", self.api_key),
                    data=data,
                    timeout=10
                )
                
                # Check response status
                if response.status_code == 200:
                    num_sent += 1
                    logger.info(f"Email sent successfully via Mailgun to {to_emails}")
                else:
                    error_msg = f"Mailgun API returned status {response.status_code}: {response.text}"
                    logger.error(error_msg)
                    if not self.fail_silently:
                        raise Exception(error_msg)
                        
            except Exception as e:
                error_msg = f"Error sending email via Mailgun: {type(e).__name__}: {e}"
                logger.error(error_msg, exc_info=True)
                if not self.fail_silently:
                    raise
        
        return num_sent
