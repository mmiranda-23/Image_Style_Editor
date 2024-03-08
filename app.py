import base64
import os
import tempfile

from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, AIMessage
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# API configuration
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
llm1 = ChatOpenAI(model="gpt-4-vision-preview", openai_api_key=os.getenv("OPENAI_API_KEY"))
# Function definitions

def encode_image(image_path):
    """Encode an image file to a base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def main():
    """Main function for the Streamlit app."""
    st.title("👩🏼‍🎨 Image Style Editor 👩🏼‍🎨")

    # File uploader
    image = st.file_uploader("Upload your image", type=["jpg","png"])
    
  
    if image is not None:
        tmpdir = tempfile.mkdtemp()
        img_path = os.path.join(tmpdir, image.name)

        # Save uploaded image to temporary directory
        with open(img_path, "wb") as f:
            f.write(image.getvalue())
        
        # Encode the image for processing
        image = encode_image(img_path)

        style = st.text_input("Set the style for the image (e.g. 'monet painting', 'disney pixar animation'):")
        if style:
            # Invoke language model for image description
            msg = llm1.invoke(
                [   AIMessage(content="You are a useful bot that is especially good at describing images in detail in an objective way"),
                    HumanMessage(
                        content=[
                            {"type": "text", "text": """
                             Describe what is in the image. Start with a short description of the whole image and then go deeper with every aspect, 
                             starting with people, animals, objects and background. Take your time and be as descriptive and concise as possible. Pay attention to the colors and shapes. """},
                            {"type": "image_url","image_url": {"url": f"data:image/jpeg;base64,{image}"}}
                        ]
                    )
                ],
                max_tokens=150,
            )
            client = OpenAI()
            # Generate image with DALL-E based on description and style
            response = client.images.generate(
            model="dall-e-2",
            prompt=f"Create an image with the following filter style: * {style} * and with the following characteristics: * {msg.content} *.",
            size="1024x1024",
            quality="standard",
            n=1,
            )

            if response:
                generated_image_url = response.data[0].url
                st.image(generated_image_url, caption="Generated Image", use_column_width=True)

# Entry point
if __name__ == "__main__":
    main()

