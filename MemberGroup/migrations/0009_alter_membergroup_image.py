# Generated by Django 3.2.4 on 2021-08-07 03:18

import MemberGroup.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MemberGroup', '0008_likemember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membergroup',
            name='Image',
            field=models.ImageField(blank=True, default='/Static/Img/Img-Default/ImageDefaultMember.jpg', null=True, upload_to=MemberGroup.models.UploadSrcImageInfo),
        ),
    ]
