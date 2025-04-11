from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
import pandas as pd
from classifications.classifier import classify

app = FastAPI()

@app.post('/classify/')
async def classify_logs(file: UploadFile):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV")
    try:
        df = pd.read_csv(file.file)

        if not {'source', 'log_message'}.issubset(df.columns):
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns")
        if df.empty:
            raise HTTPException(status_code=400, detail="CSV file is empty")

        df['target_label'] = classify(list(zip(df['source'], df['log_message'])))

        print('Dataframe:', df.to_dict())

        # Save the modified DataFrame to a new CSV file
        output_file = 'data/output.csv'
        df.to_csv(output_file, index=False)
        print('File saved to:', output_file)

        return FileResponse(output_file, media_type='text/csv', filename='output.csv')
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    finally:
        file.file.close()
        print('File closed')
        # Optionally, you can delete the temporary file if needed
        #if os.path.exists(output_file):
        #     print('Deleting file:', output_file)
        #     # os.remove(output_file)
        
