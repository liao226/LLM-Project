from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('token', models.CharField(max_length=32, null=True)),
                ('create_time', models.DateTimeField(max_length=6, null=True)),
                ('login_time', models.DateTimeField(max_length=6, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, null=True)),
                ('progress', models.CharField(max_length=50, null=True)),
                ('integrated_grade', models.CharField(max_length=50, null=True)),
                ('select_flag', models.BooleanField(default=True, null=True)),
                ('select_quantity', models.IntegerField(max_length=50, default=10, null=True)),
                ('judge_flag', models.BooleanField(default=True, null=True)),
                ('judge_quantity', models.IntegerField(max_length=50, default=5, null=True)),
                ('fill_flag', models.BooleanField(default=True, null=True)),
                ('fill_quantity', models.IntegerField(max_length=50, default=10, null=True)),
                ('calculate_flag', models.BooleanField(default=True, null=True)),
                ('calculate_quantity', models.IntegerField(max_length=50, default=6, null=True)),
                ('essay_flag', models.BooleanField(default=True, null=True)),
                ('essay_quantity', models.IntegerField(max_length=50, default=6, null=True)),
            ],
            options={
                'db_table': 'setting',
            },
        ),
        migrations.CreateModel(
            name='GenerateRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, null=True)),
                ('index', models.CharField(max_length=255, null=True)),
                ('question_range', models.CharField(max_length=255, null=True)),
                ('total_score', models.FloatField(default=0, null=True)),
                ('user_score', models.FloatField(default=0, null=True)),
                ('select_score', models.FloatField(default=0, null=True)),
                ('judge_score', models.FloatField(default=0, null=True)),
                ('fill_score', models.FloatField(default=0, null=True)),
                ('calculate_score', models.FloatField(default=0, null=True)),
                ('essay_score', models.FloatField(default=0, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
                ('generate_time', models.DateTimeField(max_length=6, null=True)),
            ],
            options={
                'db_table': 'generate_record',
            },
        ),
        migrations.CreateModel(
            name='SelectQuestion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('index', models.CharField(max_length=255, null=True)),
                ('generate_time', models.DateTimeField(max_length=6, null=True)),
                ('solution', models.CharField(max_length=255, null=True)),
                ('option_a', models.CharField(max_length=255, null=True)),
                ('option_b', models.CharField(max_length=255, null=True)),
                ('option_c', models.CharField(max_length=255, null=True)),
                ('option_d', models.CharField(max_length=255, null=True)),
                ('user_answer', models.CharField(max_length=255, null=True)),
                ('flag', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'select_question',
            },
        ),
        migrations.CreateModel(
            name='JudgeQuestion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('index', models.CharField(max_length=255, null=True)),
                ('generate_time', models.DateTimeField(max_length=6, null=True)),
                ('solution', models.CharField(max_length=50, null=True)),
                ('user_answer', models.CharField(max_length=50, null=True)),
                ('flag', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'judge_question',
            },
        ),
        migrations.CreateModel(
            name='FillQuestion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('index', models.CharField(max_length=255, null=True)),
                ('generate_time', models.DateTimeField(max_length=6, null=True)),
                ('solution', models.CharField(max_length=255, null=True)),
                ('user_answer', models.BooleanField(null=True)),
                ('flag', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'fill_question',
            },
        ),
        migrations.CreateModel(
            name='CalculateQuestion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('index', models.CharField(max_length=255, null=True)),
                ('generate_time', models.DateTimeField(max_length=6, null=True)),
                ('solution', models.CharField(max_length=255, null=True)),
                ('user_answer', models.BooleanField(null=True)),
                ('flag', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'calculate_question',
            },
        ),
        migrations.CreateModel(
            name='EssayQuestion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('index', models.CharField(max_length=255, null=True)),
                ('generate_time', models.DateTimeField(max_length=6, null=True)),
                ('solution', models.CharField(max_length=255, null=True)),
                ('user_answer', models.BooleanField(null=True)),
                ('flag', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'essay_question',
            },
        ),
    ]
