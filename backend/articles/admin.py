from django.contrib import admin
from .models import Article, ArticleComment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleComment)