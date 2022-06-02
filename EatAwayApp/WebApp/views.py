from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ConsumptionItem


def EatAppView(request):
    all_todo_items = ConsumptionItem.objects.all()
    return render(request, 'homepage.html',
    {'all_items':all_todo_items})

def addEatAppView(request):
    x = request.POST['content']
    new_item = ConsumptionItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/WebApp/')

def deleteEatAppView(request, i):
    y = ConsumptionItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/WebApp/')