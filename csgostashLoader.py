import json

rarities = {
    "Mil-Spec Skins": 0.7992,
    "Restricted Skins": 0.1598,
    "Classified Skins": 0.0319,
    "Covert Skins": 0.0063,
    "Rare Special Items": 0.0025
}

extProb = {
    "Battle-Scarred": 0.1054,
    "Field-Tested": 0.3551,
    "Minimal Wear": 0.2707,
    "Factory New": 0.1549
}


def get_item(item):
    """
    Retrieves item and its expected price
    """
    file = ('data/cases/json/chroma_2_case.json')
    data = json.load(open(file))

    for rarity in data["content"]:
        for wep in data["content"][rarity]:
            if wep["name"].startswith("â"):
                knifeName = wep["name"][4:]
                if knifeName == item:
                    return wep
            if wep["name"] == item:
                return wep


def get_rarity_prices(rarity):
    """
    Retrieves prices of a single rarity in a case
    """
    file = ('data/cases/json/chroma_2_case.json')
    data = json.load(open(file))

    item_prices = []
    for item in data["content"]["Rare Special Items"]:
        item_prices.append(item["prices"].get(rarity))
        # price = float(price[3:])
    print(item_prices)

    return data


# get_rarity_prices("Factory New")
print(get_item_price("Karambit | Rust Coat"))
