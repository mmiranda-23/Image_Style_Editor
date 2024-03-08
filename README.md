# Image Style Editor

## Description

Welcome to the Image Style Editor! this is a basic image generation program that given a provided image and a desired filter style regenerates the image with the selected filter.
It consists of two models: the first model takes the input image and generates a detailed description of it. The second model generates an image given the description from the first model and the filter style chosen.

## Installation

1. Clone the repository: `git clone https://github.com/mmiranda-23/Image_Style_Editor.git`
2. Navigate to the project directory: `cd Image_Style_Editor`
3. Install the dependencies: `pip install -r requirements.txt`
4. Create a .env file and add an OPENAI_API_KEY variable with your API key or add it in the system environment variables

## Usage

1. Run the application: `streamlit run app.py`
2. Your browser will open with the Image Style Editor.
3. Drag and drop or browse the image you want to edit.


Note: For better performance use dall-e-3 instead of dall-e-2.
