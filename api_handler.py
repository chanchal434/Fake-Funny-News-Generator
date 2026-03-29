# api_handler.py
import google.generativeai as genai
import random
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Automatically fetch the key from the environment
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API if the key exists
if api_key:
    genai.configure(api_key=api_key)

def generate_fake_news(mode, place, person, news_type, tone, custom_prompt=""):
    """
    Generates fake news using Google Gemini. 
    Falls back to a fun mock generator if no API key is found in the .env file.
    """
    if not api_key:
        return generate_mock_news(place, person, news_type, tone)

    # Construct the prompt based on the mode
    # We combine the system instructions and the format request into one clear prompt for Gemini
    if mode == "Custom Input":
        prompt = f"You are a satirical news writer. Write a {tone} {news_type} news article based on this prompt: {custom_prompt}. Make it safe, humorous, and entertaining.\n\nFormat the output EXACTLY like this:\nHeadline: [Your Headline]\n\n[Your Content]"
    else:
        prompt = f"You are a satirical news writer. Write a short, {tone} {news_type} fake news article involving a person named {person} in {place}. Include a catchy headline. Make it safe, humorous, and entertaining.\n\nFormat the output EXACTLY like this:\nHeadline: [Your Headline]\n\n[Your Content]"

    try:
        # Use the fast and free Gemini 1.5 Flash model
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        text = response.text
        
        # Parse the response into Headline and Content
        # We also strip out any markdown bolding (**) Gemini might accidentally add to the "Headline:" text
        if "Headline:" in text:
            parts = text.split("\n\n", 1)
            headline = parts[0].replace("Headline:", "").replace("**", "").strip()
            content = parts[1].replace("**", "").strip() if len(parts) > 1 else ""
        else:
            headline = f"Breaking {news_type} News in {place}!"
            content = text
            
        return headline, content
        
    except Exception as e:
        return "API Error", f"Oops! The API broke its own bakwaas. Error: {str(e)}"

def generate_mock_news(place, person, news_type, tone):
    """A fallback generator so the app works even without an API key."""
    headlines = [
        f"{person} Discovers New Element in {place} That Turns Water into Chai",
        f"Local {place} Resident {person} Claims to Have Found the End of the Internet",
        f"Aliens Appoint {person} from {place} as Earth's New Manager"
    ]
    
    contents = [
        f"A surprising event unfolded in {place} today when {person} made a shocking discovery that has left scientists baffled. 'I just followed the smell of samosas,' said {person}. The government is currently investigating the situation.",
        f"In a dramatic twist of events, {place} has been shut down temporarily after {person} accidentally unplugged the main server. Authorities urge citizens to remain calm and read a book.",
        f"Citizens of {place} are celebrating today as {person} has finally solved the city's traffic problem by suggesting everyone just stay home. A genius move!"
    ]
    
    return random.choice(headlines), random.choice(contents)