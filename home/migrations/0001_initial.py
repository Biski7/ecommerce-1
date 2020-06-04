# Generated by Django 3.0.6 on 2020-06-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(blank=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('stock', models.CharField(choices=[('In Stock', 'In Stock'), ('Out Of Stock', 'Out Of Stock')], max_length=50)),
                ('image', models.TextField()),
            ],
        ),
    ]