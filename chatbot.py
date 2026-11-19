import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Main window
root = tk.Tk()
root.title("Basic Chatbot")
root.geometry("950x750")
root.minsize(700, 550)
root.configure(bg="#edf3fc")

# Header
header = tk.Frame(root, bg="#102f59", height=145)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="🤖",
    font=("Arial", 55),
    bg="#102f59",
    fg="white"
).pack(side="left", padx=45)

title_frame = tk.Frame(header, bg="#102f59")
title_frame.pack(side="left", expand=True)

tk.Label(
    title_frame,
    text="Basic Chatbot",
    font=("Arial", 32, "bold"),
    bg="#102f59",
    fg="white"
).pack()

tk.Label(
    title_frame,
    text="Ask me anything! 😊",
    font=("Arial", 16, "italic"),
    bg="#102f59",
    fg="white"
).pack(pady=5)


# Chat area
chat_frame = tk.Frame(root, bg="white")
chat_frame.pack(fill="both", expand=True, padx=15, pady=15)

chat_area = scrolledtext.ScrolledText(
    chat_frame,
    font=("Arial", 13),
    bg="white",
    fg="#172554",
    wrap=tk.WORD,
    padx=15,
    pady=15,
    state="disabled"
)

chat_area.pack(fill="both", expand=True)


# Add messages to chat
def add_message(sender, message):

    chat_area.config(state="normal")

    if sender == "You":
        chat_area.insert(
            tk.END,
            "                       You\n",
            "user_name"
        )

        chat_area.insert(
            tk.END,
            "                       " + message + "\n\n",
            "user"
        )

    else:
        chat_area.insert(
            tk.END,
            "🤖 Bot:\n",
            "bot_name"
        )

        chat_area.insert(
            tk.END,
            message + "\n\n",
            "bot"
        )

    chat_area.tag_config(
        "user",
        background="#c9e0ff",
        foreground="#142b50",
        justify="right",
        spacing1=8,
        spacing3=8
    )

    chat_area.tag_config(
        "user_name",
        foreground="#1554bd",
        justify="right",
        font=("Arial", 10, "bold")
    )

    chat_area.tag_config(
        "bot",
        background="#e9edf4",
        foreground="#172554",
        justify="left",
        spacing1=8,
        spacing3=8
    )

    chat_area.tag_config(
        "bot_name",
        foreground="#1749a5",
        font=("Arial", 11, "bold")
    )

    chat_area.config(state="disabled")
    chat_area.see(tk.END)


# Chatbot reply function
def chatbot_reply(message):

    msg = message.lower().strip()

    if msg in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    elif "your name" in msg:
        return "I am your Basic Python Chatbot."

    elif "how are you" in msg:
        return "I am fine! Thank you for asking."

    elif "python" in msg:
        return (
            "Python is a popular programming language "
            "used for web development, automation and data analysis."
        )

    elif "time" in msg:
        current_time = datetime.now().strftime("%H:%M:%S")
        return "Current time is " + current_time

    elif "date" in msg:
        today = datetime.now().strftime("%d-%m-%Y")
        return "Today's date is " + today

    elif "thank" in msg:
        return "You're welcome! Happy to help."

    elif "help" in msg:
        return "Sure! You can ask me about Python, date, time or general questions."

    elif "bye" in msg:
        return "Goodbye! Have a nice day. 😊"

    else:
        return "Sorry, I don't understand. Please try another question."


# Send button function
def send_message(event=None):

    message = message_entry.get().strip()

    if message == "":
        return

    add_message("You", message)

    reply = chatbot_reply(message)

    add_message("Bot", reply)

    message_entry.delete(0, tk.END)


# Welcome message
add_message(
    "Bot",
    "Hello! Welcome to Basic Chatbot.\n"
    "Type a message to start chatting."
)


# Bottom input section
bottom = tk.Frame(root, bg="#edf3fc")
bottom.pack(fill="x", padx=15, pady=15)

message_entry = tk.Entry(
    bottom,
    font=("Arial", 15),
    bg="white",
    fg="#172554",
    relief="solid",
    bd=1
)

message_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=15,
    padx=(0, 12)
)

message_entry.insert(0, "")

send_button = tk.Button(
    bottom,
    text="Send",
    font=("Arial", 14, "bold"),
    bg="#1765ed",
    fg="white",
    activebackground="#124fc0",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=send_message
)

send_button.pack(side="right", ipadx=25, ipady=10)

# Enter key support
message_entry.bind("<Return>", send_message)

# Start application
message_entry.focus()
root.mainloop()

