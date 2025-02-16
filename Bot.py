from pyrogram import Client, filters

# Replace with your bot token
API_ID = 26312191
API_HASH = '83fe20a435dbf635b67fc0ee3019a419'
BOT_TOKEN = '7619930306:AAFVZuAhDVM_8cXHsjpTUH_MnyLuZl-LE_8'
app = Client("Jinwoo", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.text)
def reply(client, message):
    message.reply_text("Hello, World!")

if __name__ == "__main__":
    app.run()
