from storages.backends.azure_storage import AzureStorage
import os

AZURE_ACCOUNT_NAME = os.getenv('AZ_STORAGE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.getenv('AZ_STORAGE_KEY')


class AzureMediaStorage(AzureStorage):
    # Must be replaced by your <storage_account_name>
    account_name = AZURE_ACCOUNT_NAME
    account_key = AZURE_ACCOUNT_KEY  # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = AZURE_ACCOUNT_NAME  # Must be replaced by your storage_account_name
    account_key = AZURE_ACCOUNT_KEY  # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
