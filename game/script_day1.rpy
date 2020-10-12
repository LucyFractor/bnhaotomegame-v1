############################### Start Chapter 1 ################################
label day1:
    jump day1_morning


label day1_morning:
    scene bg_personalbedroom_day

    play sound "audio/se/bird_chirping.ogg"

    "Every good stories begins with something like this:"
    "\"The sound of birds chirping outside and the warm sun rays filtered through your bedroom window, signalling a clear sunny sky ahead.\""
    ".... Not that you can actually hear nor feel it, since you were sleeping ever so soundly on your bed, hugging your pillow against your chest and half your legs sprawled out from the blanket. Until..."

    play music "audio/music/kamiyamayoh_cutlery.mp3" fadeout 2.0

    mc "Hrghhhh...."

    "Sleepily, you squint your eyes to check the time on the alarm clock beside your bed."
    "You're not late, but you're not early either. It's best if you wake up now."

    menu:
        "Wake up":
            "Your left arm flails around until it finds your phone vibrating against the nightstand."
            "Out of habit, your thumb automatically finds the \'Dismiss\' button and taps it, effectively stopping your alarm."
            stop music
            play sound "audio/se/bird_chirping.ogg" fadeout 5.0
            "You sit up begrudgingly on your bed, one hand rubbing your eyes and your other hand still holding your phone."
            $ skippedSchool = False

        "Go back to sleep":
            stop sound
            stop music fadeout 2.0
            $ skippedSchool = True
            jump day1_evening

    "Stretching your arms above your head, you could feel and hear your bones and joints creak."
    "You wince, though it doesn't actually hurt; it's just that you feel sore all over your body, and one of your arm feels especially sensitive. Most probably because of the training you did yesterday in class."
    "Your eyes stray to the haphazard state of your gaming corner, where a heap of tangled messy cables and empty packets of your late night snacks from last night are scattered about."
    "That's going to be a pain to clean up later."
    mc "Ugh, curse you, past Me..."
    "With a huff, you stand up to do one last stretch."
    "You were about to proceed with your morning routine when your phone vibrates, begging for your attention."

    play sound "audio/se/phone_message_notif_2.mp3"

    mc "Hmm? I'm getting a text..."

    $ nickname_mi = midoriya.get_nickname("mc").value
    $ nickname_bk = bakugou.get_nickname("mc").value
    $ nickname_ts = todoroki.get_nickname("mc").value

    menu:
        "Who is texting you?"

        "[nickname_mi]":
            $ senderName = "Cinnamon Roll"
            $ route = "mi"
            jump event1_mi
        "[nickname_bk]":
            $ senderName = "King Explosion Murder"
            $ route = "bk"
            jump event1_bk
        "[nickname_ts]":
            $ senderName = "A/C Boi"
            $ route = "ts"
            jump event1_ts


########################### Event 1 scene - Midoriya ###########################
label event1_mi:
    mc "Sender is... [nickname_mi]?"
    "You have a hunch you know what he's about to say to you. The sweet boy has started to open up more and more to you lately."
    "The fact that he's super adorable when he blushes is definitely a plus in your book."

    call phone_start from _call_phone_start
    call message_start(senderName, "Good morning, [lastName]-san!", False) from _call_message_start

    call screen phone_reply1("Good morning!", "event1_mi_q1_c1")
    label event1_mi_q1_c1:
        call phone_after_menu from _call_phone_after_menu
        call message_start(firstName, "Good morning, [nickname_mi]", True) from _call_message_start_1
        call message(senderName, "Um, are you on your way to school? Or are you still at home?", False) from _call_message
    call message(senderName, "I mean, I was just worried!", False) from _call_message_1
    call message(senderName, "Yesterday training, I was careless and your arm got a full hit, so...", False) from _call_message_2
    call message(senderName, "Sorry if it sounds weird or anything!", False) from _call_message_3

    call screen phone_reply1("It's not weird at all!", "event1_mi_q2_c1")
    label event1_mi_q2_c1:
        $ midoriya.set_affection("+", 1)
        call phone_after_menu from _call_phone_after_menu_1
        call message_start(firstName, "It's not weird at all!", True) from _call_message_start_2
        call message(firstName, "No worries :)", True) from _call_message_4
    call message(senderName, "Okay, I'm glad you think so :D", False) from _call_message_5

    call screen phone_reply1("Btw actually I just woke up haha", "event1_mi_q3_c1")
    label event1_mi_q3_c1:
        call phone_after_menu from _call_phone_after_menu_2
        call message_start(firstName, "Btw actually I just woke up haha", True) from _call_message_start_3
        call message(senderName, "Oh!!", False) from _call_message_6
    call message(senderName, "Then, do you want to walk with me?", False) from _call_message_7
    call message(senderName, "To school, I mean!", False) from _call_message_8
    call message(senderName, "It's ok if you don't!!", False) from _call_message_9

    call screen phone_reply2("I'd love to!", "event1_mi_q4_c1", "What's the ocassion?", "event1_mi_q4_c2")
    label event1_mi_q4_c1:
        $ midoriya.set_affection("+", 1)
        call phone_after_menu from _call_phone_after_menu_3
        call message_start(firstName, "I'd love to!", True) from _call_message_start_4
        call message(senderName, ":D", False) from _call_message_10
        jump after_event1_mi_q4
    label event1_mi_q4_c2:
        call phone_after_menu from _call_phone_after_menu_4
        call message_start(firstName, "What's the ocassion?", True) from _call_message_start_5
        call message(senderName, "I'm just worried", False) from _call_message_11
        call message(senderName, "I mean, you're hurt!", False) from _call_message_12
        call message(senderName, "What if you encounter a villain?", False) from _call_message_13
        call message(senderName, "I mean! You're not weak or anything!", False) from _call_message_14
        call message(senderName, "And it's not like I'm much more stronger than you and all but", False) from _call_message_15
        call message(firstName, "You're so sweet Midoriya-kun :)", True) from _call_message_16
        call message(firstName, "Will you escort me to school then?", True) from _call_message_17
        call message(senderName, "Ah, gladly!", False) from _call_message_18
        jump after_event1_mi_q4

    label after_event1_mi_q4:
        call message(senderName, "Then I'll wait for you in front of your house? If that's ok with you?", False) from _call_message_19
        call message(firstName, "Yup! See you soon!", True) from _call_message_20
        call message(senderName, "See you!", False) from _call_message_21

        call phone_end from _call_phone_end
        jump after_event1


############################ Event 1 scene - Bakugou ###########################
label event1_bk:
    mc "[nickname_bk]? Wow, is it going to snow in the middle of summer tomorrow?"

    call phone_start from _call_phone_start_1

    call message_start(senderName, "oi", False) from _call_message_start_6
    call message(senderName, "wake up you lazyass", False) from _call_message_22

    call screen phone_reply1("MORNING TO YOU TOO RUDE ASS", "event1_bk_q1_c1")
    label event1_bk_q1_c1:
        call phone_after_menu from _call_phone_after_menu_5
        call message_start(firstName, "MORNING TO YOU TOO RUDE ASS", True) from _call_message_start_7
    call message(senderName, "F U", False) from _call_message_23
    call message(senderName, "bet 1000 yen you stayed up late last night", False) from _call_message_24

    call screen phone_reply1(".... So what???", "event1_bk_q2_c1")
    label event1_bk_q2_c1:
        call phone_after_menu from _call_phone_after_menu_6
        call message_start(firstName, ".... So what???", True) from _call_message_start_8
    call message(senderName, "lol called it", False) from _call_message_25
    call message(senderName, "guess today's lunch is on you, loser", False) from _call_message_26

    call screen phone_reply2("HEY WAIT HOW'D YOU KNOW I SLEPT LATE OMG STALKER ALERT", "event1_bk_q3_c1", "....", "event1_bk_q3_c2")
    label event1_bk_q3_c1:
        $ bakugou.set_affection("+", 1)
        call phone_after_menu from _call_phone_after_menu_7
        call message_start(firstName, "HEY WAIT HOW'D YOU KNOW I SLEPT LATE OMG STALKER ALERT", True) from _call_message_start_9
        call message(senderName, "WHO WOULD WANT TO STALK YOU", False) from _call_message_27
        call message(senderName, "UNATTRACTIVE LIL SHIT", False) from _call_message_28
        jump after_event1_bk_q3
    label event1_bk_q3_c2:
        $ bakugou.set_affection("+", 1)
        call phone_after_menu from _call_phone_after_menu_8
        call message_start(firstName, "....", True) from _call_message_start_10
        jump after_event1_bk_q3
    label after_event1_bk_q3:
        call message(firstName, "Did you really message me just to mock me??", True) from _call_message_29
        call message(firstName, "If you have SO MUCH free time you should, idk, learn empathy or something", True) from _call_message_30
        call message(senderName, "whatever", False) from _call_message_31
        call message(senderName, "anyway", False) from _call_message_32
        call message(senderName, "how long does it take you to prep to school", False) from _call_message_33

    call screen phone_reply2("30 minutes-ish, why?", "event1_bk_q4_c1", "2 hours-ish, why?", "event1_bk_q4_c2")
    label event1_bk_q4_c1:
        $ bakugou.set_affection("+", 1)
        call phone_after_menu from _call_phone_after_menu_9
        call message_start(firstName, "30 minutes-ish, why?", True) from _call_message_start_11
        call message(senderName, "fine, whatever", False) from _call_message_34
        call message(senderName, "it’ll do", False) from _call_message_35
        call message(senderName, "go and get it done in 30 mins then", False) from _call_message_36
        jump after_event1_bk_q4
    label event1_bk_q4_c2:
        call phone_after_menu from _call_phone_after_menu_10
        call message_start(firstName, "2 hours-ish, why?", True) from _call_message_start_12
        call message(senderName, "it’s", False) from _call_message_37
        call message(senderName, "7:04", False) from _call_message_38
        call message(senderName, "wtf", False) from _call_message_39
        call message(senderName, "get it done in 30 mins tops", False) from _call_message_40
        jump after_event1_bk_q4
    label after_event1_bk_q4:
        call message(firstName, "Uhhhh", True) from _call_message_41

    call screen phone_reply1("I mean ok but wHy???", "event1_bk_q5_c1")
    label event1_bk_q5_c1:
        call phone_after_menu from _call_phone_after_menu_11
        call message_start(firstName, "I mean ok but wHy???", True) from _call_message_start_13
        call message(senderName, "cause we’re walking to school together", False) from _call_message_42
        call message(senderName, "dumbass", False) from _call_message_43
        call message(firstName, ".... ok??? But WHY????", True) from _call_message_44
        call message(senderName, "CAUSE I SAID SO YOU LITTLE SHIT", False) from _call_message_45
        call message(senderName, "WHY ARE YOU SO ANNOYING", False) from _call_message_46
        call message(senderName, "JUST GO GET YOUR UGLY ASS READY", False) from _call_message_47
        call message(senderName, "I’LL EXPLODE YOUR DAMN HOUSE IF YOU’RE NOT READY BY THE TIME I’M THERE", False) from _call_message_48
        call message(firstName, "Man, who pissed on your milk this morning?", True) from _call_message_49
        call message(firstName, "Fiiiine", True) from _call_message_50
        call message(firstName, "See you K-A-C-C-H-A-N!", True) from _call_message_51
        call message(senderName, "FCUK", False) from _call_message_52
        call message(senderName, "OFF", False) from _call_message_53
        call message(firstName, "*FUCK", True) from _call_message_54
        call message(senderName, "DIE", False) from _call_message_55

    call phone_end from _call_phone_end_1
    jump after_event1


########################### Event 1 scene - Todoroki ###########################
label event1_ts:
    mc "Huh, [nickname_ts]?"

    call phone_start from _call_phone_start_2

    call message_start(senderName, "Good morning.", False) from _call_message_start_14

    call screen phone_reply1("Good morning!", "event1_ts_q1_c1")
    label event1_ts_q1_c1:
        call phone_after_menu from _call_phone_after_menu_12
        call message_start(firstName, "Good morning, [nickname_ts]!", True) from _call_message_start_15

    call message(senderName, "Apologies for the sudden request, but would it be alright if we walk to school together today?", False) from _call_message_56

    call screen phone_reply2("Don’t apologize! I’d love to!", "event1_ts_q2_c1", "Umm are you sure you got the right number?", "event1_ts_q2_c2")
    label event1_ts_q2_c1:
        $ todoroki.set_affection("+", 1)
        call phone_after_menu from _call_phone_after_menu_13
        call message_start(firstName, "Don’t apologize! I’d love to!", True) from _call_message_start_16
        call message(senderName, "You would?", False) from _call_message_57
        call message(senderName, "I'm a little surprised.", False) from _call_message_58
        call message(firstName, "Oh? Why?", True) from _call_message_59
        jump after_event1_ts_q2
    label event1_ts_q2_c2:
        call phone_after_menu from _call_phone_after_menu_14
        call message_start(firstName, "Umm are you sure you got the right number?", True) from _call_message_start_17
        call message(senderName, "Yes.", False) from _call_message_60
        call message(senderName, "I’m texting [lastName] [firstName], right?", False) from _call_message_61
        call message(firstName, "Yeah... But what’s with the sudden invitation then?", True) from _call_message_62
        jump after_event1_ts_q2
    label after_event1_ts_q2:
        call message(senderName, "Do you not remember what happened yesterday at training?", False) from _call_message_63
        call message(senderName, "I accidentally hurt your arm pretty badly.", False) from _call_message_64
        call message(senderName, "And even with Recovery Girl’s help, it couldn’t heal completely.", False) from _call_message_65
        call message(senderName, "I thought you would be at least a little annoyed.", False) from _call_message_66

    call screen phone_reply1("Aww", "event1_ts_q3_c1")
    label event1_ts_q3_c1:
        call phone_after_menu from _call_phone_after_menu_15
        call message_start(firstName, "Aww", True) from _call_message_start_18
        call message(firstName, "You really don’t have to worry about it!", True) from _call_message_67
        call message(senderName, "... I still feel responsible for it.", False) from _call_message_68
        call message(firstName, "(*´ω`*)", True) from _call_message_69
        call message(firstName, "Okay, then let's walk together to UA today!", True) from _call_message_70
        call message(senderName, "Great. I’ll come by your house then.", False) from _call_message_71

    call screen phone_reply2("You wanna meet at the station instead?", "event1_ts_q4_c1", "Ok! I’ll go get ready!", "event1_ts_q4_c2")
    label event1_ts_q4_c1:
        $ todoroki.set_affection("+", 1)
        call phone_after_menu from _call_phone_after_menu_16
        call message_start(senderName, "You wanna meet at the station instead?", True) from _call_message_start_19
        call message(senderName, "It’s fine, it’s not a long detour anyway.", False) from _call_message_72
        call message(senderName, "It’ll the perfect warmup since our first period is Hero Lesson.", False) from _call_message_73
        call message(firstName, "Ok! I’ll go get ready!", True) from _call_message_74
        jump after_event1_ts_q4
    label event1_ts_q4_c2:
        call phone_after_menu from _call_phone_after_menu_17
        call message_start(firstName, "Ok! I’ll go get ready!", True) from _call_message_start_20
        jump after_event1_ts_q4
    label after_event1_ts_q4:
        call message(senderName, "Ok.", False) from _call_message_75

    call phone_end from _call_phone_end_2
    jump after_event1


######################### Continue after event 1 scene #########################
label after_event1:
    mc "Well, that was an early morning surprise..."
    "You chuckle and continue your trek towards the bathroom to prepare for school."

    scene bg_black with dissolve

    show text "....." at truecenter with dissolve
    play sound "audio/se/shower.ogg"
    pause 1
    hide text with dissolve
    show text "....." at truecenter with dissolve
    play sound "audio/se/rustling.ogg"
    pause 1
    hide text with dissolve
    show text "....." at truecenter with dissolve
    play sound "audio/se/door_open.ogg"
    pause 1
    hide text with dissolve

    play sound "audio/se/bird_chirping.ogg"
    scene bg_street_day with dissolve

    "You lock the gates of your humble abode and inhales the fresh morning air. You scan the empty street. It seems like your friend hasn't arrived yet."
    "With a soft hum, you turn away from your home and leans against its wall."
    "While waiting for your classmate, your brain decides it's a good time to think about school."
    "Today’s first period is Hero Lesson. You wonder what kind of activity the teacher has in plan."
    "Will it turn into the usual sparring matches? Or perhaps a team battle? You would really like it if it's the latter."
    "Your uninjuried arm shift as you bring it to feel the smooth bandages wrapped around your other limb. Afterall, with your Quirk being mainly passive and with one of your arm down for the count, you won’t be able to use your weapons as proficiently."
    "Suddenly, a yawn breaks your train of thoughts."
    "You silently blame the video game you played last night for being too addictive. While you had learned a lot from it, you’re not sure if sacrificing your sleep was the best decision you could've made."
    mc "I should probably go to bed early today..."
    "Upon saying the statement outloud you chuckle in defeat, wondering if your determination can last later, when you're faced with the promise of being lost in the game you just bought from the video game store."

    "Fortunately, at the exact moment, you spy a movement out of the corner to your eyes."
    "You smile at the approaching figure."

    play music "audio/music/afford.mp3" fadein 1.0
    if route == "mi":
        jump event2_mi
    if route == "bk":
        jump event2_bk
    if route == "ts":
        jump event2_ts
    else:
        jump day1_evening


########################### Event 2 scene - Midoriya ###########################
label event2_mi:
    show fb_mi_school_04 with dissolve

    "You can see a sheen of sweat on Midoriya’s forehead, and you note how his breath seems more labored than usual, though not to the point of strained."
    mi "[lastName]-san! I’m so sorry, did you wait long?"

    menu:
        "Yup, my legs hurts now.":
            mc "Yup, my legs hurts now."
            show fb_mi_school_04 sorry_01
            mi "Sorry! I was supposed to be the one who picked you up, but I made you wait...."
            "He truly looks guilty and seeing his sincere eyes tugs on your heartstrings."
            mc "I was just kidding, [nickname_mi]! Did something happen?"

        "Hey, no worries! Did something happen?":
            $ midoriya.set_affection("+", 1)
            mc "Hey, no worries! Did something happen?"

    show fb_mi_school_04 shy_02
    "Midoriya looks bashful when he meets your curious gaze, and he proceeds with his explanation just as the two of you starts your walk towards the school."
    show fb_mi_school_04
    mi "Ah, the thing is, I saw a thief trying to steal this lady's handbag when I was about to get here..."

    menu:
        "Did you catch them?":
            $ midoriya.set_affection("+", 1)
            mc "Did you catch them?"
            mi "I-I did, actually..."
            mc "That's amazing, [nickname_mi]!"
            show fb_mi_school_04 shy_02
            "The green haired boy's blush deepen by your praise."
            mi "No, ah, I was just lucky they were careless! Since it's early morning and the area was fairly deserted, I bet they didn't think an aspiring hero was nearby!"
            show fb_mi_school_04
            mi "I think they were trying to keep a low profile, too, since they didn't put up too much of a fight when I managed to apprehend them."

        "Did they get caught?":
            mc "Did they get caught?"
            show fb_mi_school_04 happy_01
            mi "Yes! I apprehended them and handed them over to the police safely!"

    show fb_mi_school_04 sorry_01
    mi "But because of all that, I got here later than expected..."
    "You chuckle and wave your hand aimlessly to show that you don't mind at all."
    show fb_mi_school_04 oh_01
    "The action causes your friend to gasp, and he points shakily at your bandaged arm, voice teetering near his usual panicky edge."
    mi "T-T-The bandages! That's right! How's your arm...?"
    mc "Not a hundred percent back to normal, but no worries! "
    show fb_mi_school_04 sorry_01
    mi "Really? Does it not hurt?"
    "With a softer smile and a more sincere tone, you stretch both of your upper limbs in front of you."
    mc "Nope! See? I wouldn't be moving it around if it hurt!"
    show fb_mi_school_04 shy_02
    mi "... Okay, I believe you."
    mi "I hope it heals completely soon!"
    show fb_mi_school_04
    mi "Oh, by the way!"
    mi "Don't we have another Hero Lesson class this morning? Are you planning to participate in it?"

    menu:
        "Hell yeah!":
            mc "Hell yeah!"
            mc "I can't wait to get into some kickass actions!"
            show fb_mi_school_04 worried_03
            "The freckled boy looks conflicted at your enthusiasm, and for a moment he's reminded of his short-tempered, brash childhood friend."
            mi "Um... Don't force yourself, okay?"
            mc "I won't, I won't!"
            "You give him an optimistic smile in hope to reassure his worry."

        "It depends, I guess?":
            $ midoriya.set_affection("+", 1)
            mc "It depends, I guess?"
            mc "If it's the usual one-on-one sparring like yesterday, I might skip and opt for watching instead, since there's nothing to be learned if I just get myself beaten up."
            mc "But I'm interested in tag team matches. You know my Quirk, it's best used for support and it would be a better option to train that while I can't give my all in physical combat."
            show fb_mi_school_04 happy_01
            "Your friend smiles and nods in agreement, glad that you're thinking rationally despite your defeat yesterday."

    mc "That being said..."
    show fb_mi_school_04
    mc "You better not let your guard down! I can still kick your butt in Hero Lesson if I want to! And this time I won't lose!!"
    show fb_mi_school_04 determined_01
    mi "Ah! Bring it on! I won't lose that easily, either!"
    show fb_mi_school_04 happy_01
    "You grin and punch your friend's back playfully."
    "If there's any proof that Midoriya has grown ever since you met him the first time, it's this newfound confidence of his."
    "And the fire in his eyes suits him."
    "You're really looking forward to the Hero Lesson class today."

    jump day1_afternoon


############################ Event 2 scene - Bakugou ###########################
label event2_bk:
    show fb_bk_school_04 with dissolve

    mc "All hail King Explosion Murder!"
    show fb_bk_school_04 annoyed_03
    "A few feet away, Bakugou stares at you with that 'what-the-fuck' signature expression of his."
    bk "Haah?"
    mc "What? It’s your hero name! Right?"
    show fb_bk_school_04
    bk "You’re a fucking idiot."
    "You tap your chin thoughtfully, scrunching your eyebrows together as if you’re in the middle of solving a really difficult, college-level mathematical problem."
    mc "Well, don’t you think intellectually challenged people only gather with others who posesses similar intelligence level like them? In that case, since you’re willingly hanging out with me—"
    show fb_bk_school_04 angry_02
    bk "I ain’t hanging out with you! My mom made me do this!!"
    show fb_bk_school_04

    menu:
        "Sure, Mama's Boy.":
            $ bakugou.set_affection("+", 1)
            mc "Sure, Mama's Boy."
            show fb_bk_school_04 angry_02
            bk "YOU WANNA GO?!! HUH?!!?!"
            "You skillfully dodge away from the spitfest Bakugou has graciously bestowed upon your mortal being."
            mc "I’ll pass for now! Arm’s not healed yet!"

        "Aw, even though we trained together yesterday?":
            mc "Aw, even though we trained together yesterday?"

    show fb_bk_school_04 um_01
    "His flaming furious eyes dims at your words, and he gruffly stuck his hands down the pockets of his lowly hanging schoolpants."

    show fb_bk_school_04
    bk "Speaking of. How’s it feel?"

    menu:
        "What, my arm?":
            mc "What, my arm?"
            bk "Unless you tripped over shit and injured yourself more on the way home yesterday..."
            "You chuckle at the tone of his comment which doesn’t sound as malicious as its actual words."

        "What, my heart?":
            $ bakugou.set_affection("+", 1)
            mc "What, my heart?"
            show fb_bk_school_04 annoyed_03
            bk "Did you bash your head against your door today or what?! Your arm, moron!"
            mc "Well now my heart {i}hurts{/i}."
            "You fake a forlorn look only to be replied by annoyed grumbling from your friend."

    show fb_bk_school_04
    "Smiling in amusement, you step forward and shows Bakugou your bandaged arm, before executing some basic movements here and there."
    mc "My arm’s fine. Doesn’t hurt that bad and it’s healing great. I just have to take precautions so it doesn’t scar."
    "Thinking back at the sparring match yesterday, you wince as you remember how reckless you were being, charging heads-on to take on {b}the{/b} Bakugou Katsuki, who particularly excels in close combat."
    mc "At close range, your explosions really packs a punch."
    show fb_bk_school_04 um_01
    "You turn towards the blond, expecting a cocky comeback, but is greeted with an unusually silent Bakugou."
    bk "...."
    show fb_bk_school_04
    mc "I mean, it’s cool, you know! I’m not mad or anything!"
    mc "{b}I{/b} was the one who asked you to spar with me, and {b}I{/b} was the one who was reckless enough to charge in!"
    mc "So, um..."

    menu:
        "Thanks for not holding back.":
            $ bakugou.set_affection("+", 2)
            mc "Thanks for not holding back."
            show fb_bk_school_04 angry_02
            bk "Are you an idiot?!!"
            show fb_bk_school_04 um_01
            bk "Tch. Whatever. Of course you’d say that..."

        "Sorry if I made you worry or anything!":
            mc "Sorry if I made you worry or anything!"
            show fb_bk_school_04 angry_02
            bk "HAA?!! Worried?! Who’s worried about who!?!"
            bk "I sure ain’t worrying about you! A mere extra like you!!"
            mc "Riiiight..."

    show fb_bk_school_04 at left:
        xoffset 100
    with easeinleft
    pause 0.1
    hide fb_bk_school_04 with moveoutleft
    "The explosive male slipped past you, grumbling under his breath and stomping away with that slouched back as usual."

    "You smile."
    "The normal Bakugou would’ve rudely barrelled past you without care."
    "But just now he had purposely avoided your still healing arm."

    mc "Wait, King Explosion Murder~"
    show fb_bk_school_04 angry_01 at left:
        xoffset 100
    with easeinleft
    bk "FUCK OFF, STUPID CROSSHAIR EYES!!"
    hide fb_bk_school_04 with moveoutleft

    jump day1_afternoon


########################### Event 2 scene - Todoroki ###########################
label event2_ts:
    show fb_ts_school_04 with dissolve

    mc "Morning!"
    "You call out casually to the boy."
    "Todoroki nods in response and replies with a more toned down tone."
    ts "Hello."
    "The two of you settles easily into a steady walking pace."
    "Your classmate is considerate enough to give you the inner side of the street, and for a moment you’re touched by how unusually chivalrious he tries to be today."
    "As if he feels like he {i}needs{/i} to be, to make up for something."
    "You pick up the peculiarity of his actions easily, given how much more observational you could be towards the objects of your interest."

    menu:
        "Wow, bedhead.":
            $ todoroki.set_affection("+", 2)
            mc "Wow, bedhead."
            show fb_ts_school_04 question_01
            "Todoroki blinks in surprise at your accusation and reaches up to feel his hair."
            show fb_ts_school_04 confused_03
            "He gives you a confused look when nothing feels out of place."
            mc "Haha, I was kidding! You’re as neat as usual, [nickname_ts]!"
            show fb_ts_school_04 oh_03
            "You flash him a smile, and he relaxes, expression softening at your attempt to make him feel less guilty."
            show fb_ts_school_04
            ts "So..."

        "....":
            mc "...."
            show fb_ts_school_04 um_01
            ts "...."
            mc "...."
            "Well, this is a bad start to your morning."
            mc "You know, today’s sun is really bright."
            show fb_ts_school_04
            ts "Yeah."
            "...."
            mc "...."
            show fb_ts_school_04 um_01
            ts "...."
            "Wow, good job [firstName]. You’ve unlocked the awkwardness trophy."
            show fb_ts_school_04
            ts "Um..."
            mc "Yes?!"
            "You leap at the opportunity to create a conversation. Anything but this awkward atmosphere!"

    ts "How’s your arm?"
    mc "Ah!"
    show fb_ts_school_04 guilty_01
    "You show him your bandaged right arm, and for a moment Todoroki's calm expression shift into guilt."
    show fb_ts_school_04
    "However, as you start to show him how you’re having zero troubles moving the entirety of your right appendage, you can see that his frown starts to dissipate."
    mc "See, almost healed now! It doesn’t hurt that much when I move them."
    mc "I just applied some ointment this morning, so it should help with the recovery! Besides, yesterday Recovery Girl said there won’t be any scars or anything, so it's all good!"
    show fb_ts_school_04 um_01
    "Todoroki nods at your explanation, but he still looks a tad downcast."
    ts "Still, I’m sorry."
    ts "For... Losing control of my left side."

    menu:
        "Yeah, I managed to make you panic a little, didn't I?":
            $ todoroki.set_affection("+", 1)
            mc "Yeah, I managed to make you panic a little, didn't I?"
            show fb_ts_school_04 oh_01
            ts "You really did."
            show fb_ts_school_04
            "The both of you thought back to the training session yesterday."
            ts "I didn't think you would take the initiative to pull me into close range combat."
            mc "Yeah, but that didn't end well. I guess I need to think of another strategy against your super-offensive quirk..."
            ts ".... Sorry."

        "Were you surprised?":
            mc "Were you surprised?"
            show fb_ts_school_04 question_01
            ts "Surprised?"
            mc "Cause I was braver than you expected!"
            "He gives you a nonplussed look."
            show fb_ts_school_04 guilty_01
            ts "More like reckless."
            show fb_ts_school_04
            "You scratch your cheek in embarrassment. Though it was the truth, being told that so bluntly never feels good."
            mc "Well, I had to find a chance to make you drop your guard somehow...."
            show fb_ts_school_04 um_01
            ts "You succeded in that part, but I don't think it was a good decision to make."
            show fb_ts_school_04
            ts "Still, I was at fault too. I'm sorry."

    mc "It's fine, it was a learning experience for me!"
    show fb_ts_school_04 um_01
    "You glance at your companion, who still doesn't seem satisfied at himself."
    mc "... But hey, if you insist, you can make it up to me?"
    show fb_ts_school_04 oh_01
    ts "Yes."
    show fb_ts_school_04
    "Inwardly, you giggle at how earnest he looks when you presented an opportunity for him to redeem himself."

    menu:
        "Let me slap your wrist once, and we'll call it even?":
            mc "Let me slap your wrist once, and we'll call it even?"
            show fb_ts_school_04 oh_01
            "At the suggestion, a grimace twists his features, and his dual colored eyes reflects deep pain."
            show fb_ts_school_04 um_01
            "Instantly, you regret suggesting the physical punishment."
            "You know that look. Traumas are deeply ingrained in people and it seems like you've stepped onto a landmine."
            show fb_ts_school_04
            mc "Actually, that's not a fair trade at all!"
            mc "How about.... Partnering up with me if today's Hero Lesson class consists of tag team battle?"
            ts "That's better."

        "If today's first period is a team battle, partner up with me?":
            $ todoroki.set_affection("+", 1)
            mc "If today's first period is a team battle, partner up with me?"
            ts "Deal."
            mc ".... Eh? That easy?!"
            "Todoroki nods, and he looks very sure of himself, you can't help but feel flattered."
            ts "Out of everyone in 1-A, you have the best supportive ability. I've always wanted to try teaming up with you to see how well we can work together."

    "To express your appreciation, you give Todoroki a playful wink and a pair of finger guns."
    show fb_ts_school_04 oh_03
    "He doesn’t seem to know how to reply to that, but the amused chuckle coming from him is enough for you. Honestly, making Todoroki Shouto smile is an achievement in itself! You should be proud!"
    show fb_ts_school_04
    "The rest of the walk is mainly one sided, with you chattering away and your friend listening dedicatedly, only partaking when he has to."
    "You're really looking forward to the Hero Lesson class today."

    jump day1_afternoon


######################### Continue to afternoon scene ##########################
label day1_afternoon:
    stop music fadeout 1.0

    scene bg_black with dissolve
    play sound "audio/se/schoolbell_chime.mp3"
    pause 7
    scene bg_school_gymgamma with dissolve
    show fb_as_school_01 with dissolve
    play music "audio/music/shadow.mp3" fadein 1.0

    as_sensei "Alright, kids... Hero Lesson. Sparring matches. You know the drill."
    as_sensei "We're doing team battles today. Grab anyone and get it done. I'll be making rounds to check on your groups."
    as_sensei "Don't get ahead of yourself and remember that this is just training."
    as_sensei "I'm talking especially to you, [lastName]. After that stunt you did yesterday, I'll be observing you closely today."
    "Under your teacher's steely gaze, you grin sheepishly and nod."
    mc "Yessir!"
    hide fb_as_school_01 with dissolve

    "Almost immediately, everyone was forming teams."
    "You stretch your arms above your head, and out of the corner of your eyes, you spot your usual partner looking at you."
    "But before you can call out to her, someone tapped your shoulder to gain your attention."

    if route == "mi":
        jump event3_mi
    if route == "bk":
        jump event3_bk
    if route == "ts":
        jump event3_ts
    else:
        jump day1_evening


########################### Event 3 scene - Midoriya ###########################
label event3_mi:
    show fb_mi_hero_03 shy_02 with dissolve
    mi "[lastName]-san! Um, will you team up with me?"

    menu:
        "Hmmm, what to do...":
            $ midoriya.set_affection("+", 2)
            mc "Hmmm, what to do..."
            show fb_mi_hero_03 worried_01
            "You fake a condescending attitude, arms crossed and a finger tapping on your chin as you act as if you're weighing your options."
            mi "Ahh, no pressure, though!"
            mi "I just thought that, uhm, since it’s my fault you got injured, I should at least team up with you to make sure you won't get hurt further..."
            mc "Yeah, okay."
            mi "It’s totally fine if you refuse! I understand— Eh?"
            show fb_mi_hero_03 um_01
            "Tilting your head, you give the poor clueless boy a mischievous grin, waiting for him to figure it out."
            show fb_mi_hero_03 oh_03
            mi "... Ah."
            show fb_mi_hero_03 annoyed_01
            mi "[lastName]-san! I thought you were being serious!"
            "Midoriya looks like a splitting image of an annoyed pomeranian as he crosses his arms on his chest, and you can’t help but giggle at the adorable display."
            mc "Sorry, [nickname_mi], I couldn't help myself!"

        "I was about to ask you!":
            $ midoriya.set_affection("+", 1)
            mc "I was about to ask you!"
            show fb_mi_hero_03 happy_01
            mi "O-Oh, really?"
            "The relieved smile bloomed on your teammate's lips."

    show fb_mi_hero_03 oh_01
    mi "Is Nai-san okay with this, though?"
    "You scan the training grounds briefly and find your usual team member silently hovering by a small group consisting of Jirou, Kouda, and Ojiro."
    mc "Yeah, she'll be fine!"
    show fb_mi_hero_03 happy_01
    mi "Okay. Any idea who should we group with?"

    play music "audio/music/delusion.mp3" fadein 1.0

    show fb_ke_hero_01 at left with easeinright
    show fb_ts_hero_01 at right with easeinright
    show fb_mi_hero_03 oh_01
    ke "Yo, Midoriya, [lastName]!!"
    show fb_mi_hero_03
    show fb_ke_hero_01 determined_02
    ke "Wanna duke it out with us?"
    "Kirishima and Todoroki stands before both of you, and you smile in greeting at the two."
    show fb_ke_hero_01
    show fb_mi_hero_03 excited_01
    mi "Eh? Kirishima-kun, you're pairing with Todoroki-kun today? What an unlikely combination!"
    "Everyone can see the sparkles in Midoriya's eyes, and you know your answer was set in stone."

    menu:
        "I'm in! This sounds like an interesting match!":
            $ midoriya.set_affection("+", 2)
            mc "I'm in! This sounds like an interesting match!"
            mi "Me too! I'm so looking forward to see how the two of you will battle! Kirishima-kun is always with Kacchan, so it's going to be really cool to get a different set of data entirely!"
            show fb_mi_hero_03
            mc "On that topic, where's Bakugou-kun?"
            show fb_ke_hero_01 wink_01
            ke "I left Kaminari to deal with him. Gotta look for a different experience sometimes, y'know?"
            mc "In other words, you're tired of babysitting him, so you went to Todoroki-kun for shelter. I see how it is!"
            show fb_ke_hero_01 laugh_01
            show fb_ts_hero_01 confused_02
            ts ".... I'm a shelter?"
            show fb_ts_hero_01
            show fb_ke_hero_01

        "We'll show you what 'teamwork' is!":
            mc "We'll show you what 'teamwork' is!"
            show fb_mi_hero_03 determined_01
            mi "Y-Y-Yeah!"
            mc "A little shaky there, partner."
            show fb_mi_hero_03 worried_03
            mi "I mean! We'llshowyouwhatteamworkis!!"
            show fb_mi_hero_03 sorry_01
            mc "... What he said!"

    show fb_mi_hero_03
    mc "Anyway, if we're okay with this, should we take a block and get started?"
    "All of them agrees at your suggestion, and the four of you moves into an empty area."

    stop music

    scene bg_black with dissolve
    pause 2
    play audio "audio/se/whistle.ogg"
    scene bg_school_gymgamma with dissolve
    pause 2

    play music "audio/music/shadow.mp3" fadein 1.0

    show fb_ts_hero_01 at left with dissolve
    "At the sound of the whistle, your finger freezes on the gun's trigger."
    mc "So... That's a draw?"
    show fb_ts_hero_01 oh_03 at center with easeinright
    "Todoroki flinches, and upon spotting you hiding behind the ice he had previously created, he eyes your weapon warily."
    show fb_ts_hero_01
    ts "Were you about to shoot me?"
    "Offering him an apologetic smile, you nod in confirmation."
    mc "With a tranquilizer, yeah."
    show fb_ts_hero_01 oh_01
    ts "... So it was that kind of plan."
    show fb_ts_hero_01 at right with easeinright
    "Todoroki leans onto the pillars of ice he had created all over the fields in an attempt to trap you and Midoriya previously and starts to melt them down."
    mi "Ah, there they are! Todoroki-kun, [lastName]-san!"
    show fb_mi_hero_03 at center with easeinleft
    show fb_ke_hero_01 at left with easeinleft
    "The two of you spot your team mates running towards you, and immediately you wave at Midoriya with an apologetic grin."
    mc "Hey! Sorry, I failed!"
    show fb_mi_hero_03 worried_01
    mi "I guess our strategy didn't work?"
    ts "It almost succeeded, actually."
    $ midoriya.set_affection("+", 1)
    show fb_mi_hero_03 oh_02
    "Your teammate beams at you in awe."
    mi "Really?! Wow, [lastName]-san! Your {i}Stealth{/i} skill is amazing!"
    show fb_mi_hero_03 happy_01
    "With a cheerful wink, you grin proudly. It sure is nice to get some praises for your hard work in pulling those all nighters gaming session and researching!"
    mc "All thanks to Assassin's Creed!"
    show fb_ke_hero_01 sorry_01
    show fb_mi_hero_03
    ke "I'm so envious of your Quirk, man."
    show fb_ke_hero_01
    "You laugh at how envious Kirishima looks and decides to take his words as a compliment."
    "With that, the four of you slowly walk towards the rest of your classmates, which was starting to form a group in front of Aizawa-sensei."

    jump after_event3


########################### Event 3 scene - Bakugou ###########################
label event3_bk:
    show fb_bk_hero_02 with dissolve
    bk "Oi, crosshair bastard."

    menu:
        "Yo, explosion death murder bastard.":
            $ bakugou.set_affection("+", 2)
            mc "Yo, explosion death murder bastard."
            show fb_bk_hero_02 angry_02
            "Bakugou visibly bristled at your comeback, but he somehow managed to hold himself back from exploding you to bits when Aizawa-sensei's gaze wandered in your general direction."
            show fb_bk_hero_02
            bk "Don't make me regret coming up to you, fuckwad."
            mc "What, don't tell me you want to team up with me?"
            "Before the blond can answer, one of your classmates slipped easily onto your conversation."

        "Can't you just be nice for one second, geez.":
            mc "Can't you just be nice for one second, geez."
            show fb_bk_hero_02 annoyed_03
            bk "Why do I gotta be all nice and shit to you? You're not some kind of weakling."
            mc "Oh my, I'm so flattered."
            show fb_bk_hero_02 angry_02
            bk "I WASN'T PRAISING YOU!"
            "Before you can retort, one of your classmates slipped easily onto your conversation."

    show fb_ke_hero_01 wink_01 at center behind fb_bk_hero_02:
        xoffset -250
    with easeinleft
    ke "Hey, [lastName]!"
    "Kirishima greets you cheerfully as he slung an arm around Bakugou's shoulder."
    show fb_bk_hero_02 annoyed_03
    "For a moment, you're envious of his Quirk for allowing him to do that."
    mc "Heya, Kirishima-kun!"
    show fb_bk_hero_02
    show fb_ke_hero_01 happy_01
    ke "Hey, Bakugou, dude, we're teaming up, right? [lastName], who're you pairing up with? Should we--"

    show fb_bk_hero_02 angry_02 at center:
        xoffset 250
    with easeinright
    show fb_bk_hero_02 angry_02 at center:
        xoffset 0
    show fb_ke_hero_01 oh_01 at left:
        xoffset 0
    with easeinleft
    bk "Will you stop ordering people around, hair-for-brains?! I ain't teaming up with you today! I'm making sure this idiot won't get beaten up again like yesterday!"
    show fb_ke_hero_01
    "You beam at the declaration. Man, what a cactus. He could've just asked!"
    show fb_bk_hero_02
    show fb_ke_hero_01 oh_02
    ke "Wait, what, really?! You're teaming up?"
    show fb_bk_hero_02 surprised_02:
        parallel:
            ease .5 zoom 1.3 yoffset 150
    "You bravely push your shoulder towards your official party member for today and flash a smug grin at the red haired boy."
    mc "Yup! You didn't know? We're best friends now!"
    show fb_ke_hero_01 excited_01
    "Kirishima gasps and you could swore you saw tears in his eyes."
    ke "Duuude!! You're making best friends now! I'm so proud of you!"
    show fb_bk_hero_02:
        parallel:
            ease .2 zoom 1.0 yoffset 0
    show fb_ke_hero_01
    bk "SHUT UP, WE'RE NOT BEST FRIENDS!!"
    mc "He's just embarrassed."
    show fb_ke_hero_01 wink_01
    ke "Yeah, I know. Great job befriending Bakugou, [lastName]!"
    mc "Dude, it was nothing."
    show fb_ke_hero_01 excited_01
    show fb_bk_hero_02 angry_01
    bk "OI, ARE YOU IGNORING ME?!"
    show fb_ke_hero_01 excited_01
    show fb_bk_hero_02
    "You spare the fuming Bakugou one last playful smirk before focusing back to your sharp teethed friend."
    show fb_ke_hero_01
    mc "So, should we get one more person?"
    ke "Yeah! So it'll be Bakugou-[lastName], versus..."
    "Kirishima looks around in curiosity and you can visibly see his expression lighten up when he finds a candidate."
    hide fb_ke_hero_01 with moveoutleft
    "Swiftly, he jogs towards his team member and returns within a few seconds, dragging a certain green haired boy."

    play music "audio/music/delusion.mp3" fadein 1.0

    show fb_ke_hero_01 at left
    show fb_mi_hero_03 shy_02 at right
    with easeinleft
    show fb_bk_hero_02 oh_03
    "You're pretty sure Bakugou is going to have your head if you don't win this match."
    show fb_ke_hero_01 wink_01
    show fb_bk_hero_02
    ke "Bakugou-[lastName] versus Kirishima-Midoriya! How's that sound?"
    show fb_mi_hero_03 shy_01
    mi "H-Hi, Kacchan, [lastName]-san..."
    show fb_ke_hero_01
    show fb_bk_hero_02 evil_01
    show fb_mi_hero_03 sorry_01
    bk "Now we're talking! You better prepare yourself, Deku! We're going to sweep the floor with your asses!!"
    "At least this match will be an interesting one, you try think optimistically to yourself as the four of you moves into an empty block."

    stop music

    scene bg_black with dissolve
    pause 2
    play audio "audio/se/whistle.ogg"
    scene bg_school_gymgamma with dissolve
    pause 2

    play music "audio/music/shadow.mp3" fadein 1.0

    show fb_bk_hero_02 with dissolve
    mc "My body hurts...."
    bk "Tch, you need stamina training, you weakass shit."
    "With a scowl, you force your throbbing arm to lift your body off the ground."
    show fb_bk_hero_02:
        parallel:
            ease .5 zoom 1.3 yoffset 150
    "For a moment, you wobble unsteadily on your feet, but Bakugou grabbed you before you could faceplant onto the ground."
    show fb_bk_hero_02:
        parallel:
            ease .5 zoom 1.0 yoffset 0
    show fb_ke_hero_01 at left:
        xoffset 200
    show fb_mi_hero_03 at left
    with dissolve
    "Midoriya was almost in the same state as you, one arm slung around Kirishima's shoulder as the latter helped him to walk towards you."
    show fb_ke_hero_01 worried_02
    ke "Sorry, [lastName]! I punched you real hard, huh?"
    "To the point till it hurts to breathe, yes."
    mc "It's fine, it's cool, no problemo."
    mc "Midoriya-kun is in a worse state, I think."
    $ bakugou.set_affection("+", 1)
    show fb_ke_hero_01
    show fb_mi_hero_03 worried_02
    mi "I-I'm fine!"
    mc "Seriously? You broke your right leg."
    mi "I've been through worse..."
    "Midoriya grins weakly and you grimace."
    show fb_ke_hero_01
    show fb_mi_hero_03

    menu:
        "I know we're on the same team, but man, Bakugou-kun, you sure can... \"break\" a leg.":
            $ bakugou.set_affection("+", 1)
            mc "I know we're on the same team, but man, Bakugou-kun, you sure can... \"break\" a leg."
            show fb_bk_hero_02 angry_02
            bk "OI, DON'T MAKE IT SOUND LIKE I BROKE THE DIMWIT'S LEG ON PURPOSE!!"
            mc "I mean, you did?"
            bk "HE DID THAT TO HIMSELF!"
            show fb_mi_hero_03 sad_01

        "(Don't say anything)":
            pass

    show fb_mi_hero_03 oh_01
    show fb_ke_hero_01 oh_01
    show fb_bk_hero_02 oh_01
    "Everyone suddenly pauses, and you reply the three pairs of eyes zeroing in on you with a confused head tilt."
    ke "Uhhh [lastName]? Your nose's bleeding."
    show fb_mi_hero_03 worried_03
    show fb_ke_hero_01 worried_02
    show fb_bk_hero_02
    mc "Oh, really?"
    ke "Okay, guys, let's quickly wrap this up and get the two of you treated!"
    hide fb_mi_hero_03
    hide fb_ke_hero_01
    with moveoutleft
    "You try to take an unsteady step forward and groan."
    mc "Bakugou-kun, a little help please!"
    show fb_bk_hero_02 angry_01
    bk "GOD, YOU'RE SO ANNOYING!!"
    hide fb_bk_hero_02
    with moveoutleft

    pause 1.0

    jump after_event3


########################### Event 3 scene - Todoroki ###########################
label event3_ts:
    show fb_ts_hero_01 with dissolve
    ts "If the offer from this morning still stands, partner up with me?"

    menu:
        "The offer has no expiry date and can be extended indefinitely, pardner.":
            $ todoroki.set_affection("+", 2)
            mc "The offer has no expiry date and can be extended indefinitely, pardner."
            show fb_ts_hero_01 happy_02
            "The corner of the half-hot-half-cold quirk user's lips tugged upwards."
            ts "How reassuring. I might consider that option if we manage to do well today."
            show fb_ts_hero_01
            "A wide grin stretch your lips. It was rare for {i}the{/i} Todoroki to play along with your random silliness, but it seems like your childish side is rubbing off him well."
            mc "Well now, that means we've gotta win today, huh?"

        "Sure!":
            mc "Sure!"
            "Todoroki nods in confirmation and looks around the training arena."

    ts "Do you have anyone you're interested to train with?"

    menu:
        "Hmmm... Bakugou-kun, maybe?":
            $ todoroki.set_affection("+", 1)
            mc "Hmmm... Bakugou-kun, maybe?"
            ts "Fine with me, but are you sure you'll be okay?"
            mc "I've got a good team, so I'm feeling pretty confident today!"
            show fb_ts_hero_01 happy_02
            "You're answered with a determined nod and a level headed reply, as what you would expect of Todoroki."
            ts "I'll be sure to live up to your expectations."
            show fb_ts_hero_01
            "You scan the perimeter and spot two distinct hair colors standing close to each other."

        "Kirishima-kun, maybe?":
            $ todoroki.set_affection("+", 1)
            mc "Kirishima-kun, maybe?"
            ts "Okay. I think he's teamed up with Bakugou again."
            "Following your friend's line of sight, you find the two boys seemingly in the middle of bickering."
            "But then again, when is Bakugou not arguing with other people?"

    hide fb_ts_hero_01
    with moveoutright
    show fb_bk_hero_02 angry_02 at left
    show fb_ke_hero_01 at center
    with easeinleft

    "You wave to try and catch the yellow haired male's attention. Unfortunately, you receive nothing more than a scowl from a seemingly eternally upset Bakugou."
    hide fb_bk_hero_02
    hide fb_ke_hero_01
    with moveoutleft
    show fb_ts_hero_01 oh_01 at right with easeinright
    "With an annoyed huff, you grab on Todoroki's hand before marching resolutely towards the duo."
    show fb_ts_hero_01 worried_02
    "The tips of Todoroki's ears redden, but since you were literally dragging him forward, you don't notice."

    play music "audio/music/delusion.mp3" fadein 1.0

    show fb_ts_hero_01 at center
    show fb_bk_hero_02 at left
    show fb_ke_hero_01 at right
    with easeinleft
    mc "Kirishima-kun, Bakugou-kun, are you teamed up?"
    show fb_ke_hero_01 wink_01
    ke "Yo! Yeah, we are! I mean, who else can team up with this guy but me?"
    ke "Wanna try taking us on?"
    show fb_ke_hero_01
    mc "That's the plan!"
    show fb_bk_hero_02 annoyed_03
    bk "You're a team? What a weird-ass combination."
    show fb_bk_hero_02 evil_01
    bk "Don't come crying to us when you get your asses beat, fuckwads!"
    "You give Bakugou a challenging smirk as your group start to move towards an empty block."
    mc "Likewise, you insufferable ass!"

    stop music

    scene bg_black with dissolve
    pause 2
    play audio "audio/se/whistle.ogg"
    scene bg_school_gymgamma with dissolve
    pause 2

    play music "audio/music/shadow.mp3" fadein 1.0

    show fb_as_school_01 at right with dissolve
    as_sensei "That's enough, four of you!"
    "Your legs give out and you collapse onto the ground with a tired whine."
    as_sensei "[lastName]."
    "Uh oh."
    mc "Yes, sensei?"
    as_sensei "...."
    as_sensei "Good work today."
    "A wide grin bloom on your expression. You're pretty sure the muscles in your legs are screaming in pain, but it was worth it you suppose."
    show fb_ts_hero_01 at left with easeinleft
    as_sensei "Todoroki, you too. It seems you two work quite well together."
    ts "Yeah."
    "Todoroki is sitting a few steps away from you, just as beaten up as you were, although none of your injuries were serious."
    "You had a few singed hair and bruises, while your friend sported a few of the same injuries himself, coupled with multiple cuts on his skin - courtesy of dealing with Kirishima heads on."

    hide fb_as_school_01 with moveoutright
    show fb_ts_hero_01 at center
    show fb_bk_hero_02 angry_02 at left
    show fb_ke_hero_01 sad_01 at right
    with easeinleft
    ke "Aw man! I can't believe we didn't win!"
    bk "IT'S BECAUSE YOU KEPT PLAYING AROUND, DAMN IT!!"
    show fb_ke_hero_01 annoyed_02
    ke "Hey, I wasn't playing around! You were the one who got distracted by [lastName]!"
    show fb_bk_hero_02 angry_01
    bk "I WASN'T DISTRACTED!!! YOU WERE THE ONE WHO GOT CAUGHT IN THE ICE AND COULDN'T GET OUT!!"
    "You laugh softly at the bickering that was going on in the background."
    show fb_bk_hero_02
    show fb_ke_hero_01
    show fb_ts_hero_01:
        parallel:
            ease .5 zoom 1.3 yoffset 350
    "A hand appears before you, and you smile gratefully to Todoroki as he grabbed our hand to pull you up."
    show fb_ts_hero_01:
        parallel:
            ease .5 zoom 1.0 yoffset 0
    mc "Phew, all that taunting and running around gets really tiring after a while..."
    "While you had managed to not overuse your injured arm, you're sure your muscles are going to be so sore tomorrow."
    $ todoroki.set_affection("+", 1)
    ts "Just a little more and we could've won."
    mc "I know, right? We make quite a good pair, don't you think?"
    show fb_ts_hero_01 happy_02
    "Todoroki wordlessly gives you a tiny smile, and suddenly you're very interested to see what kind of face he'll show you if you do manage to win on the next team battle."

    jump after_event3


######################### After afternoon scene ##########################
label after_event3:
    show fb_ts_hero_01 at left:
        xoffset -100
    show fb_ke_hero_01 at left behind fb_ts_hero_01:
        xoffset 100
    show fb_mi_hero_03 at left behind fb_ke_hero_01:
        xoffset 300
    show fb_bk_hero_02 at left behind fb_mi_hero_03:
        xoffset 500
    with easeinleft

    show fb_as_school_01 at right with easeinright

    as_sensei "Anyone who's hurt can go see Recovery Girl and get yourself treated for the major wounds."
    as_sensei "Otherwise, go get changed. I expect you all to be back to class after lunch for the review session."
    as_sensei "That's all! Dismissed!"

    stop music

    scene bg_black with dissolve
    pause 1
    play sound "audio/se/schoolbell_chime.mp3"
    pause 4
    scene bg_school_classroom with dissolve
    pause 5

    "You stifle a big yawn as Iida instructs everyone to rise and bow to Ectoplasm-sensei, whom you swore had some secret second quirk that lulls you into sleep with his voice."
    ".... Or maybe you're just bad at Maths."
    ".......... Or you just really badly {b}{i}desperately{/i}{/b} need sleep."

    play music "audio/music/sweet.mp3" fadein 1.0
    if route == "mi":
        jump event4_mi
    if route == "bk":
        jump event4_bk
    if route == "ts":
        jump event4_ts
    else:
        jump day1_evening


########################### Event 4 scene - Midoriya ###########################
label event4_mi:
    show fb_mi_school_05 worried_02 with dissolve
    mi "Are you okay, [lastName]-san? You look really tired..."

    $ mi_affection = midoriya.get_affection()
    $ option_name = "Carry me home, please?"
    if mi_affection < 10:
        $ option_name = "Carry me home, please? (Locked)"
    menu:
        "[option_name]" if mi_affection == 10:
            mc "Carry me home, please?"
            show fb_mi_school_05 worried_03
            mi "E-Ehh?! I mean, well, if you're tired, um, I mean, I usually wouldn't mind, but I have prior appointment with All Might after this and my mom messaged me and she wants me to get some groceries and I don't think the time will allow it even if I--"
            "Oh, there's the infamous Midoriya Rambles™."
            mc "[nickname_mi]! Calm down! It was a joke!"
            show fb_mi_school_05 oh_03
            pause 1
            show fb_mi_school_05 sad_03 with dissolve
            mi  ".... Oh."
            "Oh no, why does he look so sad??!"
            mc "But you know! If you don't mind! We should totally walk home together sometime!"
            show fb_mi_school_05 oh_01
            "Did that sound natural? You really hope it did, and you didn't sound like a creep who's looking forward too much to hang out more with him."
            show fb_mi_school_05 happy_01
            mi "Yeah! I'd like that!"
            mc "Good! Next time!"
            show fb_mi_school_05 excited_01
            mi "Next time!"
            "At the back of your brain, you squish the budding feeling that wishes this 'next time' would be some time soon."
            mc "Mhm! You should probably go to that appointment! Don't want to keep All Might waiting for you!"
            show fb_mi_school_05 oh_01
            mi "You're right! I'll see you tomorrow, [lastName]-san!!"
            show fb_mi_school_05 happy_01
            mc "Bye, [nickname_mi]!"
            hide fb_mi_school_05 with dissolve
            "You sigh nervously once the green haired boy exited the classroom."
            "You're pretty sure that boy's adorableness is going to kill you someday."
            $ persistent.saw_trueend_mi = True

        "Yeah, I'm okay!":
            mc "Yeah, I'm-"
            "A big yawn escapes your mouth and your cheeks warms a little in embarrassment."
            mc "--okay!"
            show fb_mi_school_05 worried_03
            mi "Are you sure? You look like you'll pass out anytime soon..."
            mi "Should I get Nai-san?"
            mc "No, no, I'll be fine!"
            show fb_mi_school_05
            mi "If you say so..."
            show fb_mi_school_05 worried_01
            mi "Then, I'll be going first! See you tomorrow, [lastName]-san!"
            mc "See you!"
            hide fb_mi_school_05 with dissolve
            "Holding back more yawns that seem to be unending, you start to pack your belongings."

    jump day1_evening


########################### Event 4 scene - Bakugou ###########################
label event4_bk:
    show fb_bk_school_05 with dissolve
    "Few seats from you, Bakugou stands up and slings his bag over his shoulder like the punk he is."

    $ bk_affection = bakugou.get_affection()
    $ option_name = "Bakugou-kun! Carry me home, please?"
    if bk_affection < 10:
        $ option_name = "Bakugou-kun! Carry me home, please? (Locked)"
    menu:
        "[option_name]" if bk_affection == 10:
            mc "Bakugou-kun! Carry me home, please?"
            show fb_bk_school_05 surprised_02
            bk "WH--HELL NO!"
            show fb_bk_school_05
            mc "But why not?"
            show fb_bk_school_05 angry_02
            bk "Why should I?!"
            mc "Cause I want you to?"
            bk "I've walked you to school this morning, what more do you want from me?!"
            mc "A piggyback?"
            bk "Ahh?!! How about I explode you to bits and bring your ashes home!"
            mc "Nooo! I'm too young to die!"
            show fb_bk_school_05 angry_01
            bk "DROP OFF A CLIFF SOMEWHERE AND LEAVE ME ALONE!!"
            "Man, what a rude ass, you think to yourself as you respond to his middle finger with your own."
            hide fb_bk_school_05 with moveoutright
            "In retaliation, Bakugou slams the classroom door close behind him."
            "Chuckling in amusement at the childishness you two were blatantly displaying, you began to gather your belongings."
            ".... Then again, maybe that's why you feel so comfortable around him."
            $ persistent.saw_trueend_bk = True

        "See you tomorrow, King Explosion Murder!":
            mc "See you tomorrow, King Explosion Murder!"
            show fb_bk_school_05 angry_02
            bk "GO TRIP OVER THE STAIRS FUCKWIPE!!"
            mc "You could've just replied with 'see you tomorrow', you know?"
            "You shout over his shoulders as he stomped away angrily, grumbling grouchily like an entitled old man of some kind."
            hide fb_bk_school_05 with moveoutright
            "What an amusing kid, you think as you start gathering your own belongings."

    jump day1_evening


########################### Event 4 scene - Todoroki ###########################
label event4_ts:
    "Your eyes meet with Todoroki's as the others filters out the classroom."
    show fb_ts_school_05 with dissolve

    $ ts_affection = todoroki.get_affection()
    $ option_name = "Pardner, can you carry me, please?"
    if ts_affection < 10:
        $ option_name = "Pardner, can you carry me, please? (Locked)"
    menu:
        "[option_name]" if ts_affection == 10:
            mc "Pardner, can you carry me, please?"
            show fb_ts_school_05 um_01
            ts "...."
            "You can see that he's seriously thinking about it, and for some reason it's making you feel embarrassed."
            show fb_ts_school_05
            ts "Sorry, I have to drop by somewhere else and I promised my sister I'll help with dinner today."
            mc "Ah."
            "The straightforward rejection left you unable to hold yourself back from sounding disappointed."
            mc "Well, I guess it was a rather sudden invitation, haha! Sorry, don't mind me!"
            show fb_ts_school_05 um_01
            "His set of different colored eyes stares at you, and the next words that leaves him renders your brain into a halt."
            show fb_ts_school_05
            ts "We should do that some other time."
            "Wait."
            "Did... Did Todoroki just potentially inisuate he wouldn't mind walking you home sometime in the future?!"
            "Uh oh, you're panicking."
            "You did want this, but this response was way out of your prediction."
            "No, you've got to calm down."
            "What kind of answer won't sound overly excited but also positive? Think [firstName], think!"
            mc "Huh? O-Oh, well, I mean, only if you want to!"
            ts "Sure. It'll make for a good training. We can take turns."
            "Again, your brain stops. More from confusion rather than shock, this time round."
            mc ".... Take turns?"
            show fb_ts_school_05 question_01
            ts "Yeah. Carrying each other. Weren't you thinking of training?"
            show fb_ts_school_05
            "..... Oh."
            mc "I, uh, totally was! Yup! Isn't it a good idea?"
            "Right. Of course. Why did you have to get your hopes up? Why would Todoroki of all people would willingly want to hang out with you? Even this morning, he wouldn't have walked you to school if not for what happened yesterday in training, right? And if it wasn't him who was your opponent, he wouldn't have given you a spare thought, would he? He's way out of--"
            ts "And afterwards, we could get dinner."
            "...?"
            pause 0.5
            play audio "audio/se/phone_message_notif_2.mp3"
            pause 1.0
            "The boy rummages through his bag for his phone to check his notifications, and after sparing it a quick glance, he turns towards you."
            ts "Then, I'll see you tomorrow."
            mc "S-See you..."
            hide fb_ts_school_05 with moveoutright
            "...."
            "...."
            "Holy shit, Todoroki {b}does{/b} want to hang out with you afterall."
            $ persistent.saw_trueend_ts = True

        "Bye Todoroki-kun! Be careful on your way home!":
            mc "Bye Todoroki-kun! Be careful on your way home!"
            ts "See you tomorrow."
            show fb_ts_school_05 um_01
            "The boy scrutinizes the sleepy state you're in and decides to add."
            ts "You be careful on your way home."
            show fb_ts_school_05
            mc "Don't you worry your pretty face, I'll be fine!"
            ts ".... Okay."
            hide fb_ts_school_05 with dissolve
            "You watch him exit the classroom and start gathering your own belongings, eyes heavy with sleep."

    jump day1_evening


################################ Evening scene #################################
label day1_evening:
    stop music

    scene bg_black with dissolve
    pause 1
    scene bg_personalbedroom_night with dissolve

    play music "audio/music/love.mp3"

    if skippedSchool:
        "When you woke up, it was night time. It seems like you've literally slept the day away."
        "You feel absolutely refreshed."
        "But you can't shake the feeling that you've missed a whole story by staying on your bed."
        ".... Oh well."

        return
    else:
        "Freshly out from the shower, you fall onto your bed with an inelegant flop."
        "Today has been another hard day at school. You feel absolutely exhausted."
        "For a moment, your eyes glance at the game system at the corner of your room."
        "Surprisingly, you didn't feel like you want to play your games today."
        "With a satisfied smile, you curl into your fluffy blankets and think back at the eventful day."
        $ mi_affection = midoriya.affection
        $ bk_affection = bakugou.affection
        $ ts_affection = todoroki.affection
        if mi_affection == 10:
            "You sure hope Midoriya will keep his promise whenever he's free."
        elif bk_affection == 10:
            "Someday, somehow, you swear you'll get Bakugou to carry you home."
        elif ts_affection == 10:
            "Maybe you should muster up the courage to ask Todoroki to fulfil his promise of hanging out with you tomorrow."
        "Eyes closing, you're fast asleep in mere seconds, looking forward to what tomorrow will bring."

        jump credits
