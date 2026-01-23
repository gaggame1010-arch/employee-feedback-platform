# Generated migration to add company fields to HrAccessCode

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0002_hraccesscode"),
    ]

    operations = [
        migrations.AddField(
            model_name="hraccesscode",
            name="company_name",
            field=models.CharField(blank=True, default="", max_length=150),
        ),
        migrations.AddField(
            model_name="hraccesscode",
            name="company_website",
            field=models.URLField(blank=True, default=""),
        ),
    ]

