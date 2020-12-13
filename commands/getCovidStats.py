
from app import app, get_country_info


@app.command("/covid")
def command_tip(ack, say, body, command, logger, client):
    ack()
    country_info = get_country_info(command['text'])
    if country_info == False:
        say("Invalid Country")
    else:
        block = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{country_info['country']} :flag-{country_info['country_code']}:"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": "Confirmed Cases"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{country_info['latest']['confirmed']}*"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": "Deaths"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{country_info['latest']['deaths']}*"
                }
            }
        ]

        print(f"United States:\n{get_country_info(command['text'])}\n")

        # say() sends a message to the channel where the event was triggered
        #say(f"*Country*: {country_info['country']}\n*Confirmed Cases:* {country_info['latest']['confirmed']}\n*Deaths:* {country_info['latest']['deaths']}")
        client.chat_postMessage(channel=command['channel_id'], blocks = block)
