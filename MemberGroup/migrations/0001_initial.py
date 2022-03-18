# Generated by Django 3.2.4 on 2021-06-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserNameFamily', models.CharField(blank=True, max_length=150, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('Phone', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('NationalCode', models.CharField(blank=True, max_length=30, null=True)),
                ('TitleJob', models.CharField(blank=True, max_length=300, null=True)),
                ('Address', models.TextField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='')),
                ('UserActive', models.BooleanField(default=True)),
                ('DateTimeJoin', models.DateTimeField()),
                ('UserName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]