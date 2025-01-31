import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from config import MODEL_NAME

def load_model(device):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME) # 토크나이저 로드
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device) # 모델 로드
    return tokenizer, model


def generate_text(input_text, tokenizer, model):
    inputs = tokenizer(input_text, return_tensors="pt")
    # input_text를 토큰화하여 파이토치 텐서로 변환
   
    # 텍스트 생성
    outputs = model.generate(
        **inputs,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7
    )
    # 생성된 텍스트 디코딩
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def main():
    # 프롬프트 파일에서 텍스트 읽기(open 함수 사용)
    with open('prompts.txt', 'r', encoding='utf-8') as f:
        prompts = f.readlines()
    
    # 사용 가능한 device 확인
    device = "cuda" if torch.cuda.is_available() else "cpu" #cpu 또는 cuda 사용
    print(f"Using device: {device}") # 사용 중인 device 출력
    
    try:
        # 모델 로드
        tokenizer, model = load_model(device)
        
        # 각 프롬프트에 대해 텍스트 생성
        for prompt in prompts:
            prompt = prompt.strip() # 양쪽 공백 제거
            if prompt:  # 빈 줄 건너뛰기
                print("\n" + "="*50)
                print(f"입력: {prompt}")
                response = generate_text(prompt, tokenizer, model)
                print(f"출력: {response}")
                
    except Exception as e:
        print(f"\n오류 발생: {e}") # e는 오류 메시지
        print("모델 로드에 실패했습니다.")

if __name__ == "__main__": # main 함수를 호출하여 프로그램 시작
    main()