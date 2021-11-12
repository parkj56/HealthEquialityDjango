from django.http.response import Http404
from .models import BodyData
from .serializers import BDSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AllData(APIView):

    def get(self, request):
        body = BodyData.objects.all()
        serializer = BDSerializer(body, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BodyDetail(APIView):

    def get_object(self, pk):
        try:
            return BodyData.objects.get(pk=pk)
        except BodyData.DoesNotExist:
            raise Http404

    #get by id
    def get(self, request, pk):
        body = self.get_object(pk)
        serializer = BDSerializer(body)
        return Response(serializer.data)

    #update
    def put(self, request, pk):
        body = self.get_object(pk)
        serializer = BDSerializer(body, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk):
        body = self.get_object(pk)
        body.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)