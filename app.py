# -*- coding: utf-8 -*-
import os
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

wrongEntry="Follow the darn instructions, it ain’t latin. I can enable BABY PANDA mode if you so wish. Don’t make me lose my faith in you. You can do it!"

intro="Intro : Yknow my on the spot talking needs some workin. The talk pre-holdiays ended with your trademark awkward giggles, hence what I wante-touché (wanted to say) about that, also a feeling of being misunderstood, and thougths after finally putting myself in ur shoes."

msg1_v2= "Initally w/o knowing what a relationship was like, I was like yea i'm coming into this for something serious, soon learnt that I didn't have the time at this stage of my life and that's something you realized too ig. Tho in an ideal world you're def someone that i'd like to have given a serious relationship a shot with. Anyways with that outta the way, I was happy keeping it casual, so you weren't leading me on, j wanted to clarify that fact. I guess I was sending diff signals with the goodies and I had way too much free time last sem."

msg2_v2="As much as i'd like to keep the sweet casual thing we had going on, and it's not gonna be till March that I'd have the time - with moving and starting my job. I know you said you're not sure, and we def called it off, im clear on that. You're an amazing and beautiful person, there so much I like and appreciate about you, but above all you're an awesome friend. If being JUST friends is what it takes to keep in touch, then I can do that. As with anything in life it takes time for change, the memories will last forever and a shift in perception is eventual. What do you think? Would you be alright? Type “POOP” one more time for an unrelated message *I Lied, there's a tad more*."

extraextra="Wth, everything is making me think of you. Literally was on kia website the other day and they had 'retail price' and 'panda price' like whattt?! and then yesterday I had a fast sammy for breakfast lmao. While making pasta, bam! you pop up, going to a coffee shop, bam! and so on...bam! bam! You're omnipresent. This is an interesting feeling, how I feel fine (or so I think), guess that's what the dynamics of casually seeing you have it or maybe cuz we kept it real and honest, but I def miss you and keep thinking about you and the time we spent together.\n\nHow in the world do you keep your lips so moist (u know what i'm talkin abt, lmao), it can’t be only chapstick, spill the beans!! Ure friggin cute in that christmas fam pic. The matching fits is a cool thing your fam does, who’s idea is that? TYPE “REAL” which contemplates my act of gift giving and it's outcomes (it's long af, but has instructions to end this lol, my way of forcing you to read things *smirks*)"

prankedYa="Sheesh you actually thought I had scraped a database of dad jokes for this. SMH. Well for times sake what do you call a panda that kills plants xD. I promise ya it ain't SAM, cuz sam did a good deal with the rose, i'm proud of you! Ans: it's sampada HAHAHA. Cuz sampada = sam but i've never refered to you as sampada hence, you know it just works out. It ain't funny for shit I know. Ok ok for real, why is the soda can crusher disappointed with his job. Boop ba da boop the Ans is cuz he's So Dapressing HAR HAR HAR *wheeze*. (Type POOP to continue and for each one after, until the instructions tell you to do something else)"

reason="something I read - “with each successive gift you're putting this person into a state of perpetual obligation. Even if you say you don't expect anything in return, it will be awkward and uncomfortable. They will feel pressured to agree to things because they have to barter in exchange for your unsolicited generosity. Resentment will build. After the first gift, you'll look needy, like you want attention or gratitude.”\n\nI suppose that's kinda what you've been feeling, finally projected myself from your perspective and it def can feel like that.\n\nI was tryna reason why I wanted to give you small notes/gifts every now and then. I wasn't thinking all this then tho. With your 'love languages' being quality time and touch, I realized that we spent some real good time together but I was falling short on the touch side: either being timid, or j being slow in learning what made you feel good. Although gifts wasn't your thing, sometimes words and time we spent were just not enough. The only other outlet to show my appreciation/how I felt towards you was through the act of giving. Appreciating you wasn't one dimensional, it spanned a lot of expressions. Felt shallow without expressing everything yknow.\n\nType “DONE” to end this (there's an end message, the best one!!)."

endMsg="Thanks for POOPing all the way through my Dump, that so doesn't sound right, reminds me of a porta-potty, except that's 'on top of my Dump' rather than 'through my Dump'. I promise it didn't smell, I suggest some meds for the textual diarrhea. Whatever happens between us, hope to hang out with you again! Bye Sam! You're so gonna drive NDC and graduation to the MOOOON, and good luck with your wonderful (more like chaotic) panda-nurse life ahead of you. I love making things, my curiosity knows no bounds. I really enjoyed getting to know you and loved spending time with you. And if you had a good time too, it's like a big fat juicy cherry on the top :). Take care you fudging cute Panda! Until next time when you reach out or I start sending my pestering messages again."

app = Flask(__name__)

counter = 1
wrongCounter=0
hintCounter=1
donewithyou=0
end=0

@app.route("/sms", methods=['GET', 'POST'])


def smsReply():

    global counter
    global wrongCounter
    global hintCounter
    global donewithyou
    global end

    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()
    
    print(counter)
    print(body)
    # Determine the right reply for this message
    if body == 'POOP' and counter==1:
        resp.message(intro)
        counter+=1
    elif counter==2 and body == 'POOP':
        print("in message 1")
        resp.message(msg1_v2)
        counter+=1
    elif counter==3 and body == 'POOP':
        print("in message 2")
        resp.message(msg2_v2)
        counter+=1
    elif counter==4 and body == 'POOP':
        resp.message(extraMsg)
        counter+=1
        hintCounter=1
    elif counter==4 and body != 'POOP':
        resp.message("Come on the rest of it was chill stuff, don't be a bummer.")
    elif body == 'PANDA' and hintCounter==1:
        resp.message(hint1)
        hintCounter+=1
    elif hintCounter==2 and body == 'PANDA':
        resp.message(hint2)
    elif body == 'PLANTKILLER':
        resp.message(prankedYa)
    elif body == 'REAL':
        resp.message(reason)
        end=1
    elif body=='DONE':
        resp.message(endMsg)
    elif wrongCounter==1:
        resp.message("Ughh you're really forcing my hand here, I so don't want you to take on the baby panda mode, it's basically your toxic trait against you, trust me you so don't want that, imma give you one more chance.")
        wrongCounter+=1
    elif wrongCounter>1 and donewithyou==0:
        resp.message("Danggit you got me there, I ain't got the time to mansplain the whole thing to you. Remember CAPS for the replies, just one word! And no response here pls, Mr. Poop didn't give me the capability to store your opinion, but he totally cares for it")
        donewithyou=1
    elif wrongCounter>1 and donewithyou==1:
        resp.message("Bruh for real, I'm dissapointed in ya. Saddd!")
    else: 
        resp.message(wrongEntry)
        wrongCounter+=1
    return str(resp)

if __name__ == "__main__":
    
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = "AC0fad4f27553c4f7abc30b1aad8e059e0"
    # auth_token = "a3d3d8bda1ab11d1c40263b1f4cd9162"
    auth_token = "c2a7ccacc2b9957a39ff77da520237c3"

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

    app.run(debug=True)
 
