from pyrogram import Client, filters
import random

# Replace with your bot token
API_ID = 26312191
API_HASH = '83fe20a435dbf635b67fc0ee3019a419'
BOT_TOKEN = '7619930306:AAFVZuAhDVM_8cXHsjpTUH_MnyLuZl-LE_8'
app = Client("Jinwoo", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Random response messages
responses = [
    "Ye Eren keh raha apki ma ka bhosda kaala hai true baat hai kya bro?",
    "Eren ka kehna hai apki game kafi risky hai, samajh gya kya?",
    "Yaar, Eren ne bola apki chali hui adhi pichli kismat ab samajh lo!",
    "Bhai, Eren keh raha ki apka attitude aur apke moves dono hi to bekar hai!",
    "Eren ne bola tha, apki soch thodi thandi hai, bro! Aram se samajh!",
    "Eren keh raha ki apne apne dimaag ki hawa nikal di hai!"
]

@app.on_message()
def handle_message(client, message):
    response = random.choice(responses)
    message.reply_text(response)

if __name__ == "__main__":
    app.run()
