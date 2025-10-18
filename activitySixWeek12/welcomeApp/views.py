from django.shortcuts import render

def welcome(request, name):
    """
    A Django view that renders an HTML template
    with a personalized welcome message.
    """
    return render(request, 'welcomeApp/welcome.html', {'name': name})
