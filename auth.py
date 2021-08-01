import requests
import json




URL_BASE = 'https://graph.facebook.com/v11.0/me?'

def get_data(fields:str):
    cred = open('creds.json','r')
    cred_data= json.loads(cred.read()) 
    FB_USER_ACCESS_TOKEN = cred_data['FB_USER_ACCESS_TOKEN']
    fields = 'fields=' + fields
    full_url = URL_BASE + fields + '&access_token=' + FB_USER_ACCESS_TOKEN
    response = requests.get(full_url)
    if str(response.status_code) == '200':
        print('\n Request went through')
        print('\n Data collected: \n {} \n'.format(response.text))

    else:
        print('\n Request did not go through \n')
        print(f' Status code: {response.status_code} ')
get_data('first_nam e,last_name,birthday')