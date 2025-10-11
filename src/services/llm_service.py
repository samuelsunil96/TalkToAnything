import os
from openai import OpenAI
from utils.image_utils import encode_image, get_image_input  # Import the encode_image function

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class OpenAIService:
    """Service to interact with OpenAI API."""

    def __init__(self):
        """Initialize the service with model and API key."""
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Default model if not specified
        self.client = OpenAI(api_key=self.api_key)

    def query(self, prompt):
        """Send a query to the OpenAI API and return the response.
        """
        if not isinstance(prompt, str) or not prompt.strip():
            return "Invalid input: Prompt must be a non-empty string."

        try:
            response = self.client.chat.completions.create(model=self.model,
            messages=[{"role": "user", "content": prompt}])
            return response.choices[0].message.content
        except Exception as e:        
            return f"An error occurred: {str(e)}"        

    def send_image(self, image_path):
        """Send an image to the OpenAI API and return the response."""
        if not os.path.exists(image_path):
            return "Image not found."

        try:
            base64_image = encode_image(image_path)
            response = self.client.responses.create(
                model=self.model,
                input=get_image_input(base64_image))
            return response.output_text

        except Exception as e:
            return f"An error occurred while sending the image: {str(e)}"
