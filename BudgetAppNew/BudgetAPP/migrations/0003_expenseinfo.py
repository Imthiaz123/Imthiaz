# Generated by Django 3.0.3 on 2020-07-12 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BudgetAPP', '0002_auto_20200504_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('expense_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BudgetAPP.Category')),
            ],
        ),
    ]