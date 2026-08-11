import os
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient


# Configuration

STORAGE_ACCOUNT_NAME = os.environ.get(
    "AZURE_STORAGE_ACCOUNT",
    "dcopsof4ynfphpeqny"
)

CONTAINER_NAME = os.environ.get(
    "AZURE_STORAGE_CONTAINER",
    "raw"
)

LOCAL_FILE = Path(
    os.environ.get(
        "TELEMETRY_FILE",
        "telemetry_generator/data/generated/telemetry_data.json"
    )
)

BLOB_NAME = os.environ.get(
    "AZURE_BLOB_NAME",
    "telemetry/telemetry_data.json"
)


# Upload telemetry data to ADLS Gen2

def upload_to_adls():
    """Upload the generated telemetry JSON file to ADLS Gen2."""

    if not LOCAL_FILE.exists():
        raise FileNotFoundError(
            f"Telemetry file not found: {LOCAL_FILE}"
        )

    account_url = (
        f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
    )

    print("Connecting to Azure Storage...")
    print(f"Storage account : {STORAGE_ACCOUNT_NAME}")
    print(f"Container       : {CONTAINER_NAME}")
    print(f"Local file      : {LOCAL_FILE}")
    print(f"Blob path       : {BLOB_NAME}")

    # Uses Azure Entra ID / OIDC credentials.
    # No storage account key is required.
    credential = DefaultAzureCredential()

    blob_service_client = BlobServiceClient(
        account_url=account_url,
        credential=credential
    )

    container_client = blob_service_client.get_container_client(
        CONTAINER_NAME
    )

    print("Uploading telemetry data...")

    with LOCAL_FILE.open("rb") as data:
        container_client.upload_blob(
            name=BLOB_NAME,
            data=data,
            overwrite=True
        )

    print("Upload successful.")
    print(
        f"ADLS path: "
        f"abfss://{CONTAINER_NAME}@"
        f"{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net/"
        f"{BLOB_NAME}"
    )


# Main

if __name__ == "__main__":
    upload_to_adls()