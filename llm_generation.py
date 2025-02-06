from llama_cpp import Llama
import random

MODEL_PATH = 'ai-text-game/models/<path to model>'

llm = Llama(
    model_path=MODEL_PATH,
    # n_gpu_layers=-1, # Uncomment to use GPU acceleration 
    verbose=False, 
    seed=random.randint(0,4294967295), 
    n_ctx=131072, 
    temperature=0.9)

def generateInstruction(systemcontext, userquery, summary, memory = ""):
    #AI prompt composed of system context >> memory >> user query
    prompt = systemcontext + summary + memory + f"User: {userquery}\nGame Master:"
    #Feed prompt to AI function and generate response on resp
    response = llm(prompt, max_tokens=256, stop=["User:", "Game Master:\n"])
    #print(response) #DEBUG
    return str(response["choices"][0]["text"]+"\n")

def generateSummary(summary = "", memory = "" ):
    #Summary execution prompt
    summaryCommand= "System:Create a super short summary of the above story ending with explicitly stating what the user did last. Game Master:"
    #Summary Prompt
    prompt= summary + memory + summaryCommand
    #print(prompt) #DEBUG
    #Create Summary of context
    response = llm(prompt, max_tokens=256, stop=["System:", "Game Master:\n"])
    #print(response) #DEBUG
    return str(response["choices"][0]["text"]+"\n")