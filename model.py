from transformers import pipeline

class Translator:
    def __init__(self):
        # loading the model
        self.model = pipeline("translation_en_to_fr", model = "t5-small")
    
    def translate(self, text: str) -> str:
        # Run inference
        model_output = self.model(text)

        # Post-process output to return only the tranlation text
        translation = model_output[0]["translation_text"]

        return translation

translator = Translator()

translation = translator.translate("Hello Rufino, How are you?")
print(translation)