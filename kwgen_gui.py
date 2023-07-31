import requests
from bs4 import BeautifulSoup
import os
import spacy
import nltk
from PyPDF2 import PdfReader
import docx as docx_module
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from loader import load_spacy_model

# Append the nltk_data directory to the nltk data path
nltk.data.path.append('nltk_data')

# Load the English language model in Spacy
nlp = load_spacy_model()

# Function to preprocess the text and extract top keywords
def preprocessing(text):
    text = text.lower()
    text = text.replace('.', '')
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if
              not (token.is_stop or token.like_num or token.is_punct or token.is_space or len(token) <= 2)]
    preprocessed_text = ' '.join(tokens)
    frequency = nltk.FreqDist(tokens)
    most_common_keywords = frequency.most_common(50)
    return most_common_keywords

# Function to get website content and analyze keywords
def analyze_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content of the website using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from the website
        paragraphs = soup.find_all('p')
        website_text = ' '.join([p.get_text() for p in paragraphs])

        # Preprocess the text and get the most common words
        most_common_keywords = preprocessing(website_text)

        return most_common_keywords

    except requests.exceptions.RequestException as e:
        print("Error fetching website content:", e)
        return None

# Read text from text file
def read_text_from_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Read text from PDF file
def read_text_from_pdf(file_path):
    text = ""
    pdf_reader = PdfReader(file_path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Read text from DOC or DOCX file
def read_text_from_docx(file_path):
    doc = docx_module.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + " "
    return text

def analyze_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"),
                                                      ("PDF Files", "*.pdf"),
                                                      ("Word Documents", "*.doc;*.docx")])
    if file_path:
        _, extension = os.path.splitext(file_path)

        if extension.lower() in ['.txt', '.pdf', '.doc', '.docx']:
            text = ""
            if extension.lower() == '.txt':
                text = read_text_from_text_file(file_path)
            elif extension.lower() == '.pdf':
                text = read_text_from_pdf(file_path)
            elif extension.lower() in ['.doc', '.docx']:
                text = read_text_from_docx(file_path)

            # Preprocess the text and get the most common words
            most_common_keywords = preprocessing(text)

            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Top 50 Keywords:\n")
            for keyword, count in most_common_keywords:
                result_text.insert(tk.END, f"{keyword}: {count}\n")

        else:
            messagebox.showerror("Invalid File", "Please select a valid text, PDF, DOC, or DOCX file.")

def analyze_website_from_entry():
    website_url = website_entry.get()
    if website_url:
        top_keywords = analyze_website(website_url)
        result_text.delete(1.0, tk.END)

        if top_keywords:
            result_text.insert(tk.END, "Top 50 Keywords:\n")
            for keyword, count in top_keywords:
                result_text.insert(tk.END, f"{keyword}: {count}\n")
        else:
            result_text.insert(tk.END, "Failed to analyze the website. Please check the URL and try again.")

# GUI Setup
root = tk.Tk()
root.title("Keyword Analyzer")
root.geometry("800x600")

# Website URL input
website_label = tk.Label(root, text="Enter the website URL:")
website_label.pack(pady=10)

website_entry = tk.Entry(root, width=50)
website_entry.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze Website", command=analyze_website_from_entry)
analyze_button.pack(pady=10)

# Text Result display
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
result_text.pack(padx=10, pady=10)

# Analyze Text from File button
file_button = tk.Button(root, text="Analyze Text from File", command=analyze_text)
file_button.pack(pady=10)

root.mainloop()
