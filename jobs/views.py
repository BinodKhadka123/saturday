from django.shortcuts import render
from .models import Jobs


def index(request):
    jobs=Jobs.objects.all()
    print(jobs)
    context={
        'jobs':jobs

    }
    return render(request,'jobs/index.html',context)
   
