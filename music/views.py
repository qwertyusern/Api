from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


# class HelloAPI(APIView):
#     def get(self,request):
#         data={"xabar":"birinchi API yaratildi!"}
#         return Response(data)
#
#     def post(self,request):
#         data=request.data
#         return Response(data)
# class QoshiqchiApi(APIView):
#     def get(self,request,pk):
#         q=Qoshiqchi.objects.get(id=pk)
#         serializer=Serializer(q)
#
# class AlbomlarAPI(APIView):
#     def get(self,request):
#         a=Albom.objects.all()
#         s=AlbomSerializer(a,many=True)
#         return Response(s.data)
#     def post(self,request):
#         m=request.data
#         s=AlbomSerializer(data=m)
#         if s.is_valid():
#             s.save()
#         return Response(s.data)
#
# class AlbomApi(APIView):
#     def get(self,request,pk):
#         a=Albom.objects.get(id=pk)
#         s=Serializer(a)
#         return Response(s.data)
#     def put(self,request):
#         m = request.data
#         s = AlbomSerializer(data=m)
#         if s.is_valid():
#             s.save()
#         return Response(s.data)
# class QoshiqlarApi(APIView):
#     def get(self,request):
#         q=Qoshiq.objects.all()
#         s=QoshiqSerializer(q,many=True)
#         return Response(s.data)
#     def post(self,request):
#         m = request.data
#         s=QoshiqlarSerializer(data=m)
#         if s.is_valid():
#             s.save()
#         return Response(s.data)
# class QoshiqApi(APIView):
#     def get(self,request,pk):
#         q=Qoshiq.objects.get(id=pk)
#         s=Serializer(q,data=request.data)
#         return Response(s.data)
#     def patch(self,request,pk):
#         q = Qoshiq.objects.get(id=pk)
#     s = QoshiqPatchSerializer(q,data=request.data,partial=True)
#     if s.is_valid():
#         s.save()
#         return Response(status=status.HTTP_200_OK)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
#
# def post(self, request):
#     m = request.data
#     s = QoshiqSerializer(data=m)
#     if s.is_valid():
#         s.save()
#         return Response(s.data)
#     return Response(s.errors)

class QoshiqchilarVS(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    s=QoshiqchiSerializer
    @action(detail=True,methods=['get'])
    def albomlar(self,request,pk=None):
        q=self.get_object()
        albomlar=Albom.objects.filter(qoshiqchi=q)
        s=AlbomSerializer(albomlar,many=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)
class AlbomlarVS(ModelViewSet):
    queryset = Albom.objects.all()
    s=AlbomSerializer
    @action(detail=True, methods=['get'])
    def qoshiqar(self, request, pk=None):
        q = self.get_object()
        qoshiq = Qoshiq.objects.filter(albom=q)
        s = QoshiqSerializer(qoshiq, many=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)


class QoshiqlarVS(ModelViewSet):
    queryset = Qoshiq.objects.all()
    s=QoshiqSerializer
    @action(detail=True, methods=['get'])
    def albomlar(self, request, pk=None):
        a = self.get_object()
        qoshiqlar = Albom.objects.filter(qoshiq=a)
        s = QoshiqSerializer(qoshiqlar, many=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)
