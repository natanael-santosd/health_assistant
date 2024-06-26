# Generated by Django 4.2.11 on 2024-05-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_dietnutrition_food_delete_physicalactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietnutrition',
            name='calorie_unit',
            field=models.CharField(choices=[('calorie_kcal', 'Calories (kcal)'), ('calorie_cal', 'Calories (cal)'), ('kilojoules', 'Kilojoules (kJ)'), ('joules', 'Joules (J)')], max_length=20),
        ),
    ]
