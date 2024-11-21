from django import forms

class PageRequestForm(forms.Form):
    title = forms.CharField(max_length=100, help_text="Page title")
    description = forms.CharField(widget=forms.Textarea, help_text="Page content")
    style = forms.CharField(widget=forms.Textarea, help_text="Page style")