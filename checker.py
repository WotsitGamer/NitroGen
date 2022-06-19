import requests
import time
import discord_webhook
import numpy
import string
import os
valid = []  # Keep track of valid codes
chars = []
chars[:0] = string.ascii_letters + string.digits
num = 1 
def InternetCheck():
    try:
        url = "https://github.com"
        response = requests.get(url)  # Get the response from the url
        print("Internet check")
        time.sleep(.4)
        webhook = "https://discord.com/api/webhooks/984872564579000410/C9agqQflBG_NnHIC9MoI-jtXJSeGBiYannAo-xYOepkSxHt8QHzMQDEPlgq96ybXrTxa"
        discord_webhook.DiscordWebhook(  # Let the user know it has started logging the ids
                        url=webhook,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                    ).execute()
        return webhook
    except requests.exceptions.ConnectionError:
        # Tell the user
        input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
        exit()  # Exit program
def quickChecker(nitro:str, notify=None):  # Used to check a single code at a time
        # Generate the request url
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        if notify is not None:  # If a webhook has been added
                discord_webhook.DiscordWebhook(  # Send the message to discord letting the user know there has been a valid nitro code
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

                return True  # Tell the main function the code was found

        # If the responce got ignored or is invalid ( such as a 404 or 405 )
        else:
            # Tell the user it tested a code and it was invalid
            print(f" Invalid | {nitro} \n", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  # Tell the main function there was not a code found
def Check(webhook, invalid):
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  # Loop over the amount of codes to check
                try:
                    code = ''.join(x for x in s)
                    url = f"https://discord.gift/{code}"  # Generate the url

                    result = quickChecker(url, webhook)  # Check the codes

                    if result:  # If the code was valid
                        # Add that code to the list of found codes
                        valid.append(url)
                        with open("nitro.txt", "a") as f:
                            f.write(f"Valid Nito Code detected! {url}")
                    else:  # If the code was not valid
                        with open("invalid.txt", "w") as f:
                            f.write(f"Ivalid | {url} | \n")
                        invalid += 1  # Increase the invalid counter by one
                except KeyboardInterrupt:
                    # If the user interrupted the program
                    print("\nInterrupted by user")
                    exit()  # Break the loop

                except Exception as e:  # If the request fails
                    print(f" Error | {e} ")  # Tell the user an error occurred
        return url
def main():
    invalid = 0 
    webhook = InternetCheck()
    while True:
        Check(webhook, invalid)
if __name__ == "__main__":
    main()
