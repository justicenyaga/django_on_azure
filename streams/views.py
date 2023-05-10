from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Stream
from .serializers import StreamSerializer


@api_view(['GET'])
def getStreams(request):
    streams = Stream.objects.all()
    serializer = StreamSerializer(streams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStream(request, pk):
    stream = Stream.objects.get(_id=pk)
    serializer = StreamSerializer(stream, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createStream(request):
    data = request.data
    stream = Stream.objects.create(name=data['name'])
    serializer = StreamSerializer(stream, many=False)
    return Response(serializer.data)
