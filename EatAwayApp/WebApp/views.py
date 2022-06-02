from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ConsumptionItem
# This is a sample Python script.
import requests.api
import pandas as pd
from pandas.io.json import json_normalize
import json
from pandas import json_normalize
import numpy as np


def EatAppView(request):
    all_todo_items = np.array(ConsumptionItem.objects.all().values())

    context = {
        'all_items': all_todo_items
    }
    return render(request, 'homepage.html',
    context)

def addEatAppView(request):
    x = request.POST['productName']
    new_item = ConsumptionItem(productName = x)
    new_item.save()
    return HttpResponseRedirect('/WebApp/')

def deleteEatAppView(request, i):
    y = ConsumptionItem.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/WebApp/')

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