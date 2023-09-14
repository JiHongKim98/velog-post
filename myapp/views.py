from django.shortcuts import render

def index(request, name, li_text):
    context = {
        'name' : name,
        'li_text' : li_text
    }
    return render(request, 'myapp_index.html', context)