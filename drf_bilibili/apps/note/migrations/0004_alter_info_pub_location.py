# Generated by Django 4.1.1 on 2022-09-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='pub_location',
            field=models.CharField(max_length=20, null=True, verbose_name='地址'),
        ),
    ]