from openai import OpenAI

api_key = 'sk-proj-**************************'	# ① 

client = OpenAI(api_key=api_key)# ② 

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.1,  # ③
    messages=[
        {"role": "system", "content": "답변은 3문장 이상으로 해라."},
        {"role": "user", "content": "대한민국의 수도는 어디야?"},
    ]		# ④
)

print(response)

print('----')	# ⑤
print(response.choices[0].message.content) 