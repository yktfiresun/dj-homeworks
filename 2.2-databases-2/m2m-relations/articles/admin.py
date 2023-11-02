from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article

from .models import Tags, Scopes

class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        main=[]
        try:
            for form in self.forms:
                if form.cleaned_data['is_main']:
                    main.append(form.cleaned_data['is_main'])
        except:
            pass
        if len(main)>1 or len(main)==0:
            raise ValidationError('не выбран главный тег или больше одного главного тега')

        return super().clean()

class ScopesInline(admin.TabularInline):
    model = Scopes
    formset = ScopesInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','text','published_at','image']
    inlines = [ScopesInline]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display=['name']