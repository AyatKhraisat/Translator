# Translator

This Sample convert spoken Audio from selected language, speach from other language, it uses the following AI servcies from Azure:

1.[Azure Speach](https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/?view=azure-python)
2. [Azure Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/)
```mermaid
graph LR
A[Speach to Text] -->B[Tranlsate Text] -->C[Text to Speach] 

```

## Quick Start

1. Azure subscription -  [Create one for free](https://azure.microsoft.com/free/cognitive-services).
2. You can create  ALL in One service to  enable access to multiple Azure AI services using a single API key and endpoint.
or you can create separate Speach And Translator Services 

	-[Create All in one AI Service](https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesAllInOne) 
	-[ Create Speach Service](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices)
	-[Create Text Translation](https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesTextTranslation)

3. add your API keys,region and endpoints to the Env Variables 
4. run the code 
5. select one of the languages for input and output [Language support - Speech service - Azure AI services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)
6. Enjoy!