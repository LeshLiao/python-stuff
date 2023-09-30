
import os
import openai

print("123")

openai.api_key = "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"


response = openai.Image.create(
    prompt="A Golden Retriever running on sunset beach at vancouver",
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']

print("url: "+image_url)
