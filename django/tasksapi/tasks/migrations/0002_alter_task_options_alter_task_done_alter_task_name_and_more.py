# Generated by Django 4.2.6 on 2023-10-25 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['name', 'done'], 'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Pronto?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(help_text='Breve descrição', max_length=30, verbose_name='Nome'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=180, verbose_name='Conteúdo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tasks.task')),
            ],
        ),
    ]
