# Generated by Django 4.2.11 on 2024-06-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_alter_dietnutrition_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietnutrition',
            name='food',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dietnutrition',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
