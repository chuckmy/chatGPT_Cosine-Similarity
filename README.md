# README

## Cosine Similarity Calculation for Text Embeddings using OpenAI and PyTorch

This script demonstrates the use of OpenAI's GPT-4 API to generate embeddings for text data and calculates cosine similarity between them. 

The main purpose of this script is to check the similarity between a source sentence and a set of target sentences, which can be extremely useful for tasks like document similarity, text retrieval, and other NLP tasks. 

### Dependencies

- Python 3.7+
- PyTorch
- OpenAI
- Pandas
- Google Colab

The script was created in a Google Colab environment, but it can be executed in any Python environment with the necessary dependencies installed.

### Getting Started

1. Install the required Python libraries if you haven't already:

```bash
pip install torch openai pandas
```

2. Save your OpenAI API key as a `.txt` file on your Google Drive. The script expects the file to be located at `/content/drive/MyDrive/Colab Notebooks/2023-07-02_embeddings_api_key/api_key.txt`. If you save it elsewhere, remember to update the file path in the script.

3. If you are using Google Colab, make sure to mount your Google Drive so that the script can access your API key file:

```python
from google.colab import drive
drive.mount('/content/drive')
```

### Usage

To use this script, provide your source text and a set of target texts:

1. Set your source text:

```python
sentence = "This is your source text"
TARGET_VECTOR = sentence_to_vector(sentence)
```

2. Set your target texts in a pandas DataFrame:

```python
article_df = pd.DataFrame({"title": ["This is your first target text",
                                     "This is your second target text",
                                     "This is your third target text"
                                     ]})
```

3. Run the script. The result will be a DataFrame with each target text and its similarity score to the source text, sorted in ascending order of similarity.

### Important Information

- The script uses the 'text-embedding-ada-002' model for embedding generation. If this model is not available or if you want to use a different model, remember to update the model name in the `sentence_to_vector` function.

- The script uses cosine similarity as the similarity measure. If you want to use a different measure, you will need to modify the `calc_similarity` function.

### Troubleshooting

If you encounter any issues while using this script, check if your OpenAI API key is correctly set and make sure you have the necessary permissions to read the key file from your Google Drive.

If you encounter issues related to the OpenAI GPT-4 model, check if the model name is correct and if the model is available for use.

For any other issues, please refer to the error messages for more information about the problem and potential solutions. If you can't resolve the problem, consider asking for help on relevant forums or issue trackers.

