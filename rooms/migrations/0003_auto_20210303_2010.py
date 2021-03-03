# Generated by Django 2.2.5 on 2021-03-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_room_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='room',
            name='room_tyep',
            field=models.ManyToManyField(blank=True, to='rooms.RoomType'),
        ),
    ]