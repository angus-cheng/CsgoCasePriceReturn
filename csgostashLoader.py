import json
import pandas as pd


def get_items():

    rarities = {
        "Mil-Spec Skins": 0.7992,
        "Restricted Skins": 0.1598,
        "Classified Skins": 0.0319,
        "Covert Skins": 0.0063,
        "Rare Special Items": 0.0025
    }

    with open('csgostash-scraper/data/cases/json/chroma_2_case.json', 'w') as read_file:
        data = json.load(read_file)
        df = pd.DataFrame(data)
        dfAsCsv = df.to_csv(header=False, index=False)
        # print(df.loc[:, 'content'])
        # for rarity, prob in rarities.items():
        #     for item in data['content'][rarity]:
        #         items[item] = prob
        #         print(item['name'])

        # read_file.write(dfAsCsv)
        json.dump(data, f)

    return


print(get_items())
