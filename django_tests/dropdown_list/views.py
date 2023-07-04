from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dropdown_list/home.html')

def selected_input(request):
    selected_input = str(request.GET.get('selected'))
    return render(request, 'dropdown_list/selected_input.html', {'selected_input': selected_input})
