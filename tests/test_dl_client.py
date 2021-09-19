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


def test_supported_languages(translator: Translator):
    assert len(translator.get_supported_languages()) == 26
