#!/bin/bash
# set up ocr - should just be run once and may not even be needed since we are running everything through a container 
az cognitiveservices account create -n ocr-jabras -g jabras --kind ComputerVision --location eastus --sku S1

#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services/Computer-vision
#https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/deploy-computer-vision-on-premises
#https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/computer-vision-how-to-install-containers?tabs=version-3-2

