# Generated by Django 4.2 on 2023-04-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_photo_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
