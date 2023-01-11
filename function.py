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
    
    # print(price)

    
    final_data=[]
    # for i in range(0,len(price)):
    #     data={}
    #     if  src in price[i].lower():
    #         data['company']=price[i-3]
    #         # print(company)
    #         data['flightNo']=price[i-2]
    #         # print(flightNo)
    #         data['depTime']=price[i-1]
    #         # print(depTime)
    #         data['source']=price[i]
    #         # print(source)
    #         data['duration']=price[i+1]
    #         # print(duration)
    #         data['type']=price[i+2]
    #         # print(type)
            
    #         if price[i+4]=='+ 1 DAY':
    #             data['arrivalTime']=price[i+3]+price[i+4]
    #             # print(arrivalTime)
    #             data['destination']=price[i+5]
    #             # print(destination)
    #             data['rate']=price[i+6]
    #             # print(rate)
    #         else:
    #             data['arrivalTime']=price[i+3]
    #             # print(arrivalTime)
    #             data['destination']=price[i+4]
    #              # print(destination)
    #             data['rate']=price[i+5]
    #             # print(rate)
            
    #         print("\n")
    
    #         final_data.append(data)
    # save(final_data)
    # return final_data
    
    for i in range(0,len(price)):
        
        if  src in price[i].lower():
            
            if price[i+4]=='+ 1 DAY':
                data={
                    'company':price[i-3],
                    'flightNo':price[i-2],
                    'depTime':price[i-1],
                    'source':price[i],
                    'duration':price[i+1],
                    'type':price[i+2],
                    'arrivalTime':price[i+3]+price[i+4],
                    'destination':price[i+5],
                    'rate':price[i+6]
                }
                
            else:
                data={
                    'company':price[i-3],
                    'flightNo':price[i-2],
                    'depTime':price[i-1],
                    'source':price[i],
                    'duration':price[i+1],
                    'type':price[i+2],
                    'arrivalTime':price[i+3],
                    'destination':price[i+4],
                    'rate':price[i+5]
                }
            print("\n")
            print(data)
            final_data.append(data)
    
    save(final_data)
    return final_data
            