# Generated by Django 4.1.3 on 2023-05-05 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_alter_accountdetail_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, unique=True)),
                ('last_name', models.CharField(max_length=100, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('avatar', models.ImageField(null=True, upload_to='')),
                ('user_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='AccountDetail',
        ),
    ]