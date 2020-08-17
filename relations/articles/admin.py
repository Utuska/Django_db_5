from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, Teams, Principal

from collections import Counter



class PrincipalInlineFormset(BaseInlineFormSet):
    def clean(self):
        command = []
        true = []
        for form in self.forms:
            print(form.cleaned_data)
            print(true)

            count = Counter(true)

            if 'team' in form.cleaned_data.keys():
                if form.cleaned_data['team'] in command:
                    raise ValidationError('Тут всегда ошибка')
                command.append(form.cleaned_data['team'])
                if form.cleaned_data['status'] is True:
                    true.append(form.cleaned_data['status'])
                    if true.count(True) > 1:
                        raise ValidationError('Только один раздел может быть основным')

            if True not in true:
                raise ValidationError('Обязательно должен быть основной раздел')

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

