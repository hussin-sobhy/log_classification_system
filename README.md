# Log Classification System

A multi-method log classification system that categorizes log messages from different sources using regex patterns, BERT embeddings, and LLM-based classification.

## Overview

This system classifies log messages from various sources (ModernCRM, BillingSystem, AnalyticsEngine, ModernHR, LegacyCRM, etc.) into categories such as:
- User Action
- System Notification
- Error
- Workflow Error
- Deprecation Warning
- Unclassified

The classification strategy varies based on the log source:
- LegacyCRM logs are classified using an LLM (Groq's deepseek-r1-distill-llama-70b)
- Other logs are first attempted with regex patterns
- If regex fails, a BERT-based classifier is used as a fallback

## System Architecture

The system consists of:
1. A FastAPI server for handling classification requests
2. Multiple classification processors:
   - Regex-based classifier for pattern matching
   - BERT-based classifier using sentence transformers and a pre-trained logistic regression model
   - LLM-based classifier using Groq's API
3. A main classifier that orchestrates the different classification methods

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd log_classification_system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root with your Groq API key:
```
GROQ_API_KEY=your-groq-api-key
```

You can obtain a Groq API key by signing up at [https://console.groq.com/](https://console.groq.com/).

## Usage

### Running the API Server

Start the FastAPI server from the project root directory:
```bash
uvicorn app.server:app --reload
```

The server will be available at http://localhost:8000.

### API Endpoints

#### POST /classify/
Accepts a CSV file with 'source' and 'log_message' columns and returns the same data with an additional 'target_label' column containing the classification results.

Example using curl:
```bash
curl -X POST -F "file=@data/test.csv" http://localhost:8000/classify/ -o classified_logs.csv
```

### Command Line Classification

You can also classify logs directly from the command line:

```bash
python -c "from classifications.classifier import classify_csv; classify_csv('data/test.csv')"
```

This will process the logs in `data/test.csv` and save the results to `data/output.csv`.

## Testing

1. Use the provided test data:
```bash
python -c "from classifications.classifier import classify_csv; classify_csv('data/test.csv')"
```

2. Check the output file at `data/output.csv` to see the classification results.

3. You can also test individual processors:

   - Test regex processor:
   ```bash
   python -m classifications.processor_regex
   ```

   - Test BERT processor:
   ```bash
   python -m classifications.processor_bert
   ```

   - Test LLM processor:
   ```bash
   python -m classifications.processor_llm
   ```

## Project Structure

```
/log_classification_system/
├── .env                  # Environment variables (contains Groq API key)
├── .gitignore
├── requirements.txt      # Dependencies
├── app/
│   └── server.py         # FastAPI server for log classification
├── classifications/
│   ├── classifier.py     # Main classifier that orchestrates different methods
│   ├── processor_bert.py # BERT-based classification
│   ├── processor_llm.py  # LLM-based classification using Groq
│   └── processor_regex.py # Regex-based classification
├── data/
│   ├── output.csv        # Output file with classification results
│   ├── synthetic_logs.csv
│   └── test.csv          # Test data
├── saved_models/
│   └── log_classifier_logistic.joblib # Pre-trained model
└── training/
    └── training.ipynb    # Jupyter notebook for model training
```

## Classification Methods

### Regex Classification

Uses regular expression patterns to match common log formats and categorize them. This is the fastest method but limited to predefined patterns.

### BERT Classification

Uses the `all-MiniLM-L6-v2` sentence transformer to convert log messages into embeddings, which are then classified using a pre-trained logistic regression model. This method is more flexible than regex but requires more computational resources.

### LLM Classification

Uses Groq's deepseek-r1-distill-llama-70b model to classify logs from LegacyCRM. This method is specifically designed for complex logs that require deeper understanding and context.

## Training

The BERT classifier uses a pre-trained logistic regression model. To retrain this model:

1. Open and run the Jupyter notebook:
```bash
jupyter notebook training/training.ipynb
```

2. Follow the instructions in the notebook to train and save a new model.

## License

[Specify your license here]

## Contributing

[Specify contribution guidelines here]
