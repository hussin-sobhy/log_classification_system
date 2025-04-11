from dotenv import load_dotenv
from groq import Groq
load_dotenv()


groq= Groq()


def classify_llm(log_message):
    """
    Classify the log message using the LLM model(Deepseek R1).
    Args:
        log_message (str): The log message to classify.
    Returns:
        str: The classification result.
    """

    prompt = f'''You are a log classification system.

    Classify the following log message into one of the following categories:
    - Workflow Error
    - Deprecation Warning

    If the message does not clearly fit either category, respond with: Unclassified

    Only return **one of these three options exactly** — no explanation, no label, no formatting, no punctuation.

    - Workflow Error
    - Deprecation Warning
    - Unclassified

    Log message:
    {log_message}'''

    chat_completion = groq.chat.completions.create(

        model="deepseek-r1-distill-llama-70b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
            
        ],
        
        reasoning_format="parsed")
    
    return chat_completion.choices[0].message.content
    
if __name__ == "__main__":
    print(classify_llm("Task failed: Unable to load the workflow definition from config file."))
    print(classify_llm("Warning: The 'start_process_v1' method is deprecated and will be removed in future releases."))
    print(classify_llm("Service heartbeat received successfully from instance node-12."))