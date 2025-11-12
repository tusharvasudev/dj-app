from django.http import HttpResponse

# Create your views here.
def index(request):
    name = request.GET.get("name", "world")
    return HttpResponse("Hello, %s!" % name)


def health(request):
    return HttpResponse("OK")


def info(request):

    #print system information
    import platform
    import os
    import django

    info = {
        "python_version": platform.python_version(),
        "django_version": django.get_version(),
        "os": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "system_name": platform.node(),
    }

    info_str = "\n".join("%s: %s" % (k, v) for k, v in info.items())
    return HttpResponse(info_str, content_type="text/plain")