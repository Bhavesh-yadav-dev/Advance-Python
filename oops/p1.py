# from transformers import AutoTokenizer

# model_name = "sentence-transformers/all-MiniLM-L6-v2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# text = "My grandma was one of six children. Her mom was a homemaker, and her dad worked in construction. The boys were raised to go into construction as well, and the girls were raised to get married and have children. But my grandma wanted to go to college and choose her own path in life. She didn’t have money to go, and she had pressure from her parents to get married instead. But she got good grades in school and was able to win a full scholarship to the local state college. To earn money while she went to college, she cleaned people’s homes, tutored kids in English and math, and worked in the college library. She graduated with a degree in accounting and got a good job at a bank. She met my grandpa at work, and they got married. They had three children, and my grandma continued to work at the bank while raising her family. She was a strong and independent woman who always encouraged her children to pursue their dreams and never settle for less. Her determination and hard work paid off, and she became a role model for her family and community." # (your text here)

# def text_chunker(text, chunk_size, overlap):
#     # Tokenize and get input IDs without special tokens ([CLS], [SEP]) if desired
#     encoding = tokenizer(text, add_special_tokens=False)
#     input_ids = encoding["input_ids"]

#     # chunk_text = tokenizer.decode(input_ids)
#     chunks = []
#     step = chunk_size - overlap

#     for i in range(0, len(input_ids), step):
#         chunk_ids = input_ids[i:i + chunk_size]
#         # Decode token IDs back into readable text, properly handling subwords
#         chunk_text = tokenizer.decode(chunk_ids)
#         chunks.append(chunk_text)

#     return chunks

# # Example with a larger chunk size (e.g., 64 tokens, 16 overlap)
# result = text_chunker(text, chunk_size=64, overlap=16)
# for i, chunk in enumerate(result):
#     print(f"Chunk {i + 1}: {chunk}\n")









from transformers import AutoTokenizer
from sentence_transformers import SentenceTransformer

model_name1 = "sentence-transformers/all-MiniLM-L6-v2"

model1 = SentenceTransformer(model_name1)

model_name = "sentence-transformers/all-MiniLM-L6-v2"

tokenizer = AutoTokenizer.from_pretrained(model_name)



text = "My grandma was one of six children. Her mom was a homemaker, and her dad worked in construction. The boys were raised to go into construction as well, and the girls were raised to get married and have children. But my grandma wanted to go to college and choose her own path in life. She didn’t have money to go, and she had pressure from her parents to get married instead. But she got good grades in school and was able to win a full scholarship to the local state college. To earn money while she went to college, she cleaned people’s homes, tutored kids in English and math, and worked in the college library. She graduated with a degree in accounting and got a good job at a bank. She met my grandpa at work, and they got married. They had three children, and my grandma continued to work at the bank while raising her family. She was a strong and independent woman who always encouraged her children to pursue their dreams and never settle for less. Her determination and hard work paid off, and she became a role model for her family and community."

model_name = "sentence-transformers/all-MiniLM-L6-v2"

tokenizer = AutoTokenizer.from_pretrained(model_name)

def text_Chunker(text,Chuck_Size,overlap):

    tokens = tokenizer.tokenize(text)
    chunks = []
    step = Chuck_Size - overlap

    for i in range(0,len(tokens),step):
        chunk = tokens[i:i + Chuck_Size]
        chunks.append(". ".join(chunk).strip() + ". ")

    return chunks

result = text_Chunker(text, 2,1)
embeddings = model1.encode(result)

print(embeddings)
print("Shape:", embeddings.shape)




# def text_chunker(text,chunk_size):
#     chunks = [] #store the chunks of text
#     sentences = text.split(".") # Split the text into sentences

#     for i in range(0,len(sentences),chunk_size):
#         chunk = sentences[i:i+1 + chunk_size] # Get a chunk of sentences
#         chunks.append(". ".join(chunk).strip() + ". ") # Join the sentences back
#     return chunks



# result = text_chunker(text, 2)

# for i,chunk in enumerate(result):
#     print(f"Chunk {i + 1}: {chunk}\n")
