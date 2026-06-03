# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice working with strings, file input/output, and basic text manipulation by building utilities that analyze and transform plain text files.

## 📝 Tasks

### 🛠️ Text Analysis

#### Description
Write functions that read a text file and compute summary statistics and simple insights.

#### Requirements

Completed program should:

- Read a UTF-8 encoded text file passed by path
- Return the number of lines, words, and characters in the file
- Identify the top 5 most common words (case-insensitive, stripped of punctuation)
- Provide an example usage and sample output in the README

### 🛠️ Text Transformation

#### Description
Implement utilities to clean and transform text and to save results to a new file.

#### Requirements

Completed program should:

- Provide a function to remove punctuation and normalize whitespace
- Save the cleaned text to a new file when requested
- Support a simple search-and-replace operation over the file contents

## How to run

1. Create a virtual environment and install dependencies (if any):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the starter script to see usage instructions:

```bash
python assignments/python-text-processing/starter_code.py --help
```

3. Example: compute statistics for the provided sample text:

```bash
python assignments/python-text-processing/starter_code.py stats sample_text.txt
```

## Starter code

See `starter_code.py` for a small CLI that implements file reading, basic stats, and a cleaning function.
