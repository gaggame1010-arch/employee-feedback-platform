# Generated migration for HrAccessCode model

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HrAccessCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_code', models.CharField(db_index=True, max_length=20, unique=True)),
                ('notification_email', models.EmailField(blank=True, help_text="Email address to receive notifications for submissions using this code. If empty, uses user's email.")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='hr_access_code', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'HR Access Code',
                'verbose_name_plural': 'HR Access Codes',
            },
        ),
        migrations.AddField(
            model_name='submission',
            name='hr_access_code',
            field=models.ForeignKey(blank=True, help_text='The HR access code used to submit this feedback', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submissions', to='submissions.hraccesscode'),
        ),
    ]
