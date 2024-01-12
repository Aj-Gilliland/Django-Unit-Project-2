# Generated by Django 4.2.6 on 2024-01-12 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_bugreport_messages_bugreport_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='most_correct',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_report_most_correct', to='app.message'),
        ),
    ]
