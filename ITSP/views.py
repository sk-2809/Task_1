from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from datetime import datetime
from ITSP.models import ITSP
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ITSPSerializer

# Create your views here.
def index(request):
    all_team=ITSP.objects.all()
    return render(request,'index.html',{'Teams':all_team})

    #return HttpResponse("this is homepage")


def form(request):
    if request.method=="POST":
        teamname=request.POST.get('teamname')
        mem1=request.POST.get('mem1')
        mem2=request.POST.get('mem2')
        Email1=request.POST.get('Email1')
        Email2=request.POST.get('Email2')
        topic=request.POST.get('topic')
        comment=request.POST.get('comment')
        detail=ITSP(Team=teamname,memeber1=mem1,memeber2=mem2,email1=Email1,email2=Email2,Topic=topic,desc=comment,date=datetime.today())
        detail.save()
    return render(request,'form.html')

def  navigate(request):
    all_team=ITSP.objects.all()
    return render(request,'navigate.html',{'Teams':all_team})




def details(request,id):
    all_team=ITSP.objects.get(id=id)
    return render(request,'details.html',{'Teams':all_team})

@api_view(['GET'])
def ITSP_List(request):
    if request.method=='GET':
        obj=ITSP.objects.all()
        serializer=ITSPSerializer(obj,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def _List(request,id):
    if request.method=='GET':
        obj=ITSP.objects.get(id=id)
        serializer=ITSPSerializer(obj,many=False)
        return Response(serializer.data)
