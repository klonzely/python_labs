#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from lib.text import normalize, tokenize, count_freq, top_n

text = sys.stdin.read().strip()
if not text: 
    print("No input")
    sys.exit()

normalized = normalize(text)
tokens = tokenize(normalized)
freq = count_freq(tokens)
top_words = top_n(freq, 5)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for word, count in top_words:
    print(f"{word}:{count}")