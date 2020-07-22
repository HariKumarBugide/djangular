from django.shortcuts import render
def hello_template(request):
    return render(request, 'templates/home.html')
