# Generated by Django 3.1.6 on 2021-02-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('event_img', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_starts_with', models.PositiveIntegerField()),
                ('hostel_name', models.CharField(max_length=50)),
                ('menu_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_starts_with', models.PositiveIntegerField()),
                ('branch_name', models.CharField(max_length=50)),
                ('menu_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
