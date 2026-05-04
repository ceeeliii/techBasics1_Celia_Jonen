import time

def slow_print(text, delay=0.5):
    print(text)
    time.sleep(delay)

def ask_choice(prompt, valid_options):
    while True:
        answer = input(prompt).strip().upper()
        if answer in valid_options:
            return answer
        slow_print("That doesn't look right. Please try again.", 0.6)

def ask_int_in_range(prompt, min_value, max_value):
    while True:
        raw = input(prompt).strip()

        # Conditional 1: check if input is a number
        if not raw.isdigit():
            slow_print("Please enter a whole number, eg. '8' (digits only).", 0.6)
            continue

        n = int(raw)

        # Conditional 2: range check
        if min_value <= n <= max_value:
            return n
        else:
            slow_print(f"Number must be between {min_value} and {max_value}. Try again.", 0.7)

def normalize_text(s):
    return " ".join(s.strip().lower().split())

def main():
    slow_print("Welcome to the Harry Potter Quiz 🪄!", 0.6)
    slow_print("You will answer 5 questions.", 0.9)
    time.sleep(0.4)

    # Nested game loop: restart option
    while True:
        score = 0

        # User Input 1
        name = input("What is your name? ").strip()
        if name == "":
            # Conditional 3
            slow_print("No name entered. I'll call you 'Wizard'.", 0.6)
            name = "Wizard"
        else:
            slow_print(f"Great, {name}!", 1.0)

        time.sleep(0.4)

        # User Input 2 (branching choice before the quiz)
        difficulty = ask_choice( "Choose difficulty: (E)asy or (H)ard: ",
            valid_options={"E", "H"} )

        if difficulty == "E":
            # Conditional 4
            slow_print("Easy mode: You get a small hint when needed.", 0.5)
        else:
            # Conditional 4
            slow_print("Hard mode: No hints. Go for it!", 0.5)

        time.sleep(0.7)

        enemy_house = "Slytherin"  # just for story flavor

        slow_print("Question 1/5: In which house is Harry Potter?", 0.5)
        slow_print("Type your answer.", 0.4)

        # User Input 3 (text input)
        q1 = normalize_text(input("Your answer: "))

        # Conditional 5
        if q1 in {"gryffindor"}:
            slow_print("Correct! 🦁", 0.6)
            score += 1
        else:
            # Conditional 6 (nested within else path)
            if difficulty == "E":
                slow_print("Hint: Think of courage and bravery.", 0.7)
            slow_print("Not quite. The answer was 'Gryffindor'.", 0.7)

        time.sleep(0.5)

        slow_print("Question 2/5: What is the name of Harry's owl?", 0.5)
        q2 = normalize_text(input("The name of his owl is... : "))

        # Conditional 7
        if q2 == "hedwig":
            slow_print("Correct! Owls deliver magic mail. 🦉", 0.6)
            score += 1
        else:
            if q2 == "hedwig's" or q2 == "hedwig,":
                slow_print("That is effectively correct—nice try!", 0.6)
                score += 1
            else:
                slow_print("Incorrect. The correct answer is 'Hedwig'.", 0.7)

        time.sleep(0.6)

        slow_print("Question 3/5: Which spell lets Harry control his broom? (Choose A/B/C)", 0.5)
        slow_print("A) Wingardium Leviosa")
        slow_print("B) Accio")
        slow_print("C) Stupefy")

        # User Input 4 (choice input)
        q3 = ask_choice("Your choice (A, B, or C): ", valid_options={"A", "B", "C"})

        # Conditional 8
        if q3 == "A":
            if difficulty == "H":
                slow_print("Hard mode penalty: That doesn't control a broom.", 0.6)
            slow_print("Answer: Not this one. (Correct spell isn't among these choices.)", 0.7)
        elif q3 == "B":
            slow_print("Not quite—'Accio' is for summoning objects.", 0.7)
        else:
            slow_print("Correct for the quiz answer? Actually 'Stupefy' stuns opponents — not brooms.", 0.7)

        # For a fun twist, we’ll make question 3 award points based on a range input next.
        slow_print("Mini-task: To earn points here, give your 'confidence' (1 to 10).", 0.5)

        confidence = ask_int_in_range("Confidence number (1-10): ", 1, 10)

        # Conditional 9 (range-based scoring)
        if confidence >= 7:
            slow_print("High confidence! Bonus points granted. ✨", 0.6)
            score += 1
        else:
            slow_print("Confidence was a bit low. No bonus this time.", 0.6)

        time.sleep(0.7)

        slow_print("Question 4/5: Choose the Patronus animal: (A) Doe (B) Wolf (C) Snake", 0.5)
        slow_print("In your story, what would you pick?")

        # User Input 5
        q4 = ask_choice("Your choice (A/B/C): ", valid_options={"A", "B", "C"})

        # Conditional 10 (branching point with different results)
        if q4 == "A":
            slow_print("A doe: You are calm, kind, and protective. 🦌", 0.6)
            score += 1
        elif q4 == "B":
            slow_print("A wolf: Strong instincts and loyalty. 🐺", 0.6)
            score += 0  # different result
        else:
            # Conditional 11 (nested inside else-if)
            if difficulty == "H":
                slow_print("Snake pick on Hard mode? Risky... Slytherin energy! 🐍", 0.7)
                score += 1
            else:
                slow_print("Snake pick, but Easy mode keeps you balanced. You gain no point.", 0.7)

        time.sleep(0.6)

        slow_print("Question 5/5: True or False?", 0.5)
        slow_print("Prompt: 'Voldemort could not be destroyed because he had Horcruxes.'")

        q5 = ask_choice("Answer (T/F): ", valid_options={"T", "F"})

        # Conditional 12 (another nested conditional)
        if q5 == "T":
            if enemy_house == "Slytherin":
                # This is a nested conditional inside the True branch
                slow_print("Correct! Even Slytherins can't deny this fact.", 0.7)
            else:
                slow_print("Correct!", 0.6)
            score += 1
        else:
            slow_print("Incorrect. With Horcruxes, it was just much harder to fully destroy him.", 0.8)

        time.sleep(0.6)

        # Final results
        slow_print(f"Quiz finished! {name}, your score is {score}/5.", 0.7)

        if score == 5:
            slow_print("Perfect score. You are a real wizard! 🏆", 0.8)
        elif score >= 3:
            slow_print("Nice job! You know your magic.", 0.8)
        else:
            slow_print("Not bad — but you should learn your spells. Try again!", 0.8)

        # Restart option
        time.sleep(0.8)
        restart = ask_choice("Do you want to restart? (Y/N): ", valid_options={"Y", "N"})
        if restart == "N":
            slow_print("Thanks for playing! Goodbye! ✨", 0.6)
            break
        else:
            slow_print("Restarting the quiz...", 0.6)
            time.sleep(0.4)

if __name__ == "__main__":
    main()
