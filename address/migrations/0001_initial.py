# Generated by Django 3.0.8 on 2020-07-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('class_room', models.CharField(max_length=20)),
                ('student_id', models.CharField(max_length=16)),
                ('student_name', models.CharField(max_length=50)),
                ('student_gender', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=50)),
                ('student_type', models.IntegerField()),
                ('student_phone', models.CharField(max_length=18)),
                ('student_email', models.CharField(max_length=50)),
            ],
        ),
    ]
