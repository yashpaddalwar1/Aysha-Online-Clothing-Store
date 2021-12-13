# Generated by Django 3.1.7 on 2021-09-24 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='clothing_store/productimg')),
                ('label', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('hoodie-male', 'hoodie-male'), ('hoodie-female', 'hoodie-female'), ('sweatshirt-male', 'sweatshirt-male'), ('sweatshirt-female', 'sweatshirt-female'), ('longsleeve-male', 'longsleeve-male'), ('longsleeve-female', 'longsleeve-female')], max_length=30)),
                ('description', models.TextField()),
                ('XS', models.PositiveIntegerField()),
                ('XSprice', models.FloatField()),
                ('S', models.PositiveIntegerField()),
                ('Sprice', models.FloatField()),
                ('M', models.PositiveIntegerField()),
                ('Mprice', models.FloatField()),
                ('L', models.PositiveIntegerField()),
                ('Lprice', models.FloatField()),
                ('XL', models.PositiveIntegerField()),
                ('XLprice', models.FloatField()),
                ('XXL', models.PositiveIntegerField()),
                ('XXLprice', models.FloatField()),
                ('XXXL', models.PositiveIntegerField()),
                ('XXXLprice', models.FloatField()),
            ],
        ),
    ]
