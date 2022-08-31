import requests

h = {'ken-auth' : '5a87homn23w4wmf6keg0mp5b9'}
x = requests.get('https://kencove.com/fence/codebehind/api.php?webhook=orderNumberSync',headers=h)


web_orders = x.text

web_orders_array = web_orders.split(',')

web_orders_array[0] = web_orders_array[0].replace('[','')

web_orders_array[len(web_orders_array)-1] = web_orders_array[len(web_orders_array)-1].replace(']','')

print(web_orders_array[len(web_orders_array)-1])

for x in range(len(web_orders_array)):
    web_orders_array[x] = web_orders_array[x].replace('"','')

for i in web_orders_array:
    try:
        x = int(i)
    except:
        print(i)
