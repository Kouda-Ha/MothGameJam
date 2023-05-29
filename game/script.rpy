# The script of the game goes in this file.

# The game/script starts here
label start:
#Starting with Caterpillar being vain and uppity
    #play music "audio/cafe.mp3"
    scene backg1
    show c moth
#OPENING SCENE.
    #play sound "audio/Narrator1.mp3"
    c "I'm such a beautiful caterpillar."
    #play sound "audio/Narrator2.mp3"
    show c catpangry
    c "I'm going to flaunt it at the ugly caterpillars today, those guys disgust me."

#FIRST CONTACT
    scene img02
    #play sound "audio/Narrator21.mp3"
    show c catplove
    c "Heyyyyyyy everyone~! How's it feel being so boring?"
    show c catp
    my "*whispering* oh god it's them again..."
    #play sound "audio/Narrator12.mp3"
    my "Hello, Carl."
    menu:
        "CATERPILLAR Carl":
            my "Ah yes, Caterpillar Carl, because that's a needed clarification"
        "caterpillar talking":
            c "response to it."
        "...":
            "you're too good to talk to these ugly caterpillars"

    r "Hi Carl"

#Gone home
    #INTRO
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
            $ not_imposter = not_imposter +1 #Good Answer!
            jump love_hware
            label love_hware:
                c "placeholder"
                menu:
                    "placeholder":
                        $ not_imposter = not_imposter -1 #BAD Answer!

                        c "placeholder"
                    "placeholder":
                        $ not_imposter = not_imposter +1 #Good Answer!
                        c "placeholder"
        "placeholder":
            c "placeholder"

    #Q3
    my "placeholder placeholder"
    menu:
        "placeholderplaceholder":
            my "placeholder"

            "placeholder"
        "placeholder":
            my "placeholder"

            "placeholder"

    my "See you!"


    # This ends the game.
    return
