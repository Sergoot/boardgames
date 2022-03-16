from django.contrib import admin
from .models import Game, Comment


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Game, GameAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'pub_date', 'active',)
    list_filter = ('active', 'pub_date')
    search_fields = ('user', 'post' 'text')
    prepopulated_fields = {'username': ('user',)}




admin.site.register(Comment, CommentAdmin)
# Register your models here.
