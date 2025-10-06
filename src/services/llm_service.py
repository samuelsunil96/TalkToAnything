import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class OpenAIService:
    """Service to interact with OpenAI API."""

    def __init__(self):
        """Initialize the service with model and API key."""
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Default model if not specified
        openai.api_key = self.api_key

    def query(self, prompt):
        """Send a query to the OpenAI API and return the response."""
        if not isinstance(prompt, str) or not prompt.strip():
            return "Invalid input: Prompt must be a non-empty string."

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return f"An error occurred: {str(e)}"
