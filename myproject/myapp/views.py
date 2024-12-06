from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from myapp.forms import SampleForm 

def normal_view(request):
    context = {'message': 'Hello from the normal view!'}
    return render(request, 'normal_view.html', context)

@api_view(['GET'])
def drf_endpoint(request):
    return Response({'message': 'Hello from the DRF endpoint!'})

def sample_post(request, *args, **kwargs):  
    form = SampleForm(request.POST or None)  

    if form.is_valid():  
        print(f'{ form.cleaned_data= }')  
        return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')  
    else:  
        return HttpResponse(f'<p class="error">Your form submission was unsuccessful ❌. Please would you correct the errors? The current errors: {form.errors}</p>')


def example(request):  
    return render(request, 'example.html')
