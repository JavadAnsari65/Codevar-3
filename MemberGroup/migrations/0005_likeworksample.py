# Generated by Django 3.2.4 on 2021-07-09 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MemberGroup', '0004_worksample_datecreate'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeWorkSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorkSample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MemberGroup.worksample')),
            ],
        ),
    ]
