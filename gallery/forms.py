from django import forms
from .models import HandmadeItem

class HandmadeItemForm(forms.ModelForm):
    class Meta:
        model = HandmadeItem
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 rounded-full border-2 border-brand-100 dark:border-brand-700 bg-white dark:bg-brand-950 focus:ring-4 focus:ring-brand-200 focus:border-brand-300 dark:focus:ring-brand-800 transition dark:text-brand-100 placeholder-brand-300 text-lg',
                'placeholder': 'Titre de la merveille...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-6 py-4 rounded-[2rem] border-2 border-brand-100 dark:border-brand-700 bg-white dark:bg-brand-950 focus:ring-4 focus:ring-brand-200 focus:border-brand-300 dark:focus:ring-brand-800 transition dark:text-brand-100 placeholder-brand-300 resize-y min-h-[5rem]',
                'rows': 2,
                'placeholder': 'Son histoire...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-brand-500 file:mr-4 file:py-3 file:px-6 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-brand-100 file:text-brand-700 hover:file:bg-brand-200 cursor-pointer',
            }),
        }
