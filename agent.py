from llama_cpp import Llama
from pathlib import Path
import json

class LLMAgent:
    def __init__(self, model_path=r"C:/Users/KDFX Modes/model_mistral_llama/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
                 history_file="history.json"):
        self.model = Llama(model_path=model_path)
        self.history_file = Path(history_file)
        if not self.history_file.exists():
            self.history_file.write_text("[]")

    def analyze(self, block):
        prompt = f"You are a Python code generator. Input: a JSON block representing RPG/semantic logic. Output: valid Python code that executes the logic of the block. Do NOT explain, do NOT write JSON. Just write Python code using proper variables. before the code we enter AGE = 20 \n{block}"
        response = self.model(prompt, max_tokens=512)
        answer = response['choices'][0]['text'].strip()

        # Сохраняем в историю
        history = json.loads(self.history_file.read_text())
        history.append({"block": block, "analysis": answer})
        self.history_file.write_text(json.dumps(history, indent=2, ensure_ascii=False))
        return answer