# Translator for Slack
This is a Slack application to translate Slack messages using DeepL and Google Translate

## Configuration
### Slack
 - Create a new App (https://api.slack.com/apps）
 - Settings
  - Go to "Basic Information" -> "Display Information"
    - Set the icon, short description and color
  - Go to "OAuth & Permissions" -> "Scopes"
    - Add `channels:history`, `chat:write`, `groups:history` and `reactions:read` scopes.
    - Click "Install to Workspace" and set he "Bot User OAuth Token" (`xoxb-...`) to `SLACK_BOT_TOKEN_TRANSLATOR` environment variable.
  - Go to "Socket Mode"
    - Enable Socket Mode
    - Set the "App-Level Token" (`x-app...`) to `SLACK_APP_TOKEN_TRANSLATOR` environment variable.
  - Go to "Event Subscriptions"
    - Enable Events
    - Add `reaction_added` Bot User Event


## Execution
### local environment
```sh
poetry install
poetry run python -m tfs.app
```