# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from app.models import Docinfo
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def tool_folder(request):
    
    docinfo = Docinfo.objects.all()
    foldernames = Docinfo.objects.values('foldername').distinct()

    return render(request,'folder.html',{'foldernames':foldernames})

def tool_file(request,foldername):

    # Docinfo.objects.all()
    docinfo = Docinfo.objects.all()
    foldernames = Docinfo.objects.values('foldername').distinct()
    filenames = Docinfo.objects.all().filter(foldername = foldername)    

    return render(request,'file.html',{'foldernames':foldernames,'filenames':filenames})

def tool_annot(request,foldername,fileno):

    docinfo = Docinfo.objects.all()
    foldernames = Docinfo.objects.values('foldername').distinct()
    filenames = Docinfo.objects.all().filter(foldername = foldername)    
    # foldername 
    # filename   
    # iscomplete 
    # iscorrect  

    return render(request,'annot.html',{'foldernames':foldernames,'filenames':filenames,'foldername':foldername,'fileno':fileno})

@csrf_exempt
def tool_eval_post(request):

    if request.method == "POST" and request.is_ajax():
        
        folder_name = request.POST['folder_name']
        file_name = request.POST['file_name']
        checked   = request.POST['checked']
        completed = 'true'
        Docinfo.objects.all().filter(foldername=folder_name,filename=file_name).update(iscorrect=checked,iscomplete=completed)

        return HttpResponse("Updated")


    return (request)