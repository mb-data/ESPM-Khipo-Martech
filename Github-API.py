## pip install pip install azure-storage-blob==2.1.0
## pip install requests
## pip install pandas

from azure.storage.blob import (BlockBlobService)
import pandas as pd
import requests
import base64

token = "" # SEU TOKEN AQUI

try:

    headers = { "Accept": "application/vnd.github+json", 
               "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": "Bearer " + token }

    response = requests.get("https://api.github.com/repos/mb-data/BaurFrontComercial/commits", headers=headers)

    print(response.json())

    df = pd.json_normalize(response.json(), max_level=0)

    print(df.head())
    
    # accountName = "khipoespm"
    # accountKey = "OSjJx/Gz+L0jFu0mG3pBJouT543Yg9+IhrByAZc0N0uLNZfURLTfFphxfSrV/gcb7Gaqb89Op+0T+AStRnFVOg=="
    # containerName = "khipo-espm"

    # blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

    # blobService.create_blob_from_text('khipo-espm', 'my-jira-projects.csv', df.to_csv(index=False))

except Exception as ex:
    print('Exception:')
    print(ex)
