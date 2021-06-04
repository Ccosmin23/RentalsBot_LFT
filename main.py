import requests as requests
from googlesearch import *
import webbrowser

luisURL = "https://searchwebbot.cognitiveservices.azure.com/luis/prediction/v3.0/apps/fe32d3bb-d321-40ba-965a-3d34283897cf/slots/staging/predict?subscription-key=a04e5a3a6c2549f78234bd76c7ab0d5b&verbose=true&show-all-intents=true&log=true&query="

#query = input("Search on web:")

def getStop():

    while False:

        break

def make_query(query):
    return requests.get(luisURL + query).json()

def main(count):
    print("\nHello World I'm ToBi")
    user_input = input("What's your name?\n")

    response = make_query(user_input)
    user_prediction = make_query(user_input).get("prediction")
    user_intent = user_prediction.get("topIntent")
    user_entities = user_prediction.get("entities").get("$instance")
    getName(count, user_intent, user_input)



def getHelp(count, count2):

    user_input = input()
    user_prediction = make_query(user_input).get("prediction")
    user_intent = user_prediction.get("topIntent")

    if user_intent == "name":
        count2 += 1
        print("Nice name bro, tell me how can I help you please")
        if count2 < 2:
            getHelp(count, count2)
        else:
            print("Leave it mate, you have no one with")
            print("------------------------------------------------------------------------------")
            print("\n")
            main(0)

    if user_intent == "greeting":
        if count < 1 :
            count += 1
            print(count)
            print("over and over again")
            print("\nHi OkieDokie, how can I help you with?")
            getHelp(count, count2)
        else:
            print("You waste my time...bye bye OkieDokie")
            print("------------------------------------------------------------------------------")
            print("\n")
            main(0)

    if user_intent == "None":
        print("Bla bla bla\n keep calm mate, you're annoying and I'm here to help you")
        query = 'hello'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(query, tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open(
                "https://www.healthline.com/health/how-to-calm-down?q=%s" % query)
        print("------------------------------------------------------------------------------")
        print("\n")
        main(0)

    if user_intent == "rental":
        user_input = input("What are you looking for more exactly?\n")
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(user_input, tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open(
                "https://www.google.com/search?q=%s" % user_input)
        print("------------------------------------------------------------------------------")
        print("\n")
        main(0)


def getName(count, user_intent, user_input):
        if user_intent == "name":
            print("\nHi " + user_input + ", how can I help you?")
            getHelp(0, 0)
        if user_intent == "greeting":
            count += 1
            user_input = input("Can you enter your name please?\n")
            user_prediction = make_query(user_input).get("prediction")
            user_intent = user_prediction.get("topIntent")
            if user_intent == "name":
                print("\nHi " + user_input + ", how can I help you?")
                getHelp(0, 0)
            if count < 2:
                getName(count, user_intent, user_input)
            else:
                print("\nNice joke mate, I have no words...anyway hopefully you're not getting dumb")
                print("I pretend you're fine, and I nickname you OkieDokie")
                user_input = 'OkieDokie'
                print("\n\nHi " + user_input + ", how can I help you with?")
                getHelp(0, 0)


if __name__ == "__main__":
    main(0)










