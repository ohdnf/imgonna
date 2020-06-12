from django.contrib import admin
from .models import Review, ReviewComment

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)

# Register your models here.
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewComment)