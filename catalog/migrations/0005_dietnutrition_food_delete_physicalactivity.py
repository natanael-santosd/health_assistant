# Generated by Django 4.2.11 on 2024-05-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_healthindicator_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietnutrition',
            name='food',
            field=models.CharField(default='Unknown Food', max_length=100),
        ),
        migrations.DeleteModel(
            name='PhysicalActivity',
        ),
    ]