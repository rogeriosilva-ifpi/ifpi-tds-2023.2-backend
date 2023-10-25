from django.contrib import admin
from .models import Task, Comment


# class CommentInline(admin.TabularInline):
#     model = Comment
#     extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'comments_count', 'done']
    search_fields = ['name',]
    list_filter = ['done']

    # inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']

# admin.site.register(Task)
