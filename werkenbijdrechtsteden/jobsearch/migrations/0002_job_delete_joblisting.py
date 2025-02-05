# Generated by Django 4.2.7 on 2024-01-18 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('posted_date', models.DateField()),
                ('employment_type', models.CharField(choices=[('PT', 'Part time'), ('FT', 'Full time'), ('CT', 'Contract'), ('IN', 'Internship')], default='FT', max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsearch.jobcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='JobListing',
        ),
    ]
