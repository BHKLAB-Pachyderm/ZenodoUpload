import requests
import json

ACCESS_TOKEN = "sqWlSNzLeWaRcXAWck9qVeJJxs47PCrqZdOJp4gvfOOnFjfZDTaBcYqvECti"
r = requests.post('https://zenodo.org/api/deposit/depositions',
                        params={'access_token': ACCESS_TOKEN}, json={},
                        headers={"Content-Type": "application/json"})

r.status_code
r.json()

bucket_url = r.json()['links']['bucket']

with open('/pfs/getGRAYP_2013/GRAY_2013.rds', 'rb') as fp:
    res = requests.put(
        bucket_url + '/GRAY_2013.rds',
        data=fp,
        # No headers included in the request, since it's a raw byte request
        params=params,
    )
print(res.json())

data = {
     'metadata': {
        'title': 'My first upload',
        'upload_type': 'poster',
        'description': 'This is my first upload',
        'creators': [{'name': 'Doe, John',
                      'affiliation': 'Zenodo'}]
        }
     }
     deposition_id = r.json()['id']
    r = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
                      params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
                      headers=headers)

r.status_code

##POST Request

url = 'https://orcestra-beta.azurewebsites.net/pset/complete'
myobj = {'COMMIT': '6hdhs8283', "ZENODO DOI": "10.32.5:zenodo.15432"}

x = requests.post(url, data = myobj)

print(x.text)
