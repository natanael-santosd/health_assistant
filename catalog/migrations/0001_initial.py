# Generated by Django 4.2.11 on 2024-05-21 12:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthIndicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmi', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('body_fat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('date_entry', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('u', 'Underweight'), ('n', 'Normal Weight'), ('o', 'Overweight'), ('ob', 'Obese')], default='', help_text='BMI status', max_length=2)),
            ],
            options={
                'ordering': ['-date_entry'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for a person', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('weight', models.ManyToManyField(help_text='Health Indicators for the user', to='catalog.healthindicator')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='PhysicalActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(choices=[('biking', 'Biking'), ('jogging', 'Jogging'), ('running', 'Running'), ('gym', 'Gym')], max_length=10)),
                ('date_entry', models.DateField(blank=True, null=True)),
                ('intensity', models.CharField(blank=True, choices=[('l', 'Light'), ('m', 'Moderate'), ('v', 'Vigorous')], default='m', help_text='Activity Intensity', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.userprofile')),
            ],
            options={
                'ordering': ['-date_entry'],
            },
        ),
        migrations.AddField(
            model_name='healthindicator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.userprofile'),
        ),
        migrations.CreateModel(
            name='DietNutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorie_intake', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('calorie_unit', models.CharField(choices=[('calorie_kcal', 'Calorie (kcal)'), ('calorie_cal', 'Calorie (cal)'), ('kilojoules', 'Kilojoules (kJ)'), ('joules', 'Joules (J)')], max_length=20)),
                ('date_entry', models.DateField(blank=True, null=True)),
                ('macro', models.CharField(blank=True, choices=[('p', 'Protein'), ('f', 'Fat'), ('c', 'Carbohydrate'), ('fi', 'Fiber')], default='', help_text='Macronutrient type', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.userprofile')),
            ],
            options={
                'ordering': ['-date_entry'],
            },
        ),
    ]
