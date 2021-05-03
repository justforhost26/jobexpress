from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from job.models import Contact_Us
from job_management.models import Add_Job, sub_sub_category


def index(request):
    data=Add_Job.objects.all().order_by('-id')
    return render(request,"index.html",{"data":data})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def Contact_View(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        title=request.POST['title']
        message=request.POST['message']
        user=Contact_Us( first_name=first_name,last_name=last_name,email=email,title=title,message=message,)
        user.save()
        messages.success(request,'Message send successfuly')
        return render(request,"contact.html")
    else:
        messages.error(request,'Not Contact yet')
        return render(request,"contact.html")

# Create your views here.
def jobs(request):
    if 'job_cat' in request.GET:
        job_cat = request.GET['job_cat']
        cat=sub_sub_category.objects.get(id=job_cat)
        data=Add_Job.objects.filter(sub_sub_category_name=cat.sub_sub_category_name)
        context={
            'job_data':data,
        }
    elif 'main_job' in request.GET:
        main_job = request.GET['main_job']
        print()
        data=Add_Job.objects.get(id=main_job)
        context={
                'main_job':data,
        }
    else:
        data = Add_Job.objects.all()
        context = {
            'job_data': data,
        }
    return render(request,"jobs.html",context)