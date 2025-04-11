from processor_regex import classify_regex
from processor_bert import classify_bert
from processor_llm import classify_llm
import pandas as pd


def classify_log_message(source, log_message):
    """
    Classify log messages based on their source.
    Args:
        source (str): The source of the log message (e.g., "System", "LegacyCRM").
        log_message (str): The log message to classify.
    Returns:
        str: The classification label.
    """

    if source == "LegacyCRM":
        label = classify_llm(log_message)

    else:
        label = classify_regex(log_message)

        if label is None:
            label = classify_bert(log_message)

    return label


def classify(logs):

    labels = []
    for source, log_message in logs:
        label = classify_log_message(source, log_message)
        labels.append(label)
    return labels


def classify_csv(input_file):

    df= pd.read_csv(input_file)
    df['target_label']= classify(list(zip(df['source'], df['log_message'])))
    df.to_csv('data/output.csv', index=False)

if __name__ == "__main__":
    # Example usage
    classify_csv('data/test.csv')

    '''logs = [
            ("ModernCRM", "IP 192.168.133.114 blocked due to potential attack"),
            ("BillingSystem", "User User12345 logged in."),
            ("AnalyticsEngine", "File data_6957.csv uploaded successfully by user User265."),
            ("AnalyticsEngine", "Backup completed successfully."),
            ("ModernHR", "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 RCODE  200 len: 1583 time: 0.1878400"),
            ("ModernHR", "Admin access escalation detected for user 9429"),
            ("LegacyCRM", "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."),
            ("LegacyCRM", "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module."),
            ("LegacyCRM", "The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' for improved functionality."),
            ("LegacyCRM", " The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025")
        ]
    
    labels = classify(logs)
    print(labels)'''