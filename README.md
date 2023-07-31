# KEYzer
The KEYzer or Keyword Analyzer is a Python application that allows you to extract the most common keywords from various sources, such as websites, text files, PDFs, and Word documents. The application uses the Natural Language Toolkit (nltk) and spaCy libraries to preprocess the text and identify the top keywords.

## Installation and Setup:

1. Clone the repository or download the project files.

2. Create a virtual environment (optional but recommended) to ensure a clean and isolated environment for running the application:

python -m venv myenv   # Create a virtual environment named 'myenv'

source myenv/bin/activate   # On Windows: myenv\Scripts\activate


3. Install the required dependencies from the requirements.txt file:

pip install -r requirements.txt


4. Download the spaCy model 'en_core_web_sm' using the following command:

python -m spacy download en_core_web_sm


## Usage

To run the Keyword Analyzer application, 
1. Click on the KEYzer.exe file.
2. Or, execute the kwgen_gui.py script:

python kwgen_gui.py

### The application will open a graphical user interface (GUI) with the following features:

#### Analyze Website: 
Enter the URL of a website and click the "Analyze Website" button to extract the top 50 keywords from the website's content.

#### Analyze Text from File: 
Click the "Analyze Text from File" button to browse and select a text, PDF, DOC, or DOCX file. The application will preprocess the text and display the top 50 keywords.

## Important Note
The Keyword Analyzer application requires the 'en_core_web_sm' spaCy language model. Ensure that you have downloaded the model as mentioned in the Installation and Setup section.

## Troubleshooting
If you encounter any issues while running the application, make sure you have followed the installation steps correctly and that all required dependencies are installed in the virtual environment.

In case of any errors related to the spaCy model, please check the model path defined in loader.py. The model path should point to the location where the 'en_core_web_sm' model is installed.

If you encounter any other problems or need assistance, feel free to open an issue in the project's repository.

## Credits
The Keyword Analyzer application was created by Vineetha Padimiti and is distributed under the Apache 2.0 license. For more information, please refer to the [LICENSE] file.

## Contributions
Contributions to the project are welcome! If you would like to improve the application or add new features, please submit a pull request.

## License
This project is licensed under the [Apache 2.0]. For more details, see the [LICENSE] file.

Happy keyword analysis!
