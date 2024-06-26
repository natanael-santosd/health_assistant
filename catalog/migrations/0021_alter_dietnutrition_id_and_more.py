# Generated by Django 4.2.11 on 2024-06-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_alter_dietnutrition_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietnutrition',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddConstraint(
            model_name='dietnutrition',
            constraint=models.UniqueConstraint(fields=('food', 'date_entry'), name='unique_user_food_date_entry'),
        ),
    ]
