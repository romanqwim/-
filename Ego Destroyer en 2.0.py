"""
SELF-ESTEEM DESTROYER 3.0
With emojis. With swearing. With soul.
"""

import random
import time
from typing import List, Optional

# ============================================
# QUESTION CLASS
# ============================================

class Question:
    def __init__(self, text: str, answer_yes: str, answer_no: str,
                 answer_maybe: str = "", answer_dont_know: str = "",
                 needs_followup: bool = False, is_contract: bool = False):
        self.text = text
        self.answer_yes = answer_yes
        self.answer_no = answer_no
        self.answer_maybe = answer_maybe or "🤔 Maybe? Maybe you're just afraid of the truth. Coward. 🐔"
        self.answer_dont_know = answer_dont_know or "🤷 You don't know? Then who does? Do you even know anything? 😂"
        self.needs_followup = needs_followup
        self.is_contract = is_contract

    def get_answer(self, answer: str) -> str:
        if answer == "yes":
            return self.answer_yes
        elif answer == "no":
            return self.answer_no
        elif answer == "maybe":
            return self.answer_maybe
        elif answer == "don't know":
            return self.answer_dont_know
        return "🤖 Are you fucking crazy? I don't know that answer."


# ============================================
# QUESTION DATABASE (50 QUESTIONS)
# ============================================

def create_questions() -> List[Question]:
    return [
        Question("Did you eat laundry detergent?",
                 "🧼 Fuck. You've got the spin cycle inside you. Soon you'll become powder yourself. 😂",
                 "🧹 Why not? Try it. At least you'll wash yourself from the inside, you dirty bastard. 🤣"),

        Question("Is your IQ below room temperature?",
                 "🧊 You can tell. You don't have a brain, you have a refrigerator. Snow will come out of your ears soon. ❄️",
                 "🧊 You can tell. You don't have a brain, you have a refrigerator. Snow will come out of your ears soon. ❄️",
                 "🌡️ Doubting yourself? You're just afraid to admit you've got absolute zero in there. 🧊",
                 "🤔 You don't know? Go check it. Although why bother, it's empty anyway. 🏖️",
                 needs_followup=True),

        Question("Have you ever used your brain?",
                 "🧠 Until proven otherwise, who gives a fuck. Where's the proof? You lost it. 😂",
                 "💀 You can tell. That's not a brain, those are ping-pong balls. 😏",
                 "🤔 Used it? Or did it use you? Judging by everything, it ran away. 🏃",
                 "🧐 You don't know? Try to remember. Oh wait, you can't. 😂"),

        Question("Have you ever sucked?",
                 "👄 Damn, you're a swallower. Got a lot of experience? Don't burst from all that effort, you vacuum cleaner. 🤣",
                 "👀 Don't lie. Your lips show you've got experience. There are calluses on your lips already. 😂",
                 "🤫 Maybe? We all know you suck. You just don't want to admit it. 🏆",
                 "😏 You don't know? Your lips say otherwise. 💋"),

        Question("Have you slept with the neighbor?",
                 "🚪 Damn, you're a slut. What if the people behind the wall hear? The neighbors are already listening. 🎵",
                 "💤 Of course not. They wouldn't let you in even for extra pay. 🚫",
                 "🤭 Maybe? So the wall heard everything? 🎤",
                 "🤷 You don't know? The bed knows. The springs already told everything. 🛏️"),

        Question("Do you like licking asphalt?",
                 "🛣️ You lip gourmet. How do the stones and dirt taste? Soon you'll open a menu called 'Asphalt with Mayo'. 😂",
                 "🧹 Too bad. I thought you were a street vacuum cleaner. 😏",
                 "🤔 Maybe? So you're a road taster. 🍽️",
                 "🤷 You don't know? Your tongue is already used to the taste of rubber. 🚗"),

        Question("Are you going to have diarrhea?",
                 "💩 Good luck running. Got spare pants? There's already a line of shits waiting. 🚽",
                 "🪠 You will. I already put laxatives in there. Keep a bucket ready. 😈",
                 "🤫 Maybe? Your body will decide. But I wouldn't trust your ass. 🔥",
                 "🤔 You don't know? But I do. You'll find out soon. Keep toilet paper ready. 🧻"),

        Question("Are you sugar sugar?",
                 "🍬 Damn, you're sweet. It's sickening. You've got more sugar in your blood than in a sugar bowl. 🍭",
                 "🧂 You're not sugar. You're boring shit with no imagination. 😂",
                 "🤔 Maybe? Well, you're definitely not salt. More like pepper. 🌶️",
                 "🤷 You don't know? You're cotton candy. Just as empty and sticky. 🍭"),

        Question("Are you ready to eat cat food?",
                 "🐱 Whiskas or Kitiket? Just don't start purring with pleasure. 🤣",
                 "🍽️ Too bad. Judging by your face, it's your main diet. 😂",
                 "🤔 Maybe? Cat food is a delicacy for the chosen ones. 🐾",
                 "🤷 You don't know? But I do. You'd eat it. You've already tried dry dog food. 🐕"),

        Question("Would you stick your fingers in a socket for 15 rubles?",
                 "⚡ Damn, you're cheap. For a hundred bucks they could buy you into slavery. 💡",
                 "💰 Right. Save up 20 rubles first, you businessman. 🏛️",
                 "🤔 Maybe? Negotiating? 10 rubles and you're a hero. 🔌",
                 "🤷 You don't know? But I do. You'd stick them in. You love risk, you dumbass. 😂"),

        # CONTRACT
        Question("Would you sell your soul for a pack of Skittles and 3 rubles?",
                 "", "", is_contract=True),

        Question("Would you eat used chewing gum?",
                 "🤢 Fuck, you're disgusting. Eating other people's saliva. 🦠",
                 "😏 Come on. Peel it off from under the table in the hallway and eat it. The germs are already used to you. 🦟",
                 "🤔 Maybe? You're a pervert. But I respect it. At least some interest in someone else's DNA. 🧬",
                 "🤷 You don't know? But I do. You'd eat it. You've tried worse. 😂"),

        Question("Have you tried washing?",
                 "🧴 Then why do you smell so much like shit? Did you wash in the toilet or in a lake with ducks? 🦆",
                 "👃 You can tell. You're not a person, you're a walking smell. Even flies die from you. 🪰",
                 "🤔 Maybe? You're definitely not from the shower. More like from a landfill. 🗑️",
                 "🤷 You don't know? But I do. You didn't wash. There's already an ecosystem living on you. 🌿"),

        Question("Did you fuck the toilet?",
                 "🚽 Damn, you're a pervert. Did you fall in love with it? Go see a psychologist urgently. 🧠",
                 "💩 Why not? Don't offend the toilet. It wants love too. 😂",
                 "🤔 Maybe? So you're a plumbing romantic. 🚽",
                 "🤷 You don't know? But I do. You fucked it. There are already cracks from love. 💔"),

        Question("Are you gay?",
                 "🏳️‍🌈 Congratulations. You've got style now. Question: have you already ordered a rainbow flag? 🌈",
                 "😏 Why not? Afraid to admit it? All gays say they're not gay, and you're not gay. Classic. 🤣",
                 "🤔 Maybe? So you're searching for yourself. The rainbow is already waiting. 🌈",
                 "🤷 You don't know? But I do. You're just afraid. Fear is normal. But just admit it already. 🏳️‍🌈"),

        Question("Do you like eating snot?",
                 "🤧 Damn, you're sick. Do you have a cold or a love for snacks? This isn't caviar. 🤢",
                 "👃 Why not? Free protein. Take it while they're giving it. There are vitamins. 😂",
                 "🤔 Maybe? So you're a connoisseur of nasal cuisine. 🌿",
                 "🤷 You don't know? But I do. You love it. You already tried it as a kid. 👶"),

        Question("Did you suck a sausage?",
                 "🌭 Damn, you're a glutton. Sucked a sausage, maybe not a sausage. Just don't choke. 💀",
                 "😏 Why not? It's tasty. Didn't you eat hot dogs as a kid? 🤔",
                 "🤔 Maybe? So you're a gourmet. Hot dogs are art. 🎨",
                 "🤷 You don't know? But I do. You sucked it. There are already calluses on your lips. 💋"),

        Question("Are you as dumb as a cork?",
                 "🍾 Finally, an admission. I'm proud of you. You're officially a cork now. 🎉",
                 "😏 Sure. You're such a cork that the box won't close. 🤣",
                 "🤔 Maybe? But corks are important in the household. 🍾",
                 "🤷 You don't know? But I do. You're dumb. There's already a plug made of brains. 🧠"),

        Question("Did you suck a dick?",
                 "🍆 Damn, you're something else. You've got a lot of experience. Soon you'll be going to competitions. 🏆",
                 "😏 Why not? It's tasty. So they say. You know what I mean. 💀",
                 "🤔 Maybe? So you're just an expert. You've already got a PhD. 🎓",
                 "🤷 You don't know? But I do. You sucked it. There's already a professional skill. 💪"),

        Question("Do you have three hairs on your head?",
                 "🧑‍🦲 Poor you. That's not a head, it's a figure skating rink. ⛷️",
                 "🧑‍🦰 Bragging? Then why are you bald? There's already an island of three hairs there. 😂",
                 "🤔 Maybe? Three hairs is also wealth. 💰",
                 "🤷 You don't know? But I do. You've got two. There's already a census. 📊"),

        Question("Did you drink from a puddle?",
                 "💧 Damn, you're extreme. Taste of water with tires? Soon you'll have immunity to everything. 🦠",
                 "🌊 Why not? Free drink. Advertisement: 'Puddle - summer in every drop'. 🦆",
                 "🤔 Maybe? So you're a water taster. Soon you'll open a puddle bottling plant. 💧",
                 "🤷 You don't know? But I do. You drank it. It already tastes like gasoline and tires. ⛽"),

        Question("Are you from the village?",
                 "🌾 I knew it. I can smell the manure on you. Missing the chickens in the city? 🐔",
                 "🏙️ Why not? The village is great. It's peaceful. But you're just a disguised villager. 😂",
                 "🤔 Maybe? So you're a secret country person. In your heart, you're always with the cows. 🐄",
                 "🤷 You don't know? But I do. You're from there. They already miss your smell. 🌾"),

        Question("Are you ready to dance on a table for 5 rubles?",
                 "💃 Cheap. You'd dance for a kopeck too. There's already a line of people wanting to watch. 🤑",
                 "😎 Why not? Embarrassed? I'd dance for 5 rubles. But only if they move the chairs. 💺",
                 "🤔 Maybe? So you're waiting for 10 rubles. You businessman. 💰",
                 "🤷 You don't know? But I do. You'll dance. You're a disco star. 💃"),

        Question("Do you shit in your slippers?",
                 "🩴 Damn, you're a pervert. You've got your own system. Soft and warm. Just don't step in it. 😂",
                 "😏 Why not? Convenient. Just clean them every day. 🧦",
                 "🤔 Maybe? Slippers are convenient. 🩴",
                 "🤷 You don't know? But I do. You do. There's already a flower garden growing there. 🌸"),

        Question("Have you washed this year?",
                 "🛁 Wow. You're clean. Just once a year, but beautifully. Just don't wash until next year. 🗓️",
                 "🧼 Damn, you stink. There are already mushrooms growing on you. You could collect mold. 🍄",
                 "🤔 Maybe? Once a year is normal. 🌊",
                 "🤷 You don't know? But I do. You didn't wash. There's already an ecosystem thriving. 🌿"),

        Question("Did you eat instant noodles at 3 AM?",
                 "🍜 Damn, you're a lazy ass. Eating instant noodles at 3 AM is the peak of degradation. 😂",
                 "😏 Why not? Instant noodles are worthy food for true connoisseurs. 🍜",
                 "🤔 Maybe? So you're a night gourmet. 🍜",
                 "🤷 You don't know? But I do. You ate them. There are already cups all over the room. 🗑️"),

        Question("Did you watch anime with the door open?",
                 "🗿 ANIME FAN. The neighbors now know you collect waifus. 🤓",
                 "😎 Right. You need to watch anime secretly. Otherwise, mom will see your waifus. 😂",
                 "🤔 Maybe? The whole street knows your tastes. 📺",
                 "🤷 You don't know? But I do. You watched it. There's already cosplay for breakfast. 🎭"),

        Question("Did you drink beer at 8 AM?",
                 "🍺 Beer at 8 AM. You're either on a bender or an alcoholic with experience. 🥴",
                 "😏 What's the big deal? Sunday beer has to be somewhere. 🤣",
                 "🤔 Maybe? Beer has vitamins. 🍺",
                 "🤷 You don't know? But I do. You drank it. There's already a beer belly growing. 🐷"),

        Question("Did you try to teach a cat to talk?",
                 "🐱 Damn, you're crazy. Cats can't talk. With your IQ, you'd sooner talk to flowers. 🌸",
                 "😏 Why not? My cat already says 'meow'. That's almost human. 🤣",
                 "🤔 Maybe? So you're a cat psychologist. Soon your cat will learn to swear. 🐱",
                 "🤷 You don't know? But I do. You tried. The cat is already laughing at you. 😹"),

        Question("Did you watch TikTok at full volume?",
                 "📱 TIKTOKER. Turn it on for grandma too, let the whole street know. 🎵",
                 "😏 Why not? It's fine. Let everyone know your taste. 🤣",
                 "🤔 Maybe? The whole street dances to your music. 💃",
                 "🤷 You don't know? But I do. You watched it. Your neighbors' ears are already blocked. 🎧"),

        Question("Did you fish in the toilet?",
                 "🎣 Damn, you're a fisherman. There are no fish in the toilet. Only your fantasies float there. 🐟",
                 "😏 Why not? What if there's a carp there? You'd try fishing in a puddle too. 🌊",
                 "🤔 Maybe? So you're a plumbing hunter. 🚽",
                 "🤷 You don't know? But I do. You fished. The trout is already used to you. 🐠"),

        Question("Did you talk to plants?",
                 "🌿 Are you a botanist-psychologist? Plants can't hear you, but they definitely want to get away from you. 🌱",
                 "😏 Why not? They're alive. You just don't know how to talk to them. 🍃",
                 "🤔 Maybe? So you're a doctor for flowers. They love you. 🌸",
                 "🤷 You don't know? But I do. You talked to them. They're already tired of your chatter. 💬"),

        Question("Did you wear a tinfoil hat?",
                 "🧠 Are you afraid of aliens? Foil won't save you from your stupidity. 👽",
                 "😏 Why not? It works. You just don't have the brains to appreciate it. 🛸",
                 "🤔 Maybe? So you're a superhero. Foil Man. 🦸",
                 "🤷 You don't know? But I do. You wore it. There's already rust on your head. 🦾"),

        Question("Did you try to fix an iron with a hammer?",
                 "🔧 Genius repairman. Hammers are for nails, not irons. 💥",
                 "😏 Why not? The impact method is the most reliable. 🔨",
                 "🤔 Maybe? So you're Kulibin. A hammer is a universal tool. 🛠️",
                 "🤷 You don't know? But I do. You tried. The iron is already in the past. 💀"),

        Question("Did you wear socks with sandals?",
                 "👣 Damn, you're a fashionista. Socks with sandals are the peak of style. They'll put you in a magazine soon. 📸",
                 "😏 Why not? It's comfortable. You just don't understand fashion. 👌",
                 "🤔 Maybe? So you're a style icon. 🕶️",
                 "🤷 You don't know? But I do. You wore them. There's already a photo on Instagram. 📱"),

        Question("Did you eat bread with mayonnaise?",
                 "🍞 Damn, you're a pervert. Mayonnaise isn't food, it's a condiment. ☕",
                 "😏 Why not? It's tasty. You just haven't tried it. 😇",
                 "🤔 Maybe? Mayonnaise is art. 🎨",
                 "🤷 You don't know? But I do. You ate it. Your stomach already hurts from fat. 🐷"),

        Question("Did you sing in the shower?",
                 "🎤 Are you a singer? Everyone sings in the shower, but you sing like a sick cat. 🐸",
                 "😏 Why not? I've got talent. You're just jealous. 🎶",
                 "🤔 Maybe? Soon there'll be a concert in the bathroom. 🛁",
                 "🤷 You don't know? But I do. You sang. The neighbors already called the police. 🚔"),

        Question("Did you bite your toenails?",
                 "🦶 Damn, you're flexible. Toenails aren't a snack. 🐍",
                 "😏 Why not? It's convenient. You're just not that flexible. 🧘",
                 "🤔 Maybe? You've got incredible flexibility. 🤸",
                 "🤷 You don't know? But I do. You bit them. Your toes are already chewed off. 🦷"),

        Question("Did you win the lottery?",
                 "💰 Damn, you're lucky. Won? Yeah, right. 🎰",
                 "😏 Why not? People get lucky. You're just a loser. 🏆",
                 "🤔 Maybe? Soon you'll buy an island. 🏝️",
                 "🤷 You don't know? But I do. You didn't win. There are tons of tickets, but zero wins. 🎫"),

        Question("Did you build a castle out of a sofa?",
                 "🏰 Damn, you're an architect. Sofas aren't building materials. 🛋️",
                 "😏 Why not? It's comfortable. You just don't know how to build. 🛏️",
                 "🤔 Maybe? Sofa architecture is a trend. 📐",
                 "🤷 You don't know? But I do. You built it. The sofa has already collapsed. 🛋️"),

        Question("Did you do a puzzle without the picture?",
                 "🧩 Damn, you're extreme. A puzzle without a picture is like life without a purpose. 😩",
                 "😏 Why not? It's a challenge. You're just afraid of difficulties. ⏱️",
                 "🤔 Maybe? Suffering is fun. 😈",
                 "🤷 You don't know? But I do. You did it. 10 years have passed and the puzzle isn't finished. 🕒"),

        Question("Did you play hide and seek with yourself?",
                 "👻 Damn, you're a sociopath. Hiding from yourself is god-level. 🎭",
                 "😏 Why not? It's fun. You just don't know how to entertain yourself. 🧍",
                 "🤔 Maybe? Self-discovery is important. 🧘",
                 "🤷 You don't know? But I do. You played. You've been looking for yourself for 20 years. 🔍"),

        Question("Did you drink onion compote?",
                 "🧅 Damn, you're a cook. Onions aren't for compote. 🧄",
                 "😏 Why not? It's healthy. You just don't understand the taste. 🍵",
                 "🤔 Maybe? Experiments are cool. 👨‍🍳",
                 "🤷 You don't know? But I do. You drank it. There are already tears from the taste. 😭"),

        Question("Did you sleep with the light on?",
                 "💡 Damn, you're a coward. Afraid to turn off the light? The monsters under the bed will eat you. 👹",
                 "😏 Why not? It's cozy. You're just afraid of the dark. 🛌",
                 "🤔 Maybe? Light is safety. 🔦",
                 "🤷 You don't know? But I do. You sleep. The light bulb has already burned out. 💡"),

        Question("Did you try to put pasta up your nose?",
                 "🍝 Damn, you're an experimenter. Pasta up your nose is a new trend. 🍜",
                 "😏 Why not? They fit. You just haven't tried. 🤥",
                 "🤔 Maybe? Pasta is a universal thing. 🧘",
                 "🤷 You don't know? But I do. You put it in. The pasta has already gone to your brain. 🧠"),

        Question("Did you write a letter to Santa Claus as an adult?",
                 "🎅 Damn, you're a child. An adult and believing in fairy tales. Santa died from your stupidity. 🪦",
                 "😏 Why not? Let him know what I want. You're just afraid to dream. 💫",
                 "🤔 Maybe? Santa is belief in miracles. ✨",
                 "🤷 You don't know? But I do. You wrote it. The letter is already in the archive. 📨"),

        Question("Did you ride a cat?",
                 "🐱 Damn, you're a pervert. Cats aren't transportation. 🐕",
                 "😏 Why not? They can run fast. You just don't know how to negotiate with them. 🐈",
                 "🤔 Maybe? A cat is a loyal friend. 🐾",
                 "🤷 You don't know? But I do. You rode it. The cat has already run away to Africa. 🌍"),

        Question("Did you eat snow with salt?",
                 "❄️ Damn, you're a cook. Snow with salt is like soup with sugar. 🌍",
                 "😏 Why not? It's tasty. You just don't understand. 🧂",
                 "🤔 Maybe? Exotic is fashionable. 🍽️",
                 "🤷 You don't know? But I do. You ate it. The salt has already run out. 🧂"),

        Question("Did you try to summon Satan?",
                 "😈 Damn, you're crazy. Satan won't come to such a loser. ☕",
                 "😏 Why not? It's interesting. You're just afraid. I summoned him, he came, we had tea. 🧙",
                 "🤔 Maybe? The dark forces love you. 🌑",
                 "🤷 You don't know? But I do. You tried. The candles burned out, but Satan's not here. 🕯️"),

        Question("Did you watch horror movies alone at night?",
                 "👻 Damn, you're brave. Night horror is a challenge. Soon you'll be hiding under the bed. 🛏️",
                 "😏 Why not? It's scary. But you're just a coward. I watch them every day. 🎥",
                 "🤔 Maybe? Fear is fun. 😱",
                 "🤷 You don't know? But I do. You watched it. You're already having nightmares. 😴"),

        Question("Did you try to fall asleep with your eyes open?",
                 "👁️ Damn, you're extreme. Only fish sleep with their eyes open. 🧍",
                 "😏 Why not? I'm training my willpower. You just haven't tried. 🧘",
                 "🤔 Maybe? Your eyes are open, but you're asleep. 😴",
                 "🤷 You don't know? But I do. You tried. Your eyes have already dried out. 👀"),
    ]


# ============================================
# REACTION PHRASES (50 PIECES)
# ============================================

def get_phrases() -> List[str]:
    return [
        "what the fuck",
        "holy shit",
        "oh my god",
        "damn",
        "you're such a loser",
        "are you fucking crazy",
        "you're a genius... 🐽",
        "I'm in shock",
        "are you bald?",
        "facepalm",
        "you're something else",
        "I'm crying from you",
        "are you an idiot?",
        "hold me seven",
        "god save the queen",
        "have you lost your mind?",
        "I don't know what to say...",
        "congratulations, you're a loser",
        "kek",
        "O_о",
        "did you fall out of a tree? 🌳",
        "what the actual fuck",
        "god save you... actually no 🙏",
        "you're seriously insane 🤯",
        "damn, you're something else 😳",
        "you're a god... a god of stupidity 🤡",
        "I'd put up a monument... made of shit 🗿",
        "your brain is in 'dead calm' mode 🌊",
        "you're worse than my cat, and he shits in slippers 🐈",
        "even jokes are scary with you 😨",
        "you'd ask how to breathe properly 😂",
        "your intelligence is at the level of a sandwich 🥪",
        "I'm shocked by your adequacy, it doesn't exist 🚫",
        "you're like that meme nobody remembers anymore 📉",
        "go ahead, surprise me... oh, nothing 😐",
        "you'd ask a tree for advice 🌳",
        "god give me patience... better yet, give me alcohol 🍷",
        "you're like a wardrobe — useless, but big 🪑",
        "I'd think if I were you... but you can't 🤔",
        "your level — even children laugh 🧒",
        "you're crazy, but I love those 😂",
        "you're like that old gum — no longer needed, but still sticking 🍬",
        "your brain went on vacation and never came back 🏖️",
        "I'd make a joke about you, but it'd be too smart 🧠",
        "you're like an unnecessary function — everyone forgot about you 🔧",
        "fuck, do you actually exist? Or is it a glitch? 👻",
        "your stupidity has its own gravity 🌍",
        "you're like that dinosaur — already extinct, but still walking 🦕",
        "I'd pity you, but I'm lazy 🦥",
        "you're the reason GOD doesn't talk to people 🙏"
    ]


# ============================================
# HANDLERS
# ============================================

def handle_iq_followup(original_answer: str) -> str:
    if original_answer == "no":
        answer = input("\n😏 So even lower? (yes/no/maybe/don't know): ").lower().strip()
        if answer == "yes":
            return "\n❄️ There you go. You admitted it yourself. Your brain temperature is absolute zero. Where's your Nobel Prize? Oh right, they don't give them for uselessness. 😂\n"
        elif answer == "no":
            return "\n🌡️ Denial is the first stage of acceptance. Did your thermometer break or did your brain just freeze? 😏\n"
        elif answer == "maybe":
            return "\n🤔 Maybe? Well, you're on the right track — doubting your own stupidity. But we know the truth. 😂\n"
        elif answer == "don't know":
            return "\n🤷 You don't know? Then who does? Your ping-pong balls? They already ran away. 🏃\n"
        else:
            return "\n🤡 Can't even answer properly here. You'd use a calculator for answers too. 🧮\n"
    return ""


def handle_soul_contract() -> None:
    print("\n📜 ATTENTION. An official SOUL PURCHASE AGREEMENT has been generated:")
    print("=" * 55)
    print("I, the undersigned loser and dumbass, hereby agree to transfer my")
    print("immortal soul (which nobody needs anyway)")
    print("in exchange for 1 pack of Skittles and money in the amount of 3 rubles.")
    print("Signature: ___________")
    print("=" * 55)

    input("\n✒️ Leave your electronic signature (enter your name): ")

    while True:
        final = input("\n🩸 Do you confirm the terms of the contract WITH BLOOD? (yes/no): ").lower().strip()
        if final == "yes":
            print("\n😈 Contract signed. Skittles are on the way. We'll come for your soul at midnight. Hell awaits. ☕🔥\n")
            break
        elif final == "no":
            print("\n😒 Deal fell through. You bastard. Give back the money for the paper. 💰\n")
            break
        else:
            print("\n🤬 Just write yes or no. How long can this go on? I'm getting old here. ⏰")


def show_question(q: Question, answer: str, phrase: str) -> None:
    print(f"\n😎 {phrase.upper()}! You answered '{answer.upper()}' to:")
    print(f"👉 \"{q.text}\"")
    print("-" * 50)


def process_answer(q: Question, answer: str, phrases: List[str]) -> int:
    phrase = random.choice(phrases)
    show_question(q, answer, phrase)

    if q.is_contract:
        handle_soul_contract()
        return 1

    if q.needs_followup and answer == "no":
        print(handle_iq_followup(answer))
        return 1

    print(q.get_answer(answer))
    print("-" * 50)
    return 1


def get_valid_answer() -> Optional[str]:
    user_input = input("\n😏 Type yes/no/maybe/don't know or stop: ").lower().strip()

    if user_input == "stop":
        return None
    elif user_input in ["yes", "no", "maybe", "don't know"]:
        return user_input
    else:
        print("\n🤡 Are you dumb? I said yes/no/maybe/don't know. Write properly.\n")
        return "invalid"


# ============================================
# MAIN GAME
# ============================================

def main_game() -> None:
    questions = create_questions()
    phrases = get_phrases()
    destroyed = 0

    print("\n🐍 WELCOME TO THE SELF-ESTEEM DESTROYER 3.0")
    print("🔥 WITH SWEARING. WITH SOUL.")
    print("💀 GET READY FOR HUMILIATION ON A NEW LEVEL!")
    print("=" * 55)
    print("\n⚠️ ANSWER OPTIONS:")
    print("- yes (classic)")
    print("- no (classic)")
    print("- maybe (doubt)")
    print("- don't know (be dumb)")
    print("=" * 55)

    while True:
        if not questions:
            print("\n🎉 You answered all 50 questions. Game over.")
            print(f"💀 Self-esteem destroyed: {destroyed}")
            break

        answer = get_valid_answer()

        if answer is None:
            print("\n👋 Running away? Coward. Your self-esteem was already destroyed.")
            print(f"💀 Total destroyed: {destroyed}")
            break

        if answer == "invalid":
            continue

        q = questions.pop(random.randint(0, len(questions) - 1))
        destroyed += process_answer(q, answer, phrases)


if __name__ == "__main__":
    try:
        main_game()
    except KeyboardInterrupt:
        print("\n\n👋 Running away? Coward. Your self-esteem was already destroyed. 💀")
    except Exception as e:
        print(f"\n💀 Game crashed. Even the code couldn't handle your stupidity. Error: {e}")