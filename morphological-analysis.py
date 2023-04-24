# Install required packages
pip install morfessor pycld2 pyicu polyglot

# Download language models
from polyglot.downloader import downloader

if not downloader.is_installed("morph2.en"):
    downloader.download("morph2.en")
if not downloader.is_installed("morph2.ar"):
    downloader.download("morph2.ar")
if not downloader.is_installed("embeddings2.en"):
    downloader.download("embeddings2.en")
if not downloader.is_installed("pos2.en"):
    downloader.download("pos2.en")

# Example 1: Splitting words into morphemes
from polyglot.text import Text, Word

words = ["preprocessing", "processor", "invaluable", "thankful", "crossed"]
word_morphemes = [(Word(w, language="en"), Word(w, language="en").morphemes) for w in words]
for w, m in word_morphemes:
    print("{:<20}{}".format(w, m))

# Example 2: Splitting string by morphemes
blob = "Wewillmeettoday."
text = Text(blob, language="en")
morphemes = [word.morphemes for word in text.words]
print(morphemes)

# Example 3: Part-of-speech tagging
blob = """We will meet at eight o'clock on Thursday morning."""
text = Text(blob, language="en")
pos_tags = [(word.string, word.pos) for word in text.words]
print(pos_tags)
