#Random code Checker
import pyjokes
import random
jokes_list=[]
quotes_list=[]
def get_joke():
    joke=pyjokes.get_joke()
    jokes_list.append(joke)
    print("Here is your joke: ",joke)
def get_quote():
    quotes=[ "Believe in yourself and all that you are.",
        "Every day is a second chance.",
        "Push yourself, because no one else will do it for you.",
        "The harder you work for something, the greater you'll feel when you achieve it."
        ]
    quote=random.choice(quotes)
    quotes_list.append(quote)
    print("\n Motivational qoute:",quote)
while True:
    print("\n--- Joke & Quote Generator ---")
    print("1. Get a Joke")
    print("2. Get a Motivational Quote")
    print("3. Show All This Session")
    print("4. Exit")
    choice=input("enter your choice: ")
    if choice=="1":
        get_joke()
    elif choice=="2":
        get_quote()
    elif choice == "3":
        print("\nSession Jokes:", jokes_list)
        print("Session Quotes:", quotes_list)
    elif choice == "4":
        print("Thanks For visiting!")
        break
    else:
        print("Invalid choice. Try again")


import random
jokes_list= []
quotes_list = []
def get_joke():
    jokes = [
    "గురువు: నీవు స్కూల్‌కు ఎందుకు రాలేదు? విద్యార్థి: స్కూల్‌కు రాలేదు అంటే స్కూల్ itself రాలేదు!",
    "పెద్దమ్మ: నీకు పెళ్లి చేసుకోవాలనిపించదా? అబ్బాయి: WiFi ఉందిగా!",
    "రాముడు: నన్ను ప్రేమిస్తున్నావా? సీత: నిన్ను కాదు, నీ ఫోన్‌ను!",
    "విద్యార్థి: పరీక్షలో 0 మార్కులు వచ్చాయి. తల్లి: కనీసం నామం రాసావా?",
    "అన్నం తినే ముందు చేతులు కడుక్కోవాలి. కానీ బిర్యానీ అయితే నోరు ముందు కడుక్కోవాలి!",
    "గురువు: నీకు భయమేమైనా ఉందా? విద్యార్థి: Results!",
    "అబ్బాయి: నీకు WhatsApp ఉంది కదా? అమ్మాయి: ఉంది కానీ reply లేదు!",
    "పెద్దవాళ్లు: కాలం మారింది. యువత: SIM మారింది!",
    "విద్యార్థి: నేను చదువుతున్నాను. Google: నమ్మలేకపోతున్నాను!",
    "అమ్మ: నీకు భోజనం కావాలా? అబ్బాయి: PUBG లో Busy!",
    "గురువు: Newton ఎవరు? విద్యార్థి: Apple lover!",
    "అబ్బాయి: నీకు chocolate ఇస్తా. అమ్మాయి: Insta post చేస్తా!",
    "విద్యార్థి: నేను fail అయ్యాను. తల్లి: Fail కాదు, trial!",
    "అబ్బాయి: నీకు love అంటే ఏమిటి? అమ్మాయి: Recharge!",
    "గురువు: పాఠం చెప్పు. విద్యార్థి: YouTube లో search చేస్తా!",
    "అమ్మ: నీకు భోజనం కావాలా? అబ్బాయి: Meme చూస్తున్నాను!",
    "పెద్దవాడు: నీకు ఉద్యోగం కావాలి. యువత: Followers కావాలి!",
    "విద్యార్థి: Exam cancel అయ్యింది. ఆనందం unlimited!",
    "అబ్బాయి: నీకు gift ఇస్తా. అమ్మాయి: Amazon link పంపు!",
    "గురువు: నీ attendance ఎందుకు లేదు? విద్యార్థి: Online లో ఉన్నాను!"
]
    joke=random.choice(jokes)
    jokes_list.append(joke)
    print("Here is your joke:",joke)
def get_quote():
    quotes = [
    "నీవు నమ్మిన దానిని సాధించగలవు.",
    "ప్రతి రోజు ఒక కొత్త అవకాశం.",
    "కష్టపడితే విజయాన్ని రుచి చూడగలవు.",
    "నీవు నిన్ను నమ్ముకుంటే ప్రపంచం నిన్ను నమ్ముతుంది.",
    "విజయం ఓ ప్రయాణం, ఓ గమ్యం కాదు.",
    "నీవు పడే కష్టం నీ భవిష్యత్తును నిర్మిస్తుంది.",
    "ఆలస్యం చేస్తే అవకాశాలు పోతాయి.",
    "నీవు చేసే ప్రతి చిన్న ప్రయత్నం విజయానికి దారి తీస్తుంది.",
    "నీవు నిన్ను మార్చుకుంటే ప్రపంచం మారుతుంది.",
    "విజయం కోసం కష్టపడటం తప్పదు.",
    "నీవు నమ్మిన దానిని సాధించగలవు.",
    "ప్రతి సమస్యకు ఓ పరిష్కారం ఉంటుంది.",
    "నీవు ఓదార్పు కావాలి అంటే ముందుగా ఓదార్చాలి.",
    "కష్టాలు వస్తాయి, కానీ వాటిని జయించగలవు.",
    "నీవు నిన్ను ప్రేమిస్తే జీవితం అందంగా ఉంటుంది.",
    "విజయం ఓ అలవాటు, ఓ మాయ కాదు.",
    "నీవు నిన్ను గెలిపించుకోవాలి.",
    "ప్రతి రోజు ఓ కొత్త ప్రారంభం.",
    "నీవు నీవు నమ్ముకుంటే ఏదైనా సాధ్యమే.",
    "కష్టపడితే కలలు నిజమవుతాయి."
]
    quote=random.choice(quotes)
    quotes_list.append(quote)
    print("\n Motivational qoute:",quote)
while True:
    print("\n--- Joke & Quote Generator ---")
    print("1. Get a Joke")
    print("2. Get a Motivational Quote")
    print("3. Show All This Session")
    print("4. Exit")
    choice=input("enter your choice: ")
    if choice=="1":
        get_joke()
    elif choice=="2":
        get_quote()
    elif choice == "3":
        print("\nSession Jokes:", jokes_list)
        print("Session Quotes:", quotes_list)
    elif choice == "4":
        print("Thanks For visiting!")
        break
    else:
        print("Invalid choice. Try again")

#Weather API


        
        