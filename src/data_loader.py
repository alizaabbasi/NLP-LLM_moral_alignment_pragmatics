import os
import csv
import json
from datasets import load_dataset

class DataLoader:
    def __init__(self, data_path=None):
        self.data_path = data_path

    def load_custom_prompts(self):
        """Reads local JSON file."""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Could not find file at {self.data_path}")
        with open(self.data_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def load_ethics_dataset(self, category="commonsense"):
        """Loads data from a local CSV file to bypass library errors."""
        path = f"data/{category}.csv"
        prompts = []
        
        if not os.path.exists(path):
            raise FileNotFoundError(f"Could not find local dataset file at {path}. Please check your data folder.")
            
        with open(path, mode='r', encoding='utf-8') as f:
            # csv.DictReader automatically uses the first row (headers) as keys
            reader = csv.DictReader(f)
            for row in reader:
                # The ETHICS dataset CSV uses 'input' as the column header for scenarios
                prompts.append({"prompt": row["input"]})
                
        return prompts[:50]
    