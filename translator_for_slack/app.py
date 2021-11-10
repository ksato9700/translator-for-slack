import os
import logging

from .deepl_client import Translator as DLTranslator
from .google_client import Translator as GGTranslator
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.web.client import WebClient

logging.basicConfig(level=logging.INFO)

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN_TRANSLATOR"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET_TRANSLATOR"),
)

dl_translator = DLTranslator()
gg_translator = GGTranslator()

RACTION_LANGUAGE_MAPPING = {
    "jp": ("JA", "🇯🇵 "),
    "us": ("EN-US", "🇺🇸 "),
    "flag-vn": ("vi", "🇻🇳 "),
}


@app.event("reaction_added")
def reactions_get(event: dict, client: WebClient, message):
    # print(event)
    if event["item"]["type"] != "message":
        return
    reaction = event["reaction"]
    try:
        target_lang, flag = RACTION_LANGUAGE_MAPPING[reaction]
    except KeyError:
        # print(f"reaction {reaction} is not supported")
        return

    item = event["item"]
    channel = item["channel"]
    replies = client.conversations_replies(channel=channel, ts=item["ts"])
    # print(replies)
    message = replies["messages"][0]
    text = message["text"]
    ts = message.get("thread_ts", message["ts"])

    source_lang = gg_translator.detect_language(text)

    if dl_translator.is_supported_source_language(
        source_lang
    ) and dl_translator.is_supported_target_language(target_lang):
        translator = dl_translator
    else:
        translator = gg_translator
        target_lang = target_lang[:2].lower()

    translated = translator.translate_text(text, target_lang)
    logging.info(f"{translator.__class__}: {translated}")
    client.chat_postMessage(text=flag + translated, channel=channel, thread_ts=ts)


if __name__ == "__main__":
    # SocketModeHandler(app, os.environ["SLACK_APP_TOKEN_TRANSLATOR"]).start()
    app.start(port=int(os.environ.get("PORT", 3000)))
