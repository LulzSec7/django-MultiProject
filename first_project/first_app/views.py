from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpages,AccessRecord
# Create your views here.

def index(request):
    web_list  = AccessRecord.objects.order_by('date')
    acc_dict = {'acc_rec':web_list}
    return render(request,'first_app/index.html',context=acc_dict)