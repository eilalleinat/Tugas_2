from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_home(request):
    Flowers = {
        'flower_name_0': 'A Bouquet of Tulips',
        'amount_0': 3,
        'description_0': 'A tulip bouquet with a burst of vibrant elegance, blending eloquent purples and serene blues for a timeless expression of beauty.',

        'flower_name_1': 'Rose Bouquets',
        'amount_1': 4,
        'description_1': 'A rose bouquet with a timeless symbol of love, with velvety petals in shades from deep crimson to soft pastels, an expression of affection.',
        
        'flower_name_2': 'Sunny flowers',
        'amount_2': 7,
        'description_2': 'A sunflower bouquet bursts with the golden radiance of sunflowers, evoking joy and the warmth of sunny days in a single, vibrant arrangement.',
    }

    return render(request, 'home.html', Flowers)

def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Taniella', # Your name
        'class': 'PBP D', # Your PBP Class
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


