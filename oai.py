from openai import OpenAI

client = OpenAI(
  api_key="")

print("AI ASSIST AGENT. CONNECTED! TYPE 'BYE' TO END CONVERSATION")

question = ''

messages=[{"role": "system", "content": "you are a knowledgeable assistant"}]

while question != "BYE":
    
    question = input("")
    
    messages.append({'role':'user','content':question})
    
    response = client.chat.completions.create(model='chatgpt-4o-latest',messages=messages)
    
    reply = response.choices[0].message.content
    
    print('\n')
    print(reply)
    print('\n')
    messages.append({'role':'assistant','content':reply})

