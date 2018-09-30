# Generated by Django 2.0.4 on 2018-09-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('breed', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('abbr', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'breed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Breeder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('url', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'breeder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=65)),
                ('class_field', models.CharField(db_column='class', max_length=50)),
                ('result', models.IntegerField()),
                ('participants', models.IntegerField()),
                ('winnings', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'competition',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Copyright',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('url', models.CharField(blank=True, max_length=145, null=True)),
                ('license', models.CharField(blank=True, max_length=45, null=True)),
                ('license_url', models.CharField(blank=True, max_length=145, null=True)),
                ('info', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'copyright',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('status', models.PositiveIntegerField()),
                ('breed', models.CharField(max_length=45)),
                ('sex', models.CharField(blank=True, max_length=5, null=True)),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('colour', models.CharField(blank=True, max_length=45, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('pedigree', models.CharField(blank=True, max_length=45, null=True)),
                ('evm', models.IntegerField()),
                ('vh', models.CharField(blank=True, max_length=45, null=True)),
                ('owner', models.CharField(blank=True, max_length=15, null=True)),
                ('stable', models.CharField(blank=True, max_length=45, null=True)),
                ('discipline', models.CharField(blank=True, max_length=45, null=True)),
                ('level', models.CharField(blank=True, max_length=45, null=True)),
                ('shows', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'horse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HorseImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'horse_img',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HorseText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('copy', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'horse_text',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Merit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merit', models.CharField(max_length=10)),
                ('event', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateField()),
                ('url', models.CharField(max_length=65)),
                ('info', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'db_table': 'merit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('vrl', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=65)),
                ('url', models.CharField(max_length=65)),
            ],
            options={
                'db_table': 'owner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=65)),
                ('url', models.CharField(max_length=65)),
                ('class_field', models.CharField(db_column='class', max_length=65)),
                ('result', models.CharField(max_length=10)),
                ('evaluation', models.CharField(blank=True, max_length=10, null=True)),
                ('judge', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'show',
                'managed': False,
            },
        ),
    ]
