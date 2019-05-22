from django.shortcuts import render, redirect

# Create your views here.
from doc_app.models import Dept


def dept_page(request):
    result=Dept.objects.all()

    return render(request,'department/departmentlist.html',{'list1':result})




def dept_add_page(request):
    return render(request,'department/addDepartment.html')


def dept_add(request):
    name=request.POST.get('name')
    note=request.POST.get('note')
    Dept.objects.create(name=name,note=note)
    return redirect('bm:bmjm')

def xq(request):
    id=request.GET.get('id')
    D_name=Dept.objects.get(id=id)
    bm=Dept.objects.get(name=D_name.name)
    user=bm.task_set.all()
    print(user,type(user))
    return render(request,'department/emplist.html',{'user1':user,'D_name':D_name})


def update_page(request):
    id=request.GET.get('id')
    data=Dept.objects.get(id=id)
    return render(request,'department/updateDept.html',{'obj':data})



def update(request):
    id=request.GET.get('id')
    name=request.POST.get('name')
    note=request.POST.get('note')
    a=Dept.objects.get(id=id)
    a.name=name
    a.note=note
    a.save()
    return redirect('bm:bmjm')



def d_dep_page(request):
    id=request.GET.get('id')
    return render(request,'department/addEmp.html',{'id':id})


def d_dep(request):
    id=request.GET.get('id')
    name=request.POST.get('name')
    age=request.POST.get('age')
    salary=request.POST.get('salary')
    print(id)
    dep=Dept.objects.get(id=id)
    print(dep)
    dep.task_set.create(name=name,age=age,salary=salary)
    return redirect('bm:bmjm')

