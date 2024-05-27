import csv
from io import StringIO
from fastapi import HTTPException

def validate_csv(file):
    # Validate that the file is a CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Uploaded file must be a CSV")
    
def process_csv(file_contents: str, equals: str = None):
    try:
        rows = []
        reader = csv.DictReader(StringIO(file_contents))
        for row in reader:
            # Validate that the CSV contains only the columns "Response" and "Value"
            if set(row.keys()) != {'Response', 'Value'}:
                raise HTTPException(status_code=400, detail="CSV must contain only 'Response' and 'Value' columns")
            
            # Validate that there are no empty strings in the "Response" column
            response = row['Response'].strip()
            if not response:
                raise HTTPException(status_code=400, detail="Empty string found in 'Response' column")
            
            # Validate that each value in the "Value" column is an integer 
            try:
                int(row['Value'])
            except ValueError:
                raise HTTPException(status_code=400, detail="VValue column must contain only integers")
            
            # Validate that each value in the response column is a string
            try:
                str(row['Response'])
            except ValueError:
                raise HTTPException(status_code=400, detail="Response column must contain only string")

            # Validate Value column
            value = int(row['Value'])

            # Strip trailing and leading whitespace from all values in the "Response" column and appending ito list
            rows.append({'Response': response.strip(), 'Value': value})

        if equals is not None:
            rows = [row for row in rows if row['Value'] == int(equals)]
        return rows
    
    except ValueError:
        raise HTTPException(status_code=400, detail="Values in 'Value' column must be integers")