from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    seach_field = ['question_text']
    #list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
      
admin.site.register(Question, QuestionAdmin)
#este es para agregar choice en la parte inferior de question
#admin.site.register(Choice)