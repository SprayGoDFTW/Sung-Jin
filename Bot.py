from pyrogram import Client, filters
import random

# Replace with your bot token
API_ID = 26312191
API_HASH = '83fe20a435dbf635b67fc0ee3019a419'
BOT_TOKEN = '7619930306:AAFVZuAhDVM_8cXHsjpTUH_MnyLuZl-LE_8'
app = Client("Jinwoo", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# List of 100+ random messages
messages = [
    "Ye Eren keh raha apki ma ka bhosda kaala hai true baat hai kya bro?",
    "Aaj kuch zyada hi acha lag raha hai, kya scene hai?",
    "Yeh to kaafi weird tha, aapko laga nahi!",
    "Aapko pata hai ki kal kya hone wala hai?",
    "Kya tum bhi mere jaise ho? Bas thoda alag",
    "Yeh joke samajh paaye toh aapki soch bhi level up ho gayi",
    "Main toh keh raha hoon bas chill maaro",
    "Kya scene hai, aaj ka din kaisa gaya?",
    "Mujhe lagta hai apni soch badalni padegi!",
    "Kal ka plan kya hai? Mai soch raha hoon kuch alag karne ka",
    "Mujhe yeh lagta hai ki sab kuch sort ho jayega",
    "Chill karo, sab kuch sahi ho jayega",
    "Aaj toh kuch alag hi vibe thi!",
    "Yeh kiski baat kar rahe ho? Main samajh nahi paaya",
    "Agar aap samajh gaye toh aap ek step aage ho!",
    "Mujhe lagta hai apne decision se sab kuch badal sakta hai",
    "Jab tak aap khud ko samajh nahi paate, tab tak yeh sab confusion rahega",
    "Kya tumne yeh dekha? Mein toh shock ho gaya",
    "Yeh sochne ka tareeka bhi ajeeb hai, samjha karo!",
    "Kabhi socha hai ki zindagi ka asli maza kya hai?",
    "Chalo koi nahi, sab thik ho jayega",
    "Aaj ka din kaafi exciting raha!",
    "Kya lagta hai tumhe, sab kuch thik ho jayega ya nahi?",
    "Yeh zindagi ka game hai, aap har waqt level up kar rahe ho!",
    "Kahani ka plot twist abhi baaki hai!",
    "Mujhe lagta hai sab kuch randomly hota hai, bas samajhne ki der hai",
    "Aapne kabhi apne dreams ke bare mein socha?",
    "Zindagi mein kuch ajeeb ho raha hai aajkal, kya lagta hai?",
    "Mujhe lagta hai humare dimaag ki speed bhi kuch zyada hi fast ho gayi hai",
    "Aaj kuch seekhne ko mila, kaafi interesting tha",
    "Kuch bhi ho, main apni soch ko nahi badalunga",
    "Aapko kabhi laga hai ki duniya kuch zyada hi complex hai?",
    "Mujhe toh lagta hai kuch zyada hi intense ho raha hai",
    "Yeh jo log hote hain, samajh nahi aata unka kya scene hai",
    "Zindagi ka koi purpose hona chahiye, aapke kya thoughts hain?",
    "Dosto ke saath waqt guzarna zindagi ka sabse accha hissa hai",
    "Agar kuch karna hai toh abhi karlo, time ka pataa nahi",
    "Aap jab apni soch badalte ho, tab sab kuch alag lagne lagta hai",
    "Zindagi mein sab kuch time par hi hota hai",
    "Kabhi socha hai ki aap kis direction mein ja rahe ho?",
    "Kya tumhare paas apna time hai ya duniya tumhe time de rahi hai?",
    "Agar kuch chhupana hai toh duniya ko pata chalne do",
    "Mujhe laga tha ki aaj ka din kaafi boring hoga, par sab badal gaya",
    "Aapko lagta hai sab kuch random hai ya iske peeche koi logic hai?",
    "Aaj ka mood kaisa hai? Kuch crazy hone wala hai",
    "Jab aap kaam karte ho, toh zindagi apne aap smooth ho jaati hai",
    "Aapke liye kis cheez ka time hai abhi?",
    "Zindagi ke maze kabhi kabhi bahut ajeeb lagte hain",
    "Aaj kuch naya seekhne ka mann ho raha hai",
    "Kya tumne yeh dekha? Bahut hi interesting tha",
    "Aapke paas kuch ideas hain jo aap share karna chahenge?",
    "Zindagi ka ultimate secret kya hai, aapko kya lagta hai?",
    "Agar aapko kuch seekhna ho, toh sabse pehle apne aapko samajhna hoga",
    "Aapko kabhi laga hai ki aap apni soch mein fas gaye hain?",
    "Mujhe lagta hai aaj ka din pura concentrate karne ka hai",
    "Zindagi ke baare mein ek baat samajh lo: sab kuch apne time pe hota hai",
    "Aaj kuch zyada hi mind-blowing ho gaya!",
    "Kya aap apni life ke plan ke saath satisfied ho?",
    "Zindagi mein agar confusion hai, toh uska solution time hi dega",
    "Aap kis cheez se motivated hote ho?",
    "Aaj kal sab kuch fast ho gaya hai, aapke thoughts kaise hain?",
    "Kya aapne apne dreams ko follow karna start kiya hai?",
    "Sab kuch apni thinking pe depend karta hai",
    "Aapko kabhi laga hai ki apna kaam alag tarike se karna chahiye?",
    "Yeh jo life ka twist hai, samajhna thoda mushkil ho raha hai",
    "Apne emotions ko samajhna bohot zaroori hai",
    "Kya tumhare paas time hai apne ideas ko explore karne ka?",
    "Agar aap ko aaj kuch seekhna ho toh apne aapko samajh lo"
]

@app.on_message(filters.text)
def handle_message(client, message):
    random_message = random.choice(messages)
    message.reply_text(random_message)

if __name__ == "__main__":
    app.run()
