from django.shortcuts import render
from .models import Product
from .forms import ProductFilterForm
# Create your views here.
def catalog(request):
    action = request.get_full_path().split('/')[2]
    title = ""


    products = Product.objects.order_by('name')
    form = ProductFilterForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')



        if name:
            products = products.filter(name__icontains=name)
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)


    if 'mens_outerwear' in action:
        title = "Мужская верхняя одежда в Кокшетау"
        products = products.filter(gender='M')
        products = products.filter(type='Верхняя одежда')
        clothing_type = form.cleaned_data.get('clothing_type')
        if clothing_type and form.is_valid():
            products = products.filter(clothing_type=clothing_type)
    if 'mens_accessories' in action:
        title = 'Мужские аксессуары в Кокшетау'
        products = products.filter(gender='M')
        products = products.filter(type='Аксессуар')
        accessories_type = form.cleaned_data.get('accessories_type')
        if accessories_type and form.is_valid():
            products = products.filter(clothing_type=accessories_type)


    if 'women_outerwear' in action:
        title = "Женская верхняя одежда в Кокшетау"
        products = products.filter(gender='F')
        products = products.filter(type='Верхняя одежда')
        clothing_type = form.cleaned_data.get('clothing_type')

        if clothing_type and form.is_valid():
            products = products.filter(clothing_type=clothing_type)
    if 'women_accessories' in action:
        title = 'Женские аксессуары в Кокшетау'
        products = products.filter(gender='F')
        products = products.filter(type='Аксессуар')
        accessories_type = form.cleaned_data.get('accessories_type')
        if accessories_type and form.is_valid():
            products = products.filter(clothing_type=accessories_type)
    return render(request, 'main/catalog.html', {'products': products, 'form': form, 'action': action, 'title': title})

def ask_Men(request):
    return render(request, 'main/ask_Men.html')

def ask_Women(request):
    return render(request, 'main/ask_Woman.html')
