@description('Name prefix for the Data Center storage account.')
param storagePrefix string = 'dcops'

@description('Azure region for the storage account.')
param location string = resourceGroup().location

var storageAccountName = toLower('${storagePrefix}${uniqueString(resourceGroup().id)}')

resource storageAccount 'Microsoft.Storage/storageAccounts@2025-06-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true
    supportsHttpsTrafficOnly: true
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
    accessTier: 'Hot'
  }
}

resource rawContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2025-06-01' = {
  name: '${storageAccount.name}/default/raw'
  properties: {
    publicAccess: 'None'
  }
}

resource bronzeContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2025-06-01' = {
  name: '${storageAccount.name}/default/bronze'
  properties: {
    publicAccess: 'None'
  }
}

resource silverContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2025-06-01' = {
  name: '${storageAccount.name}/default/silver'
  properties: {
    publicAccess: 'None'
  }
}

resource goldContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2025-06-01' = {
  name: '${storageAccount.name}/default/gold'
  properties: {
    publicAccess: 'None'
  }
}

output storageAccountName string = storageAccount.name
output storageAccountId string = storageAccount.id
output dfsEndpoint string = storageAccount.properties.primaryEndpoints.dfs
