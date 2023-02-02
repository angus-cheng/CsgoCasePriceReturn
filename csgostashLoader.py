import json


from constants import souvProb, caseProb, floatProb, floatRange, statTrakProb


def get_item(item, case):
    """
    Retrieves item and its expected price
    """
    file = ("csgostash-scraper/data/cases/json/" + case + "_case.json")
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

    BucketRange = {}

    battleScarredEndpoint = maxFloat - (1 - floatRange.get("Battle-Scarred")[0]) * (maxFloat - minFloat)
    wellWornEndpoint = maxFloat - (1 - floatRange.get("Well-Worn")[0]) * (maxFloat - minFloat)
    fieldTestedEndpoint = maxFloat - (1 - floatRange.get("Field-Tested")[0]) * (maxFloat - minFloat)
    minimalWearEndpoint = maxFloat - (1 - floatRange.get("Minimal Wear")[0]) * (maxFloat - minFloat)

    BucketRange["Bucket 1"] = [battleScarredEndpoint, maxFloat]
    BucketRange["Bucket 2"] = [wellWornEndpoint, battleScarredEndpoint]
    BucketRange["Bucket 3"] = [fieldTestedEndpoint, wellWornEndpoint]
    BucketRange["Bucket 4"] = [minimalWearEndpoint, fieldTestedEndpoint]
    BucketRange["Bucket 5"] = [minFloat, minimalWearEndpoint]

    floatPortions = {}
    bucketList = (BucketRange.keys())

    for bucket, bucketVal in BucketRange.items():
        for wear, wearVal in floatRange.items():
            bucketStart, bucketEnd = bucketVal[0], bucketVal[1]
            wearStart, wearEnd = wearVal[0], wearVal[1]
            if wearStart <= bucketStart and bucketStart <= wearEnd:
                if bucketEnd >= wearEnd:
                    print(wear, wearVal)
                    print(get_prev_float(wear))

    return


def get_prev_float(wear):
    floatList = (list(floatRange.keys()))
    for key, item in enumerate(floatList):
        if item == wear:
            return floatList[key - 1], floatRange.get(floatList[key - 1])


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

    return data


# print(get_rarity_prices("Rare Special Items", "chroma_2"))
# print(get_item_expected_value("Desert Eagle | Corinthian", "Revolver"))
# print(get_item("Karambit | Rust Coat", "chroma_2"))
# print(calc_float_dist("Desert Eagle | Corinthian", "Revolver"))
print(calc_float_dist("Negev | Loudmouth", "Falchion"))