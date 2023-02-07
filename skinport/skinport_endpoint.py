import requests
import base64
import numpy as np
import pandas as pd

client_id = '2c91c91f08c44645bf3005f4fab7ee9b'
client_secret = 'KhBvHKk8sKL/t2ejI4M+3Pr8mtHEkpODOyzdgZvLoQumd3AtalJlvGG+F4OGSDmZG7dkM8SMZwLZqDGzqkG4mg=='
client_data = f'{client_id}:{client_secret}'
encoded_data = str(base64.b64encode(client_data.encode('utf-8')), 'utf-8')
authorization_header_string = f'Basic {encoded_data}'

url = 'https://api.skinport.com/v1/items'
payload = {
    'app_id': 730,
    'currency': 'AUD',
    'tradable': 0
}

req = requests.get(url, params=payload).json()

data = np.asarray(req)
# df = pd.DataFrame(data, columns=['market_hash_name', 'currency',
#                                  'suggested_price', 'item_page',
#                                  'market_page', 'min_price', 'max_price',
#                                  'mean_price', 'median_price',
#                                  'quantity', 'created_at', 'updated_at'])
df = pd.DataFrame(data)
df = df.iloc[:, 0].dropna().apply(pd.Series)

df.to_csv('./items.csv', index=False)

print('test')