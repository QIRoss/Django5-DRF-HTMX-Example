from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

def normal_view(request):
    context = {'message': 'Hello from the normal view!'}
    return render(request, 'normal_view.html', context)

@api_view(['GET'])
def drf_endpoint(request):
    return Response({'message': 'Hello from the DRF endpoint!'})
