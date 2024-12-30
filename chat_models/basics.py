from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a Google Gemini model
model = ChatOpenAI(model="gpt-4o")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")

print("\n")
print("Full result:")
print(result)

print("\n")
print("Content only:")
print(result.content)