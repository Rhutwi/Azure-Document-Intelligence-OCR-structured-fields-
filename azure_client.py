import os
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential

def get_client():
    ep = os.environ["AZURE_DI_ENDPOINT"]
    key = os.environ["AZURE_DI_KEY"]
    return DocumentIntelligenceClient(ep, AzureKeyCredential(key))

def analyze_prebuilt(client, path):
    with open(path, "rb") as f:
        poller = client.begin_analyze_document("prebuilt-layout", body=f)
    return poller.result()

def analyze_custom(client, model_id, path):
    with open(path, "rb") as f:
        poller = client.begin_analyze_document(model_id, body=f)
    return poller.result()
