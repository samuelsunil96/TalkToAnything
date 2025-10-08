from src.services.llm_service import OpenAIService

def main():
    print("Hello from talktoanything!")
    service = OpenAIService()
    response = service.query("Hello, how can I assist you today?")
    print(response)


if __name__ == "__main__":
    main()
