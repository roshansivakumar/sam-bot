# -*- coding: utf-8 -*-
import os
from twilio.rest import Client


# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC0fad4f27553c4f7abc30b1aad8e059e0"
auth_token = "a3d3d8bda1ab11d1c40263b1f4cd9162"

# texts defined

firstMsg="YO Sammy! You keep invading my thougts, aliens do exist. This is an automated bot programmed by My smart ass, set to send 2 weeks after we talked (might get delayed). Type “POOP” (in caps without the quotation) to see the next one. There’s 3 more after this, so send POOP after Each one. It's an approach for you to READ at your own convenience. Dw i'm disconencted from your interaction with this. You'll incur Mr. Poop's (the bots name) wrath *shivers* with a wrong reply. Before you Type “POOP” lets start with something fun, type “PLANTKILLER” to invoke a dad joke bot xD. \n\nI feel like i'm inching toward one of those wacko 'Doom Patrol' peeps, THE MOST UNPREDICTABLE, INSANE SUPERHERO SHOW, you so gotta watch it."

firstMsgV2="YO Sammy! I'm Mr.Poop, a bot designed by that persistant ass. *Sobbing* He left me alone for 10 days on the lonely web, made me go onto your phone on the 17th instead of 7th. Type “POOP” (in caps without the quotation) to start seeing whatver Roshan wanted you to see. There’s 3 more after this, so send POOP after Each one. Apparently it's an approach for you to READ at your own convenience, I reckon he just misses you and it's an excuse to send something to ya. Dw he's totally disconencted from your interaction with moi. Watch out tho, with a wrong response you'll incur my wrath *Evil laughter*. Before you Type “POOP” lets start with something fun, type “PLANTKILLER” to invoke my dad joke function xD." 
#\n\nNote from Roshan : Feel like i'm inching toward one of those wacko 'Doom Patrol' peeps, THE MOST UNPREDICTABLE, INSANE SUPERHERO SHOW, you so gotta watch it.

client = Client(account_sid, auth_token)

message = client.messages.create(
  body=firstMsgV2,
  from_="+16693381260",
  to="+12165437808"
)

print(message.sid)



