from django import forms


class blog_posts(forms.Form):
    title = forms.CharField(required=True)
    body = forms.CharField(required=True)
