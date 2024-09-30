from django.shortcuts import render,redirect,HttpResponse
from django.db.models import Q
from .models import *
from django.utils import timezone

def index(request):
    return render(request,'index.html')
def emp_add(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = request.POST['salary']
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept_id = request.POST['dept']
        role_id = request.POST['role']
        
        dept = Department.objects.get(id=dept_id)
        role = Role.objects.get(id=role_id)
        employee = Employee(
            firstname=firstname,
            lastname=lastname,
            salary=salary,
            bonus=bonus,
            phone=phone,
            dept=dept,
            role=role,
            hire_date=timezone.now()
        )
        employee.save()
        
        return HttpResponse('<h1>Success</h1>')
    
    elif request.method == 'GET':
        depts = Department.objects.all()
        roles = Role.objects.all()
        
        return render(request, 'emp_add.html', {"depts": depts, "roles": roles})
    
    else:
        return HttpResponse('Some exception')

    
    

def emp_remove(request):
    emp = Employee.objects.all()

   
    id = request.GET.get("employee")
    if id:
            employee_to_remove = Employee.objects.get(id=id)
            employee_to_remove.delete()  
            return HttpResponse('success')  
    else:

      return render(request, 'emp_remove.html', {"emp": emp})
def view_all_emp(request):
    emps=Employee.objects.all()
    return render(request,'view_all_emp.html',{"emps":emps})
    

def emp_single(request):
    emps = Employee.objects.all()
    depts = Department.objects.all()
    roles = Role.objects.all()
    context = {
        'emps': emps,
        'depts' : depts,
        'roles':roles,
        }
    return render(request,'emp_single.html',context)

def disp(request, emp_id = 0):
    if emp_id:
        try:
            emp_selected = Employee.objects.get(id=emp_id)
            context={
               'emp_selected' : emp_selected
            }
            return render(request,'disp.html',context)        
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
def filter(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')
        print(name)
        emps = Employee.objects.all()
        print(emps)
        
        if name:
            emps = emps.filter(Q(firstname__icontains=name) | Q(lastname__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept) 
        if role:
            emps = emps.filter(role__name__icontains=role)  
        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)
    else:
        return render(request, 'filter.html')