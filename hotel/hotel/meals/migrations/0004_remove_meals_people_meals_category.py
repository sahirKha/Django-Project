# Generated by Django 4.0.4 on 2022-07-21 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_category_alter_meals_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meals',
            name='people',
        ),
        migrations.AddField(
            model_name='meals',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meals.category'),
        ),
    ]
