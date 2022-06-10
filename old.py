import requests
import random
while True:
    code = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUIVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(16))
    url = f'https://discord.com/api/v8/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true'
    r = requests.get(url)
    if r.status_code == 404:
        print(f"API RESPONSE: {r.status_code} on url: {url}")
    elif r.status_code == 200:
        print(f"Correct on url {url}")
    else:
        print(f"Probably being rate limited! on url: {url}")
        