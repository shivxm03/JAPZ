# Generated by Django 3.2.7 on 2021-09-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='FEMALE', max_length=6)),
                ('Preference', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='FEMALE', max_length=6)),
                ('Age_range_from', models.CharField(choices=[('FROM', (('18', '20'), '24')), ('TO', (('30', '35'), '40'))], default=18, max_length=2)),
                ('Age_range_to', models.CharField(choices=[('FROM', (('18', '20'), '24')), ('TO', (('30', '35'), '40'))], default=30, max_length=2)),
                ('Country', models.CharField(choices=[('India', 'India'), ('Japan', 'Japan'), ('England', 'England')], default='India', max_length=7)),
            ],
        ),
    ]
