# Translator for Slack
This is a Slack application to translate Slack messages using DeepL and Google Translate

## Configuration
### Slack
 - Create a new App (https://api.slack.com/apps/new)
 - Settings
  - Go to "Basic Information" -> "Display Information"
    - Set the icon, short description and color
  - Go to "OAuth & Permissions" -> "Scopes"
    - Add `channels:history`, `chat:write`, `groups:history` and `reactions:read` to "Bot Token Scopes"
    - Click "Install to Workspace" and set he "Bot User OAuth Token" (`xoxb-...`) to `SLACK_BOT_TOKEN_TRANSLATOR` environment variable.
  - Go to "Event Subscriptions"
    - Enable Events
    - Add `reaction_added` to "Subscribe to bot events"

#### For local testing
  - Go to "Socket Mode"
    - Enable Socket Mode
    - Set the "App-Level Token" (`x-app...`) to `SLACK_APP_TOKEN_TRANSLATOR` environment variable.
    - Set `TRANSLATOR_SOCKET_MODE` environment variable.

#### For deployment
  - Go to "Socket Mode"
    - Disable Socket Mode
  - Go to Enable Events
    - Set "Request URL" to "<service-url>/slack/events"

  - Go to "Basic Information" -> "App Credentials"
    - Set the value of "Signing Secret" to `SLACK_SIGNING_SECRET_TRANSLATOR` environment variable.


### DeepL
 - Set your DeepL Authentication Key to `DEEPL_AUTH_TOKEN`

### Google Translation
 - Enable Google Translate API at your project
 - Set the path of the credential JSON file to `GOOGLE_APPLICATION_CREDENTIALS` environment variable

## Execution
### local environment
```sh
poetry install
poetry run python -m translator_for_slack.app
```
