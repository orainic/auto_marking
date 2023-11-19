# Auto Marking Streamlit

This repo serves as a simple app for marking uploaded exam papers.

## Development and Deployment

### 1. Install the development tools and software

| Tools/Software | Description and Application                                                                                                                                                       | Links                                                                      |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Anaconda       | Anaconda is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment.                           | [Installation](https://docs.anaconda.com/free/anaconda/install/index.html) |
| Python 3.11    | Python is a high-level, general-purpose programming language.                                                                                                                     | [Download](https://www.python.org/downloads/)                              |
| Tesseract OCR  | Tesseract 4 adds a new neural net (LSTM) based OCR engine which is focused on line recognition. Installers for Windows for Tesseract are available from Tesseract at UB Mannheim. | [Installation](https://github.com/UB-Mannheim/tesseract/wiki)              |

### 2. Install the Development Libraies

| Library       | Description and Application                                                                                                  | Links                                                                                                               |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Streamlit     | Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes. | [Installation](https://docs.streamlit.io/library/get-started/installation) or via pip with `pip install streamlit`. |
| Tesseract OCR | Tesseract 4 adds a new neural net (LSTM) based OCR engine which is focused on line recognition.                              | [Installation](https://github.com/tesseract-ocr/tesseract) or via pip with `pip install pytesseract`.               |
| Pillow        | Pillow package for handling images in Python. recognition.                                                                   | install via pip with `pip install Pillow`                                                                           |

_Note that when setting up the StreamLit app, you should make sure to add `OPENAI_API_KEY` as a secret environment variable._

Read [StreamLit secrets management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management) section "Develop locally with secrets" to setup the file strucre on your local driver during the development, and follow [Best Practices for API Key Safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety) to manage the API key.
