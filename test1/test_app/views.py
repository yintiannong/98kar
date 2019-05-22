from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from test_app.models import Table

def test_page(request):
    return render(request,'test_app/test.html')

def test1(request):
    a=request.POST.get('val')
    username=Table.objects.filter(username__contains=a).values('username')
    list1=list(username)
    print(list1)
    if a=='':
        return JsonResponse('',safe=False)
    else:
        return JsonResponse(list1,safe=False)
