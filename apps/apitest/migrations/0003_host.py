# Generated by Django 2.2 on 2022-03-22 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20220321_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('host', models.CharField(max_length=1024, verbose_name='Host地址')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_list', to='apitest.Project', verbose_name='所属项目')),
            ],
        ),
    ]
