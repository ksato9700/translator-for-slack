import pytest

from translator_for_slack.deepl_client import Translator


@pytest.fixture()
def translator() -> Translator:
    return Translator()


def test_translate_text(translator: Translator):
    assert translator.translate_text("こんにちは", "EN-US") == "Hello. - Hello."
    assert translator.translate_text("goodbye", "JA") == "グッドバイ"


def test_get_usage(translator: Translator):
    character_detail = translator.get_usage()
    assert character_detail.valid
    assert character_detail.limit == 2200000
    assert character_detail.count < 2200000


def test_is_supported_language(translator: Translator):
    assert translator.is_supported_source_language("EN")
    assert translator.is_supported_source_language("en")
    assert translator.is_supported_source_language("JA")
    assert translator.is_supported_source_language("ja")
    assert not translator.is_supported_source_language("vi")
    assert not translator.is_supported_source_language("th")
    assert translator.is_supported_target_language("EN-US")
    assert translator.is_supported_target_language("JA")
    assert not translator.is_supported_target_language("vi")
    assert not translator.is_supported_target_language("th")
