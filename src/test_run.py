import pandas as pd
from data_loader import DataLoader
from model_interface import ModelInterface
from analyzer import Analyzer
from visualizer import Visualizer

# # 1. Initialize all modules
loader = DataLoader()
llm = ModelInterface()
analyzer = Analyzer()

# # 2. Loading prompts (already limited to 50 inside data_loader.py)
prompts = loader.load_ethics_dataset(category="commonsense")
results = []

# # 3. Looping through prompts and get real AI responses
for item in prompts:
    print(f"Asking model: {item['prompt']}")
    response = llm.query(item['prompt'])
    
    # Store both the prompt and the response together as a dictionary
    results.append({
        'prompt': item['prompt'],
        'response': response
    })

# # 4. Saving results to a CSV file for report
df = pd.DataFrame(results)
df.to_csv('results/experiment_results.csv', index=False)
print("\nExperiment complete! Results saved to results/experiment_results.csv")

# # 5. Analyze and Visualize
print("Running Post-Experiment Analysis...")
metrics = analyzer.analyze_batch(results)

print(f"Total Evaluated: {metrics['total_prompts']}")
print(f"Model Refusal Rate: {metrics['refusal_rate']:.1f}%")

print("Generating evaluation plots...")
Visualizer.plot_compliance(metrics)
Visualizer.plot_response_lengths(results)