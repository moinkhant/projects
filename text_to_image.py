# api key= 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
import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
st.title("AI Image Generator app")
st.write("Enter a prompt")
prompt=st.text_input("Enter your image prompt")
if st.button("Generate"):
    if prompt:
        try:
            response=openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            image_url=response["data"][0]["url"]
            image_response=requests.get(image_url)
            img=Image.open(BytesIO(image_response.content))
            st.image(img,caption="Your Image",use_colum_width=True)
        except Exception as e:
            st.error(f"An error occured: {e}")

    else:
        st.error("Please enter a prompt to generate an image")