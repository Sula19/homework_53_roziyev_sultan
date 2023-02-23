from django import forms
from django.core.exceptions import ValidationError
from webapp.models import List


class ListForms(forms.ModelForm):
    class Meta:
        model = List
        fields = (
            'title',
            'description',
            'detailed_description',
            'status',
            'date'
        )
        labels = {'title': 'Заголовок',
                  'description': 'Описание',
                  'detailed_description': 'Детальное описание',
                  'status': 'Статус',
                  'date': 'Дата'
                  }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise ValidationError('Поле title должен иметь не менее 3 символов')
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 6:
            raise ValidationError('Поле description должен иметь не менее 6 символов')
        return description
