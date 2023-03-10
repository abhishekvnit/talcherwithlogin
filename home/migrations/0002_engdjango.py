# Generated by Django 4.0.1 on 2023-01-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engdjango',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('orgn_drg_no', models.TextField(blank=True, db_column='ORGN DRG NO', null=True)),
                ('drg_title', models.TextField(blank=True, db_column='DRG_TITLE', null=True)),
                ('sub_system', models.TextField(blank=True, db_column='SUB_SYSTEM', null=True)),
                ('boi_name', models.TextField(blank=True, db_column='BOI_NAME', null=True)),
                ('sch_date', models.TextField(blank=True, db_column='SCH_DATE', null=True)),
                ('details', models.TextField(blank=True, db_column='DETAILS', null=True)),
                ('area', models.TextField(blank=True, db_column='AREA', null=True)),
                ('purpose', models.TextField(blank=True, db_column='PURPOSE', null=True)),
                ('remarks', models.TextField(blank=True, db_column='REMARKS', null=True)),
                ('appr_rvsn_no', models.TextField(blank=True, db_column='APPR\nRVSN NO', null=True)),
                ('upload_dt', models.TextField(blank=True, db_column='UPLOAD_DT', null=True)),
                ('release_dt', models.TextField(blank=True, db_column='RELEASE_DT', null=True)),
                ('release_cat', models.TextField(blank=True, db_column='RELEASE_CAT', null=True)),
                ('category_id', models.TextField(blank=True, db_column='CATEGORY ID', null=True)),
                ('mu', models.TextField(blank=True, db_column='MU', null=True)),
                ('due_sub', models.TextField(blank=True, db_column='Due_sub', null=True)),
                ('under_resubmission', models.TextField(blank=True, db_column='Under_Resubmission', null=True)),
                ('appr', models.TextField(blank=True, db_column='Appr', null=True)),
            ],
            options={
                'db_table': 'engdjango',
                'managed': False,
            },
        ),
    ]
