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

# Caterpillar Morph time

    menu:
        "placeholder":
    #        play sound "audio/Narrator17.mp3"
            c "placeholder"
        "...":

    #        play sound "audio/Narrator18.mp3"
            c "placeholder"



    #Q2
    c "placeholder"
    menu:
        "placeholder":
            $ evil = evil +1 #Good Answer!
            jump love_hware
            label love_hware:
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
