from textblob import TextBlob 

intents = {
    "hours":{
        "keywords":["hours","open", "close"],
        "response": "We are open from 9AM to 5PM, Monday to Friday."
    },
    "return":{
         "keywords": ["refund"],
         "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent."
    }
}
def get_response(message):

    message = message.lower() 
    for intent_name, intent_data in intents.items():   
        if any(word in message for word in intent_data["keywords"]):
            return intent_data["response"]

    sentiment = TextBlob(message).sentiment.polarity
    if sentiment < 0:
        return "That's go great to hear!"
    elif sentiment < 0:
        return "I'm so sorry to hear that.How can I help?"
    else:
        return "I see. Can you tell me more about that?"

def chat():
    print("Chatbot: Hi how can I helpyou today?")
    while (user_message := input("You; ").strip().lower()) not in ['exit', 'quit', 'bye']:
        print(f"\nChatbot: {get_response(user_message)}")


        print("ChatBot: Thank you for chatting. Have a great day!")

if __name__ == "__main__":
    chat()