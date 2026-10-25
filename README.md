# Simple Tokenizer

A simple word-level tokenizer built from scratch in Python. It converts text into integer token IDs and back, which is the first step in preparing text for a language model.

## Features

- Splits text into words and punctuation using a regular expression
- Builds a vocabulary (token to integer ID) from a text file
- Encodes text into a list of token IDs
- Decodes token IDs back into readable text
- Handles unknown words with the `<|unk|>` special token
- Supports `<|endoftext|>` to separate documents

## How it works

1. **Load** the story from `little_library_story.txt`.
2. **Tokenize** the text by splitting on whitespace and punctuation:
   ```python
   re.split(r'([,.:;?_!"()\']|--|\s)', text)
   ```
3. **Build the vocabulary** from the sorted set of unique tokens, then add two special tokens:
   ```python
   all_words = sorted(set(preprocessed))
   all_words.extend(["<|endoftext|>", "<|unk|>"])
   vocab = {token: integer for integer, token in enumerate(all_words)}
   ```
4. **Encode** replaces any word not in the vocabulary with `<|unk|>`, then maps each token to its ID.
5. **Decode** maps IDs back to tokens, joins them with spaces, and removes the extra space before punctuation.

## Project structure

```
Simple_tokenizer/
├── tokenizer.py              # Tokenizer code
├── little_library_story.txt  # Text used to build the vocabulary
└── README.md
```

## Requirements

- Python 3.8 or newer
- No external libraries (uses only the built-in `re` module)

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/ankitrajofficial2005/simple-tokenizer.git
cd simple-tokenizer
python3 tokenizer.py
```

Or use the tokenizer in your own code:

```python
tokenizer = SimpleTokenizerV2(vocab)

text = "Mira pushed the door open."
ids = tokenizer.encode(text)
print(ids)                      # list of token IDs
print(tokenizer.decode(ids))    # Mira pushed the door open.
```

## Example with unknown words

Words that are not in the story are mapped to `<|unk|>`:

```python
text = "Hello , do you like coffe? <|endoftext|> It described a lighthouse."
ids = tokenizer.encode(text)
print(tokenizer.decode(ids))
# <|unk|>, do you like <|unk|>? <|endoftext|> It <|unk|> a <|unk|>.
```

## Limitations

- The vocabulary is built from one small story, so many common words are unknown.
- Whitespace and line breaks are not preserved when decoding.
- Word-level tokenization cannot handle new words. Modern models use subword methods such as Byte Pair Encoding (BPE) to solve this.

## Next steps

- Add Byte Pair Encoding (BPE)
which i can upload in up coming days


## Author

Ankit Raj ([@ankitrajofficial2005](https://github.com/ankitrajofficial2005))
