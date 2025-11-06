# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Duckie")
default times_fed = 0
default times_pet = 0

image d neutral = "images/Duckie_Neutral.png"
image d annoyed = "images/Duckie_Annoyed.png"
image d sweet = "images/Duckie_Sweet.png"
image d angry = "images/Duckie_Angry.png"
image d pleading = "images/Duckie_Pleading.png"
image d intense = "images/Duckie_Intense.png"


# The game starts here.

label start:

    scene bg room

    show d neutral

    d "Feed duckie 3 times, and pet her twice."
    jump prompt_1

    return

label prompt_1:
    show d pleading
    d "Hello, I’m terribly hungry; starving, in fact."
    show d neutral
    d "Will you give me breakfast?"

    menu:
        "Give Duckie breakfast":
            $ times_fed += 1
            jump prompt_2
        "Pet her":
            $ times_pet += 1
            jump prompt_2
        "Ignore her":
            jump prompt_2
    return

label prompt_2:
    if times_pet > 2:
        jump overstimulated
    show d neutral
    d "I’m still hungry. You’re killing me."
    show d intense
    d "Give me food."

    menu:
        "Give Duckie dry food":
            $ times_fed += 1
            jump prompt_3
        "Pet her":
            $ times_pet += 1
            jump prompt_3
        "Ignore her":
            jump prompt_3
    return

label prompt_3:
    if times_pet > 2:
        jump overstimulated

    show d annoyed
    d "I can’t believe you don’t feed me ever."
    show d pleading
    d "Ever ever ever. I’m starving."
    d "Feed me?"

    menu:
        "Give Duckie dry food":
            $ times_fed += 1
            jump prompt_4
        "Pet her":
            $ times_pet += 1
            jump prompt_4
        "Ignore her":
            jump prompt_4
    return


label prompt_4:
    if times_pet > 2:
        jump overstimulated
    
    show d sweet
    d "Hello I love you soooooo much. Wow you’ve never seen me be this sweet before ever. Right?"
    d "Guess you’ve gotta feed me to reward me for my good behavior."

    menu:
        "Give Duckie dry food":
            $ times_fed += 1
            jump prompt_5
        "Pet her":
            $ times_pet += 1
            jump prompt_5
        "Ignore her":
            jump prompt_5
    return


label prompt_5:
    if times_pet > 2:
        jump overstimulated

    show d intense
    d "IT’S DINNER TIME HELLO HELLO IM HUNGRY HELLO"

    menu:
        "Give Duckie dinner":
            $ times_fed += 1
            jump determine_end
        "Pet her":
            $ times_pet += 1
            jump determine_end
        "Ignore her":
            jump determine_end
    return

label determine_end:
    if times_pet > 2:
        jump overstimulated
    if times_fed == 3 and times_pet == 2:
        jump good_ending
    if times_fed == 3 and times_pet < 2:
        jump understimulated
    if times_fed < 3:
        jump starved
    if times_fed > 3:
        jump overfed
    return

    
label good_ending:
    show d sweet
    d "Hmmmm. Today has been adequate."
    show d neutral
    d "I’m still going to get the zoomies late at night and I might chew a bit of cardboard."
    show d sweet
    d "But I’m also going to sit in your lap and purr very faintly for a solid 20 mins until your foot falls asleep."
    show d annoyed
    d "Then I’ll become mildly violent."
    hide d
    "Well, I think that’s the best you can ask for. You win!"

    return

label understimulated:
    show d annoyed
    d "I’m fed, but I’m understimulated and I’m going to chew up all your cardboard and paper now. Screw you, man!"
    hide d
    "Uh oh! You ignored your cat and now she’s a problem. Do better!"

    return

label overstimulated:
    show d angry
    d "How dare you TOUCH me? I’m going to BITE you now."
    hide d
    "You pet duckie too many times! Now you’ve been injured, go get a bandaid. You lose!"

    return

label starved:
    show d annoyed
    d "I’m STARVING and you didn’t feed me."
    show d angry
    d "Now I’m ANGRY and I’m going to hiss at you."
    hide d
    "Wow, she hissed at you. That feels bad emotionally! You lose."

    return

label overfed:
    show d intense
    d "Haha, you FOOL! I tricked you and now I’ve eaten too much."
    show d annoyed
    d "I’m going to have the zoomies all night long, and maybe poop on the floor."
    hide d
    "Oops, you gave her too much food! Now the vet’s going to call her plump again. You lose!"

    return