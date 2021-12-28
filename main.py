import requests
import time
import pickle
from pushbullet import Pushbullet
api_key = ''
pb = Pushbullet(api_key)  # add the api key

def card_tracker(cards_name, target, quality):
    url = 'https://api.x.immutable.com/v1/orders?direction=asc&include_fees=true&order_by=buy_quantity&page_size=1&sell_token_address=0xacb3c6a43d15b907e8433077b6d38ae40936fe2c&sell_token_type=ERC721&status=active&sell_token_name="%s"&sell_metadata={"quality":["%s"]}&buy_token_type=ETH' % (
        cards_name, quality)
    response = requests.get(url)
    data = response.json()

    data = data["result"]
    # print(data)
    decimal = int(data[0]["buy"]["data"]["decimals"])
    quantity = int(data[0]["buy"]["data"]["quantity"])
    price = (quantity / pow(10, decimal))

    print("The price of the", cards_name, "card is",
          price, "eth and the price target is", target)

    if price <= target:
        print("You have to buy the card :", cards_name)
        if notif == 'Yes':
            title = "You have to buy the card :" + str(cards_name)
            body = "The price of the" + cards_name + "card is" + \
                str(price) + "eth and the price target is" + str(target)
            push = pb.push_note(title, body)


list_cards = []

save = input("Do you want to use your backup? (Yes or No)")
while True:
    if save == "Yes":
        notif = input("Do you want the notifications? (Yes or No) :")
        with open("list_cards.txt", "rb") as fp:   # Unpickling
            list_cards = pickle.load(fp)
            print(list_cards)
            break

    card = []
    cards_name = input("Name of the card ? :  ")
    target = float(input("Price wish ? :  "))
    quality = input(
        "Quality of the card ? (Meteorite,Shadow,Gold,Diamond) :  ")
    card.append(cards_name)
    card.append(target)
    list_cards.append(card)
    next = input("Do you want to add another card (Enter or No)")
    if next == "No":
        save = input("Do you want to save the list of cards? (Yes,No)")
        if save == "Yes":
            with open("list_cards.txt", "wb") as fp:  # save
                pickle.dump(list_cards, fp)
                print("save")
            notif = input("Do you want the notifications? (Yes or No) :")
            break

while True:
    for i in range(len(list_cards)):
        cards_name = list_cards[i][0]
        target = list_cards[i][1]
        quality = list_cards[i][2]
        card_tracker(cards_name, target, quality)
        time.sleep(300)  # wait 5 min

