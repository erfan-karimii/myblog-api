# Generated by Django 4.0.4 on 2022-07-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_blog_comment_blog_alter_comment_massage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='massage',
            field=models.TextField(null=True),
        ),
    ]
