from sentence_transformers import SentenceTransformer
import joblib


transformer_model = SentenceTransformer('all-MiniLM-L6-v2')
model = joblib.load('saved_models/log_classifier_logistic.joblib')

def classify_bert(log_message):
    """""
    Classify a log message using a pre-trained BERT model.

    Args:
        log_message (str): The log message to classify.

    Returns:
        str: The predicted category of the log message.
    """
    message_embedding = transformer_model.encode(log_message)
    probabilities = model.predict_proba([message_embedding])[0]

    if max(probabilities) < 0.5:
        #print(max(probabilities))
        return 'unclassified'
    
    predicted_category = model.predict([message_embedding])[0]
    
    return predicted_category

if __name__ == "__main__":
    logs = [
    "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
    "GET /v2/3454/servers/detail HTTP/1.1 RCODE 404 len: 1583 time: 0.1878400",
    "System crashed due to drivers errors when restarting the server",
    "Multiple login failures occurred on user 6454 account",
    "Server A790 was restarted unexpectedly during the process of data transfer",
    "this meassege will retern unknown"
]

    for log in logs:
        category = classify_bert(log)
        print(f"Log: {log} | Predicted Category: {category}")


    