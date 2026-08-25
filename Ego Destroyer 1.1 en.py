"""
SELF-ESTEEM DESTROYER - Refactored Version
A fun game that turns your answers against you with savage humor!
"""

import random
import time
from typing import List, Dict, Optional

# ============================================
# DATA STRUCTURES
# ============================================

class Question:
    """Represents a single question with its responses."""
    
    def __init__(self, text: str, response_yes: str, response_no: str, 
                 requires_follow_up: bool = False, is_contract: bool = False):
        self.text = text
        self.response_yes = response_yes
        self.response_no = response_no
        self.requires_follow_up = requires_follow_up
        self.is_contract = is_contract
    
    def get_response(self, answer: str) -> str:
        """Returns the appropriate response based on the answer."""
        if answer == "yes":
            return self.response_yes
        return self.response_no

# ============================================
# QUESTION BANK (EXPANDED - 30 QUESTIONS)
# ============================================

def create_question_bank() -> List[Question]:
    """Creates and returns the complete list of questions (30 questions)."""
    
    return [
        # ===== ORIGINAL 25 QUESTIONS =====
        
        # 1. Laundry detergent
        Question(
            "Did you eat laundry detergent?",
            "🧼 Holy shit, you've got the spin cycle going inside!\nSoon you'll become powder yourself, you chemical freak! 😂",
            "🧹 Why not? Try it, at least you'll wash off the dirt from the inside, you pig.\nThere's toilet stains to get rid of! 🤣"
        ),
        
        # 2. IQ below room temperature
        Question(
            "Is your IQ below room temperature?",
            "🧊 I can tell by looking at you! That's not a brain, it's a refrigerator!\nSnowflakes are gonna start falling out of your ears! ❄️",
            "🧊 I can tell by looking at you! That's not a brain, it's a refrigerator!\nSnowflakes are gonna start falling out of your ears! ❄️",
            requires_follow_up=True
        ),
        
        # 3. Used brain
        Question(
            "Have you ever used your brain?",
            "🧠 Until proven otherwise, I don't buy it!\nWhere's the evidence? Oh right, you lost it! 😂",
            "💀 I can tell! That's not a brain, it's ping pong balls!\nBonus: they make a nice sound when you shake your head! 😏"
        ),
        
        # 4. Sucked (you know what)
        Question(
            "Have you ever sucked... you know what?",
            "👄 Damn, you're a professional! Got a lot of experience?\nYou're gonna choke on that enthusiasm, you vacuum cleaner! 🤣",
            "👀 Don't lie, your lips tell a different story!\nYou've got calluses from all that work! 😂"
        ),
        
        # 5. Slept with neighbor
        Question(
            "Did you sleep with your neighbor?",
            "🚪 You slut! What if the other neighbors hear?\nThey've already got their ears pressed to the wall! 🎵",
            "💤 Of course not, they wouldn't let you in even for extra pay!\nYou'd probably forget to knock anyway! 🚫"
        ),
        
        # 6. Licking asphalt
        Question(
            "Do you love licking asphalt?",
            "🛣️ What a gourmet! How's it taste, rocks and dirt?\nSoon your menu: 'Asphalt with mayonnaise'! 😂",
            "🧹 Too bad, I thought you were a street sweeper!\nSo your mouth is only for talking, how disappointing! 😏"
        ),
        
        # 7. Diarrhea
        Question(
            "Are you going to have diarrhea?",
            "💩 Good luck running, got spare pants?\nThere's already a queue of turds waiting! 🚽",
            "🪠 Yes you will, I already put laxatives in your drink!\nKeep a bucket handy, my friend! 😈"
        ),
        
        # 8. Sweet like sugar
        Question(
            "Are you sweet like sugar?",
            "🍬 Damn you're sweet, I'm getting diabetes!\nYou've got more sugar in your blood than a candy store! 🍭",
            "🧂 You're not sugar, you're boring shit with no imagination!\nYou're the salt of the earth that burns everyone's eyes! 😂"
        ),
        
        # 9. Cat food
        Question(
            "Are you ready to eat cat food?",
            "🐱 Whiskas or Kitiket? Don't start purring too loud, you animal!\nSoon you'll be shitting in the corner! 🤣",
            "🍽️ Too bad, judging by your face, that's your main diet!\nThere's the whole periodic table in one pack! 😂"
        ),
        
        # 10. Fingers in outlet
        Question(
            "Would you stick your fingers in an outlet for $0.50?",
            "⚡ Damn you're cheap! For $20 they could probably buy you into slavery!\nCome on, let me give you a shock! 💡",
            "💰 Smart, save up for $1.00, you entrepreneur!\nYou'd fit right in government, same level of intelligence! 🏛️"
        ),
        
        # 11. Sell soul for Skittles (special contract question)
        Question(
            "Would you sell your soul for a pack of Skittles and 10 cents?",
            "",  # Handled separately
            "",  # Handled separately
            is_contract=True
        ),
        
        # 12. Used chewing gum
        Question(
            "Would you eat used chewing gum?",
            "🤢 DISGUSTING! You're a walking biohazard!\nEating other people's saliva, you make me sick! 🦠",
            "😏 Come on, peel it off from under the desk in the hallway!\nThe germs already know you, don't be shy! 🦟"
        ),
        
        # 13. Tried showering
        Question(
            "Have you ever tried showering?",
            "🧴 Then why do you smell like shit?\nDid you shower in the toilet or in a pond with ducks? 🦆",
            "👃 I can tell! You're not a person, you're a walking smell!\nEven flies drop dead around you! 🪰"
        ),
        
        # 14. F*cked toilet
        Question(
            "Have you ever f*cked a toilet?",
            "🚽 You pervert! Did you fall in love with the plumbing?\nYou need to see a therapist, urgently! 🧠",
            "💩 Why not? The toilet wants love too!\nAre you homophobic towards bathroom fixtures? 😂"
        ),
        
        # 15. Gay
        Question(
            "Are you gay?",
            "🏳️‍🌈 Congratulations! You finally have style!\nBut question: have you ordered your rainbow flag yet? 🌈",
            "😏 Why so scared to admit it?\nAll gay people say they're not gay, and you're not gay! Classic! 🤣"
        ),
        
        # 16. Eating snot
        Question(
            "Do you love eating snot?",
            "🤧 You're sick! Is that a cold or a snack preference?\nThis isn't caviar, Vasya! 🤢",
            "👃 Why not? Free protein! Take it while it's available!\nVitamins and minerals included! 😂"
        ),
        
        # 17. Sucked sausage
        Question(
            "Did you suck a sausage?",
            "🌭 You food lover! Sucked a sausage, or maybe not a sausage...\nJust don't choke on it! 💀",
            "😏 Why not? It's tasty... or so I've heard!\nYou've never had a hot dog before? 🌭"
        ),
        
        # 18. Dumb as a rock
        Question(
            "Are you dumb as a rock?",
            "🍾 Finally an admission! I'm proud of you!\nYou're officially a rock! Can I use you as a doorstop? 🎉",
            "😏 Yeah right, and I'm the Queen of England!\nYou're so dumb you can't even spell 'dumb'! 🤣"
        ),
        
        # 19. Sucked a dick
        Question(
            "Did you suck a dick?",
            "🍆 You're something else! You've got some experience!\nWhen's the competition, champ? 🏆",
            "😏 Why not? I heard it's delicious... I mean, it's a thing!\nJust don't choke on happiness! 💀"
        ),
        
        # 20. Three hairs
        Question(
            "Do you have three hairs on your head?",
            "🧑‍🦲 You poor thing! That's not a head, that's an ice rink!\nAt least you can go skiing! ⛷️",
            "🧑‍🦰 Bragging? Then why are you bald?\nThat's an island of three hairs, time for a vacation! 😂"
        ),
        
        # 21. Drank from puddle
        Question(
            "Did you drink from a puddle?",
            "💧 You daredevil! How's the tire-flavored water?\nSoon you'll be immune to everything! 🦠",
            "🌊 Free drink! Advertising: 'Puddle - summer in every drop'!\nToo bad there's ducks swimming in it... 🦆"
        ),
        
        # 22. From the village
        Question(
            "Are you from the village?",
            "🌾 I knew it! I can smell the manure on you!\nMissing the chickens in the city? 🐔",
            "🏙️ What's wrong with the village? It's peaceful there!\nYou're just a village person in disguise! 😂"
        ),
        
        # 23. Dance on table for 20 cents
        Question(
            "Would you dance on a table for 20 cents?",
            "💃 You cheap bastard! You'd dance for a penny!\nThere's already a line of people wanting to see your moves! 🤑",
            "😎 Too embarrassed? I'd dance for 20 cents!\nAs long as they move the chairs! 💺"
        ),
        
        # 24. Shit in slippers
        Question(
            "Do you shit in your slippers?",
            "🩴 You sicko! You've got your own system!\nSoft and warm, just don't step on it! 😂",
            "😏 Try it! You just have to clean them daily!\nMaybe try a sock next time! 🧦"
        ),
        
        # 25. Showered this year
        Question(
            "Have you showered this year?",
            "🛁 Wow! Look at you, Mr. Clean! Once a year but beautifully!\nJust don't shower again until next year! 🗓️",
            "🧼 You stink! There's mushrooms growing on you!\nI could harvest mold from you! 🍄"
        ),
        
        # ===== NEW 5 QUESTIONS =====
        
        # 26. Ate instant noodles at 3 AM
        Question(
            "Did you eat instant noodles at 3 AM?",
            "🍜 You lazy ass! Eating instant noodles at 3 AM is peak degradation!\nSoon you'll be living in a dorm with habits like that! 😂",
            "😏 What's wrong with it? Instant noodles are a respectable meal for true connoisseurs!\nBut you just don't understand the depth of noodles! 🍜"
        ),
        
        # 27. Watched anime with door open
        Question(
            "Did you watch anime with the door open?",
            "🗿 ANIME FAN DETECTED! The neighbors now know you collect waifus!\nSoon they'll send a summons to your school! 🤓",
            "😎 That's right, anime should be watched in secret - it's not for the weak!\nOtherwise your mom will see your waifus and get upset! 😂"
        ),
        
        # 28. Drank beer at 8 AM
        Question(
            "Did you drink beer at 8 AM?",
            "🍺 Beer at 8 AM - you're either in a bender or an alcoholic with experience!\nSoon you'll be drinking with bums in the park! 🥴",
            "😏 What's the big deal? It's Sunday somewhere, right?\nYou just don't know how to live life to the fullest like me! 🤣"
        ),
        
        # 29. Tried to teach cat to talk
        Question(
            "Did you try to teach your cat to talk?",
            "🐱 You're fucking crazy! Cats can't talk, you idiot!\nAlthough with your IQ, you'd sooner talk to flowers! 🌸",
            "😏 Why not? My cat already says 'meow' - that's practically human!\nYou're just jealous of our communication! 🤣"
        ),
        
        # 30. Watched TikTok on full volume
        Question(
            "Did you watch TikTok on full volume?",
            "📱 TIKTOKER DETECTED! You should turn it on for your grandma too, let the whole street know!\nSoon the whole building will be hooked on this crap! 🎵",
            "😏 What's wrong with it? Let everyone know your taste!\nTikTok is a new culture, you're just an old fart! 🤣"
        )
    ]

# ============================================
# FUNNY PHRASES (EXPANDED - 25 PHRASES)
# ============================================

def get_funny_phrases() -> List[str]:
    """Returns a list of funny reaction phrases (expanded to 25 phrases)."""
    return [
        # Original phrases (20)
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
        "O_о",
        
        # NEW 5 PHRASES
        "did you fall from a tree? 🌳",
        "holy shit, i'm in shock",
        "god bless you... actually nevermind 🙏",
        "you're seriously messed up in the head 🤯",
        "damn, you're something else 😳"
    ]

# ============================================
# GAME LOGIC
# ============================================

def handle_iq_follow_up(original_answer: str) -> str:
    """Handles the special follow-up for the IQ question."""
    if original_answer == "no":
        follow_up = input("\n😏 So it's even lower? (yes/no): ").lower().strip()
        if follow_up == "yes":
            return "\n❄️ There you go, you admitted it yourself! Your brain temperature is absolute zero!\nWhere's your Nobel Prize? Oh wait, they don't give them for uselessness! 😂\n"
        elif follow_up == "no":
            return "\n🌡️ Denial is the first stage of acceptance, relax.\nIs your thermometer broken or did your brain just freeze? 😏\n"
        else:
            return "\n🤡 Can't even answer properly, it's probably even lower...\nMaybe try using a calculator next time? 🧮\n"
    return ""

def handle_soul_contract() -> None:
    """Handles the special soul-selling contract scenario."""
    print("\n📜 ATTENTION! Official SOUL PURCHASE CONTRACT generated:")
    print("=" * 55)
    print("I, the undersigned dumbass and loser, agree to transfer my")
    print("immortal soul (which nobody wanted anyway)")
    print("in exchange for 1 pack of Skittles (taste the rainbow)")
    print("and monetary compensation of 10 cents (0.10 USD).")
    print("Signature: ___________ (squiggle-squiggle)")
    print("=" * 55)
    
    input("\n✒️ Leave your electronic signature (enter name): ")
    
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

def display_question(question: Question, answer: str, phrase: str) -> None:
    """Displays the question and the reaction."""
    print(f"\n😎 {phrase.upper()}! You answered '{answer.upper()}' to:")
    print(f"👉 \"{question.text}\"")
    print("-" * 50 + "\n")

def process_answer(question: Question, answer: str, phrases: List[str]) -> int:
    """
    Processes the user's answer and returns the response.
    Returns 1 if self-esteem was destroyed, 0 otherwise.
    """
    phrase = random.choice(phrases)
    display_question(question, answer, phrase)
    
    # Handle special cases
    if question.is_contract:
        handle_soul_contract()
        return 1
    
    # Handle IQ follow-up
    if question.requires_follow_up and answer == "no":
        print(handle_iq_follow_up(answer))
        return 1
    
    # Normal response
    print(question.get_response(answer))
    print("-" * 50 + "\n")
    return 1

def get_valid_answer() -> Optional[str]:
    """Gets a valid answer from the user (yes/no/stop)."""
    answer = input("\n😏 Type yes/no or stop: ").lower().strip()
    
    if answer == "stop":
        return None
    elif answer in ["yes", "no"]:
        return answer
    else:
        print("\n🤡 Hey you mentally challenged creature, no brain cells left?")
        print("🤪 Let me explain in simple terms: write 'yes' or 'no'!\n")
        print("I'm getting tired of you, seriously! 😫")
        return "invalid"

# ============================================
# MAIN GAME
# ============================================

def self_esteem_destroyer() -> None:
    """Main game loop."""
    
    questions = create_question_bank()
    phrases = get_funny_phrases()
    destroyed_self_esteem = 0
    
    print("\n🐍 WELCOME TO \"SELF-ESTEEM DESTROYER\"!")
    print("🔥 YOUR ANSWERS WILL BE TURNED AGAINST YOU!")
    print("💀 PREPARE FOR HUMILIATION!")
    print("=" * 55)
    print("\n⚠️ WARNING: This game may cause:")
    print("- Uncontrollable laughter")
    print("- Deep self-reflection")
    print("- Existential crisis")
    print("- Sudden urge to rethink your life")
    print("- Irreversible psychological damage (just kidding... or am I?)")
    print("=" * 55)
    
    while True:
        if not questions:
            print("\n🎉 Holy shit, you answered all questions! The list is empty, go home.")
            print(f"💀 Total self-esteem destroyed: {destroyed_self_esteem}")
            break
        
        answer = get_valid_answer()
        
        if answer is None:  # User typed "stop"
            print("\n 👋 Get the f*ck out of here, one less clown in the world! (｀∀´)Ψ")
            print(f"💀 Total self-esteem destroyed: {destroyed_self_esteem}")
            break
        
        if answer == "invalid":
            continue
        
        # Valid answer (yes/no)
        print("\n[Analyzing your answer...]")
        time.sleep(1)
        
        # Get random question
        random_question = questions.pop(random.randint(0, len(questions) - 1))
        
        # Process the answer
        destroyed_self_esteem += process_answer(random_question, answer, phrases)

# ============================================
# ENTRY POINT
# ============================================

if __name__ == "__main__":
    try:
        self_esteem_destroyer()
    except KeyboardInterrupt:
        print("\n\n😏 Running away? Coward! (⌐■_■)")
        print("Your self-esteem was already destroyed anyway! 💀")
    except Exception as e:
        print(f"\n💀 Game crashed! Even the code couldn't handle your stupidity! 😂")
        print(f"Error: {e}")

# ============================================
# UNIT TESTS
# ============================================

def test_game_logic() -> None:
    """Basic tests to verify game functionality."""
    
    # Test Question class
    q = Question("Test?", "Yes response", "No response")
    assert q.get_response("yes") == "Yes response"
    assert q.get_response("no") == "No response"
    
    # Test question bank creation (now 30 questions)
    questions = create_question_bank()
    assert len(questions) == 30  # Was 25, now 30
    assert all(isinstance(q, Question) for q in questions)
    
    # Check new questions
    new_questions = [
        "Did you eat instant noodles at 3 AM?",
        "Did you watch anime with the door open?",
        "Did you drink beer at 8 AM?",
        "Did you try to teach your cat to talk?",
        "Did you watch TikTok on full volume?"
    ]
    question_texts = [q.text for q in questions]
    for new_question in new_questions:
        assert new_question in question_texts
    
    # Test phrases (now 25)
    phrases = get_funny_phrases()
    assert len(phrases) == 25
    assert "did you fall from a tree? 🌳" in phrases
    assert "holy shit, i'm in shock" in phrases
    assert "god bless you... actually nevermind 🙏" in phrases
    assert "you're seriously messed up in the head 🤯" in phrases
    assert "damn, you're something else 😳" in phrases
    
    print("✅ All tests passed!")

# Uncomment to run tests:
# test_game_logic()