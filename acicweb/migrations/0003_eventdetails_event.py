# Generated by Django 4.2.1 on 2023-08-17 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acicweb', '0002_remove_eventdetails_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acicweb.events'),
            preserve_default=False,
        ),
    ]
