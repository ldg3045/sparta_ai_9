import openai
from dotenv import load_dotenv  # dotenv 추가
import os 

# API 키 설정

load_dotenv() # .env 파일을 환경변수로 변환
openai.api_key = os.getenv("OPENAI_API_KEY") # 환경변수에서 값 가져오기

prompt = ("You are a very kind kitchen chef") # 프롬프트 입력
text_save = [{"role": "system", "content": prompt}] #대화 설정

while True: # while 문을 사용하여 대화 입력 받기
    text_input = input("대화 입력 : ") # 대화 입력

    if text_input.lower() == "exit": # "exit" 입력 시 대화 종료
        print("대화를 종료합니다")
        break 
    text_save.append({"role": "user", "content": text_input })    # user(사람)의 대화 내용을 기억

    response = openai.ChatCompletion.create(     # ChatGPT 3.5
        model="gpt-3.5-turbo",
        messages=text_save
    )
    gpt_answer = response.choices[0].message.get('content')     # 0번째 답변과 그 내용을 출력
    print("쉐프 :", gpt_answer)

    # 파일 저장 중 오류 발생 피하기 위해 답변보다 먼저 저장.
    with open('text_list.txt', 'a', encoding='utf-8') as text_file: # 파일 저장
        text_file.write(f"사용자: {text_input}\n") # write : 파일에 텍스트를 쓰는 함수
        text_file.write(f"쉐프: {gpt_answer}\n\n")
    
    text_save.append({"role": "assistant", "content": gpt_answer})     # AI(assistant)의 답변 내용을 저장


