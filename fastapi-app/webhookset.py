import requests

bot_token = "7595651059:AAHh-Gl8IwpQTFumVTyQ8blgg7_dTegugGc"
webhook_url = "https://happy-olives-kiss.loca.lt/webhook"  

response = requests.get(f"https://api.telegram.org/bot{bot_token}/setWebhook?url={webhook_url}")
print(response.json())
