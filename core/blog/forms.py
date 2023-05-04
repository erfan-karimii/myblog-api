from django import forms


class SearchForm(forms.Form):
	title = forms.CharField(max_length=100,required=False)

class CommentForm(forms.Form):
	Full_name= forms.CharField(max_length=200)
	Email_address = forms.EmailField(max_length=254)
	massage = forms.CharField(widget=forms.Textarea())
