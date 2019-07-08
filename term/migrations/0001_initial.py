# Generated by Django 2.2.2 on 2019-07-07 16:03

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('data_platform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='acr_category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='名称')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='简称')),
            ],
            options={
                'verbose_name': '缩略语分类',
                'verbose_name_plural': '缩略语分类',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='term_category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='名称')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='简称')),
            ],
            options={
                'verbose_name': '术语分类',
                'verbose_name_plural': '术语分类',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='term',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='词条')),
                ('content', models.TextField(verbose_name='词条说明')),
                ('source', models.TextField(verbose_name='词条来源')),
                ('acmodel', models.ForeignKey(limit_choices_to={'if_intra_ac': True}, on_delete=django.db.models.deletion.CASCADE, related_name='适用机型', to='data_platform.acmodel')),
                ('category', models.ForeignKey(default='无分类', on_delete=django.db.models.deletion.CASCADE, related_name='acr_category', to='term.term_category')),
                ('tag', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '术语',
                'verbose_name_plural': '术语',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='acronym',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='缩略语')),
                ('full_name', models.TextField(verbose_name='英文全称')),
                ('zh_name', models.TextField(verbose_name='中文全称')),
                ('category', models.ForeignKey(default='无分类', on_delete=django.db.models.deletion.CASCADE, related_name='acr_category', to='term.acr_category')),
                ('tag', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '缩略语',
                'verbose_name_plural': '缩略语',
                'ordering': ('name',),
            },
        ),
    ]
