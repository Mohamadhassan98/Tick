# Generated by Django 2.2 on 2019-05-28 07:51

import Tick_server.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('percent', models.IntegerField(default=5)),
                ('count', models.IntegerField(default=5)),
                ('product_brand', models.CharField(max_length=50, null=True)),
                ('product_id', models.CharField(max_length=50, null=True)),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('product_barcode', models.ImageField(null=True, upload_to='')),
                ('expire_date', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='CheckBoxOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CheckBoxPollAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Code4Digit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Code4DigitSalesman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=4)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkbox_poll_answers', models.ManyToManyField(through='Tick_server.CheckBoxPollAnswer', to='Tick_server.CheckBoxOption')),
            ],
        ),
        migrations.CreateModel(
            name='LinearScalePoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('remaining_time', models.IntegerField()),
                ('text', models.TextField()),
                ('choices_count', models.IntegerField()),
                ('start', models.IntegerField()),
                ('step', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParagraphPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('remaining_time', models.IntegerField()),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(null=True, upload_to=Tick_server.models.upload_to_path)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('business_license', models.ImageField(blank=True, null=True, upload_to='')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tick_server.City')),
                ('salesman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tick_server.Salesman')),
            ],
        ),
        migrations.CreateModel(
            name='ShopKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShortAnswerPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('remaining_time', models.IntegerField()),
                ('text', models.TextField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tick_server.Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('SU', 'Super User'), ('CU', 'Customer'), ('SM', 'Salesman')], max_length=2)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tick_server.City')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ShortAnswerPollAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('answer_text', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='short_answer_poll_answer', to='Tick_server.Customer')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='short_answer_poll_answer', to='Tick_server.ShortAnswerPoll')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tick_server.ShopKind'),
        ),
        migrations.AddField(
            model_name='salesman',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ParagraphPollAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('answer_text', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraph_poll_answer', to='Tick_server.Customer')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraph_poll_answer', to='Tick_server.ParagraphPoll')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='paragraphpoll',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tick_server.Shop'),
        ),
        migrations.CreateModel(
            name='MultipleChoicePoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('remaining_time', models.IntegerField()),
                ('text', models.TextField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tick_server.Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultipleChoiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=100)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tick_server.MultipleChoicePoll')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiple_choice_answer', to='Tick_server.Customer')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiple_choice_answer', to='Tick_server.MultipleChoiceOption')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LinearScalePollAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('answer', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linear_scale_poll_answer', to='Tick_server.Customer')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linear_scale_poll_answer', to='Tick_server.LinearScalePoll')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='linearscalepoll',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tick_server.Shop'),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=5, unique=True)),
                ('expire_date', models.DateField(default=django.utils.timezone.now)),
                ('candidate_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='Tick_server.CandidateProduct')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='Tick_server.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='linear_scale_poll_answers',
            field=models.ManyToManyField(through='Tick_server.LinearScalePollAnswer', to='Tick_server.LinearScalePoll'),
        ),
        migrations.AddField(
            model_name='customer',
            name='multiple_choice_poll_answers',
            field=models.ManyToManyField(through='Tick_server.MultipleChoiceAnswer', to='Tick_server.MultipleChoiceOption'),
        ),
        migrations.AddField(
            model_name='customer',
            name='paragraph_poll_answers',
            field=models.ManyToManyField(through='Tick_server.ParagraphPollAnswer', to='Tick_server.ParagraphPoll'),
        ),
        migrations.AddField(
            model_name='customer',
            name='short_answer_poll_answers',
            field=models.ManyToManyField(through='Tick_server.ShortAnswerPollAnswer', to='Tick_server.ShortAnswerPoll'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='checkboxpollanswer',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkbox_poll_answer', to='Tick_server.Customer'),
        ),
        migrations.AddField(
            model_name='checkboxpollanswer',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkbox_poll_answer', to='Tick_server.CheckBoxOption'),
        ),
        migrations.CreateModel(
            name='CheckBoxPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('remaining_time', models.IntegerField()),
                ('text', models.TextField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tick_server.Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='checkboxoption',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tick_server.CheckBoxPoll'),
        ),
        migrations.AddField(
            model_name='candidateproduct',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='Tick_server.Shop'),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tick_server.Shop')),
            ],
        ),
    ]
