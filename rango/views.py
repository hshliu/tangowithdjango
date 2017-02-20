from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #sContent = "Rango says hey there partner! <br/>\
    #        <a href='/rango/about/'>About</a>" 
    #return HttpResponse(sContent)
    context_dict = {'boldmessage':
            "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)    

def about(request):
    context_dict = {'myname':'Hongshun Liu'}
    return render(request, 'rango/about.html', context=context_dict)
