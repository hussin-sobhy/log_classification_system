from processor_regex import classify_regex
from processor_bert import classify_bert

def classify_log_message(source, log_message):
    if source == "LegacyCRM":
        pass #LLM
    else:
        label = classify_regex(log_message)

        if label is None:
            label = classify_bert(log_message)

        return label
    

if __name__ == "__main__":
    # Example usage
    log_message = "User User123 logged in."
    source = "System"
    
    label = classify_log_message(source, log_message)
    print(f"Log message: {log_message}")
    print(f"Label: {label}")