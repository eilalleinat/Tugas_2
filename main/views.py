from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
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

    return render(request, 'home.html', context)