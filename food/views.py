from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from food.models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    item_template = loader.get_template('food/index.html')
    context = {
        
    }
    return HttpResponse(item_template.render(context, request))

def item(request):
    return HttpResponse("<h1>This is the item</hi")