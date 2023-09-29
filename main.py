
##Created By:Ayat Khrisat
##Email: v-akhrisat@microsoft.com
import os
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError
import azure.cognitiveservices.speech as speechsdk

speech_key = os.environ.get('speach_key')
region=os.environ.get('region')
translation_key=os.environ.get("translation_key")
translation_endpoint=os.environ.get('translation_endpoint')

def speech_recognize_once_from_mic(input_language):

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)

    auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
        languages=[input_language])
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,auto_detect_source_language_config=auto_detect_source_language_config)


    result = speech_recognizer.recognize_once()
    input=''
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        input=result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    return input

def get_text_translation_auto(input,output_language):
    credential = TranslatorCredential(translation_key, region)
    text_translator = TextTranslationClient(endpoint=translation_endpoint, credential=credential)
    result=''

    try:
        target_languages = [output_language]
        input_text_elements = [ InputTextItem(text = input) ]

        response = text_translator.translate(content = input_text_elements, to = target_languages)
        translation = response[0] if response else None

        if translation:
            detected_language = translation.detected_language
            if detected_language:
                print(f"Detected languages of the input text: {detected_language.language} with score: {detected_language.score}.")
            for translated_text in translation.translations:
                result=result+' '+translated_text.text
                print(f"Text was translated to: '{translated_text.to}' and the result is: '{translated_text.text}'.")

    except HttpResponseError as exception:
        if exception.error is not None:
            print(f"Error Code: {exception.error.code}")
            print(f"Message: {exception.error.message}")
        raise
    return result

def speak(text,language):

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)
    speech_config.speech_synthesis_language = language
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    result = speech_synthesizer.speak_text_async(text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to speaker for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

if __name__ == '__main__':

    print("select the input language:\n")
    input_language =str(input())
    print("select the output language:\n")
    output_language = str(input())
    print("start speaking we are listening....")
    text=speech_recognize_once_from_mic(input_language)
    translated_text=get_text_translation_auto(text,output_language)
    speak(translated_text,output_language)


