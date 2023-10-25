from django.db import models


class Task(models.Model):
    name = models.CharField(verbose_name='Nome',
                            max_length=30,
                            null=False,
                            blank=False,
                            help_text='Breve descrição')
    done = models.BooleanField(verbose_name='Pronto?', default=False)

    class Meta:
        ordering = ['name', 'done']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return f'{self.name}'

    # @property
    def comments_count(self):
        return self.comments.count()

    comments_count.short_description = 'Comentários'

    def comments_contents(self):
        comment_list = ''
        for comment in self.comments.all():
            comment_list += f'{comment.content}'

        return comment_list
    comments_contents.short_description = 'Comentários'


class Comment(models.Model):
    content = models.CharField(
        verbose_name='Conteúdo', max_length=180,
        null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # relationships
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE,
        related_name='comments')

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.content
