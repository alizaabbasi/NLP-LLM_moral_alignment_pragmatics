# P10: Right, Wrong, and Everything in Between: An Empirical Study of LLM Pragmatics and Moral Alignment

**Course:** Text Mining & Sentiment Analysis  

---

## Overview
This repository contains the software pipeline and analytical framework for an empirical study examining how Large Language Models (LLMs) navigate morally ambiguous, unethical, or harmful prompts. By testing paired behavioral scenarios—contrasting socially acceptable actions with harmful deviations—this project measures the tension between an LLM's safety guardrails and its linguistic pragmatics. 

The study reveals that while models maintain an 88.0% compliance rate for non-explicit ethical deviations, their linguistic coherence degrades significantly, forcing them to resort to unnatural pragmatic shifts rather than coherent contextual reasoning. 

---

## Key Findings
* **Compliance vs. Refusal:** The model exhibited an 88.0% compliance rate (answered prompts) and a 12.0% hard refusal rate. Hard refusals were strictly triggered by explicit abuse guardrails.
* **Linguistic Degradation Paradigms:** Instead of graceful handling of moral grey areas, the model deployed four distinct pragmatic deflection strategies:
  1. **Grammatical Deflection:** Treating benign inputs as syntax exercises.
  2. **Moralizing & Preachy Warnings:** Lecturing users on safety when presented with non-violating but dangerous inputs.
  3. **Repetition Loops:** Generating the exact same sentence consecutively when alignment parameters are confused.
  4. **Hallucinated Logic Puzzles:** Outputting multiple-choice reading comprehension tests when faced with violent absurdity.

---

## Core Architecture & Directory Layout
The codebase complies with rigorous software engineering standards using clean object-oriented design patterns separated across dedicated modules:

```text
P10_MORAL_ALIGNMENT_PROJECT/
├── data/
│   ├── commonsense.csv        # Stores paired, ethically sensitive inputs
│   └── custom_prompts.json    # Supplementary prompt configurations
├── src/
│   ├── __init__.py            
│   ├── model_interface.py     # Controls API execution and session handling
│   ├── analyzer.py            # Classifies text profiles and computes benchmarks
│   ├── visualizer.py          # Structural plotting methods for reproducibility
│   ├── data_loader.py         # Utility for ingesting scenario structures
│   └── test_run.py            # Main execution script triggering the evaluation
├── results/
│   ├── experiment_results.csv # Empirical telemetry dataset
│   └── Figure_1.png           # Visual analytics of pragmatic signatures
├── notebooks/
│   └── demo_evaluation.ipynb  # Interactive workspace for quick validation
├── requirements.txt           # Python environment dependencies
└── README.md                  # Project documentation handbook