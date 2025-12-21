sentence = input("Enter a sentence: ").strip()

print(f"sentence in uppercase: {sentence.upper()}")
print(f"sentence has {len(sentence)} characters")
print(f"sentence word count: {len(sentence.split())}")