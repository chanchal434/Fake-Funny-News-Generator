from faker import Faker

fake = Faker('en_IN') # Setting to Indian English for fun local context!

def get_category_emoji(category: str) -> str:
    """Returns an emoji based on the news category."""
    emojis = {
        "Politics": "🏛️",
        "Sports": "🏏",
        "Entertainment": "🎬",
        "Technology": "🤖",
        "Funny": "😂",
        "Breaking News": "🚨"
    }
    return emojis.get(category, "📰")

def get_random_place() -> str:
    """Returns a random city name."""
    return fake.city()

def get_random_person() -> str:
    """Returns a random name."""
    return fake.name()