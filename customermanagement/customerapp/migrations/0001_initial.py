# Generated by Django 4.1.1 on 2022-09-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notification_email', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_type', models.CharField(choices=[('INDIVIDUAL', 'INDIVIDUAL'), ('CORPORATE', 'INDIVIDUAL')], default='INDIVIDUAL', max_length=20)),
            ],
        ),
    ]