from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=30)
    loc = models.CharField(max_length=30)
    def __str__(self) -> str:
        return str(self.deptno)
class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    mgr = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    sal = models.DecimalField(max_digits=10,decimal_places=2)
    hiredate = models.DateField()
    comm = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno = models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.empno)