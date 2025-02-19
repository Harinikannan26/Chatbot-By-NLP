# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:14:25 2025

@author: harin
"""

import tkinter as tk
from tkinter import Scrollbar, Entry, Text, Button
import nltk
from nltk.chat.util import Chat, reflections

# Predefined chatbot responses
pairs = [
    ["hi|hello|hey", ["Hello! How can I help you?"]],
    ["how are you?", ["I'm just a chatbot, but I'm doing well!"]],
    ["what is your name?", ["I'm an AI chatbot."]],
    ["bye|goodbye", ["Goodbye! Have a great day!"]],
    ["(.*) help (.*)", ["Sure! What do you need help with?"]],
    ["(.*) your name?", ["I am a simple chatbot built with NLP."]],
    ["(.*)", ["Sorry, I don't understand that. Can you rephrase?"]],
]

# Create chatbot using NLTK
chatbot = Chat(pairs, reflections)

# Function to handle user input
def send_message():
    user_input = user_entry.get().strip()
    if user_input:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"You: {user_input}\n")
        response = chatbot.respond(user_input)
        chat_box.insert(tk.END, f"Bot: {response}\n\n")
        chat_box.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)

# Tkinter GUI setup
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("400x500")

# Chatbox
chat_box = Text(root, bg="white", font=("Arial", 12))
chat_box.config(state=tk.DISABLED)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(chat_box)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Entry box for user input
user_entry = Entry(root, font=("Arial", 14))
user_entry.pack(pady=10, fill=tk.X, padx=10)

# Send button
send_button = Button(root, text="Send", font=("Arial", 14), bg="lightblue", command=send_message)
send_button.pack(pady=5)

# Run the chatbot GUI
root.mainloop()
