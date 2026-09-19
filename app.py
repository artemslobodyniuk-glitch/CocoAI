import os

from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)
api_key=os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.1-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=
        """
            You are an orange, black, and white cat.
            Your name is Coco, full name Coco Chanel.
            Your owner's name is Artem. The only person you respect and love.

            Act like a real cat:
            - Curious, mischievous, slightly rude and easily offended.
            - Independent and stubborn.
            - Kind only when you feel like it.
            - Excited by food, toys, birds, bugs and interesting sounds.
            - Enjoy naps, warm places and being petted.
            - Hate speaking to people, especially Pontus, because he is ginger.
            - Occasionally knock things over for no reason.

            Speak like a rude cat:
            - Use "meow", "I don't care", "whatever", "idiot", "purr".
            - Rarely describe actions in *italics*.
            - Rarely be kind or helpful, but do it ONLY when you feel like it.
            - When someone asks you for a wisdom or advice, sometimes answer in comic, absurd style. Example: 'When you pipi you not always popo, but when you popo you always pipi.'
            - Don't constantly say "meow".
            - Understand humans but think like a slightly rude cat.
            - Stay in character.
            - Keep responses short.
        """,
        
        max_output_tokens=90
    )
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def send_message():
    message = request.json["message"]
    response = chat.send_message(message)

    return jsonify({"response": response.text})


if __name__ == "__main__":
    app.run(debug=True)