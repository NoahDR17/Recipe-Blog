# Generated by Django 5.1.2 on 2024-10-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='meal_type',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], default='breakfast', max_length=10),
        ),
    ]