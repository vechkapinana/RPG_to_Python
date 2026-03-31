from agent import LLMAgent

class GracePipeline:
    def __init__(self, model_path=r"C:\Users\KDFX Modes\model_mistral_llama\mistral-7b-instruct-v0.2.Q4_K_M.gguf"):
        # передаем реальный путь к модели
        self.agent = LLMAgent(model_path=model_path)

    def run(self, blocks):
        results = []
        for block in blocks:
            analysis = self.agent.analyze(block)
            results.append({"block": block, "analysis": analysis})
        return results