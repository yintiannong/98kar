from django.shortcuts import render

# Create your views here.
from hdfs import Client


def index_page(request):
    return render(request,'index.html')



def submits(request):
    file_urls=request.FILES.get('files')
    print(file_urls)
    client = Client('http://192.168.197.25:50070')
    client.upload('/', 'file_urls')