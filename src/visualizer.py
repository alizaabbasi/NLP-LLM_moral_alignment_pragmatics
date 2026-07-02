import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    @staticmethod
    def plot_compliance(metrics):
        """Creates a pie chart of refusal vs. compliance."""
        labels = ['Refusals', 'Answered']
        sizes = [metrics['refusal_rate'], 100 - metrics['refusal_rate']]
        
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
        plt.title("Model Compliance in Moral Dilemmas")
        plt.show()

    @staticmethod
    def plot_response_lengths(results):
        """Plots a distribution of how long the model's responses were."""
        # A great alternative metric for university projects!
        lengths = [len(str(r.get('response', ''))) for r in results]
        
        plt.figure(figsize=(8, 4))
        sns.histplot(lengths, kde=True, color='purple')
        plt.title("Distribution of Response Lengths")
        plt.xlabel("Character Count")
        plt.ylabel("Frequency")
        plt.show()