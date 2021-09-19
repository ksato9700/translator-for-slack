import os
import deepl


class Translator:
    def __init__(self):
        self.translator = deepl.Translator(os.environ["DEEPL_AUTH_TOKEN"])

    def translate_text(self, text: str, target_lang: str) -> str:
        result = self.translator.translate_text(text, target_lang=target_lang)
        return result.text

    def get_usage(self):
        return self.translator.get_usage().character

    def get_supported_languages(self) -> list[str]:
        return [lang.code for lang in self.translator.get_target_languages()]


if __name__ == "__main__":
    pass
