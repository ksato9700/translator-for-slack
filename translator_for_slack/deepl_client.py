import os

import deepl


class Translator:
    def __init__(self):
        self.translator = deepl.Translator(os.environ["DEEPL_AUTH_TOKEN"])
        self.supported_source_languages = [
            lang.code for lang in self.translator.get_source_languages()
        ]
        self.supported_target_languages = [
            lang.code for lang in self.translator.get_target_languages()
        ]
        # print(f"{self.supported_source_languages=}")
        # print(f"{self.supported_target_languages=}")

    def translate_text(self, text: str, target_lang: str) -> str:
        result = self.translator.translate_text(text, target_lang=target_lang)
        # print(result.detected_source_lang)
        return result.text

    def get_usage(self):
        return self.translator.get_usage().character

    def is_supported_source_language(self, code: str) -> bool:
        return code.upper() in self.supported_source_languages

    def is_supported_target_language(self, code: str) -> bool:
        return code.upper() in self.supported_target_languages


if __name__ == "__main__":
    # translator = Translator()
    pass
