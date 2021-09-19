import pytest
from tfs.deepl_client import Translator


@pytest.fixture()
def translator() -> Translator:
    return Translator()


def test_translate_text(translator: Translator):
    assert translator.translate_text("こんにちは", "EN-US") == "Hello."
    assert translator.translate_text("goodbye", "JA") == "さよなら"


def test_get_usage(translator: Translator):
    charactor_detail = translator.get_usage()
    assert charactor_detail.valid
    assert charactor_detail.limit == 500000
    assert charactor_detail.count < 500000


def test_is_supported_language(translator: Translator):
    assert translator.is_supported_source_language("EN")
    assert translator.is_supported_source_language("en")
    assert translator.is_supported_source_language("JA")
    assert translator.is_supported_source_language("ja")
    assert not translator.is_supported_source_language("vi")
    assert translator.is_supported_target_language("EN-US")
    assert translator.is_supported_target_language("JA")
    assert not translator.is_supported_target_language("vi")
