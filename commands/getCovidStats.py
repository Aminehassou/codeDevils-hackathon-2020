
from app import app, get_country_info, create_plot, os
from slack.errors import SlackApiError


@app.command("/covid")
def command_tip(ack, say, body, command, logger, client):
    ack()
    plot_command = "GRAPH"
    if plot_command in command['text'].upper():
        command_text = command['text'].rsplit(' ', 1)

    else:
        command_text = [command['text']]

    country_info = get_country_info(command_text[0])
        
    if country_info == False:
        say("Invalid Country")

    elif command_text[-1].upper() == plot_command:
        file_name = country_info["country"]
        create_plot(country_info["timelines"]["confirmed"]["timeline"], file_name)
        try:
            result = client.files_upload(
                channels=command['channel_id'],
                initial_comment=f"Graph of confirmed cases in {file_name}",
                file=f"{file_name}.png",
            )
            logger.info(result)

        except SlackApiError as e:
            logger.error("Error uploading file: {}".format(e))
        os.remove(f"{file_name}.png")
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

        client.chat_postMessage(channel=command['channel_id'], blocks = block)
