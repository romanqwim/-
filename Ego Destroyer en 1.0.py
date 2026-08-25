import random
import time

def self_esteem_destroyer():
    # ✍️ QUESTION LIST (expanded)
    question_list = [
        "Did you eat laundry detergent?",
        "Is your IQ below room temperature?",
        "Have you ever used your brain?",
        "Have you ever sucked... you know what?",
        "Did you sleep with your neighbor?",
        "Do you love licking asphalt?",
        "Are you going to have diarrhea?",
        "Are you sweet like sugar?",
        "Are you ready to eat cat food?",
        "Would you stick your fingers in an outlet for $0.50?",
        "Would you sell your soul for a pack of Skittles and 10 cents?",
        "Would you eat used chewing gum?",
        "Have you ever tried showering?",
        "Have you ever f*cked a toilet?",
        "Are you gay?",
        "Do you love eating snot?",
        "Did you suck a sausage?",
        "Are you dumb as a rock?",
        "Did you suck a dick?",
        "Do you have three hairs on your head?",
        "Did you drink from a puddle?",
        "Are you from the village?",
        "Would you dance on a table for 20 cents?",
        "Do you shit in your slippers?",
        "Have you showered this year?"
    ]
    
    funny_phrases = [
        "oh f*ck",
        "what the hell",
        "oh my god",
        "holy shit",
        "you dumbass",
        "are you insane",
        "you're a genius... 🐽",
        "i'm shook",
        "are you bald?",
        "facepalm",
        "you're something else",
        "i'm crying",
        "are you stupid?",
        "hold me back",
        "god save the queen",
        "have you lost your mind?",
        "i don't know what to say...",
        "congratulations, you're a loser",
        "lol",
        "O_о"
    ]
    
    destroyed_self_esteem = 0
    
    while True:
        if not question_list:
            print("🎉 Holy shit, you answered all questions! The list is empty, go home.")
            print(f"💀 Total self-esteem destroyed: {destroyed_self_esteem}")
            break

        answer = input("\n😏 Type yes/no or stop: ").lower().strip()
        
        if answer == "stop":
            print("\n 👋 Get the f*ck out of here, one less clown in the world! (｀∀´)Ψ")
            print(f"💀 Total self-esteem destroyed: {destroyed_self_esteem}")
            break
            
        elif answer == "yes" or answer == "no":
            destroyed_self_esteem += 1
            print("\n[Analyzing your answer...]")
            time.sleep(1)
            
            random_question = question_list.pop(random.randint(0, len(question_list) - 1))
            random_phrase = random.choice(funny_phrases)
            
            print(f"\n😎 {random_phrase.upper()}! You answered '{answer.upper()}' to:")
            print(f"👉 \"{random_question}\"")
            print("-" * 50 + "\n")
            
            # =========================================================================
            # UNIQUE RESPONSES FOR EACH QUESTION:
            # =========================================================================

            # 1. Laundry detergent
            if random_question == "Did you eat laundry detergent?":
                if answer == "yes":
                    print("🧼 Holy shit, you've got the spin cycle going inside!\nSoon you'll become powder yourself, you chemical freak! 😂\n")
                else:
                    print("🧹 Why not? Try it, at least you'll wash off the dirt from the inside, you pig.\nThere's toilet stains to get rid of! 🤣\n")

            # 2. IQ below room temperature
            elif random_question == "Is your IQ below room temperature?":
                if answer == "no":
                    follow_up = input("😏 So it's even lower? (yes/no): ").lower().strip()
                    if follow_up == "yes":
                        print("\n❄️ There you go, you admitted it yourself! Your brain temperature is absolute zero!\nWhere's your Nobel Prize? Oh wait, they don't give them for uselessness! 😂\n")
                    elif follow_up == "no":
                        print("\n🌡️ Denial is the first stage of acceptance, relax.\nIs your thermometer broken or did your brain just freeze? 😏\n")
                    else:
                        print("\n🤡 Can't even answer properly, it's probably even lower...\nMaybe try using a calculator next time? 🧮\n")
                else:
                    print("🧊 I can tell by looking at you! That's not a brain, it's a refrigerator!\nSnowflakes are gonna start falling out of your ears! ❄️\n")

            # 3. Used brain
            elif random_question == "Have you ever used your brain?":
                if answer == "yes":
                    print("🧠 Until proven otherwise, I don't buy it!\nWhere's the evidence? Oh right, you lost it! 😂\n")
                else:
                    print("💀 I can tell! That's not a brain, it's ping pong balls!\nBonus: they make a nice sound when you shake your head! 😏\n")

            # 4. Sucked (you know what)
            elif random_question == "Have you ever sucked... you know what?":
                if answer == "yes":
                    print("👄 Damn, you're a professional! Got a lot of experience?\nYou're gonna choke on that enthusiasm, you vacuum cleaner! 🤣\n")
                else:
                    print("👀 Don't lie, your lips tell a different story!\nYou've got calluses from all that work! 😂\n")

            # 5. Slept with neighbor
            elif random_question == "Did you sleep with your neighbor?":
                if answer == "yes":
                    print("🚪 You slut! What if the other neighbors hear?\nThey've already got their ears pressed to the wall! 🎵\n")
                else:
                    print("💤 Of course not, they wouldn't let you in even for extra pay!\nYou'd probably forget to knock anyway! 🚫\n")

            # 6. Licking asphalt
            elif random_question == "Do you love licking asphalt?":
                if answer == "yes":
                    print("🛣️ What a gourmet! How's it taste, rocks and dirt?\nSoon your menu: 'Asphalt with mayonnaise'! 😂\n")
                else:
                    print("🧹 Too bad, I thought you were a street sweeper!\nSo your mouth is only for talking, how disappointing! 😏\n")

            # 7. Diarrhea
            elif random_question == "Are you going to have diarrhea?":
                if answer == "yes":
                    print("💩 Good luck running, got spare pants?\nThere's already a queue of turds waiting! 🚽\n")
                else:
                    print("🪠 Yes you will, I already put laxatives in your drink!\nKeep a bucket handy, my friend! 😈\n")

            # 8. Sweet like sugar
            elif random_question == "Are you sweet like sugar?":
                if answer == "yes":
                    print("🍬 Damn you're sweet, I'm getting diabetes!\nYou've got more sugar in your blood than a candy store! 🍭\n")
                else:
                    print("🧂 You're not sugar, you're boring shit with no imagination!\nYou're the salt of the earth that burns everyone's eyes! 😂\n")

            # 9. Cat food
            elif random_question == "Are you ready to eat cat food?":
                if answer == "yes":
                    print("🐱 Whiskas or Kitiket? Don't start purring too loud, you animal!\nSoon you'll be shitting in the corner! 🤣\n")
                else:
                    print("🍽️ Too bad, judging by your face, that's your main diet!\nThere's the whole periodic table in one pack! 😂\n")

            # 10. Fingers in outlet
            elif random_question == "Would you stick your fingers in an outlet for $0.50?":
                if answer == "yes":
                    print("⚡ Damn you're cheap! For $20 they could probably buy you into slavery!\nCome on, let me give you a shock! 💡\n")
                else:
                    print("💰 Smart, save up for $1.00, you entrepreneur!\nYou'd fit right in government, same level of intelligence! 🏛️\n")

            # 11. Sell soul for Skittles
            elif random_question == "Would you sell your soul for a pack of Skittles and 10 cents?":
                print("📜 ATTENTION! Official SOUL PURCHASE CONTRACT generated:")
                print("=" * 55)
                print("I, the undersigned dumbass and loser, agree to transfer my")
                print("immortal soul (which nobody wanted anyway)")
                print("in exchange for 1 pack of Skittles (taste the rainbow)")
                print("and monetary compensation of 10 cents (0.10 USD).")
                print("Signature: ___________ (squiggle-squiggle)")
                print("=" * 55)
                
                input("✒️ Leave your electronic signature (enter name): ")
                
                while True:
                    final = input("\n🩸 Do you confirm the contract with BLOOD? (yes/no): ").lower().strip()
                    if final == "yes":
                        print("\n😈 Contract signed! Skittles are on their way (3-5 business days)!\nWe'll come for your soul at midnight, put the kettle on! ☕🔥\n")
                        break
                    elif final == "no":
                        print("\n😒 Deal fell through at the last second! You bastard!\nGive me my money back for the paper! 💰\n")
                        break
                    else:
                        print("\n🤬 You dumbass, just answer yes or no!\nHow long do I have to wait? I'm getting old here! ⏰")

            # 12. Used chewing gum
            elif random_question == "Would you eat used chewing gum?":
                if answer == "yes":
                    print("🤢 DISGUSTING! You're a walking biohazard!\nEating other people's saliva, you make me sick! 🦠\n")
                else:
                    print("😏 Come on, peel it off from under the desk in the hallway!\nThe germs already know you, don't be shy! 🦟\n")

            # 13. Tried showering
            elif random_question == "Have you ever tried showering?":
                if answer == "yes":
                    print("🧴 Then why do you smell like shit?\nDid you shower in the toilet or in a pond with ducks? 🦆\n")
                else:
                    print("👃 I can tell! You're not a person, you're a walking smell!\nEven flies drop dead around you! 🪰\n")

            # 14. F*cked toilet
            elif random_question == "Have you ever f*cked a toilet?":
                if answer == "yes":
                    print("🚽 You pervert! Did you fall in love with the plumbing?\nYou need to see a therapist, urgently! 🧠\n")
                else:
                    print("💩 Why not? The toilet wants love too!\nAre you homophobic towards bathroom fixtures? 😂\n")

            # 15. Gay
            elif random_question == "Are you gay?":
                if answer == "yes":
                    print("🏳️‍🌈 Congratulations! You finally have style!\nBut question: have you ordered your rainbow flag yet? 🌈\n")
                else:
                    print("😏 Why so scared to admit it?\nAll gay people say they're not gay, and you're not gay! Classic! 🤣\n")

            # 16. Eating snot
            elif random_question == "Do you love eating snot?":
                if answer == "yes":
                    print("🤧 You're sick! Is that a cold or a snack preference?\nThis isn't caviar, Vasya! 🤢\n")
                else:
                    print("👃 Why not? Free protein! Take it while it's available!\nVitamins and minerals included! 😂\n")

            # 17. Sucked sausage
            elif random_question == "Did you suck a sausage?":
                if answer == "yes":
                    print("🌭 You food lover! Sucked a sausage, or maybe not a sausage...\nJust don't choke on it! 💀\n")
                else:
                    print("😏 Why not? It's tasty... or so I've heard!\nYou've never had a hot dog before? 🌭\n")

            # 18. Dumb as a rock
            elif random_question == "Are you dumb as a rock?":
                if answer == "yes":
                    print("🍾 Finally an admission! I'm proud of you!\nYou're officially a rock! Can I use you as a doorstop? 🎉\n")
                else:
                    print("😏 Yeah right, and I'm the Queen of England!\nYou're so dumb you can't even spell 'dumb'! 🤣\n")

            # 19. Sucked a dick
            elif random_question == "Did you suck a dick?":
                if answer == "yes":
                    print("🍆 You're something else! You've got some experience!\nWhen's the competition, champ? 🏆\n")
                else:
                    print("😏 Why not? I heard it's delicious... I mean, it's a thing!\nJust don't choke on happiness! 💀\n")

            # 20. Three hairs
            elif random_question == "Do you have three hairs on your head?":
                if answer == "yes":
                    print("🧑‍🦲 You poor thing! That's not a head, that's an ice rink!\nAt least you can go skiing! ⛷️\n")
                else:
                    print("🧑‍🦰 Bragging? Then why are you bald?\nThat's an island of three hairs, time for a vacation! 😂\n")

            # 21. Drank from puddle
            elif random_question == "Did you drink from a puddle?":
                if answer == "yes":
                    print("💧 You daredevil! How's the tire-flavored water?\nSoon you'll be immune to everything! 🦠\n")
                else:
                    print("🌊 Free drink! Advertising: 'Puddle - summer in every drop'!\nToo bad there's ducks swimming in it... 🦆\n")

            # 22. From the village
            elif random_question == "Are you from the village?":
                if answer == "yes":
                    print("🌾 I knew it! I can smell the manure on you!\nMissing the chickens in the city? 🐔\n")
                else:
                    print("🏙️ What's wrong with the village? It's peaceful there!\nYou're just a village person in disguise! 😂\n")

            # 23. Dance on table for 20 cents
            elif random_question == "Would you dance on a table for 20 cents?":
                if answer == "yes":
                    print("💃 You cheap bastard! You'd dance for a penny!\nThere's already a line of people wanting to see your moves! 🤑\n")
                else:
                    print("😎 Too embarrassed? I'd dance for 20 cents!\nAs long as they move the chairs! 💺\n")

            # 24. Shit in slippers
            elif random_question == "Do you shit in your slippers?":
                if answer == "yes":
                    print("🩴 You sicko! You've got your own system!\nSoft and warm, just don't step on it! 😂\n")
                else:
                    print("😏 Try it! You just have to clean them daily!\nMaybe try a sock next time! 🧦\n")

            # 25. Showered this year
            elif random_question == "Have you showered this year?":
                if answer == "yes":
                    print("🛁 Wow! Look at you, Mr. Clean! Once a year but beautifully!\nJust don't shower again until next year! 🗓️\n")
                else:
                    print("🧼 You stink! There's mushrooms growing on you!\nI could harvest mold from you! 🍄\n")

            print("-" * 50 + "\n")
                
        else:
            print("\n🤡 Hey you mentally challenged creature, no brain cells left?") 
            print("🤪 Let me explain in simple terms: write yes or no!\n")
            print("I'm getting tired of you, seriously! 😫")

# ============================================
# 🚀 LAUNCH THE DESTROYER
# ============================================

print("🐍 WELCOME TO \"SELF-ESTEEM DESTROYER\"!")
print("🔥 YOUR ANSWERS WILL BE TURNED AGAINST YOU!")
print("💀 PREPARE FOR HUMILIATION!")
print("=" * 55)
print("\n⚠️ WARNING: This game may cause:\n- Uncontrollable laughter\n- Deep self-reflection\n- Existential crisis\n- Sudden urge to rethink your life\n")
print("=" * 55)

self_esteem_destroyer()