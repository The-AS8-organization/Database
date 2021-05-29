# Generated by Django 3.2.3 on 2021-05-23 09:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210523_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('social_link', models.URLField()),
            ],
        ),
    ]
