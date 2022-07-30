# Generated by Django 4.0.6 on 2022-07-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_code', models.AutoField(primary_key=True, serialize=False)),
                ('member_id', models.CharField(max_length=20)),
                ('member_password', models.CharField(max_length=25)),
                ('member_name', models.CharField(max_length=10)),
                ('member_nickname', models.CharField(max_length=10)),
                ('member_email', models.CharField(max_length=35)),
                ('member_gender', models.CharField(blank=True, max_length=1, null=True)),
                ('member_dob', models.DateField(blank=True, null=True)),
                ('member_join_date', models.DateField()),
                ('member_pic', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
