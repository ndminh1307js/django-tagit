from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Search on TagIt'}))
