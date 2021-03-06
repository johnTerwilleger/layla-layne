# Generated by Django 3.1.1 on 2020-09-05 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('review', models.TextField()),
                ('summary', models.TextField()),
                ('genre', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('date_entered', models.DateField()),
                ('tags', models.TextField()),
            ],
        ),
    ]
