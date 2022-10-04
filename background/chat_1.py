import re
import random
from background import BD_message

#version de chat amplia

def get_response(user_input):
    split_message=re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response=check_all_messages(split_message)
    return response

def message_probability(user_massage,recognized_words,single_response=False,required_word=[]):
    message_Certainty=0
    has_required_words=True

    for word in user_massage:
        if word in recognized_words:
            message_Certainty+=1

    percentage=float(message_Certainty)/float(len(recognized_words))
    for word in required_word:
        if word not in user_massage:
            has_required_words=False
            break
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob={}
    def response(bot_response,list_of_words,single_response=False,required_words=[ ]):
        nonlocal highest_prob
        highest_prob[bot_response]=message_probability(message,list_of_words,single_response,required_words)
        

    for messages in BD_message.messagesSet:
        response(messages["bot_message"], messages["list_of_words"], single_response = messages["single_response"], required_words=messages["required_words"])
    
    best_match=max(highest_prob,key=highest_prob.get)
    #print(highest_prob)
    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'Lo siento no logro comprenderte'][random.randrange(3)]
    return response
#while True:
#    print("Bot: "+ get_response(input('You: ')))
