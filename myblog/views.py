from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, Django!")

def msg(request):
    return HttpResponse("welcome!!")