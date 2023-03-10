
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPaper', '0002_alter_author_user_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('A', 'Статья'), ('N', 'Новость')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
