import pytest
from tfs.google_client import Translator


@pytest.fixture()
def translator() -> Translator:
    return Translator()


def test_translate_text(translator: Translator):
    assert translator.translate_text("こんにちは", "en") == "Hello"
    assert translator.translate_text("こんにちは", "vi") == "xin chào"
    assert translator.translate_text("goodbye", "ja") == "さようなら"
    assert translator.translate_text("goodbye", "vi") == "Tạm biệt"


def test_is_supported_language(translator: Translator):
    assert translator.is_supported_language("en")
    assert translator.is_supported_language("ja")
    assert translator.is_supported_language("vi")
    assert not translator.is_supported_language("EN-US")
    assert not translator.is_supported_language("JA")


def test_detect_language(translator: Translator):
    assert translator.detect_language("こんにちは") == "ja"
    assert translator.detect_language("goodbye") == "en"
    assert translator.detect_language("Tạm biệt") == "vi"
