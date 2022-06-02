from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ConsumptionItem, ListingItem
# This is a sample Python script.
import requests.api
import pandas as pd
from pandas.io.json import json_normalize
import json
from pandas import json_normalize
import numpy as np
from django.db.models import Q  # New


def EatAppView(request):
    search_post = request.GET.get('search')

   #search_list = pd.read_csv('/Users/egemenokur/PycharmProjects/EatAway27/EatAwayApp/WebApp/app.csv')


    if search_post:
        search_list =  np.array(ListingItem.objects.filter(Q(ReadeyProductName__icontains=search_post)))


    else:
        # If not searched, return default posts
        search_list = np.array(ListingItem.objects.all().values())

    all_todo_items = np.array(ConsumptionItem.objects.all().values())

    context = {'all_items': all_todo_items,
               'search_items': search_list
               }


    return render(request, 'homepage.html',context)


"""
    search_list = pd.read_csv('/Users/egemenokur/PycharmProjects/EatAway27/EatAwayApp/WebApp/app.csv')
    listing = np.array(search_list)
    for i in range(0,4):
        print(search_list['product'][i])
        ListingItem.objects.create(ReadeyProductName=search_list['product'][i], ApproximateProductLifeMin=search_list['min'][i], ApproximateProductLifeMax=search_list['max'][i])
    """

def addEatAppView(request):
    x = request.POST['productName']
    new_item = ConsumptionItem(productName = x)
    new_item.save()
    return HttpResponseRedirect('/WebApp/')

def deleteEatAppView(request, i):
    y = ConsumptionItem.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/WebApp/')

def dynamic_articles_view(request):

    object_list = ConsumptionItem.objects.filter(title__icontains=request.GET.get('search'))
    return render(request, "homepage.html", object_list)

def MergeWithKiwi(request):
    all_todo_items = np.array(ConsumptionItem.objects.all().values())
    api_url = "https://kiwi-anubis.azurewebsites.net/stock/8c1d7205-f9b3-4dbd-8fb5-c166fd45c724"
    r = requests.get(api_url)
    content = json.loads(r.text)
    df2 = pd.DataFrame([content])

    df2 = df2['stockEntries']
    df1 = pd.DataFrame()
    df4 = pd.DataFrame()

    for enum, i in enumerate(df2[0]):
        s1 = json.dumps(df2[0][enum])
        d2 = json.loads(s1)
        normalizedData = json_normalize(d2)
        df1 = pd.concat([normalizedData, df1], sort=False)
    for enum,j in enumerate(df1['products']):
        DetailedData = json_normalize(j)
        df4 = pd.concat([DetailedData, df4], sort=False)
        #newArray = np.append(DetailedData['productName'],all_todo_items , axis=0)
        SingleData = DetailedData['productName'][0]
        ConsumptionItem.objects.create(productName=SingleData)
        #df4 = pd.concat([DetailedData, df4], sort=False)

    return HttpResponseRedirect('/WebApp/')