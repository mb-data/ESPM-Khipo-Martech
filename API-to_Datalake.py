## pip install pip install azure-storage-blob==2.1.0
## pip install requests
## pip install pandas

from azure.storage.blob import (BlockBlobService)
import pandas as pd
import requests

try:
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

    df = pd.json_normalize(response.json())

    accountName = "khipoespm"
    accountKey = "OSjJx/Gz+L0jFu0mG3pBJouT543Yg9+IhrByAZc0N0uLNZfURLTfFphxfSrV/gcb7Gaqb89Op+0T+AStRnFVOg=="
    containerName = "khipo-espm"

    blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

    blobService.create_blob_from_text('khipo-espm', 'my_output.csv', df.to_csv(index=False))

except Exception as ex:
    print('Exception:')
    print(ex)
