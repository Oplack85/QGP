import google.generativeai as genai
import telebot
import datetime
import os

# Set up Google Generative AI
genai.configure(api_key=os.getenv("API_KEY"))

# Define the model generation configuration
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# Define the safety settings for the model
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Create the Generative Model instance
model = genai.GenerativeModel(model_name="gemini-pro",
               generation_config=generation_config,
               safety_settings=safety_settings)

# Set up Telegram bot
token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(token)

# Handle messages from users
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  # Extract the user's message
  user_message = message.text

  # Send a preliminary response
  message_id = bot.send_message(message.chat.id, "جاري الرد...").message_id

  # Construct the prompt for the model
  prompt_parts = [user_message]

  try:
    # Generate a response using the model
    response = model.generate_content(prompt_parts)

    # Send the response back to the user
    bot.send_message(message.chat.id, response.text)

    # Delete the preliminary response
    bot.delete_message(message.chat.id, message_id)

  except Exception as e:
    # Handle the exception and send an error message to the user
    bot.send_message(message.chat.id, f"عذراً، حدث خطأ: {e}")
    bot.delete_message(message.chat.id, message_id)

# Start the bot
bot.polling()
