# Generated by Django 3.1.5 on 2024-03-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0007_auto_20240306_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('PRESENT', 'PRESENT')], default='PRESENT', max_length=50),
        ),
    ]