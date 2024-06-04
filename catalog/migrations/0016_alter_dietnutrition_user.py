# Generated by Django 4.2.11 on 2024-06-02 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_dietnutrition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietnutrition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='catalog.userprofile'),
        ),
    ]