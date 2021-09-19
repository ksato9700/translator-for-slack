import os

from .deepl_client import Translator as DLTranslator
from .google_client import Translator as GGTranslator
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.web.client import WebClient

# from slack_sdk.errors import SlackApiError

app = App(token=os.environ.get("SLACK_BOT_TOKEN_TRANSLATOR"))

dl_translator = DLTranslator()
gg_translator = GGTranslator()

RACTION_TRANSLATOR_MAPPING = {
    "jp": (dl_translator, "JA", "🇯🇵 "),
    "us": (dl_translator, "EN-US", "🇺🇸 "),
    "flag-vn": (gg_translator, "vi", "🇻🇳 "),
}


@app.event("reaction_added")
def reactions_get(event: dict, client: WebClient, message):
    # print(event)
    if event["item"]["type"] != "message":
        return
    reaction = event["reaction"]
    try:
        translator, lang, flag = RACTION_TRANSLATOR_MAPPING[reaction]
    except KeyError:
        # print(f"reaction {reaction} is not supported")
        return

    item = event["item"]
    channel = item["channel"]
    replies = client.conversations_replies(channel=channel, ts=item["ts"])

    message = replies["messages"][0]
    text = message["text"]
    ts = message.get("thread_ts", message["ts"])

    translated = translator.translate_text(text, lang)
    print(translated)
    # say(flag + translated)
    client.chat_postMessage(text=flag + translated, channel=channel, thread_ts=ts)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN_TRANSLATOR"]).start()
