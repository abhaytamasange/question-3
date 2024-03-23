import os
from PyPDF2 import PdfReader
from collections import defaultdict


def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
    return text


total_files = 0
total_directories = 0
word_counts = defaultdict(lambda: [0, set()])

directory = "./files"

for root, dirs, files in os.walk(directory):
    total_directories += len(dirs)
    for file in files:
        if file.endswith(".pdf"):
            total_files += 1
            file_path = os.path.join(root, file)
            text = extract_text_from_pdf(file_path)
            words = text.split()
            unique_words = set(words)
            for word in unique_words:
                word_counts[word][0] += 1
                word_counts[word][1].add(file)


sorted_words = sorted(word_counts.items(), key=lambda x: (x[1][0], x[0].lower(), x[0].islower()))

print(f"Total files: {total_files}")
print(f"Total directories: {total_directories}")
print("\nList of words\n")
print("{:<20} {:<10} {:<15}".format("Word", "Count", "Number_Files"))
for word, (count, files) in sorted_words:
    print("{:<20} {:<10} {:<15}".format(word, count, len(files)))


print("\nOrdering sequence\n")
for word, (count, files) in sorted_words:
    print("{:<20} {:<10} {:<15}".format(word, count, len(files)))