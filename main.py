import random

# Predefined story elements
locations = ["enchanted forest", "haunted castle", "desert of forgotten dreams", "underground cavern", "frozen wasteland", "abandoned village", "mountain pass"]
goals = ["treasure", "mysterious artifact", "hidden kingdom", "ancient knowledge", "relic of power", "cure for a deadly disease"]
items = ["magic sword", "mystic crystal", "cursed necklace", "enchanted cloak", "shield of light", "potion of immortality"]
characters = ["a talking wolf", "an old wizard", "a lost princess", "a fearless knight", "a rogue thief", "a mysterious stranger"]
plot_twists = [
    "The map was cursed, and anyone who followed it would vanish from the world.",
    "The mysterious figure was actually a trickster who deceived {name} into an impossible mission.",
    "It turned out that the legendary {goal} was a trap set by an ancient dragon who guarded its secrets.",
    "The guide {name} trusted turned out to be an enemy in disguise, leading them to a deadly ambush.",
    "The item {item} was cursed, and using it would bring great misfortune."
]
conclusions = [
    "In the end, {name} succeeded, but at a great personal cost. The {goal} was found, but the journey had changed them forever.",
    "{name} reached the {goal}, but they soon realized that achieving their dreams wasn't as fulfilling as they had imagined.",
    "{name} discovered that sometimes the journey itself was the greatest reward, and they returned home wiser and more content.",
    "The twist of fate was cruel, and {name} never returned, their quest for the {goal} having cost them everything.",
    "Despite all odds, {name} triumphed and changed the world forever, their legend living on for generations."
]

# Function to generate the introduction
def generate_introduction(name):
    goal = random.choice(goals)  # Pick a goal from the predefined list
    introduction = f"{name} had always dreamed of adventure, but little did they know that this journey would change their life forever when they set off to find the legendary {goal} hidden deep within the {random.choice(locations)}. It was a quest that would challenge their very soul and test their courage like never before."
    return introduction, goal  # Return goal to be used in other chapters

# Function to make decisions based on user input
def make_decision(decision_prompt):
    decision = input(decision_prompt)
    if decision.lower() == "y":
        return True
    elif decision.lower() == "n":
        return False
    else:
        print("Invalid input. Please respond with 'y' or 'n'.")
        return make_decision(decision_prompt)

# Function to generate Chapter 1 content based on choices
def generate_chapter_1(name, take_item, goal):
    item = random.choice(items) if take_item else "nothing"
    chapter_1 = f"{name} sets out on their quest to find the {goal}, accepting a gift of {item} along the way. Little did they know, this gift would play a pivotal role in the challenges ahead. With a heart full of hope and a mind brimming with anticipation, {name} begins the journey into the unknown, unaware of the dangers that lie in wait."
    return chapter_1, item

# Function to generate Chapter 2 content based on choices
def generate_chapter_2(name, item):
    print("\n--- Chapter 2 ---")
    decision = make_decision("Do you venture further into the dark forest? (y/n): ")
    if decision:
        chapter_2 = f"With the {item} in hand, {name} presses forward, deeper into the dark and foreboding forest, where every step seems to echo in the silence. The air is thick with uncertainty, and every rustle in the bushes could signal an unseen threat. Though {name} feels ready, there’s a nagging sense of doubt, but they press on, knowing there’s no turning back now."
    else:
        chapter_2 = f"Despite the temptation to push forward, {name} chooses to rest, hoping to regain strength for the next leg of their journey. The forest remains eerily silent, with no sign of danger or escape. But the weight of the journey looms large."
    return chapter_2

# Function to generate Chapter 3 content based on choices
def generate_chapter_3(name, goal):
    print("\n--- Chapter 3 ---")
    decision = make_decision(f"Do you continue your search for the {goal}? (y/n): ")
    if decision:
        chapter_3 = f"At their darkest hour, {name} finds themselves standing at the edge of despair. With every passing day, the path to the {goal} seems further out of reach, and the weight of the journey begins to take its toll. In the dead of night, {name} wonders if they will ever find what they seek, but with a deep breath, they resolve to press on, knowing that true adventurers never quit."
    else:
        chapter_3 = f"After much reflection, {name} decides to turn back, uncertain of the future. They leave the pursuit of the {goal} behind, but the journey is far from over. Perhaps another path will reveal itself. The adventure is not yet at an end."
    return chapter_3

# Function to generate Chapter 4 content based on choices
def generate_chapter_4(name):
    print("\n--- Chapter 4 ---")
    decision = make_decision("Do you confront your former ally who betrayed you? (y/n): ")
    if decision:
        chapter_4 = f"After months of searching, {name} uncovers a shocking truth: the true enemy was hiding in plain sight all along. The face they had trusted, the ally they had believed in, was the very force behind the perilous trials. With this revelation, the stakes have never been higher. {name} must prepare for the final confrontation, knowing that everything they’ve fought for could be lost in an instant."
    else:
        chapter_4 = f"Despite the revelation, {name} chooses not to confront the betrayer just yet. The weight of betrayal hangs heavy, but they decide to focus on the quest, putting their personal feelings aside. There may be more to this story than meets the eye."
    return chapter_4

# Function to generate Chapter 5 content based on choices
def generate_chapter_5(name):
    print("\n--- Chapter 5 ---")
    decision = make_decision("Are you ready for the final battle? (y/n): ")
    if decision:
        chapter_5 = f"With newfound resolve, {name} braces for the ultimate showdown. The forces of evil are powerful and relentless, but so too is {name}'s determination. Every lesson learned, every trial faced, has led to this moment. The fate of the quest—and possibly the world—rests in their hands. It’s now or never. With a roar, {name} charges into battle, heart pounding with the weight of destiny."
    else:
        chapter_5 = f"{name} feels uncertain, but the time has come. They prepare for the inevitable battle, steeling themselves for the harsh realities that lie ahead. The air is thick with tension, but they know this is the final challenge."
    return chapter_5

def generate_chapter_6(name, item, goal):
    chapter_6 = f"{name} reaches the ultimate test, standing before a challenge that will determine the fate of their quest for the {goal}. The journey has been long and perilous, but it all comes down to this one final moment. The stakes couldn’t be higher, and the challenge is unlike anything they’ve faced before. Their courage will be tested like never before."
    plot_twist = random.choice(plot_twists)
    chapter_6 += f" The journey ends with a twist: {plot_twist.format(name=name, goal=goal, item=item)}"
    
    return chapter_6

# Function to generate the full story with choices after each chapter
def generate_full_story():
    print("\nWelcome to the Adventure Story Generator!")
    name = input("Enter your name: ")

    # Ask the user how long they want the story to be
    story_length = input("How long do you want your adventure to be? (short/medium/long): ").lower()

    while True:
        # Generate and display the introduction
        introduction, goal = generate_introduction(name)
        print(f"\n--- Introduction ---\n{introduction}\n")  # Added separation for the introduction

        # Chapter 1 choices
        print("\n--- Chapter 1 ---")
        take_item = make_decision("Do you accept the gift of a magic item? (y/n): ")

        chapter_1, item = generate_chapter_1(name, take_item, goal)
        print(chapter_1)

        # Based on story length, decide how many chapters to create
        if story_length == "short":
            chapter_2 = generate_chapter_2(name, item)
            print(chapter_2)

            chapter_3 = generate_chapter_3(name, goal)
            print(chapter_3)

            chapter_5 = generate_chapter_5(name)
            print(chapter_5)

        elif story_length == "medium":
            chapter_2 = generate_chapter_2(name, item)
            print(chapter_2)

            chapter_3 = generate_chapter_3(name, goal)
            print(chapter_3)

            chapter_4 = generate_chapter_4(name)
            print(chapter_4)

            chapter_5 = generate_chapter_5(name)
            print(chapter_5)

        elif story_length == "long":
            chapter_2 = generate_chapter_2(name, item)
            print(chapter_2)

            chapter_3 = generate_chapter_3(name, goal)
            print(chapter_3)

            chapter_4 = generate_chapter_4(name)
            print(chapter_4)

            chapter_5 = generate_chapter_5(name)
            print(chapter_5)

            # Add additional chapters for extended stories
            print("\n--- Chapter 6 ---")
            additional_chapters = input("Do you wish to continue the adventure with more challenges? (y/n): ").lower()

            # Ensuring no chapter repeats
            chapter_6_added = False

            while additional_chapters == 'y' and not chapter_6_added:
                chapter_6 = generate_chapter_6(name, item, goal)
                print(chapter_6)
                chapter_6_added = True  # Mark that Chapter 6 has been added
                additional_chapters = input("Do you want to add more to your story? (y/n): ").lower()

        # Generate and display the inevitable conclusion
        print("\n--- Inevitable Conclusion ---")
        conclusion = random.choice(conclusions).format(name=name, goal=goal)
        print(conclusion)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to generate another story? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break

# Start the story generation
generate_full_story()