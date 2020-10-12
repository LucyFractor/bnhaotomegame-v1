define config.menu_include_disabled = True

init python:

    import array

    class Nickname:
        def __init__(self, locked, selected, value, fromWho):
            self.locked = locked
            self.selected = selected
            self.value = value
            self.fromWho = fromWho

        def get_self(self):
            return self

    class aCharacter:
        def __init__(self, lastName, firstName, colorCode):
            self.lastName = lastName
            self.firstName = firstName
            self.fullName = lastName + " " + firstName
            self.initials = lastName[0].lower() + firstName[0].lower()
            self.color = colorCode
            self.affection = 0
            self.nicknames = []

        def add_nickname(self, nickname):
            self.nicknames.append(nickname)
        def get_nickname(self, fromWho):
            for nickname in self.nicknames:
                n = nickname.get_self()
                if n.selected == True and n.fromWho == fromWho:
                    return nickname

        def set_affection(self, what, point):
            if what == "+":
                self.affection = self.affection + point
            elif what == "-":
                self.affection = self.affection - point

            if self.affection > 100:
                self.affection = 100
            elif self.affection < 0:
                self.affection = 0
        def get_affection(self):
            return self.affection

        def get_self(self):
            return self


################################## Start scene #################################

label start:
    scene bg_black

    python:
        firstName = renpy.input("What is your first name?\n{size=-10}(Default: \"Kaede\"){/size}")
        firstName = firstName.strip()

        if not firstName:
            firstName = "Kaede"

        lastName = renpy.input("What is your last name?\n{size=-10}(Default: \"Suzuki\"){/size}")
        lastName = lastName.strip()

        if not lastName:
            lastName = "Suzuki"

        ## START ::: initialize "ACHARACTER" -----------------------------------
        theplayer = aCharacter(lastName, firstName, "#A5C8E4")
        theplayer.add_nickname(Nickname(False, True, lastName + "-san", "all"))
        theplayer.add_nickname(Nickname(True, False, firstName + "-san", "all"))
        theplayer.add_nickname(Nickname(True, False, firstName + "-chan", "all"))
        theplayer.add_nickname(Nickname(True, False, firstName + "-kun", "all"))
        theplayer.add_nickname(Nickname(True, False, "Sweetheart", "mi"))
        theplayer.add_nickname(Nickname(True, False, "Babe", "bk"))
        theplayer.add_nickname(Nickname(True, False, "Love", "ts"))
        midoriya = aCharacter("Midoriya", "Izuku", "#C0ECCC")
        midoriya.add_nickname(Nickname(False, True, "Midoriya-kun", "mc"))
        midoriya.add_nickname(Nickname(True, False, "Izuku-kun", "mc"))
        midoriya.add_nickname(Nickname(True, False, "Cutie", "mc"))
        bakugou = aCharacter("Bakugou", "Katsuki", "#F9F0C1")
        bakugou.add_nickname(Nickname(False, True, "Bakugou-kun", "mc"))
        bakugou.add_nickname(Nickname(True, False, "Katsuki-kun", "mc"))
        bakugou.add_nickname(Nickname(True, False, "Honey", "mc"))
        todoroki = aCharacter("Todoroki", "Shouto", "#F6A8A6")
        todoroki.add_nickname(Nickname(False, True, "Todoroki-kun", "mc"))
        todoroki.add_nickname(Nickname(False, True, "Shouto-kun", "mc"))
        todoroki.add_nickname(Nickname(True, False, "Darling", "mc"))
        kirishima = aCharacter("Kirishima", "Eijirou", "#F47C7C")
        ## END ::: initialize "ACHARACTER" -------------------------------------

    $ char_mc = theplayer.get_self()
    define mc = Character("[char_mc.fullName]", who_color="#A5C8E4")

    $ char_mi = midoriya.get_self()
    define mi = Character("[char_mi.fullName]", who_color="#C0ECCC")
    $ char_bk = bakugou.get_self()
    define bk = Character("[char_bk.fullName]", who_color="#F9F0C1")
    $ char_ts = todoroki.get_self()
    define ts = Character("[char_ts.fullName]", who_color="#F6A8A6")
    $ char_ke = kirishima.get_self()
    define ke = Character("[char_ke.fullName]", who_color="#F47C7C")

    define as_sensei = Character("Aizawa Shota", who_color="#DCD2D3")

    jump init_character_images


################################### CREDITS ####################################
label credits:
    if not persistent.saw_credits:
        scene bg_black with dissolve
        pause 2

        play music "audio/music/IT'S GOOD FOR MIDNIGHT.mp3"

        define dev = Character(None, kind=nvl)

        nvl show

        dev "Hi, the author / developer here! If you have reached here, congrats! It's the end of the demo!"
        dev "This whole game itself is still in development, and this is just the first release, which I'm using to gauge whether there are people who would be interested in the game."
        dev "Since I am doing this for absolutely free, it's always nice to know if there are any feedbacks from the community :)"
        dev "If you want to drop a comment or follow the progress of this small project of mine, you can do so at {a=https://bnha-scenarios.tumblr.com/ask}my Tumblr, bnha-scenarios{/a}, under the tag {a=https://bnha-scenarios.tumblr.com/tagged/bnha-scenarios+otome+game}bnha-scenarios otome game{/a}."
        dev "This game won't be possible if not for the awesome people I mentioned under \"About\" page! Please check them out if you're interested!"

        nvl clear

        dev "With that said, thank you for playing this game! Do consider replaying it! There are some scenes where you can only see when you've maxed out the 'affection' of your character of choice! ;)"
        dev "I hope to see your {a=https://bnha-scenarios.tumblr.com/ask}feedback / comments{/a}! Here's to hoping this project will grow as planned!"
        dev "Catherine, signing off! Bye bye!"

        nvl hide

        $ persistent.saw_credits = True
    else:
        pass

    return
