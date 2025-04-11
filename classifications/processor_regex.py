import re
def classify_regex(log_message):

    """
    Classify a log message by regex pattern into a category.

    Args:
        log_message (str): The log message to classify.

    Returns:
        str: The category of the log message if it matches a regex pattern, otherwise None.
    """

    regex_patterns = {
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }


    for pattern, category in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return category        
        return None


if __name__ == "__main__":
    log_message = "User User123 logged in."
    category = classify_regex(log_message)
    print(f"Log message: {log_message}")
    print(f"Category: {category}")