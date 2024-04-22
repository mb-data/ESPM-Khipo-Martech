## pip install pip install azure-storage-blob==2.1.0
## pip install requests
## pip install pandas

from azure.storage.blob import (BlockBlobService)
import pandas as pd
import requests
import base64

token = ""

try:

    headers = { "Accept": "application/vnd.github+json", 
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": "Bearer " + token }
    
    # GET - All repositories

    repos = requests.get("https://api.github.com/orgs/mb-data/repos", headers=headers)

    df_repos = pd.json_normalize(repos.json(), max_level=0)

    df_repos.to_json("C:\\...\\source\\repos\\ESPM-Khipo\\ESPM-Khipo-Martech\\Github-API-Repos.json")

    # GET - All repository commits
    
    commits = requests.get("https://api.github.com/repos/mb-data/ESPM-Khipo-Martech/commits", headers=headers)

    df_commits = pd.json_normalize(commits.json(), max_level=0)

    df_commits['parents'] = df_commits['parents'].to_numpy().flatten()

    df_commits.to_json("C:\\...\\source\\repos\\ESPM-Khipo\\ESPM-Khipo-Martech\\Github-API-Commits.json")

    # GET - All repository Pull-Requests

    pullrequests = requests.get("https://api.github.com/repos/mb-data/ESPM-Khipo-Martech/commits", headers=headers)

    df_pullrequests = pd.json_normalize(pullrequests.json(), max_level=0)

    df_pullrequests.to_json("C:\\...\\source\\repos\\ESPM-Khipo\\ESPM-Khipo-Martech\\Github-API-PRs.json")
    
    # accountName = "khipoespm"
    # accountKey = ""
    # containerName = "khipo-espm"

    # blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

    # blobService.create_blob_from_text('khipo-espm', 'my-jira-projects.csv', df.to_csv(index=False))

except Exception as ex:
    print('Exception:')
    print(ex)
