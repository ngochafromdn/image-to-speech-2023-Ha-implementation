

'''
The code is a Streamlit application that uses the easyocr library to perform OCR on an uploaded image.
It extracts text from the image and then speaks the extracted words.
'''
import cv2
import numpy as np
import streamlit as st
from PIL import Image
import time
from OCR.perform_ocr import OCR
from voice.read_aloud import ReadingWord
import os




def main():
    # Add CSS style
    css = """
    <style>
    body {
        background-color: #f2f2f2; /* background color */
    }
    .title {
        color: #3366ff; /* title*/
        font-size: 24px; /* font size */
        font-weight: bold; /* title font weight */
    }
    .loader {
        border: 16px solid #f3f3f3;
        border-top: 16px solid #3498db;
        border-radius: 50%;
        width: 80px;
        height: 80px;
        animation: spin 2s linear infinite;
        margin: 0 auto;
        margin-top: 20px;
    }
    </style>
    """

    # Initialize OCR and ReadingWord classes
    ocr_processor = OCR()
    reader = ReadingWord()

    # Add description
    st.markdown("# OCR with OpenCV and Speech for Vietnamese")
    st.markdown(
        "This web application allows you to perform OCR on an uploaded image and extract text from it. The extracted text can then be read aloud using text-to-speech functionality."
    )
    st.title("Text extraction")

    # Image selection
    option = st.radio(
        "Select an image or upload your own", ("Example 1", "Example 2", "Example 3", "Upload Image")
    )

    # Example images
    example_images = {
        "Example 1": "Example/image1.jpeg",
        "Example 2": "Example/image2.jpeg",
        "Example 3": "Example/image3.jpeg",
    }

    # Uploaded image
    uploaded_image = None

    if option != "Upload Image":
        # Read the example image
        image_path = example_images[option]
        image = Image.open(image_path)
        st.image(image, caption="Selected Image", width=400)
    else:
        # Upload image
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            uploaded_image = np.array(Image.open(uploaded_file))
            st.image(uploaded_image, channels="RGB", caption="Uploaded Image", width=400)

    # Speech speed input
    speed = st.slider("Speech Speed", min_value=50, max_value=300, value=150, step=10)

    # Begin extraction button
    if st.button("Begin Extraction"):
        with st.spinner("Performing OCR..."):
            if option != "Upload Image" and image is not None:
                # Perform OCR on the example image
                extracted_text = ocr_processor.perform_ocr(image)
            elif uploaded_image is not None:
                # Perform OCR on the uploaded image
                extracted_text = ocr_processor.perform_ocr(uploaded_image)
            else:
                st.warning("Please select or upload an image to begin extraction.")

            # Display the extracted text
            st.header("Extracted Text:")
            st.text(extracted_text)

            # Generate audio file
            audio_file = f"audio_{int(time.time())}.mp3"
            reader.read_aloud(extracted_text, audio_file)

            # Provide download link for the audio file
            st.markdown(f"**[Download Audio]({audio_file})**")

            # Play audio
            if st.button("Read Aloud"):
                st.markdown("Please wait while the text is being read aloud...")
                reader.read_aloud(audio_file)

if __name__ == "__main__":
    main()

