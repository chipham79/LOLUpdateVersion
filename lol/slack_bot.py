from ast import parse
import requests

def sendMessageToSlack(message: str):
    "Send a message to our Slack"
    payload = '{"text": "%s"}' % message
    response = requests.post(
        #First create a app ( https://api.slack.com/apps )
        #Generate Webhook URLs -> Copy this link url
        'https://hooks.slack.com/services/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',
        data=payload
    )

    print(response.text)


def main(message_text: str):
    """ Main function where we can build our logic"""
    sendMessageToSlack(message_text)

#Termial: python {filename} -m "{message}" -> Example: python slack_bot.py -m "OMG"
if __name__ == '__main__':
    import argparse
    parse = argparse.ArgumentParser(description='Send message')
    parse.add_argument('--message', '-m', type=str, default='')
    args = parse.parse_args()

    msg = args.message

    if(len(msg)) == 0:
        print("Give me a message!")
    else:
        main(message_text = msg)

