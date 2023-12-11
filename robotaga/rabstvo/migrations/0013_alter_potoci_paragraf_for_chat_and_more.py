# Generated by Django 4.1.5 on 2023-09-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabstvo', '0012_telegramuser_password_2fa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potoci',
            name='paragraf_for_chat',
            field=models.TextField(blank=True, choices=[('test0', 'test0'), ('test1', 'test1'), ('text_zagatovga', 'text_zagatovga'), ('spintaxst', 'spintaxst')], null=True),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='icon_telegram/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='name',
            field=models.TextField(blank=True, max_length=30, null=True, verbose_name='name'),
        ),
    ]
