# Generated by Django 4.2.11 on 2024-05-21 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthindicator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='catalog.userprofile'),
        ),
        migrations.RemoveField(
            model_name='healthindicator',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='weight',
        ),
        migrations.AddField(
            model_name='healthindicator',
            name='weight',
            field=models.ManyToManyField(help_text='Your Weight', related_name='health_indicator', to='catalog.userprofile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
