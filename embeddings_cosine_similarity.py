# -*- coding: utf-8 -*-
"""2023-07-02_embeddings_cosine-similarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gUMpTUo0Z-0wTud2ntWQAUdk4DZNaVk1
"""

pip install openai

import torch
import openai

from google.colab import drive
drive.mount('/content/drive')

with open('/content/drive/MyDrive/Colab Notebooks/2023-07-02_embeddings_api_key/api_key.txt', 'r') as f:
    api_key = f.read().strip()
openai.api_key = api_key
# your own api is save in the api_key.text on your google drive. Chage the path accordingly.

def sentence_to_vector(sentence):
  res = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=sentence
    )

  return torch.tensor(res['data'][0]["embedding"])
  # model is selected according to the one available on the GPT API

sentence = "私たちが開発したファンデーションはあなたの自然な美しさを引き立てます。シームレスに肌に溶け込み、まるで素肌そのもののような仕上がりを提供します。"
TARGET_VECTOR = sentence_to_vector(sentence)
# type your source text

import pandas as pd
article_df = pd.DataFrame({"title": ["Our newly developed foundation enhances your natural beauty. It blends seamlessly into your skin, providing a finish that's just like your own bare skin.",
                                     "Experience the natural beauty enhancement with our specially designed foundation. Its unique formulation blends effortlessly into your skin, giving the impression of flawless, bare skin.",
                                     "The foundation we've created serves to amplify your inherent beauty. Seamlessly melting into your skin, it leaves you with a finish indistinguishable from your natural skin."
                                     ]})
# type your target text

def calc_similarity(sentence):
  sentence_vector = sentence_to_vector(sentence)

  score = torch.nn.functional.cosine_similarity(TARGET_VECTOR, sentence_vector, dim=0).detach().numpy().copy()
  return score

article_df["similarity"] = article_df["title"].apply(lambda title: calc_similarity(title))

print(article_df)

article_df.sort_values('similarity', ascending=False)
# This lists the results in ascending order.