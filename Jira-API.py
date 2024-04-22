## pip install pip install azure-storage-blob==2.1.0
## pip install requests
## pip install pandas

from azure.storage.blob import (BlockBlobService)
import pandas as pd
import requests
import base64

token = ""

try:

    headers = { "Authorization": "Basic " + token }

    projects = requests.get("https://khipo.atlassian.net/rest/api/3/project", headers=headers)

    print(projects.json())
    
    # df.to_json("C:\\...\\source\\repos\\ESPM-Khipo\\ESPM-Khipo-Martech\\Jira-API-Data.json")
    
    # accountName = "khipoespm"
    # accountKey = ""
    # containerName = "khipo-espm"

    # blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

    # blobService.create_blob_from_text('khipo-espm', 'my-jira-projects.csv', df.to_csv(index=False))

except Exception as ex:
    print('Exception:')
    print(ex)
