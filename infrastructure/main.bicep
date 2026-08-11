targetScope = 'resourceGroup'

@description('Prefix used for the Data Center storage account name.')
param storagePrefix string = 'dcops'

@description('Prefix used for the Azure Key Vault name.')
param keyVaultPrefix string = 'dcops-kv'

@description('Prefix used for the Azure Databricks workspace name.')
param databricksPrefix string = 'dcops-dbx'

@description('Azure region for the resources.')
param location string = resourceGroup().location

// Naming

var storageAccountName = toLower('${storagePrefix}${uniqueString(resourceGroup().id)}')
var keyVaultName = toLower('${keyVaultPrefix}-${uniqueString(resourceGroup().id)}')

// ADLS Gen2 Storage Account

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

// ADLS Gen2 Containers

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

// Azure Key Vault

resource keyVault 'Microsoft.KeyVault/vaults@2025-05-01' = {
  name: keyVaultName
  location: location

  properties: {
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
    enableSoftDelete: true
    softDeleteRetentionInDays: 7
    publicNetworkAccess: 'Enabled'

    sku: {
      family: 'A'
      name: 'standard'
    }
  }
}

// Azure Databricks Workspace

// ------------------------------------------------------------
// Azure Databricks Serverless Workspace
// ------------------------------------------------------------

var databricksWorkspaceName = toLower(
  '${databricksPrefix}-${uniqueString(resourceGroup().id)}'
)

resource databricksWorkspace 'Microsoft.Databricks/workspaces@2026-01-01' = {
  name: databricksWorkspaceName
  location: location

  sku: {
    name: 'premium'
  }

  properties: {
    computeMode: 'Serverless'
    publicNetworkAccess: 'Enabled'
  }
}

// Outputs

output storageAccountName string = storageAccount.name

output storageAccountId string = storageAccount.id

output dfsEndpoint string = storageAccount.properties.primaryEndpoints.dfs

output keyVaultName string = keyVault.name

output keyVaultId string = keyVault.id

output keyVaultUri string = keyVault.properties.vaultUri

output databricksWorkspaceName string = databricksWorkspace.name

output databricksWorkspaceId string = databricksWorkspace.id

output databricksWorkspaceUrl string = databricksWorkspace.properties.workspaceUrl
