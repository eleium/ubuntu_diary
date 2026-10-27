from django import forms

from .models import Diary, Entry


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["title"]  # noqa: RUF012
        labels = {"title": ""}  # noqa: RUF012


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "text"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
