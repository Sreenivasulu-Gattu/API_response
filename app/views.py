from django.shortcuts import render

# Create your views here.


from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['get','post'])
@permission_classes([IsAuthenticated])
def hello(request):
    DJANGOOBJ = School.objects.all()
    JSONOBJ = SchoolModelSerial(DJANGOOBJ,many=True)
    JSONDATA = JSONOBJ.data
    return Response(JSONDATA)