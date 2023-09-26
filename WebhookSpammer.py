# Imports
from discord_webhook import DiscordWebhook


# Vars
webhook = input("Webhook: ")
do = 0
stop = False

# User inputs
message = input("Message: ")
time = int(input("How many times ?: "))

# Set message
webhook = DiscordWebhook(url=webhook, content=message)


while not stop:
    do += 1
    response = webhook.execute()
    print("Message Send.")
    if do == time:
        stop = True
