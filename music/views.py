
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .models import *
from .serializers import *


class HelloAPI(APIView):
    def get(self,request):
        data={"xabar":"birinchi API yaratildi!"}
        return Response(data)

    def post(self,request):
        data=request.data
        return Response(data)
class QoshiqchiApi(APIView):
    def get(self,request,pk):
        q=Qoshiqchi.objects.get(id=pk)
        serializer=Serializer(q)

class AlbomlarAPI(APIView):
    def get(self,request):
        a=Albom.objects.all()
        s=AlbomSerializer(a,many=True)
        return Response(s.data)
    def post(self,request):
        m=request.data
        s=AlbomSerializer(data=m)
        if s.is_valid():
            s.save()
        return Response(s.data)

class AlbomApi(APIView):
    def get(self,request,pk):
        a=Albom.objects.get(id=pk)
        s=Serializer(a)
        return Response(s.data)
    def put(self,request):
        m = request.data
        s = AlbomSerializer(data=m)
        if s.is_valid():
            s.save()
        return Response(s.data)
class QoshiqlarApi(APIView):
    def get(self,request):
        q=Qoshiq.objects.all()
        s=QoshiqSerializer(q,many=True)
        return Response(s.data)
    def post(self,request):
        m=request.data
        s=QoshiqSerializer(data=m)
        if s.is_valid():
            s.save()
        return Response(s.data)
class QoshiqApi(APIView):
    def get(self,request,pk):
        q=Qoshiq.objects.get(id=pk)
        s=Serializer(q)
        return Response(s.data)

