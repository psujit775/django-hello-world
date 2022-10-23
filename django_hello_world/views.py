from django.http import HttpResponse


def index(request):
    return HttpResponse("Congratulatios, Your Django Hello World Project is up and running.")
