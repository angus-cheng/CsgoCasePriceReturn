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
    """Retrives expected price of an item"""
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
    """Calculates the float distribution of an item"""
    wep = get_item(item, case)
    wepFloatRange = wep["float_range"]
    maxFloat, minFloat = float(wepFloatRange[1]), float(wepFloatRange[0])

    floatPortions = {}
    bucketRange = calc_bucket_dist(minFloat, maxFloat)

# error somewhere in here:
    for bucket, bucketVal in bucketRange.items():
        for wear, wearVal in floatRange.items():
            # if wearStart <= bucketStart and bucketStart <= wearEnd:
            #     if bucketEnd >= wearEnd:
            #         if (wearEnd - bucketStart >= 0):
            #             bucketRange -= (wearEnd - bucketStart)
            #             floatPortions[wear] = (wearEnd - bucketStart)
            #             floatPortions.update(iter_float_portions(wear, bucketRange, bucketStart))
            if bucketEnd >= wearEnd:
                if (wearEnd - bucketStart >= 0):
                    bucketRange -= (wearEnd - bucketStart)
                    floatPortions[wear] = (wearEnd - bucketStart)
                    floatPortions.update(iter_float_portions(wear, bucketRange, bucketStart))
            # portions = iter_float_portions(wear, bucketVal, wearVal)
            # for key, val in portions.items():
            #     if key in floatPortions:
            #         val += floatPortions.get(key)
            #     floatPortions[key] = val

    return floatPortions


def calc_bucket_dist(minFloat, maxFloat):
    """Calculates the bucket distribution of an item"""
    bucketRange = {}

    battleScarredEndpoint = maxFloat - (1 - floatRange.get("Battle-Scarred")[0]) * (maxFloat - minFloat)
    wellWornEndpoint = maxFloat - (1 - floatRange.get("Well-Worn")[0]) * (maxFloat - minFloat)
    fieldTestedEndpoint = maxFloat - (1 - floatRange.get("Field-Tested")[0]) * (maxFloat - minFloat)
    minimalWearEndpoint = maxFloat - (1 - floatRange.get("Minimal Wear")[0]) * (maxFloat - minFloat)

    bucketRange["Bucket 1"] = [battleScarredEndpoint, maxFloat]
    bucketRange["Bucket 2"] = [wellWornEndpoint, battleScarredEndpoint]
    bucketRange["Bucket 3"] = [fieldTestedEndpoint, wellWornEndpoint]
    bucketRange["Bucket 4"] = [minimalWearEndpoint, fieldTestedEndpoint]
    bucketRange["Bucket 5"] = [minFloat, minimalWearEndpoint]

    return bucketRange

    
def recur_float_portions(wear, bucketRange, bucketStart):
    """Recursively calculates the float portions of an item bucket distribution"""
    floatPortions = {}
    if bucketRange >= 0:
        prev_wear = get_prev_wear(wear)
        wearEnd = prev_wear[1][1]
        wearRange = wearEnd - prev_wear[1][0]
        bucketRange -= wearRange
        floatPortions[prev_wear[0]] = (wearEnd - bucketStart)
        return floatPortions
    else:
        return recur_float_portions(wear, bucketRange, bucketStart)


def iter_float_portions(wear, bucketVal, wearVal):
    """Iteratively calculates the float portions of an item bucket distribution"""
    bucketStart, bucketEnd = bucketVal[0], bucketVal[1]
    wearStart, wearEnd = wearVal[0], wearVal[1]

    bucketRange = bucketEnd - bucketStart
    wearRange = wearEnd - wearStart

    floatPortions = {}
    callStack = []
    callStack.append(wear)

    while callStack:
        wear = callStack.pop()
        # Case 1
        if bucketStart >= wearStart and bucketEnd <= wearEnd:
            floatPortions[wear] = bucketRange
        # Case 2
        elif bucketStart <= wearStart and bucketEnd >= wearEnd:
            floatPortions[wear] = wearRange
        # Case 3
        elif bucketStart <= wearStart and bucketEnd <= wearEnd:
            print(bucketStart, wearStart, bucketEnd, wearEnd)
            floatPortions[wear] = bucketEnd - wearStart
            print(floatPortions)
        # Case 4
        # elif bucketStart >= wearStart and bucketEnd >= wearEnd:
        #     floatPortions[wear] = wearEnd - bucketStart
        else:
            continue 

    return floatPortions


def get_prev_wear(currentWear):
    """Retrieves the previous float wear given the current wear of an item"""
    floatList = (list(floatRange.keys()))
    for key, item in enumerate(floatList):
        if item == currentWear:
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
# print(sum(calc_float_dist("Negev | Loudmouth", "Falchion").values()))