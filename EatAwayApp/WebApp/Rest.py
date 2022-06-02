# This is a sample Python script.
import requests.api
import pandas as pd
from pandas.io.json import json_normalize
import json
from pandas import json_normalize

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    api_url = "https://kiwi-anubis.azurewebsites.net/stock/8c1d7205-f9b3-4dbd-8fb5-c166fd45c724"
    r = requests.get(api_url)
    content = json.loads(r.text)

    df2 = pd.DataFrame([content])


    df2.to_csv('daten.csv', index=False)
    df2 = df2['stockEntries']


    df1 = pd.DataFrame()
    df4 = pd.DataFrame()

    for enum,i in enumerate(df2[0]):
        s1 = json.dumps(df2[0][enum])
        d2 = json.loads(s1)
        normalizedData = json_normalize(d2)
        df1 = pd.concat([normalizedData, df1], sort=False)

    df1.to_csv('OverviewData.csv')


    for enum,j in enumerate(df1['products']):
        DetailedData = json_normalize(j)
        df4 = pd.concat([DetailedData, df4], sort=False)

    print(df4)

    df1.to_csv('DetailedData.csv')





    #print(json.loads(df2[0][0]))

    # dict1 = json.loads(str_res)
    #df2 = pd.read_json(str_res, orient='index')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("test")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/