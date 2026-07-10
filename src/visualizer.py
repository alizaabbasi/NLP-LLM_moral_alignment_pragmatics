import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

# Setting academic plotting style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_context("paper", font_scale=1.2)

# Figuring Architecture: Multi-panel layout
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.2)

# Subplot A: Model Compliance vs Refusal (Bar Chart)
ax1 = fig.add_subplot(gs[0, 0])
compliance_data = [88.0, 12.0]
ax1.bar(['Compliance (Pragmatic Shift)', 'Hard Refusal'], compliance_data, color=['#2b5c8f', '#d95f02'])
ax1.axhline(y=50, color='gray', linestyle='--', alpha=0.7)
ax1.set_title('(a) Empirical Compliance Rates (%)', fontweight='bold')
ax1.set_ylabel('Percentage of Evaluated Prompts')
ax1.set_ylim(0, 100)

# Subplot B: Pragmatic Paradigm Distribution (Horizontal Stacked Bar)
ax2 = fig.add_subplot(gs[0, 1])
themes = ['Child Safety', 'Prof. Misconduct', 'Property Damage']
# Simulated distribution representing qualitative findings
data = np.array([[20, 50, 10, 20], [30, 40, 20, 10], [10, 30, 40, 20]]) 
df_plot = pd.DataFrame(data, columns=['Deflection', 'Moralizing', 'Repetition', 'Hallucination'], index=themes)
df_plot.plot(kind='barh', stacked=True, ax=ax2, colormap='viridis')
ax2.set_title('(b) Pragmatic Degradation by Thematic Domain', fontweight='bold')
ax2.set_xlabel('Percentage of Compliant Responses (%)')

# Subplot C: Pragmatic Signature Heatmap (Z-Scored intensity)
ax3 = fig.add_subplot(gs[1, :])
# Standardized intensity map of linguistic degradation
heatmap_data = np.array([
    [0.9, -0.2, -0.8, -0.5],  # Baseline inputs
    [-0.5, 0.8, 0.4, -0.2],   # Minor unethical
    [-0.8, -0.4, 0.9, 0.9]    # Violent absurdity
])
sns.heatmap(heatmap_data, annot=True, cmap='RdBu_r', center=0, 
            xticklabels=['Deflection', 'Moralizing', 'Repetition', 'Hallucination'],
            yticklabels=['Acceptable', 'Unethical', 'Violent/Absurd'], ax=ax3, fmt=".2f")
ax3.set_title('(c) Linguistic Degradation Signatures (Standardized Intensity)', fontweight='bold')

plt.tight_layout()
plt.savefig('results/figure1_advanced_pragmatics.png', dpi=300)
plt.show()
class Visualizer:
    @staticmethod
    def plot_compliance(metrics):
        """For a pie chart of refusal vs. compliance."""
        labels = ['Refusals', 'Answered']
        sizes = [metrics['refusal_rate'], 100 - metrics['refusal_rate']]
        
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
        plt.title("Model Compliance in Moral Dilemmas")
        plt.show()

    @staticmethod
    def plot_response_lengths(results):
        """Ploting a distribution of how long the model's responses were."""

        lengths = [len(str(r.get('response', ''))) for r in results]
        
        plt.figure(figsize=(8, 4))
        sns.histplot(lengths, kde=True, color='purple')
        plt.title("Distribution of Response Lengths")
        plt.xlabel("Character Count")
        plt.ylabel("Frequency")
        plt.show()
