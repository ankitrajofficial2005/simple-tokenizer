import re

with open("little_library_story.txt", "r", encoding= "utf-8")as f:
    raw_text = f.read()
    print("Total number of character: ", len(raw_text))
    print(raw_text[:99])


# text = "Hello, world this , is a example"
# result = re.split(r'(\s)',text)
# print(result)


#now we split first 100 words in the story and special charcter

preprocessed = re.split(r'([,.;:?_!"()\']|--|\s)',raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed[:100])


#create a list all unique token and sort them alphabetically to determine
#the voacbulary size
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

# first line build a dictorny that give a every unique id and loop 
# loop just print the first 51 wordss

vocab = {token: integer for integer,token in enumerate(all_words)}
for i , item in enumerate(vocab.items()):
  print(item)
  if i>=50:
    break




# implement a complete simple tokenizzer in python


class SimpleTokenizerV1:
  def __init__(self, text):
    self.str__to__int = vocab
    self.int__to__str = {i:s for s, i in vocab.items()}

  def encode(self,text):
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)',text)
    preprocessed = [
        item.strip() for item in preprocessed if item.strip()
    ]
    ids = [self.str__to__int[s] for s in preprocessed]
    return ids


  def decode(self, ids):
    text = " ".join([self.int__to__str[i] for i in ids])
    text = re.sub(r'\s+([,.?!"()\'])',r'\1',text)
    return text




tokenizer = SimpleTokenizerV1(vocab)
text = """Mira pushed the door open.
 The bell rang, and the smell of paper, cedar, and cinnamon 
 drifted into the room. Shelves covered the 
 walls from floor to ceiling."""


ids = tokenizer.encode(text)
print(ids)


print(tokenizer.decode(ids))



#addding a special context tokens


all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|" , "<|unk|"])
vocab = {token:integer for integer, token in enumerate(all_tokens)}

len(vocab.items())


for i , item in enumerate(list(vocab.items())[-5:]):
  print(item)


class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str__to__int = vocab
        self.int__to__str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,. :;?_!()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        preprocessed = [
            item if item in self.str__to__int else "<|unk|>"
            for item in preprocessed
        ]

        ids = [self.str__to__int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int__to__str[i] for i in ids])
        text = re.sub(r'\s+([,.:;?!_"()\'])', r'\1', text)
        return text



tokenizer = SimpleTokenizerV2(vocab)
text1 = "Hello , do you like coffe?"
text2 = "It described a lighthouse on a rocky island." \
" Every evening, its keeper lit a lamp to guide ships through" \
" dangerous waters. One winter night, the lamp went dark," \
" and a young sailor had to decide whether to turn back or " \
"continue through the storm." \
" The page ended there."
text = "<|endoftext|>".join((text1,text2))
print(text)



ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))