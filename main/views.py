from django.shortcuts import render
from .forms import PageRequestForm
from .utils import generate_page_code

# Create your views here.

def generate_page(request):
    if request.method == "POST":
        form = PageRequestForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            style = form.cleaned_data['style']
            page_code = generate_page_code(title, description, style)
            return render(request, 'main/result.html', {'page_code': page_code})
    else:
        form = PageRequestForm()
    return render(request, 'main/form.html', {'form': form})
