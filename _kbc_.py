import random
import time

print("WELL COME TO KBC LITE")
time.sleep(2)
print("YOUR LIFE LINES ARE:-")
time.sleep(2)
print("*PHONE A FRIEND")
time.sleep(2)
print("*50-50")
time.sleep(2)
print("RULES OF THE GAME :)")
time.sleep(2)
print("1.IN QUIZ FOR EVERY QUESTION U WILL BE PROVIDED 4 OPTIONS")
time.sleep(3)
print("2. YOU WIN 1 MILLION FOR EACH CORRECT ANSWER ")
time.sleep(3)
print("3.ONE INCORRECT ANSWER YOU WILL BE OUT OF THIS NO SECOND CHANCE")
time.sleep(3)
print("4.U CAN PRESS 1 FOR 50-50 ")
time.sleep(2)
print("AND 2 FOR PHONE A FRIEND")
time.sleep(2)
print("6.NO TIME LIMIT ")
time.sleep(2)
print("7.ANSWERS WILL BE CASE SENSITIVE!!!")
print("ALL THE BEST:)")

questions=[
   {
       "question":"Which is the most sensitive organ in our body?",
        "options":["A.eyes","B.brain","C.heart","D.skin"],
        "answer":"D"
    },
    {
        "question":"Gir national park is famous for?",
        "options":["A.tiger","B.lion","C.deer","D.peacock"],
        "answer":"A"
   },
   {   
        "question":"Highest dam of india is?",
        "options":["A.kolar dam","B.tehri dam","C.bagha dam","D.rimjhim dam"],
        "answer":"B"
   },
   {   
        "question":"Baby of horse is called?",
        "options":["A.puppy","B.cub","C.colt","D.kitten"],
        "answer":"C"
    },
    {   
        "question":"Who wrote romeo and juliet",
        "options":["A.Shakespear","B.Robert.frost","C.J.drowney","D.Martin"],
        "answer":"A"
    },
    { 
        "question":"Cry of loin is called?",
        "options":['A.roar','B.cry','C.trumph','D.morn'],
        "answer":"A"
    },
    { 
        "question":"Which planet is nearest to earth?",
        "options":['A.mars',"B.vinus","C.moon","D.neptune"],
        "answer":"B"
    },
    { 
        "question":"Where does a dog live?",
        "options":["A.hive","B.stable","C.den","D.kennel"],
        "answer":"C"
    },
    {
        "question": "Largest island in the world ?",
        "options":["A.lakshdeep","B.andaman nicobar","C.greenisland","D.iceland"],
        "answer":"B"
    },
    {
        "question":"A place where bees are kept is called?",
        "options":["A.hive","B.aviary","C.resty","D.class"],
        "answer":"A"
     }
]
def fifty_fifty(options, correct_answer):
    remaining_options = [correct_answer]
    for option in options:
        if option != correct_answer:
            remaining_options.append(option)
            if len(remaining_options) == 2:
                break
    return remaining_options
def phone_a_friend(question):
    
    print("Your friend says: 'I think the answer is...'")
    if random.random() < 0.7:
        return question["answer"]
    else:
        wrong_options = [option for option in question["options"] if option != question["answer"]]
        return random.choice(wrong_options)
money_won = 0
lifelines_available = {"50-50": True, "Phone a Friend": True}

for i, question in enumerate(questions):
    print(f"\nQuestion {i + 1}: {question['question']}")
    for option in question["options"]:
        print(option)
    
    if lifelines_available["50-50"]:
        print("Enter '1' to use 50-50 lifeline")
    if lifelines_available["Phone a Friend"]:
        print("Enter '2' to use Phone a Friend lifeline")
    
    answer = input("Your answer: ").strip().upper()
    
    if answer == "1" and lifelines_available["50-50"]:
        lifelines_available["50-50"] = False
        remaining_options = fifty_fifty(question["options"], question["answer"])
        print(f"Remaining options after using 50-50: {', '.join(remaining_options)}")
        answer = input("Your answer: ").strip().upper()
    
    elif answer == "2" and lifelines_available["Phone a Friend"]:
        lifelines_available["Phone a Friend"] = False
        friend_answer = phone_a_friend(question)
        print(f"Your friend suggests the answer: {friend_answer}")
        answer = input("Your answer: ").strip().upper()
    
    if answer == question["answer"]:
        print("Correct!\n")
        money_won += 1000000 
    else:
        print("Sorry, that's incorrect. Game Over!")
        break

print(f"You've won ${money_won}")