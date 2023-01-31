import json


from constants import souvProb, caseProb, floatProb, floatRange, statTrakProb


def get_item(item, case):
    """
    Retrieves item and its expected price
    """
    file = ("data/cases/json/" + case + "_case.json")
    data = json.load(open(file))

    for rarity in data["content"]:
        for wep in data["content"][rarity]:
            if wep["name"].startswith("â"):
                knifeName = wep["name"][4:]
                if knifeName == item:
                    return wep
            if wep["name"] == item:
                return wep


def get_item_expected_value(item, case):
    wep = get_item(item, case)
    itemPrices = wep["prices"]
    print(itemPrices)
    extPrices = itemPrices.copy()
    for ext in floatProb:
        if itemPrices[ext] == "Not Possible":
            continue
        extPrice = float(itemPrices[ext][3:]) * floatProb.get(ext)
        extPrices[ext] = extPrice

    extPrices = {key: val for key, val in extPrices.items() if val != "Not Possible"}
    expectedPrice = sum(extPrices.values())
    print(extPrices)
    return expectedPrice


def calc_float_dist(item, case):
    wep = get_item(item, case)
    wepFloatRange = wep["float_range"]
    maxFloat, minFloat = float(wepFloatRange[1]), float(wepFloatRange[0])

    bucketRanges = {}
    # bucketRanges.append(maxFloat)

    # for bucket in floatProb:
    #     bucketRange = (maxFloat - minFloat) * floatProb.get(bucket)
    #     bucketRanges.append(bucketRange)

    battleScarredEndpoint = maxFloat - (1 - floatRange.get("Battle-Scarred")[0]) * (maxFloat - minFloat)
    wellWornEndpoint = maxFloat - (1 - floatRange.get("Well-Worn")[0]) * (maxFloat - minFloat)
    fieldTestedEndpoint = maxFloat - (1 - floatRange.get("Field-Tested")[0]) * (maxFloat - minFloat)
    minimalWearEndpoint = maxFloat - (1 - floatRange.get("Minimal Wear")[0]) * (maxFloat - minFloat)
    factoryNewEndpoint = maxFloat - (1 - floatRange.get("Factory New")[0]) * (maxFloat - minFloat)

    bucketRanges["Battle-Scarred"] = [battleScarredEndpoint, maxFloat]
    bucketRanges["Well-Worn"] = [wellWornEndpoint, battleScarredEndpoint]
    bucketRanges["Field-Tested"] = [wellWornEndpoint, fieldTestedEndpoint]
    bucketRanges["Minimal Wear"] = [minimalWearEndpoint, wellWornEndpoint]
    bucketRanges["Factory New"] = [minimalWearEndpoint, minFloat]

    # bucketRanges.append(minFloat)

    return bucketRanges 


def get_rarity_prices(rarity, case):
    """
    Retrieves prices of a single rarity in a case
    """
    file = ("data/cases/json/" + case + "_case.json")
    data = json.load(open(file))

    item_prices = []
    for item in data["content"][rarity]:
        item_prices.append(item["prices"])
        # price = float(price[3:])
    print(item_prices)

    return data


# get_rarity_prices("Rare Special Items", "chroma_2")
# print(get_item_expected_value("Desert Eagle | Corinthian", "Revolver"))
# print(get_item("Karambit | Rust Coat", "chroma_2"))
# print(calc_float_dist("Desert Eagle | Corinthian", "Revolver"))
print(calc_float_dist("Negev | Loudmouth", "Falchion"))