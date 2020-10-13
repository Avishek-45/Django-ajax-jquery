from django.shortcuts import render
from .forms import Newform
from django.http import JsonResponse

# Create your views here.
def contact(request):
    form=Newform()

    if request.is_ajax():
        form=Newform(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(
                {'message':'Sucess'}
            )


    return render(request, 'ajaxify/contact.html',{'form':form})