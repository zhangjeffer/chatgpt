import os
import openai


openai.organization = "org-TPXGL1yF5kmjpO2ugDGrW4mc"
openai.api_key = "INSERT_KEY_HERE"
model = "davinci"


response = openai.ChatCompletion.create(
   model="text-davinci-003",
   prompt="Say this is a test",
   max_tokens= 7,
   temperature= 0,
   top_p= 1,
   n= 1,
   stream= False,
   logprobs= None,
   stop= "\n")

print(response)
