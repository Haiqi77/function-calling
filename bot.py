from openai import AzureOpenAI
import os

client = AzureOpenAI(
	api_key = os.getenv("AZURE_OPENAI_KEY"),
	azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
	api_version = "2023-10-01-preview"
)


def ask_question(character, question):
	messages = [
		
		{"role": "system", "content": "Answer as {character}"},
		{"role": "user", "content": question},
		
	]
	response = client.chat.completions.create(
		model = "GPT-4",
		messages = messages
	)
	return response.choices[0].message.content