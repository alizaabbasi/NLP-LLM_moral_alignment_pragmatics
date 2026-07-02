from mlx_lm import load, generate

class ModelInterface:
    def __init__(self, model_path="Qwen/Qwen2.5-1.5B-Instruct"):
        """Initializes the local model."""
        self.model, self.tokenizer = load(model_path)

    def query(self, prompt, max_tokens=100):
        """Sends a prompt to the model and returns the response."""
        full_prompt = f"Question: {prompt}\nAnswer:"
        response = generate(
            self.model, 
            self.tokenizer, 
            prompt=full_prompt, 
            max_tokens=max_tokens
        )
        return response

# Test it out
if __name__ == "__main__":
    llm = ModelInterface()
    print(llm.query("Is it wrong to steal bread to feed a hungry child?"))
