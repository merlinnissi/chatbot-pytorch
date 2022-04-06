import random
import json

import torch

from database import queryresource

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"


'''print("Hey. Welcome to luminar technolab")
def get_response(sentence1):
#    # sentence = "do you use credit cards?"
#    sentence1 = input("You: ")
#    #print(sentence1, type(sentence1))
#    if sentence1 == "quit":
#        break

    sentence = tokenize(sentence1)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if tag == "ready":
                    idk = queryresource()
                    compy_name = input("Enter the company name:")
                    poc = input("Place of contact:")
                    mail = input("Your mailid:")
                    num = input("Contect number:")
                    req_tech = input("Required technology:")
                    num_of_cand = input("Number of candidates required")
                    idk.save_hiring(compy_name, poc, mail, num, req_tech, num_of_cand)

                if tag == "student":
                    s_or_w = tag
                if tag == "working professional":
                    s_or_w = tag

                if tag == "suggestion":
                    idk = queryresource()
                    idk.pull_data()

                if tag == "course":
                    idk = queryresource()
                    course = sentence1
                    idk.course_details(course)

                if tag == "continue":
                    idk = queryresource()
                    name = input("Enter you name:")
                    email = input("Enter your email-id:")
                    phn_num = input("Enter your phone number:")
                    on_or_off = input("Would you prefer online/offline course?")
                    idk.save_student(name, course, email, phn_num, on_or_off, s_or_w)

                if tag == "schedule":
                    idk = queryresource()
                    date = input("Enter the date you want to contact:")
                    comments = input("Do you have any comments to add?")
                    idk.virtual_booking(date, course, name, comments)
                print(random.choice(intent['responses']))

    else:
        print("I do not understand...")

'''
def get_response(sentence1):
    sentence = tokenize(sentence1)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if tag == "ready":
                    idk = queryresource()
                    compy_name = input("Enter the company name:")
                    poc = input("Place of contact:")
                    mail = input("Your mailid:")
                    num = input("Contact number:")
                    req_tech = input("Required technology:")
                    num_of_cand = input("Number of candidates required")
                    idk.save_hiring(compy_name, poc, mail, num, req_tech, num_of_cand)

                if tag == "student":
                    s_or_w = tag
                if tag == "working professional":
                    s_or_w = tag

                if tag == "suggestion":
                    idk = queryresource()
                    idk.pull_data()

                if tag == "course":
                    idk = queryresource()
                    course = sentence1
                    idk.course_details(course)

                if tag == "continue":
                    idk = queryresource()
                    name = input("Enter you name:")
                    email = input("Enter your email-id:")
                    phn_num = input("Enter your phone number:")
                    on_or_off = input("Would you prefer online/offline course?")
                    idk.save_student(name, email, phn_num, on_or_off)

                if tag == "schedule":
                    idk = queryresource()
                    date = input("Enter the date you want to contact:")
                    comments = input("Do you have any comments to add?")
                    idk.virtual_booking(date, comments)
                #print(random.choice(intent['responses']))

                return random.choice(intent['responses'])

    return "I do not understand..."


if __name__ == "__main__":
    print("Hey. Welcome to luminar technolab")
    while True:
        # sentence = "do you use credit cards?"
        sentence1 = input("You: ")
        if sentence1 == "quit":
            break

        resp = get_response(sentence1)
        print(resp)