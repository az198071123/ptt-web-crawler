import requests
event = 'ptt_give_observer'
url = f'https://maker.ifttt.com/trigger/{event}/with/key/dU3h5CdXWVPRA_73d_jrHr'
data = {'value1': 'test title', 'value2': 'test content\n123123'}
res = requests.post(url, data=data)
print(res)
