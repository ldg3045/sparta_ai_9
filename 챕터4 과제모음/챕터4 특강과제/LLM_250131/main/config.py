# 모델 설정
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"

# 생성 설정
GENERATION_CONFIG = {
    "max_length": 100,
    "num_return_sequences": 1,
    "temperature": 0.7,
}

# 결과 저장 설정
RESULTS_FILE = "results.json" 