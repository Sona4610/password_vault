from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.template import loader
from .models import Member
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def members(request):
    template=loader.get_template('home.html')
    return HttpResponse( template.render())
# ("Welcome to Members Module")

# def sona(request):
#     template=loader.get_template('index.html')
#     return HttpResponse( template.render())

def index(request):
    return render(request,"index.html")

def addrecordpage(request):
    return render(request,"addrecords.html")

def addrecorddb(request):
    fn=request.GET.get("text1")
    ln=request.GET.get("text2")
    m1=Member(firstname=fn,lastname=ln)
    m1.save()
    return HttpResponse("Record added successfully")

def displayreccordspage(request):
    mymembers=Member.objects.all().values()
    mycontext={'myrecords':mymembers,}
    return render(request,"displayrecords.html",mycontext)

def updatepage(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, "updaterecorddb.html", {"member": member})

def updaterecorddb(request, id):
        m1 = get_object_or_404(Member, id=id)
        fn = request.GET.get("text1")
        ln= request.GET.get("text2")  
        m1.firstname = fn
        m1.lastname = ln
        m1.save()
        return redirect('displayrecordspage')
        #return HttpResponse("Record updated successfully!")

def deleterecord(request, id):
    m1 = get_object_or_404(Member, id=id)
    m1.delete()
    return redirect('displayrecordspage')