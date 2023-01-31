"""
Souvenir & case probabilities taken from:
https://www.reddit.com/r/csgomarketforum/wiki/faq/#wiki_cases
"""
souvProb = {
    "Consumer": 0.7992,
    "Industrial": 0.1598,
    "Mil-Spec": 0.032,
    "Restricted": 0.0064,
    "Classified": 0.00128,
    "Covert": 0.000256
}

caseProb = {
    "Mil-Spec": 0.7992,
    "Restricted": 0.1598,
    "Classified": 0.0319,
    "Covert": 0.0063,
    "Rare Special Items": 0.0025
}

"""
Float probabilities taken from:
https://blog.csgofloat.com/analysis-of-float-value-and-paint-seed-distribution-in-cs-go/
"""
floatProb = {
    "Battle-Scarred": 0.16,
    "Well-Worn": 0.24,
    "Field-Tested": 0.33,
    "Minimal Wear": 0.24,
    "Factory New": 0.03
}

# Default float range for a skin with float range 0.00 to 1.00
floatRange = {
    "Battle-Scarred": [0.45, 1.00],
    "Well-Worn": [0.38, 0.45],
    "Field-Tested": [0.15, 0.38],
    "Minimal Wear": [0.07, 0.15],
    "Factory New": [0.00, 0.007]
}

statTrakProb = 0.1
