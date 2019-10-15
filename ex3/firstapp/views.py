from django.shortcuts import render
from firstapp.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    insert ={'insertcontent':'hello world'}
    return render(request,'index.html',context=insert)

def users (request):
    user_list =User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'users.html',context=user_dict)
