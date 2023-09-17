# Generated by Django 4.2.5 on 2023-09-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
