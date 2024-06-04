# Generated by Django 4.2.11 on 2024-06-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_dietnutrition_calorie_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietnutrition',
            name='date_entry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dietnutrition',
            name='macro',
            field=models.CharField(blank=True, choices=[('p', 'Protein'), ('f', 'Fat'), ('c', 'Carbohydrate'), ('fi', 'Fiber')], default='', help_text='Macronutrient type', max_length=2, primary_key=False, serialize=False),
        )
    ]