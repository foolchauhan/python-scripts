import requests, json, sys
# API_KEY = 'xxxxxxxx' 
API_KEY = sys.argv[1]

STOCK_NSE = 'NSE'
STOCK_BSE = 'BSE'

SHARE = 'SBICARD'

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + STOCK_NSE + ':' + SHARE + '&apikey=' + API_KEY

data = requests.get(url)

jsonData = json.loads(data.text)


print(json.dumps(data.json(), indent=2, sort_keys=False))
