from openai import AzureOpenAI
import spotipy
import os
import json
import spotipy.util as util


client = AzureOpenAI(
api_key=os.getenv("AZURE_OPENAI_KEY"),
api_version ="2023-10-01-preview",
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)

# open file with keys and set the path to your credentials JSON file
credentials = "spotify_keys.json"
with open(credentials, "r") as keys:
    api_tokens = json.load(keys)

client_id = api_tokens["client_id"]
client_secret = api_tokens["client_secret"]
redirectURI = api_tokens["redirect"]
username = api_tokens["username"]

def find_song(keyword, gerne, ):
	sp.search(q=keyword+"genre:" + genre, limit=1)
	return f"A song from {year} that is {genre} is {song}"

	

functions = [
{
"type":"function",
"function" : {
	"name" :"find_song",
	"description":"retrieve songs based on keywords and genres",
	"parameters" :{
	    "type":"object",
	    "properties":{
	        "keyword" :{
	            "type":"string",
	            "description":"A word that appears in the song title"
	         },
	         "genre":{
	             "type":"string",
	             "description":"The gerne of the song."
	         },
	         "required":["keyword","genre"],
	        },

	      },
      },
      }
]

message = [
    {"role":"user","content":"what is a pop song with thw word banana?"}        

]

response = client.chat.completions.create(
	model="GPT-4",
	message = my_message,
	tools = functions,
	tool_choice = "auto"
)

print(response.choices[0].message.content)

function_calls = response_message.tool_calls
   if function_calls:

   	available_function = {
   	"find_song":find_song,
    }

    messages.append(response_message)

    for function_call in function_calls
         function_name = function_call.function.name
         function_to_call = available_functions[function_name]
         function_args = json.loads(function_call.function.arguments)
         function_response = function_to_call(
         	keyword=function_args.get("keyword"),
         	genre=function_args.get("genre"),

         	)

         for arg in function.function_args