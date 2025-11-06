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
    d "Dialogue prompt #1"
    menu:
        "Give Food":
            $ times_fed += 1
            jump prompt_2
        "Give Pets":
            $ times_pet += 1
            jump prompt_2
        "Do nothing":
            jump prompt_2
    return

label prompt_2:
    if times_pet > 2:
        jump overstimulated
    d "Dialogue prompt #2"
    menu:
        "Give Food":
            $ times_fed += 1
            jump prompt_3
        "Give Pets":
            $ times_pet += 1
            jump prompt_3
        "Do nothing":
            jump prompt_3
    return

label prompt_3:
    if times_pet > 2:
        jump overstimulated
    d "Dialogue prompt #3"
    menu:
        "Give Food":
            $ times_fed += 1
            jump prompt_4
        "Give Pets":
            $ times_pet += 1
            jump prompt_4
        "Do nothing":
            jump prompt_4
    return


label prompt_4:
    if times_pet > 2:
        jump overstimulated
    d "Dialogue prompt #4"
    menu:
        "Give Food":
            $ times_fed += 1
            jump prompt_5
        "Give Pets":
            $ times_pet += 1
            jump prompt_5
        "Do nothing":
            jump prompt_5
    return


label prompt_5:
    if times_pet > 2:
        jump overstimulated
    d "Dialogue prompt #5"
    menu:
        "Give Food":
            $ times_fed += 1
            jump determine_end
        "Give Pets":
            $ times_pet += 1
            jump determine_end
        "Do nothing":
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
    "good ending here!"
    return

label understimulated:
    "bad end: didn't pet her enough"
    return

label overstimulated:
    "you pet duckie too much"
    return

label starved:
    "you didnt feed her enough"
    return

label overfed:
    "you fed her too much"
    return