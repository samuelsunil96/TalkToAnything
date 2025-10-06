class MockOpenAIService:
    """A mock service to simulate OpenAI API calls."""

    def __init__(self):
        """Initialize the mock service."""
        self.responses = {
            "greet": "Hello! How can I assist you today?",
            "farewell": "Goodbye! Have a great day!",
        }

    def call_api(self, prompt):
        """Simulate an API call to OpenAI."""
        return self.responses.get(prompt, "I'm not sure how to respond to that.")
