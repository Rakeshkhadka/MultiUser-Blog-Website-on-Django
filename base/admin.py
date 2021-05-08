from django.contrib import admin
from .models import Posts, Tags
# Register your models here.


@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(publish=True)
    

@admin.action(description='Mark selected stories as Drafted')
def make_drafted(modeladmin, request, queryset):
    queryset.update(publish=False)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline', 'publish']
    ordering = ['headline']
    actions = [make_published, make_drafted]

admin.site.register(Posts, ArticleAdmin)
admin.site.register(Tags)