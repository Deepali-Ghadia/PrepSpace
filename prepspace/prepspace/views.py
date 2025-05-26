from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("<H3>Welcome to PrepSpace</h3>")