import json

from mmt import *
from mmt import src

def save(final_data):
    json_object = json.dumps(final_data, indent=4, ensure_ascii=False)
    with open("final_data.json", "w", encoding='utf8') as outfile:
       outfile.write(json_object)


def submit(src:str,dest:str):    
    price=flightScrape(src,dest)   
    price = price.split('\n')
    
    # print(src)
    
    final_data=[]
    for i in range(0,len(price)):
        data={}
        if  src in price[i].lower():
            data['company']=price[i-3]
            # print(company)
            data['flightNo']=price[i-2]
            # print(flightNo)
            data['depTime']=price[i-1]
            # print(depTime)
            data['source']=price[i]
            # print(source)
            data['duration']=price[i+1]
            # print(duration)
            data['type']=price[i+2]
            # print(type)
            data['arrivalTime']=price[i+3]
            # print(arrivalTime)
            data['destination']=price[i+4]
            # print(destination)
            data['rate']=price[i+5]
            # print(rate)
            print("\n")
    
            final_data.append(data)
            save(final_data)