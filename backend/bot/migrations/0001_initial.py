# Generated by Django 4.0.2 on 2022-02-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=128, null=True)),
                ('message_text', models.TextField(null=True)),
                ('from_id', models.CharField(max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'message_telegram',
            },
        ),
    ]
