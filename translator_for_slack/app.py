import logging
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.web.client import WebClient

from .deepl_client import Translator as DLTranslator
from .google_client import Translator as GGTranslator

logging.basicConfig(level=logging.INFO)

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN_TRANSLATOR"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET_TRANSLATOR"),
)

dl_translator = DLTranslator()
gg_translator = GGTranslator()

REACTION_LANGUAGE_MAPPING = {
    "to_japanese": ("JA", "🇯🇵 "),
    "to_english": ("EN-US", "🇺🇸 "),
    "to_vietnamese": ("vi", "🇻🇳 "),
    "to_thai": ("th", "🇹🇭"),
}


def get_reaction_count(reaction: str, reactions: list[object]):
    for r in reactions:
        if r["name"] == reaction:
            return r["count"]
    return 0


@app.event("reaction_added")
def reactions_get(event: dict, client: WebClient, message):
    # print(event)
    if event["item"]["type"] != "message":
        return
    reaction = event["reaction"]
    try:
        target_lang, flag = REACTION_LANGUAGE_MAPPING[reaction]
    except KeyError:
        # print(f"reaction {reaction} is not supported")
        return

    item = event["item"]
    channel = item["channel"]
    replies = client.conversations_replies(channel=channel, ts=item["ts"])
    # print(replies)
    message = replies["messages"][0]
    if get_reaction_count(reaction, message["reactions"]) != 1:
        return
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
    if os.environ.get("TRANSLATOR_SOCKET_MODE"):
        SocketModeHandler(app, os.environ["SLACK_APP_TOKEN_TRANSLATOR"]).start()
    else:
        app.start(port=int(os.environ.get("PORT", 3000)))
