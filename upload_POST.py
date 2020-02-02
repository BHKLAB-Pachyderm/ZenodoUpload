import requests
import json

ACCESS_TOKEN = "smjHPEyfPjYliofNuOpbeZYjCJLeIFEiKMgEFVj2i9R9SxxKdUGL3KJhJc3Sw"
r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
                        params={'access_token': ACCESS_TOKEN}, json={},
                        headers={"Content-Type": "application/json"})

r.status_code
r.json()
doi = r.json()['metadata']['prereserve_doi']['doi']
doi_url = 'https://doi.org/' + doi

bucket_url = r.json()['links']['bucket']

##UPLOAD PSET

with open('/pfs/getGRAYP_2013/GRAY_2013.rds', 'rb') as fp:
    res = requests.put(
        bucket_url + '/GRAY_2013.rds',
        data=fp,
        # No headers included in the request, since it's a raw byte request
        params={'access_token': ACCESS_TOKEN},
    )
print(res.json())

##ADD METADATA

data = {
     'metadata': {
        'title': 'GRAY',
        'upload_type': 'dataset',
        'description': 'GRAY PharmacoSet (PSet) generated by ORCESTRA',
        'creators': [{'name': 'Haibe-Kains, Benjamin',
                      'affiliation': 'Zenodo'}]
        }
     }
deposition_id = r.json()['id']
r = requests.put('https://sandbox.zenodo.org/api/deposit/depositions/%s' % deposition_id, params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),headers={"Content-Type": "application/json"})

r.status_code

##PUBLISH TO ZENODO
r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/%s/actions/publish' % deposition_id,
                      params={'access_token': ACCESS_TOKEN} )

##POST Request

url = 'http://www.orcestra.ca/pset/complete'
myobj = {'COMMIT': '6hdhs8283', "ZENODO_DOI": doi, 'ORCESTRA_ID': "6hdhs8283", 'download_link': doi_url}

x = requests.post(url, data = myobj)

print(x.text)
