from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# Load the LlamaCpp language model, adjust GPU usage based on your hardware
llm = LlamaCpp(   
    model_path="models/llama-2-7b-chat.Q5_K_M.gguf",    
    # model_path="models/Meta-Llama-3-8B-Instruct-Q6_K.gguf",  
    # model_path="models/Meta-Llama-3-8B-Instruct-Q8_0.gguf", 
    n_gpu_layers=40,
    n_batch=512,  # Batch size for model processing
    verbose=False,  # Enable detailed logging for debugging
    device="cuda"
)

def import_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming each line contains a single data entry
            # Modify this part according to the structure of your text file
            data.append(line.strip())
    return data

# Example usage:
file_path = 'test_sample.txt'  # Replace 'data.txt' with your actual file path
data = import_data(file_path)

trans_lang = "French"
source_lang = "English"

# Define the prompt template with a placeholder for the question
template = """
Question: {question}

Answer:
"""
# Generate translation queries for each sentence
translation_queries = [f"Translate '{sentence}' from {source_lang} to {trans_lang}. I don't need any other sentences except the translation sentences." for sentence in data]

# translation_queries = [f"Translate '{sentence}' into {trans_lang}." for sentence in data]
print(translation_queries)

# Create an LLMChain to manage interactions with the prompt and model
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

print("Chatbot initialized, ready to translate...")
for query in translation_queries:
    answer = llm_chain.run(query)
    print(answer, '\n')