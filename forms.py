from django import forms
from forms.models import Article

class ArticleForm(forms.Modelform):

    class Meta:

        model=Article
        fields='__all__'
