# Generated by Django 2.0.6 on 2019-11-12 19:08

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db.models import Model,CharField,PositiveIntegerField,DateTimeField,IntegerField,ForeignKey,BooleanField,\
    PositiveSmallIntegerField,GenericIPAddressField,DecimalField,BigIntegerField,CASCADE,ManyToManyField,FloatField,ManyToManyField
from django.db import migrations,models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', CharField(max_length=128, verbose_name='password')),
                ('last_login', DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', PositiveSmallIntegerField(blank=True, choices=[(0, '后台开发者'), (1, '超级管理员'), (2, '平台管理员'), (3, '单位管理员'), (4, '一般用户')], null=True, verbose_name='角色')),
                ('user_name', CharField(max_length=10, verbose_name='用户姓名')),
                ('unit_id', IntegerField(blank=True, null=True, verbose_name='单位ID')),
                ('unit_name', CharField(blank=True, max_length=100, null=True, verbose_name='单位名称')),
                ('dept_id', IntegerField(blank=True, null=True, verbose_name='部门ID')),
                ('dept_name', CharField(blank=True, max_length=100, null=True, verbose_name='部门名称')),
                ('mobile', CharField(blank=True, max_length=20, null=True, verbose_name='手机号')),
                ('avatar', models.ImageField(blank=True, default='users/avatar/default.png', max_length=200, null=True, upload_to='users/avatar/%Y/%m', verbose_name='用户头像')),
                ('gender', IntegerField(blank=True, choices=[(1, '男'), (2, '女')], default='1', null=True, verbose_name='性别')),
                ('create_user', CharField(blank=True, max_length=45, null=True, verbose_name='创建者')),
                ('create_time', DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_user', CharField(blank=True, max_length=45, null=True, verbose_name='更新者')),
                ('update_time', DateTimeField(blank=True, null=True, verbose_name='更新时间')),
                ('comment', CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('status', PositiveSmallIntegerField(choices=[(1, '正常'), (2, '停用')], default=1, verbose_name='状态')),
                ('user_id_create', BigIntegerField(blank=True, null=True, verbose_name='创建用户id')),
                ('groups', ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', CharField(max_length=30, verbose_name='单位名称')),
                ('connect', CharField(blank=True, max_length=30, null=True, verbose_name='联系人')),
                ('connect_phone', CharField(blank=True, max_length=30, null=True, verbose_name='联系电话')),
                ('address', CharField(blank=True, max_length=50, null=True, verbose_name='地址')),
                ('create_user', CharField(max_length=45, verbose_name='创建者')),
                ('create_time', DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_user', CharField(blank=True, max_length=45, null=True, verbose_name='更新者')),
                ('update_time', DateTimeField(blank=True, null=True, verbose_name='更新时间')),
                ('comment', CharField(blank=True, max_length=1000, null=True, verbose_name='备注')),
                ('status', PositiveSmallIntegerField(choices=[(1, '正常'), (0, '停用')], default=1, verbose_name='状态')),
            ],
            options={
                'verbose_name': '单位',
                'verbose_name_plural': '单位',
            },
        ),
        migrations.CreateModel(
            name='UserDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', CharField(max_length=20, verbose_name='部门名称')),
                ('unit_name', CharField(max_length=30, verbose_name='所属单位')),
                ('connect', CharField(blank=True, max_length=30, null=True, verbose_name='联系人')),
                ('connect_phone', CharField(blank=True, max_length=30, null=True, verbose_name='联系电话')),
                ('create_user', CharField(max_length=45, verbose_name='创建者')),
                ('create_time', DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_user', CharField(blank=True, max_length=45, null=True, verbose_name='更新者')),
                ('update_time', DateTimeField(blank=True, null=True, verbose_name='更新时间')),
                ('comment', CharField(blank=True, max_length=1000, null=True, verbose_name='备注')),
                ('status', PositiveSmallIntegerField(choices=[(1, '正常'), (0, '停用')], default=1, verbose_name='状态')),
                ('unit', ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserCompany', verbose_name='所属单位ID')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
            },
        ),
        migrations.CreateModel(
            name='UserEmailVirificationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=254, verbose_name='接收邮箱')),
                ('purpose', CharField(choices=[('register', '注册'), ('forget', '忘记密码'), ('change_email', '修改邮箱绑定'), ('active', '用户激活')], max_length=20, verbose_name='用途')),
                ('is_use', BooleanField(default=False, verbose_name='是否被使用')),
                ('add_time', DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.CreateModel(
            name='UserLoginInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', PositiveSmallIntegerField(choices=[(1, '登录'), (2, '注销')], default=1, verbose_name='动作')),
                ('agent', CharField(max_length=200, verbose_name='客户端')),
                ('ip', GenericIPAddressField(verbose_name='IP地址')),
                ('address', CharField(max_length=100, verbose_name='登录地区')),
                ('add_time', DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('user', ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户登录信息',
                'verbose_name_plural': '用户登录信息',
            },
        ),
    ]
