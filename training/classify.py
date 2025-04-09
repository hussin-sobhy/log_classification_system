from processor_regex import classify_regex

def classify_log_message(source, log_message):
    if source == "LegacyCRM":
        pass #LLM
    else:
        label = classify_regex(log_message)

        if label is None:
            pass #BERT

        return label
    

if __name__ == "__main__":
    # Example usage
    log_message = "User User123 logged in."
    source = "System"
    
    label = classify_log_message(source, log_message)
    print(f"Log message: {log_message}")
    print(f"Label: {label}")