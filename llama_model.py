from llama_cpp import Llama

llm = Llama(
    model_path="models/Meta-Llama-3-8B-Instruct-Q8_0.gguf",
    n_ctx=4096,      # Max tokens for in + out
    n_threads=4,     # CPU cores used
    n_gpu_layers=-1,  # Load all layers into VRAM of the GPU
)
# output = llm.create_chat_completion(
#     messages = [
#         {"role": "system", "content": "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability."},
#         {
#             "role": "user", "content": "Translate from French string into English string. PV"
#         }
#     ]
# )

trans_lang = "English"
source_lang = "French"
style = "written"

system_prompt = f"Translate the following string into {trans_lang}."
# system_prompt = "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability. Translate from French string into English string."


def response_with_ai(prompt, temperature, max_tokens=2048):

    response = llm(prompt, max_tokens=max_tokens, temperature = temperature, stop=["Q:", "\n"], echo=False)

    return response

def build_prompt(string): 
    prompt = f"Translate '{string}' from French into English. I need only translation string. Do not translate numbers and symbols and abbreviation. Keep original style."
    
    prompt = f"Q: {prompt} A:"
    return prompt