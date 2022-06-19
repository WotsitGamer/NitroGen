import grequests
import time
import checker
import discord_webhook
import os
invalidcodes = 0
start_time = time.time()
# Create a 10000 requests
url = "https://discord.com/api/webhooks/984872564579000410/C9agqQflBG_NnHIC9MoI-jtXJSeGBiYannAo-xYOepkSxHt8QHzMQDEPlgq96ybXrTxa"
urls = []
discord_webhook.DiscordWebhook(  # Let the user know it has started logging the ids
                        url=url,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                    ).execute()
for i in range(1000):
    nitro = checker.Check(webhook="https://discord.com/api/webhooks/984872564579000410/C9agqQflBG_NnHIC9MoI-jtXJSeGBiYannAo-xYOepkSxHt8QHzMQDEPlgq96ybXrTxa", invalid=invalidcodes)
    urls.append(nitro)
rs = (grequests.head(u) for u in urls)
# Send them.
res = grequests.map(rs)
if res.status_code == 200:  # If the responce went through
            # Notify the user the code was valid
            print(f" Valid | {nitro} \n", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:  # Open file to write
                # Write the nitro code to the file it will automatically add a newline
                file.write(nitro)

            if url is not None:  # If a webhook has been added
                discord_webhook.DiscordWebhook(  # Send the message to discord letting the user know there has been a valid nitro code
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()
print(res)

print (time.time() - start_time) # Result was: 9.66666889191