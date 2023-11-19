from django.shortcuts import render
from forms.form import StueForm

# Create your views here.
def index(request):

stu=ArticleForm()

return render(request,'index.html',{'form':stu})

