import pytest

from translator_for_slack.google_client import Translator


@pytest.fixture()
def translator() -> Translator:
    return Translator()


def test_translate_text(translator: Translator):
    assert translator.translate_text("こんにちは", "en") == "Hello"
    assert translator.translate_text("こんにちは", "vi") == "Xin chào"
    assert translator.translate_text("こんにちは", "th") == "สวัสดี"
    assert translator.translate_text("goodbye", "ja") == "さようなら"
    assert translator.translate_text("goodbye", "vi") == "tạm biệt"
    assert translator.translate_text("goodbye", "th") == "ลาก่อน"


def test_is_supported_language(translator: Translator):
    assert translator.is_supported_language("en")
    assert translator.is_supported_language("ja")
    assert translator.is_supported_language("vi")
    assert translator.is_supported_language("th")
    assert not translator.is_supported_language("EN-US")
    assert not translator.is_supported_language("JA")


def test_detect_language(translator: Translator):
    assert translator.detect_language("こんにちは") == "ja"
    assert translator.detect_language("goodbye") == "en"
    assert translator.detect_language("Tạm biệt") == "vi"
    assert translator.detect_language("สวัสดี") == "th"
