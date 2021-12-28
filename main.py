import requests
import time

cards_name = input("Nom de la carte ? :  ")
target = float(input("Prix souhaiter  ? :  "))

def card_tracker(cards_name, target):
    while True:
        url = "https://api.x.immutable.com/v1/orders?direction=asc&include_fees=true&order_by=buy_quantity&page_size=1&sell_token_address=0xacb3c6a43d15b907e8433077b6d38ae40936fe2c&sell_token_type=ERC721&status=active&sell_token_name=" + cards_name +"&buy_token_type=ETH"
        response = requests.get(url)

        data = response.json()

        data = data["result"]
        # print(data)
        decimal = int(data[0]["buy"]["data"]["decimals"])
        quantity = int(data[0]["buy"]["data"]["quantity"])
        price = (quantity / pow(10, decimal))
        print("Le prix de la carte",cards_name,"est de" ,price, "eth. et la target est de", target)
        if price >= target:
            print("Achat")
        time.sleep(300) #wait 5 min

card_tracker(cards_name,target)