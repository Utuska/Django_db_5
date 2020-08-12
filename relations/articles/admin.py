from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, Teams, Principal



class PrincipalInlineFormset(BaseInlineFormSet):
    def clean(self):
        command = []
        for form in self.forms:
            form.cleaned_data

            if 'team' in form.cleaned_data.keys():
                if form.cleaned_data['team'] in command:
                    raise ValidationError('Тут всегда ошибка')
                command.append(form.cleaned_data['team'])
            if form.cleaned_data == {}:
                raise ValidationError('Тут всегда ошибка')
            # print(command)
            # print(form.cleaned_data)
        return super().clean()  # вызываем базовый код переопределяемого метода

@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):
    pass


class PrincipalInline(admin.TabularInline):
    model = Principal
    extra = 1
    formset = PrincipalInlineFormset

@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    inlines = [
        PrincipalInline
    ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        PrincipalInline
    ]

