import requests
from time import sleep
import csgoStashExtractor 

currencies = {
    "USD": 1,  # United States dollar
    "GBP": 2,  # British pound sterling
    "EUR": 3,  # The euro
    "CHF": 4,  # Swiss franc
    "RUB": 5,  # Russian ruble
    "PLN": 6,  # Polish złoty
    "BRL": 7,  # Brazilian real
    "JPY": 8,  # Japanese yen
    "SEK": 9,  # Swedish krona
    "IDR": 10,  # Indonesian rupiah
    "MYR": 11,  # Malaysian ringgit
    "BWP": 12,  # Botswana pula
    "SGD": 13,  # Singapore dollar
    "THB": 14,  # Thai baht
    "VND": 15,  # Vietnamese dong
    "KRW": 16,  # South Korean won
    "TRY": 17,  # Turkish lira
    "UAH": 18,  # Ukrainian hryvnia
    "MXN": 19,  # Mexican Peso
    "CAD": 20,  # Canadian dollar
    "AUD": 21,  # Australian dollar
    "NZD": 22,  # New Zealand dollar
    "CNY": 23,  # Chinese yuan
    "INR": 24,  # Indian rupee
    "CLP": 25,  # Chilean peso
    "PEN": 26,  # Peruvian sol
    "COP": 27,  # Colombian peso
    "ZAR": 28,  # South African rand
    "HKD": 29,  # Hong Kong dollar
    "TWD": 30,  # New Taiwan dollar
    "SAR": 31,  # Saudi riyal
    "AED": 32  # United Arab Emirates dirham
}

# https://www.reddit.com/r/GlobalOffensiveTrade/comments/4jd983/discussion_analysis_of_float_value_distributions/ 
extProb = {
    "Battle-Scarred": 0.1054,
    "Field-Tested": 0.3551,
    "Minimal Wear": 0.2707,
    "Factory New": 0.1549
}


souvenirProb = {
    "Consumer": 0.7992,
    "Industrial": 0.1598,
    "Mil-Spec": 0.032,
    "Restricted": 0.0064,
    "Classified": 0.00128,
    "Covert": 0.000256
}




class Item:
    def __init__(self, name):
        self.name = name
        self.skins = {}

    def add_skin(self, skin, rarity):
        self.skins[skin] = rarity

    def get_rarity_prob(self, skin):
        return caseProb.get(self.skins.get(skin))

    def get_name(self):
        return self.name

    def get_skins(self):
        return self.skins


class SouvenirPackage:
    def __init__(self):
        self.endpoint = "https://steamcommunity.com/market/priceoverview"
        self.name = ""
        self.items = [
            Item("AK-47"),
            Item("AUG"),
            Item("AWP"),
            Item("CZ75-Auto"),
            Item("Desert Eagle"),
            Item("Dual Berettas"),
            Item("FAMAS"),
            Item("Five-Seven"),
            Item("G3SG1"),
            Item("Galil AR"),
            Item("Glock-18"),
            Item("M249"),
            Item("M4A1-S"),
            Item("M4A4"),
            Item("MAC-10"),
            Item("MAG-7"),
            Item("MP5-SD"),
            Item("MP7"),
            Item("MP-9"),
            Item("Negev"),
            Item("Nova"),
            Item("P2000"),
            Item("P90"),
            Item("PP-Bizon"),
            Item("R8 Revolver"),
            Item("Sawed-Off"),
            Item("SCAR-20"),
            Item("SG 553"),
            Item("SSG 08"),
            Item("Tec-9"),
            Item("USP-S"),
            Item("UMP-45"),
            Item("XM1014")
        ]

    def get_item(self, item):
        return [i for i in self.items if i == item]

    def get_name(self):
        return self.name

    def get_all_items(self):
        return self.items

    def get_package_price(self):
        payload = {"appid": 730,
                   "currency": currencies["AUD"],
                   "market_hash_name": f"{self.name}"}
        resp = requests.get(self.endpoint, params=payload)
        return resp.json()

    def get_item_price(self, wep, skin, extProb):
        payload = {"appid": 730,
                   "currency": currencies["AUD"],
                   "market_hash_name": f"{wep} | {skin} ({extProb})"}
        resp = requests.get(self.endpoint, params=payload)
        return resp.json()

    def get_souv_price_avg(self):
        total = 0
        count = 0
        for item in self.items:
            print(self.items)
            for skin in item.get_skins():
                for wear in extProb.keys():
                    resp = self.get_item_price(item, skin, wear)
                    print(resp)
                    if ("lowest_price" in resp):
                        itemPrice = (float(resp["lowest_price"][3:]
                                     .replace(',', ''))
                                     * extProb.get(wear)
                                     * item.get_rarity_prob(skin))
                        total += itemPrice
                        count += 1
                    sleep(3)

        avg = total / count
        return avg


class AncientPackage(SouvenirPackage):
    def __init__(self):
        super().__init__()
        self.name = "Antwerp 2022 Ancient Souvenir Package"
        print(self.get_item(Item("AK-47")))
        # self.get_item(Item("AK-47")).add_skin("Panthera onca", "Classified")
        Item("AUG").add_skin("Carved Jade", "Mil-Spec")
        # Item("CZ75-Auto").add_skin("Silver", "Industrial")
        # Item("FAMAS").add_skin("Dark Water", "Mil-Spec")
        # Item("G3SG1").add_skin("Ancient Ritual", "Industrial")
        # Item("Galil AR").add_skin("Dusk Ruins", "Mil-Spec")
        # Item("M4A1-S").add_skin("Welcome to the Jungle", "Covert")
        # Item("MAC-10").add_skin("Gold Brick", "Restricted")
        # Item("MP7").add_skin("Tall Grass", "Industrial")
        # Item("Nova").add_skin("Army Sheen", "Consumer")
        # Item("P2000").add_skin("Panther Camo", "Industrial")
        # Item("P90").add_skin("Run and Hide", "Classified")
        # Item("P90").add_skin("Ancient Earth", "Consumer")
        # Item("R8 Revolver").add_skin("Night", "Consumer")
        # Item("SG 553").add_skin("Lush Ruins", "Consumer")
        # Item("SSG 08").add_skin("Jungle Dashed", "Consumer")
        # Item("Tec-9").add_skin("Blast From the Past", "Mil-Spec")
        # Item("USP-S").add_skin("Ancient Visions", "Restricted")
        # Item("XM1014").add_skin("Ancient Lore", "Restricted")


def main():
    anc = AncientPackage()
    print(f"Souvenir package price: {anc.get_package_price()}")
    # print(f"Average price from souvenir: {anc.get_souv_price_avg()}")
    return


if __name__ == "__main__":
    main()
