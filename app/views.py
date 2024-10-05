from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_dept(request):
    deptno_r = int(input("enter the empno: "))
    dname_r = input('Enter the deptname: ')
    loc_r = input('enter the location: ')

    depob = Dept.objects.get_or_create(deptno = deptno_r,dname = dname_r,loc = loc_r)
    depob = Dept.objects.all()
    d = {'department' : depob}
    return render(request,'display_dept.html',d)

def insert_emp(request):
    empno_r = int(input("enter the empno: "))
    ename_r = input('enter the ename: ')
    job_r = input('enter the job: ')
    hiredate_r = input('Enter the hiredate: ')
    sal_r = float(input('Enter the sal(decimal): '))
    comm_r = input('enter the commision(decimal): ')
    mgr = input("Enter the mgr: ")
    deptno_r = int(input('enter the deptno: '))
    mgrval = None
    deptob = Dept.objects.filter(deptno = deptno_r)
    if comm_r == "":
        comm_r = None
    if not mgr:
        mgrval = None
        empob = Emp.objects.get_or_create(empno = empno_r,ename = ename_r,job = job_r,hiredate = hiredate_r,
                                      sal = sal_r,comm = comm_r,mgr = None,deptno = deptob[0])
    else:
        mgrval = Emp.objects.filter(empno = mgr)
        empob = Emp.objects.get_or_create(empno = empno_r,ename = ename_r,job = job_r,hiredate = hiredate_r,
                                      sal = sal_r,comm = comm_r,mgr = mgrval[0],deptno = deptob[0])
    
    d = {'employee' : Emp.objects.all()}
    return render(request,'display_emp.html',d)
    

def display_emp(request):
    d = {'employee':Emp.objects.all()}
    return render(request,'display_emp.html',d)

def display_dept(request):
    d = {'department' : Dept.objects.all()}
    return render(request,'display_dept.html',d)

def display_deptemp(request):
    deo = Emp.objects.select_related('deptno').all()
    deo = Emp.objects.select_related('deptno').filter(comm__isnull=False,ename__startswith = 'T')
    deo = Emp.objects.select_related('deptno').filter(deptno__dname = 'Sales')
    deo = Emp.objects.select_related('deptno').filter(deptno__dname__startswith ='s')
    deo = Emp.objects.select_related('deptno').filter(deptno__dname = 'Accounting')
    deo = Emp.objects.select_related('deptno').all()
    deo = Emp.objects.select_related('deptno','mgr').all()
    d = {'deptemp':deo}
    return render(request,'display_deptemp.html',d)