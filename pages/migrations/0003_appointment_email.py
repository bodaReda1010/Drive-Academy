# Generated by Django 5.0.6 on 2024-06-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
