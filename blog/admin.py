from django.contrib import admin
from .models import Skill, Author, Tag
# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "author", "date",)


admin.site.register(Skill, SkillAdmin)
admin.site.register(Author)
admin.site.register(Tag)
