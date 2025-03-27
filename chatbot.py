
##Just trying to code with ai 

import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from googletrans import Translator


chatbot = ChatBot("FAQBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")


trainer = ListTrainer(chatbot)


trainer.train([
    "What is your name?", "I am an AI chatbot.",

    "What are your business hours?", "Our business hours are 9 AM to 5 PM, Monday to Friday.",
    "Who created you?", "I was created by Jepjepandfriends.",
    "Who is your maker?", "My creator is Jepjepandfriends.",
    "Who developed this chatbot?", "This chatbot was developed by Jepjepandfriends.",
    "Can you find my files?", "Yes, tell me the file or folder name, and I will search for it."
])


translator = Translator()

# Function to search for files or folders
def find_item(name, search_path="C:\\vardump"):
    found_items = []

    print(f"🔍 Searching in {search_path}... (This may take time)")

    for root, dirs, files in os.walk(search_path, topdown=True):
        try:

            if name.lower() in [f.lower() for f in files]:
                found_items.append(os.path.join(root, name))


            if name.lower() in [d.lower() for d in dirs]:
                found_items.append(os.path.join(root, name))
        except PermissionError:
            continue  # Skip directories with restricted access

    if found_items:
        return "\n".join(found_items)
    else:
        return f"⚠️ Sorry, I couldn't find '{name}' in {search_path}."


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break


    detected_lang = translator.detect(user_input).lang
    translated_input = translator.translate(user_input, src=detected_lang, dest='en').text.lower()


    if "find" in translated_input:
        parts = translated_input.replace("find", "").strip().split(" in ")

        file_or_folder_name = parts[0].strip()
        search_location = parts[1].strip() if len(parts) > 1 else "C:\\"  # Default to C:\ if no location given

        response = find_item(file_or_folder_name, search_path=search_location)
    else:
        response = chatbot.get_response(translated_input)


    translated_response = translator.translate(str(response), src='en', dest=detected_lang).text
    print(f"Bot ({detected_lang}):", translated_response)
