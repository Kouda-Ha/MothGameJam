# The script of the game goes in this file.

# The game/script starts here
label start:
#Starting with Caterpillar being vain and being uppity
    scene img02
    show c catp at right
#OPENING SCENE.
    c "I'm such a beautiful caterpillar."
    show c catlove at right
    c "I'm going to be an even MORE beautiful butterfly!"
    c "Some humans identified me as an Emporer caterpillar!"
    c "An Emporer BUTTERFLY must look EXQUISITE!!!"
    show c catangry at right
    c "I'm going to flaunt it at the ugly caterpillars again today..."
    show c catp at right
    c "those guys disgust me."

# Day 01
#FIRST CATTERPILLAR BULLYING
    scene backg1
    show c catlove at right
    c "Heyyyyyyy everyone~! How's it feel being so boring?"
    scene backg1
    show c catp  at right
    c "I see you're still green, greenie! Ha! I'm not sure why they even call you Mr Yellow"
    c "It's practically false advertising! HA HA HA!"
    scene backg1
    show m angry at left
    m "*whispering* oh god it's them again... stay back everyone, I'll get rid of him."
    show m m at left
    m "Hello, Carl."
    menu:
        "CATERPILLAR Carl!":
            scene backg1
            show c catangry at right
            show m angry at left
            m "Ah yes, CATERPILLAR Carl, because that's a needed clarification!"
            c "You're just jealous of my pink spots, you bland greenie"
        "Don't sound too excited, damn...":
            scene backg1
            show m sad at left
            m "Sorry, I'm just tired... Did you need something?"
            c "No, I'm just looking at you and feeling happy I'm an Emporer! Compared to
             whatever you are."
            m "..."
        "...":
            "You realise you're too good to be talking to these ugly caterpillars,
            so you check yourself out in a near by puddle reflection instead"
    "*leaves blow by*"
    "You're bored, and justly so! Mr Yellow is practically a grass snake"
    "with an excessive amount of legs."
    c "You all bore me. I'm going."
    "You leave for the lake, to wash the taste of talking with Mr Yellow out of your mouth."

    scene img03
    "As you are travelling to the lake, you spot Riley. Stumpy, STUMPY Riley."
    scene img03
    show r r at left
    r "Oh, hi Caterpillar Carl"
    show c catp at right
    c "Riley, Riley, Riley..."
    r "What?"
    c "Riiiiileh, Riiiilehh, RIIILEEE!"
    r "WHAT?!"
    menu:
        "Still haven't grown longer I see?":
            scene img03
            show r angry at left
            r "There's nothing wrong with being short!"
            show c catp at right
            c "We're all the same height love, you're just stubby."
            "You laugh at your own joke"
        "Do you even have feet?":
            scene img03
            show c catp at right
            show r sad at left
            r "I've got like 16! They're just... tiny..."
            "You notice Riley is tearing up"
            c "Are you really crying over short jokes? You're such a larva!"
            show c catlove at right
            c "And the same size of one too, HA! I slay me!"
            "*Giggling uncontrollably*"

    scene img03
    show c catangry at right

    "The day has been long and it's getting dark."
    "It isn't even worth it to make short jokes, Riley is probably
    going to be moth anyway. You should go get some rest."

#Gone home
    #Going home
    scene img04
    "Walking home takes a while"
    "probably because you're a caterpillar and the world is rather large in comparison"
    show c catp
    c "I love life, soon we'll become cocoons and I'll emerge a godly creature"
    "You laugh at the thought of the boring green caterpilars becoming disgusting moths"
    c "Riley will look so dumb! Like a perpetually baby moth!"
    show c catlove
    "In a moment of weakness, you think seeing Riley as a tiny moth could be cute though"
    "*You shake your head*"
    show c catangry
    c "Heh... hideous..."
    scene img05
    show c catp
    "As the sun begins to set, you ready for bed."
    c "I'll get some sleep..."

# Day 02
# Arguing with Mr Yellow
    scene img02
    show c catp at right
    "In the morning you go find a delicious plant"
    scene img05
    show c catlove at right
    "and consume the entire thing in one sitting"
    show m angry at left
    m "I can't believe you ate all the leaves on this plant! What were you thinking?"
    show c catangry at right
    c "Well, I was hungry, and those leaves looked delicious. I didn't realize you had any claim on them."
    show m m at left
    m "We're supposed to share the resources in our environment! You can't just go around devouring
    everything without considering others."
    show c catp at right
    c "Oh, please! Survival of the fittest, my friend. If I didn't eat them, someone else would have.
    It's a tough world out here, and we have to look out for ourselves."
    m "But that doesn't mean we should be selfish! There's plenty of foliage around if we all take only
    what we need. It's about balance and coexistence."
    c "Balance, schmalance! I'm just doing what comes naturally. If you're so concerned about sharing,
    why don't you find your own plant and stop bothering me?"
    show m angry at left
    m " I will find my own plant, thank you very much! And I hope you learn a lesson about consideration
    and empathy. We're all in this together, you know."
    show c catangry at right
    c "Oh, please spare me the moral lecture. I'm not interested in your idealistic notions. I'll continue
    doing what I need to survive, whether you like it or not."
    show m sad at left
    m "Fine! I'll leave you to your selfish ways. But mark my words, someday you'll realize the importance
    of cooperation and sharing. Goodbye!"
    c "Good riddance! I'll be just fine without your preaching. See you never!"
    scene img05
    show c catlove at right
    "Mr Yellow leaves"
    c "The nerve of some bugs!"
    scene img02
    "You go find another plant and eat some more leaves before once again going to sleep"

# Day 03
#
    scene img03
    show r r
    "On the way to the lake for a drink you see Riley heading over to steal your water"
    scene img03
    show r sad at left
    c "Hey! I was here first! Get away from that water!"
    show c catp at right
    r "B-but there's enough space for both of us. I'm thirsty too."
    show c catangry at right
    c "Well, find your own spot then! I found this watering hole first,
    and I'm not about to share it with you stupid greenies!"
    show r r at left
    r "Who made you the owner of the lake? I have every right to drink from
    it as well. Stop being so selfish!"
    c "Selfish? Me? Look who's talking! You're the one barging in and
    trying to take my water!"
    show r angry at left
    r "I don't see your name written anywhere around here. This lake belongs to
    everyone, and I won't let you bully me away."
    c "Bully? I'm just standing up for what's mine. I worked hard to walk to this
    lake!"
    show r sad at left
    r "If you want to be stubborn about it, why don't we take
    turns drinking from the lake, fair and square. That way, we both get some."
    show c catsad
    c "Hmph! Fine. But I'm keeping an eye on you. Don't think you can pull any tricks."
    show c catp at right
    r "Don't worry. I won't stoop to your level. Let's just get on with it and
    quench our thirst."
    scene img03
    "Riley and you take turns drinking from the lake, whiles eyeing each other warily,
    and reluctantly finding a temporary compromise."


# Caterpillar Morph time
    scene img02
    "You wake up feeling chipper... you're ready."
    show c catp
    "Ready to become a cocoon!"
    show c catlove
    "Ready to become a butterfly!"
    menu:
        "Become a cocoon":
            scene img02
            show c catlove
            c "I could tell the others, but I'm so tired I'll just start immediately."


        "Flaunt at the others that you're becoming a cocoon":
            scene bg8
            "You go find the others, to flaunt your soon to be cocoon-ness and butterfly"
            show c catp at right
            c "Hey everyone! I'm ready to make my cocoon! I'm going to look AMAZING!"
            show r r at left
            r "Oh? We were going to become cocoons too"
            show m love at center
            m "Yeah! It's going to be awesome! I'ma go get ready!"
            scene bg8
            show r love at left
            show c catp at right
            r "I'm so excited! I hope your metamorphosis goes well!"

    scene img02
    show c catlove
    c "You get ready to become a cocoon and get comfy and cosy in your home."





    #Q2
    c "placeholder"
    menu:
        "placeholder":
            $ evil = evil +1 #Good Answer!
            jump cocoon
            label cocoon:
                c "placeholder"
                menu:
                    "placeholder":
                        $ evil = evil -1 #BAD Answer!

                        c "placeholder"
                    "placeholder":
                        $ evil = evil +1 #Good Answer!
                        c "placeholder"
        "placeholder":
            c "placeholder"

    #Q3
    m "placeholder placeholder"
    menu:
        "placeholderplaceholder":
            m "placeholder"

            "placeholder"
        "placwholder":
            m "placeholder"

            "placeholder"

    m "See you!"


# Once become butterfly or moth excitedly go show off to the others


# Realisation you're a moth

# Depression




#Checking for if good or bad end
    label which_end:
        if evil >= 5:
            jump good_end
        elif evil < 5:
            jump bad_end
# ENDINGS
label good_end:
    "good ending"
    return

label bad_end:
    "bad end"
    return

    # This is the end of the game.
    return
