# Generated by Django 4.1.3 on 2022-11-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_remove_eventsubject_event_eventsubject_event"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventsubject",
            name="event",
        ),
        migrations.AddField(
            model_name="eventsubject",
            name="event",
            field=models.ManyToManyField(to="events.event"),
        ),
    ]