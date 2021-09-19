from google.cloud import translate_v2 as translate


class Translator:
    def __init__(self):
        self.translator = translate.Client()
        self.supported_languages = [
            lang["language"] for lang in self.translator.get_languages()
        ]

    def translate_text(self, text: str, target_lang: str) -> str:
        result = self.translator.translate(text, target_language=target_lang)
        return result["translatedText"]

    def get_usage(self):
        # Not supported yet
        return None

    def is_supported_language(self, code: str) -> bool:
        return code in self.supported_languages

    def detect_language(self, text: str) -> str:
        result = self.translator.detect_language(text)
        return result["language"]


if __name__ == "__main__":
    translator = Translator()
    print(translator.translate_text("こんにちは", "en"))
