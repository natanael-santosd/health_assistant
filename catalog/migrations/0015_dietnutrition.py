# Generated by Django 4.2.11 on 2024-06-02 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_delete_dietnutrition'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietNutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(default='Unknown Food', max_length=100)),
                ('calorie_intake', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('date_entry', models.DateField(blank=True, null=True)),
                ('macro', models.CharField(blank=True, choices=[('p', 'Protein'), ('f', 'Fat'), ('c', 'Carbohydrate'), ('fi', 'Fiber')], default='', help_text='Macronutrient type', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.userprofile')),
            ],
            options={
                'ordering': ['-date_entry'],
            },
        ),
    ]
