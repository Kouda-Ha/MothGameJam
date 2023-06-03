# This game was made by Kouda_Ha for the 'GAMES MADE QVIICK??? HD Remix' Game Jam
# https://itch.io/jam/games-made-qviick-hd-remix
# For the theme, the organiser said
## Quote: "If you need a theme, well, it's June! Which is moth season! Make a moth game.
## I don't know.  Maybe try this game jam theme generator."
# With this in mind, I literally made a game about moths.

# Credits:
## Script and storyline: @Kouda_Ha
## Art: @Kouda_Ha
## Leaf snack PNG: https://www.pngall.com/leaves-png/download/1764
## Hat: https://clipartcraft.com/images/cowboy-hat-transparent-orange-1.png
## Gun: https://www.pngkey.com/download/u2e6u2w7a9r5y3q8_download-hand-holding-gun-png-clipart-firearm-pistol/
## Photo backgrounds taken by @Kouda_Ha in Wales
## Sound & BGM: Zapsplat.com

# The game starts here
label start:
#    play music "audio/song.mp3" volume 0.25 # For BGM
#    play sound "audio/goodans.mp3" volume 2.0 # For sounds
#Starting with Caterpillar being vain and being uppity
    play music "audio/nature.mp3" volume 0.75 # For BGM
    scene img09
    "There's two ways for this story to go, and it all depends on your choices."
    "At some point you will start to hear pinging noises when you click on an answer."
    "If you're mean, you may hear an angry buzz, telling you your karma has gone down."
    "If you hear a delightful *ping~!* then you have answered with kind, and your karma will increase"
    "It's time to wake up, welcome, Carl."
    scene img02
    show c catp at right
#OPENING SCENE.
    c "I'm such a beautiful caterpillar."
    show c catlove at right
    c "I'm going to be an even MORE beautiful butterfly!"
    c "Some humans identified me as an Emperor caterpillar!"
    c "An Emperor BUTTERFLY must look EXQUISITE!!!"
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
            c "No, I'm just looking at you and feeling happy I'm an Emperor! Compared to
             whatever you are."
            m "..."
        "...":
            "You realise you're too good to be talking to these ugly caterpillars,
            so you check yourself out in a near by puddle reflection instead"
    "*leaves blow by*"
    "You're bored, and justly so! Mr Yellow is practically a grass snake with an excessive amount of legs."
    c "You bore me. I'm going."
    "You leave for the lake, to wash the taste of talking with Mr Yellow out of your mouth."

    scene img03
    play music "audio/waterwater.mp3" volume 0.75 # For BGM
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
            "You laugh at your own joke and Riley leaves in a hurry. You might have
            upset them"
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
            "Riley leaves in a hurry, I think you upset them"

    scene img03
    show c catp at right

    "It isn't even worth it to chase Riley and make more short jokes, they'll probably
    end up a moth anyway. You should go get some rest."
    show img04

    "The day has been long and it's getting dark."
#Gone home
    #Going home
    play music "audio/nature.mp3" volume 0.75 # For BGM
    scene img06
    "Walking home takes a while"
    "probably because you're a caterpillar and the world is rather large in comparison"
    scene img05
    show c catp
    c "I love life, soon we'll become cocoons and I'll emerge a godly creature"
    "You laugh at the thought of the boring green caterpilars becoming disgusting moths"
    c "Riley will look so dumb! They'll be a miniature moth!"
    show c catlove
    "In a moment of weakness, you think seeing Riley as a tiny moth could be cute though"
    "*You shake your head*"
    scene img02
    show c catangry
    c "Heh... yeah... Riley will be hideous..."
    show c catp
    "As the sun begins to set, you ready for bed."
    c "I'll get some sleep..."

# Day 02
# Arguing with Mr Yellow
    scene img02
    show c catp at right
    "In the morning you go out to find a delicious plant"
    scene img05
    show c catlove
    show leaf at right
    "And when you do, you consume the entire thing in one sitting"
    scene img05
    show c catp at right
    show m angry at left
    m "I can't believe you ate all the leaves on this plant! What were you thinking?"
    show c catangry at right
    c "Well, I was hungry, and those leaves looked delicious. I didn't realize you had any claim on them."
    show m m at left
    m "We're supposed to share the resources in our environment! You can't just go around devouring
    everything without considering others."
    show c catp at right
    c "Oh, please! Survival of the fittest, my friend. If I didn't eat it, someone else would have.
    It's a tough world out here, and we have to look out for ourselves."
    show m sad at left
    m "But that doesn't mean we should be selfish! There's plenty of foliage around! If we all take only
    what we need, we'd all be fed. It's about balance! And coexistence!"
    show c catangry at right
    c "Balance, schmalance! I'm just doing what comes naturally! If you're so concerned about sharing,
    why don't you find your own plant and stop bothering me?"
    show m angry at left
    m "I will find my own plant, thank you very much! And I hope you learn a lesson about consideration
    and empathy. We're all in this together, you know."
    show c catp at right
    c "Oh, please spare me the moral lecture. I'm not interested in your idealistic notions. I'll continue
    doing what I need to survive, whether you like it or not, moth breath!"
    show m sad at left
    m "Fine! I'll leave you to your selfish ways. But mark my words, someday you'll realize the importance
    of cooperation and sharing. Goodbye!"
    c "Good riddance! I'll be just fine without your preaching. See you never!"
    scene img05
    show c catangry at right
    "Mr Yellow leaves"
    c "The nerve of some bugs!"
    scene img02night
    "You go find another plant and eat some more leaves before once again going to sleep"
# Day 03

    scene img02
    show c catlove at right
    "The weather looks good today, you make your way to the lake"
    scene img03
    play music "audio/waterwater.mp3" volume 0.75 # For BGM
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
    scene img3close
    play music "audio/water.mp3" volume 0.2 # For BGM
    "Riley and you take turns drinking from the lake, whiles eyeing each other warily,
    and reluctantly finding a temporary compromise."

    "Once again, it is time for bed."
    scene img05
    play music "audio/nature.mp3" volume 0.75 # For BGM
    "So you make your way home"
    scene img02night
    "And get some well deserved rest!"
# Caterpillar Morph time
    scene img02
    "You wake up feeling chipper... you're ready."
    show c catp
    "Ready to become a cocoon!"
    show c catlove
    "Ready to become a butterfly!"
    #choice time
    menu:
        "No need to disturb everyone, just become a cocoon":
            play sound "audio/goodans.mp3" volume 1.0 # For sounds
            $ good = good + 1 #Good Answer!
            scene img02
            show c catlove
            c "I could tell the others, but I'm so tired I'll just start it immediately."

        "Flaunt at the others that you're becoming a cocoon":
            play sound "audio/badans.mp3" volume 1.0 # For sounds
            $ evil = evil +1 #BAD Answer!
            scene bg8
            "You go find the others, to flaunt your soon to be cocoon-ness and soon to become butterfly-ness!"
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
            scene bg8
            show c catlove at right
            c "why would they wish it went well for me? They should worry about themselves!"
            show c catp at right
            "The time has come and you need to go back home"

    scene img02
    show c catp
    c "Well, here goes nothing!"
    show c catlove
    play sound "audio/insidemetamo.mp3" volume 1.0 # For sounds
    "A restlessness stirred within, and as this feeling intensified,
    you were drawn to a secluded spot where you instinctively began building
    a protective shelter, your cocoon."
    scene img02
    play sound "audio/inmetamo.mp3" volume 1.0 # For sounds
    "Nestled within the cocoon, you embrace a profound stillness.
    It became a time of reflection and surrender, as the forces of transformation
    worked their magic. Cells rearranged, tissues dissolved, and new structures
    took shape within the safety of the cocoon."
    scene bg8
    play sound "audio/insidemetamo.mp3" volume 1.0 # For sounds
    "Weeks passed, and as you patiently underwent metamorphosis,
     trusting in the unseen process happening within your fragile enclosure.
     It was a delicate dance between vulnerability and hope. A shedding of the old
     to make room for the new."
    play sound "audio/inmetamo.mp3" volume 1.0 # For sounds
    scene backg1
    "Finally, the time came for you to emerge from your cocoon."
    "With determined effort, it pushed against the confines, discovering newfound
    strength."
    play sound "audio/endmetamo.mp3" volume 1.0 # For sounds
    "And then, in a breathtaking moment, you were transformed!"


# Once become butterfly or moth excitedly go show off to the others
    scene img02
    show c moth
    cc "AHHHH! I feel both refreshed and new but also my back is killing me sitting in that cocoon for so long!"
    scene img02
    show c mothsad
    "You take a moment to do some stretches"
    cc "Huh... feels kind of weird being out in the daytime. I must still be recovering."
    "You shake it off"
    scene img02
    show c mothlove
    cc "I can't believe I'm a butterfly! I'M FINALLY A BUTTERFLY!"
    show c moth
    cc "Ohhhh my catterpillar godddddddddddd I need to show myself off! I need to see what happened to Riley and Mr Yellow too!"
    scene img07
    show c mothlove
    cc "Hah! They probably ended up being stupid moths! I can't wait to see the look on their faces!"
    "Flying at practically the speed of sound to show off your new physique to the other caterpillars, you spot
    the most BEAUTIFUL being you could ever imagine in the distance"
    scene img06
    show m bm at left
    show c mothlove at right
    cc "Who? Who are you? I haven't seen you around here before?"
    m "Carl?"
    show c mothangry at right

    #Choice time
    cc "THAT'S CATTERPILLAR CARL TO YOU... wait!?"
    menu:
        #OptionA
        "Mr Yellow? You're a butterfly?":
            play sound "audio/goodans.mp3" volume 1.0 # For sounds
            $ good = good + 1 #Good Answer!
            m "Yeah! An Orange Tip Butterfly! Came to a bit of a shock to myself as well!"
            jump cocoon
            label cocoon:
                menu:
                    #Option AA
                    "BUT YOU'RE SUPPOSED TO BE A DUMB MOTH!":
                        play sound "audio/badans.mp3" volume 1.0 # For sounds
                        $ evil = evil +1 #BAD Answer!
                        show m bangry
                        m "How can you say moths are dumb? Haven't you looked at your own reflection yet?"
                        show c mothangry
                        "You glare"
                        ccc "What are you talking about?"
                        show m bm
                        m "You're an Emperor Moth."
                        m "You look great too! Your wing span is amazing!"
                        show c mothangry
                        ccc "You need glasses!"
                        m "I'm a butterfly, I can't wear glasses."
                        ccc "Shut up! You need glasses! I'm an Emperor Butterfly! Why would anybody call a moth an emperor?!? Moths stink!"
                        show c mothsad
                        show m bsad
                        m "Hey, it's ok to be a moth you know? Moths do a lot of..."
                        ccc "Moths are stupid... I can't be a moth!"
                        show c mothangry
                        show m bm
                        ccc "Stop talking! This can't be right!"
                        "You fly away as fast as you can"
                    #Option AB
                    "You look... great!":
                        play sound "audio/goodans.mp3" volume 1.0 # For sounds
                        $ good = good + 1 #Good Answer!
                        "In stunned silence you realise Mr Yellow is an Orange Tip Butterfly"
                        m "T-thanks Catterpillar Carl! Or I guess now it'd be Moth Carl, right?"
                        cc "It'd be 'what Carl'?"
                        show c mothsad
                        "You must have misheard him"
                        cc "Mr Yellow? Why did you say Moth... Carl?"
                        show m bsad
                        m "Haven't you looked at your reflection yet? You're an Emperor Moth."
                        show m blove
                        m "You look great too! Your wing span is amazing!"
                        show c mothangry
                        ccc "You need glasses!"
                        show m bsad
                        m "I'm a butterfly, I can't wear glasses."
                        ccc "Shut up! You need glasses! I'm an Emperor Butterfly! Why would anybody call a moth an emperor?!?"
                        show c mothsad
                        show m bm
                        ccc "Moths are stupid... I can't be a moth!"
                        m "Hey, it's ok to be a moth you know? Moths do a lot of..."
                        show c mothangry
                        ccc "Stop talking! This can't be right!"
                        "You fly away as fast as you can"
        #Option B
        "Mr Yellow?! A butterfly?!? But you were a boring greenie!":
            play sound "audio/badans.mp3" volume 1.0 # For sounds
            $ evil = evil +1 #BAD Answer!
            "In stunned silence you realise Mr Yellow is an Orange Tip Butterfly"
            show m blove
            m "Yeah, it's me! I was just as surprised as you are! I feel fantastic!"
            show c mothsad
            cc "I was looking forward to seeing you as a moth"
            show m bangry
            m "I mean, just because you're a moth, doesn't mean we can't talk to each other."
            show c moth
            cc "Just because I'm a... what?"
            show c mothsad
            "You must have misheard him"
            ccc "I'm a what, Mr Yellow?"
            show m bsad
            m "Haven't you looked at your reflection yet? You're an Emporer Moth."
            show c mothangry
            ccc "You need glasses!"
            show m bm
            m "I'm a butterfly, I can't wear glasses"
            ccc "Shut up! You need glasses! I'm an Emporer Butterfly! Why would anybody call a moth emporer?!?"
            show c mothsad
            ccc "Moths are stupid... I can't be a moth!"
            "You fly away as fast as you can"

#Denile
    play music "audio/waterwater.mp3" volume 0.5 # For BGM
    scene img03
    show c mothsad
    "There's no way you're a dumb moth, right?"
    scene img04
    show c moth
    ccc "There must be some sort of mistake! He's obviously lying!"

# Viewing yourself or refusing to confirm you're a moth
    "There's water right there, all you need to do is look for yourself, Carl."
    #Choice time
    ccc "But..."
    menu:
        "Shut up brain! I don't want to! Ignorance is bliss! I'M A BUTTERFLY!":
            play sound "audio/badans.mp3" volume 1.0 # For sounds
            $ evil = evil +1 #BAD Answer!
            ccc "He was obviously lying! I don't need to look!"

        "I'm just... scared to look":
            play sound "audio/goodans.mp3" volume 1.0 # For sounds
            $ good = good +1 #GOOD Answer!
            ccc "If I look and I'm a moth, what can I do? I'm stuck like this for the rest of my life"

    "..."

    menu:
        "*look*":
            play music "audio/water.mp3" volume 0.2 # For BGM
            play sound "audio/goodans.mp3" volume 1.0 # For sounds
            $ good = good +1 #GOOD Answer!
            scene mothwater
            ccc "It's true"
            play sound "audio/horror.mp3" volume 1.0 # For sounds
            ccc "I'm a moth..."
            ccc "What about Riley? Maybe Riley become a moth too?"

        "*Don't look*":
            play sound "audio/badans.mp3" volume 1.0 # For sounds
            $ evil = evil +1 #BAD Answer!
            ccc "I'm not looking, I don't NEED to look! It's obvious that Mr Yellow was just jealous because I'm an Emperor!"
            ccc "I should find Riley! They probably ended up a moth! I can laugh at them!"

    play music "audio/nature.mp3" volume 0.75 # For BGM
# Find Riley
    scene img09
    show c moth
    ccc "Where'd Riley be hiding if they were a dumb moth?"
    "You ponder the locations known for Riley to hang out at"
    menu:
        "The lake! Riley's always at the lake":
            play music "audio/waterwater.mp3" volume 0.5 # For BGM
            play sound "audio/goodans.mp3" volume 1.0 # For sounds
            $ good = good + 1 #GOOD Answer!
            scene img03
            "You go look by the lake where you once shared a drink together"
            show c moth at right
            ccc "Hmm... looks like nobody is here right now..."
            "suddenly a flutter is heard from behind you and a whoosh of air brushes past your face"
            show r blove at left
            r "Oh, hi Carl!"
            show c mothangry at right
            ccc "AHH!"
            show r bbangry at left
            r "AHHH! WHAT!?! Are you ok?!?"
            show c mothsad at right
            play sound "audio/horror.mp3" volume 1.0 # For sounds
            ccc "Oh no... you're hot!"
            show r bblove at left
            r "I!?! That's very sudden! I don't know how to respond to that!"
            show c moth at right
            ccc "This is so unfair! Why is everyone so hot?!!"
            show r bbr
            r "Everyone? Ohhh, you must have seen Mr Yellow already"
            show c mothsad
            ccc "You mean Mr Orange-Tipped-Beautiful-Butterfly!"
            ccc "It's so unfair! "
            r "What do you mean?"

            menu:
                "I'm a disgusting moth! Bound to the darkness of the night!":
                    $ evil = evil +1 #BAD Answer!
                    play sound "audio/badans.mp3" volume 1.0 # For sounds
                    show c mothsad at right
                    ccc "I'm forever trapped in the shadows. While my butterfly
                    counterparts bask in the glory of the sun's warm embrace,
                    I'm confined to a nocturnal existence, devoid of your vibrant colours
                    and joyful dances that adorn the daylight hours!"
                    show r bbr
                    r "This seems a little overly dramatic, you know moths are cool too."

                "I didn't think my metamorphosis would go this way...":
                    $ good = good + 1 #GOOD Answer!
                    play sound "audio/goodans.mp3" volume 1.0 # For sounds
                    show c moth at right
                    ccc "Everyone is so cool looking and I'm just exhausted and my wings are dull"
                    show r bblove at left
                    r "Moths are cool too though, your feelers are really fluffy"
                    r "And no wonder you're exhausted! You're a moth, nocturnal"
                    show r bbr at left
                    r "If you get some rest, you might feel better. It'll be ok."
                    show c mothlove at right
                    ccc "You know what, you might be right."


        "Some rocks you never saw Riley at prior to metamorphosis but just in case Riley isn't a moth,
         you'd like to stay in denile a little longer and avoid
        the beautiful butterfly armarda that seems to be overtaking the hills":
            jump rocks
            label rocks:
                play sound "audio/badans.mp3" volume 1.0 # For sounds
                $ evil = evil +1 #BAD Answer!
                ccc "Must be at those rocks!"
                scene img10
                ccc "Rocks they've never been to before!"
                ccc "If I was a stupid moth Riley I'd probably go hide by those rocks!"
                show c moth
                ccc "Because it's a new experience and so is being a smelly moth!"
                ccc "And it might be a nice and secluded place to hang out where nobody is going to find me..."
                ccc "... I mean Riley"
                "..."
                "......"
                "............"
                show r br at left
                r "Oh, hi Carl!"
                show c mothangry at right
                play sound "audio/horror.mp3" # for sounds
                ccc "WHAT THE HELL!?! WHY ARE YOU HERE?!?"
                show r blove at left
                r "I thought I'd come check out these rocks, I'd never been here before and thought a new experience
                would be nice. It is nice, isn't it? So secluded."
                show c mothsad at right
                ccc "Oh come on!!!"
                "You flee"
                scene img10
                show r bbr at left
                r "Was it something I said?"
                show r bblove at left
                r "Damn, these are some cool rocks!"


    play music "audio/nature.mp3" volume 0.75 # For BGM
    scene img02
    show c mothsad
    "You return home, but wonder why you even bother."
    ccc "I should get some sleep..."

    # The night time
    scene img02night
    "..."
    "You're surprised... You slept through the rest of the day with ease"
# Riley comes check on Moth Carl, and discuss the benefits of moths and butterflies
# Economically both pollinate different flowers which helps the environment
    "and you actually feel a lot more refreshed"
    show c mothlove
    ccc "Huh... how about that..."
    play sound "audio/inmetamo.mp3" volume 1.0 # For sounds
    "There is a little russle in the flowers next to your rock"
    show c mothangry at right
    ccc "Who's there?!"
    "Riley pops out from the shadows"
    show r bbr at left
    r "*yawning* Hi Carl!"
    show c moth at right
    ccc "What are you doing here?"
    show r bbsad at left
    r "Well you seemed really down earlier, so I wanted to make sure you were ok."

    menu:
        "Leave me alone! I'm gross. You're only here to show off":
            play sound "audio/badans.mp3" volume 1.0 # For sounds
            $ evil = evil +1 #BAD Answer!
            show r bbsad
            r "No I'm not and you are not gross! There's nothing wrong with moths!"
            show c mothsad
            show r bbr at left
            r "A moth is just as important as a butterfly. Just like the intricate
            dance of a delicate ecosystem, both moths and butterflies have our parts to play."
            show c mothsad at right
            ccc "What do you mean?"
            show r bbr at left
            r "When it comes to plant diversity, we both have our unique preferences.
            While butterflies tend to favor brightly colored flowers, moths are often
            drawn to more subtly scented and pale-coloured blooms."
            show r bblove at left
            r "This diversity of plant preferences allows for a wider range of pollination interactions."
            show c mothangry at right
            play sound "audio/horror.mp3" volume 1.5 # for sound
            ccc "You see? Gloting! I'm only interested in pale-coloured flowers and you get
            the flashy ones! Leave me alone!"
            show r bsad at left
            r "I was only trying to cheer you up *sniffle*"
            "Riley flys away crying"
            scene img02night
            show c mothangry
            "The nerve of some bugs! Butterflies are even worse than moths!"

        "I'll be fine, I'm just adjusting.":
            play sound "audio/goodans.mp3" volume 1.0 # For sounds
            $ good = good + 1 #GOOD Answer!
            show c moth at right
            show r bbr at left
            r "I understand that! We've all just gone through a huge change, but yours will take
             even longer to get used to because you've ended up nocturnal"
            show c mothsad at right

            menu:
                "Why are you being nice to me? I've always been horrible to you":
                    play sound "audio/goodans.mp3" volume 1.0 # For sounds
                    $ good = good + 1 #GOOD Answer!
                    show r bblove at left
                    r "Because we're friends!"
                    show r bbr
                    show c mothlove at right
                    ccc "!!"
                    show moth at right
                    ccc "I guess we could be friends"
                    show r bblove at left
                    r "!!"
                    r "YEAH!"
                    scene night3
                    show r bbr at left
                    show c moth at right
                    "You both fly about talking until Riley is too tired to stay awake"
                    scene night4
                    show r bbr at left
                    show c moth at right
                    ccc "If you're too tired, you should go to sleep. We can talk again at the start or end of any night!"
                    show r bblove at left
                    r "Thanks, Carl! I look forward to it!"
                    "You fly Riley home"

                "I'm not nocturnal! YOU'RE NOCTURNAL!":
                    play sound "audio/badans.mp3" volume 1.0 # For sounds
                    $ evil = evil + 1 #BAD Answer!
                    scene img02night
                    show c mothangry at right
                    show r bbangry at left
                    r "I'm not?!... That isn't an insult! There's nothing wrong with being nocturnal!"
                    r "If you're going to be like this I'm leaving!"
                    scene img02night
                    show c mothangry
                    ccc "GOOD RIDDANCE!"
                    "..."
                    show c mothsad
                    play sound "audio/horror.mp3"
                    "*sniffle*"


    "It's the day time again, and you're very tired. Maybe you should get some rest"
    scene img02
    show c mothsad at right
    play sound "audio/horror.mp3" # plays sound
    ccc "I miss the sun... but it makes me so tired now"
    "You sleep in a deep sleep and once again wake up at dusk"
    scene img02night


# Mr Yellow brings a treat to Moth Carl
## Either accept and feel happy/guilt for being mean
## Or reject and be spiteful and jealous, accusing him of coming over to glout
    play sound "audio/inmetamo.mp3" volume 1.0 # For sounds
    "You hear rustling in the bushes again"
    show c mothangry
    ccc "Who's there?!... R-Riley?"
    show c mothlove at right
    show m blove at left
    show c mothangry at right
    m "Hi mot... erm Caterp.. errmmm..."
    m "Hi Cool Carl!"
    show c moth at right
    menu:
        "Why are you here? I was always mean to you.":
            play sound "audio/goodans.mp3" volume 1.0 # For sounds
            $ good = good + 1 #GOOD Answer!
            show m bsad at left
            m "I heard you were having a difficult time"
            show c mothsad at right
            play sound "audio/horror.mp3"
            ccc "I might be..."
            show m blove at left
            m "So I got you a present!"
            show leaf
            "Mr Yellow drops a pile of your favourite leaves on the floor"
            show c mothlove
            ccc "Mother of GOD! I love these leaves!"
            scene img02night
            show c mothlove
            ccc "That was FANTASTIC!"
            scene img02night
            show m blove at left
            show c mothlove at right
            m "I'm happy you liked it. I remember you eating them as a caterpillar so I thought it'd cheer you up"
            show c mothsad at right
            ccc "Why are you being nice to me when all I did was berate you?"
            show m bsad at left
            m "Everyone deserves a second chance and it's never too late to change for the better"
            play sound "audio/horror.mp3" # sound
            ccc "I'll try to be better from now on..."
            "*sniffle*"
            show m bm at left
            m "I look forward to hanging out with you more often, friend!"
            m "I am too tired to be awake now though, how about we all meet up at dawn?"
            show c moth at right
            ccc "Sure!"
            show img02night
            show c moth at right
            "Mr Yellow flutters away to his home for some sleep"
            "And you start your day as a rather full moth thanks to the leaves, but it'd be good to have a drink!"
            scene night3
            "You enjoy a nice drink and stretched your wings a bit before returning to your home again"

        "You here to brag about being a stinkin' butterfly!? HUH!?! GET LOST!":
            play sound "audio/badans.mp3" volume 1.0 # For sounds
            $ evil = evil + 1 #BAD Answer!
            show m bangry at left
            m "I'm not a bully! Unlike you! I was genuinely trying to see if you were alright!"
            show c mothangry at right
            ccc "Liar! You've come to make fun of me!"
            show m bsad at left
            m "If I had come to berate you, then why did I bring you a gift?!"
            show leaf
            "Mr Yellow throws a pile of your favourite leaves on the floor"
            scene img02night
            show c mothsad at right
            show m bsad at left
            ccc "You got me my favourite leaves?"
            m "Yeah! I'm actually nice if you get to know me instead of shouting at me all the time! But I guess
            you don't care about anybody but yourself!"
            scene img02night
            "Mr Yellow flys away crying"
            play sound "audio/horror.mp3" # sad sounds
            show c mothsad
            "*sniffle*"
            ccc "Good riddance..."
            "After sad eating the leaves, you're too full to move and decide to just hide in your home instead"

    scene night4
    "Now then, what will the future bring?"
    scene img02
    "~Some Time into the Future~"

#Checking for if good or bad end
    label which_end:
        if evil <= good:
            jump good_end
        elif evil > good:
            jump bad_end

# ENDINGS
label good_end:
    scene img05
    "From then on, you met up with Mr Yellow and Riley each dusk to hang out and talk."
    show r blove
    show m blove at left
    show c mothlove at right
    "And life wasn't that bad afterall"
    scene night1
    show c moth at left
    "You even met other moths"
    scene night1
    show c mothangry at right
    show rick rick at left
    rick "CARLLLLLL!!!!!!"
    scene night1
    show c moth at right
    ccc "What was that?"
    scene night3
    show c mothsad at right
    "And when you'd feel lonely or sad"
    scene night4
    "All you needed to do was meet with Riley or Mr Yellow at dusk or dawn"
    show c mothlove at right
    show r bblove at left
    "To be comforted and appreciated"
    scene img05
    show c mothlove at right
    show m blove at left
    "by your friends"
    scene img02night
    show c mothlove
    "Good End"
    return

label bad_end:
    scene img02night
    show c mothangry
    "From then on, you lived in spite, never talking to the butterflies again"
    scene night1
    show c mothsad
    "Never talking to fellow moths either! As they are disgusting creatures!"
    scene night3
    show c moth at left
    "Shamefully you would leave to get food, then return to your home"
    scene night4
    show c mothangry
    "Cursing the gods or lack thereof for making you into the one thing you truely hate..."
    scene img02night
    "A stinky moth with moth breath"
    show c mothsad
    "Bad End"
    return

    # This is the end of the game.
    return
