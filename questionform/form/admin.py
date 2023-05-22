from django.contrib import admin

from .models import Division, Company, Question


class DivisionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'division')
    list_filter = ('division',)
    search_fields = ('title',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'company', 'pub_date', 'email', 'text')
    list_filter = ('company',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Division, DivisionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Question, QuestionAdmin)
