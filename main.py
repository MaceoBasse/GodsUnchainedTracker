import requests
import time
import pickle


def card_tracker(cards_name, target):
    url = "https://api.x.immutable.com/v1/orders?direction=asc&include_fees=true&order_by=buy_quantity&page_size=1&sell_token_address=0xacb3c6a43d15b907e8433077b6d38ae40936fe2c&sell_token_type=ERC721&status=active&sell_token_name=" + cards_name + "&buy_token_type=ETH"
    response = requests.get(url)
    data = response.json()

    data = data["result"]
    # print(data)
    decimal = int(data[0]["buy"]["data"]["decimals"])
    quantity = int(data[0]["buy"]["data"]["quantity"])
    price = (quantity / pow(10, decimal))

    print("Le prix de la carte", cards_name, "est de",
          price, "eth et la target est de", target)

    if price <= target:
        print("Achat")


list_cards = []
save = input("Veux-tu utiliser ta sauvegarde ? (Oui,Non)")
while True:
    if save == "Oui":
        with open("list_cards.txt", "rb") as fp:   # Unpickling
            list_cards = pickle.load(fp)
            print(list_cards)
            break
    card = []
    cards_name = input("Nom de la carte ? :  ")
    target = float(input("Prix souhaiter  ? :  "))
    card.append(cards_name)
    card.append(target)
    list_cards.append(card)
    next = input("Voulez-vous ajouter une carte (Enter ou Non)")
    if next == "Non":
        save = input("Veux-tu sauvegarder la liste de cartes ? (Oui,Non)")
        if save == "Oui":
            with open("list_cards.txt", "wb") as fp:  # save
                pickle.dump(list_cards, fp)
                print("sauvegarde")
        break

while True:
    for i in range(len(list_cards)):
        cards_name = list_cards[i][0]
        target = list_cards[i][1]
        card_tracker(cards_name, target)
        time.sleep(300)  # wait 5 min
