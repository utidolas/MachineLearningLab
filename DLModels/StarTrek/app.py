import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import io

# page config
st.set_page_config(page_title="Star Trek Classifier", page_icon="🖖")

# load model 
@st.cache_resource
def load_trained_model():
    return tf.keras.models.load_model('custom_model_stclassifier.keras')

model = load_trained_model()
classes = ['commandRed', 'operationGold', 'scienceBlue']

# UI mapping for UX
map_metadata = {
    'commandRed':    {'name': 'Command (RED)',    'color': '#FF0000'},
    'operationGold': {'name': 'Operations (GOLD)', 'color': '#D4AF37'},
    'scienceBlue':   {'name': 'Science (BLUE)',    'color': '#0000FF'}
}

# HEADER
st.title("🖖 Star Trek Division Identifier")

# file upload settings
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
uploaded_file = st.file_uploader("Upload a crew member's photo to determine their department.", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # check file size
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("File is too large. Please upload an image smaller than 5MB.")
    else:
        # display img for UI
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', width='stretch')
        
        # predictions
        if st.button('ANALYZE!'):
                # preprocess - resize to match model - 128x128
                img = image.convert('RGB').resize((128, 128))
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                img_array = img_array / 255.0  
                img_array = np.expand_dims(img_array, axis=0)

                # inference
                predictions = model.predict(img_array, verbose=0)
                class_idx = np.argmax(predictions[0])
                confidence = 100 * np.max(predictions[0])
            
                # text result
                internal_id = classes[class_idx]
                class_name = map_metadata[internal_id]['name']
                chosen_color = map_metadata[internal_id]['color']

                st.divider()
                # display dividion
                st.markdown(f"### Division: <span style='color:{chosen_color}'>{class_name}</span>", unsafe_allow_html=True)

                # display progress bar and confidence level
                st.markdown(f"""
                    <div style="width: 100%; background-color: #e0e0e0; border-radius: 5px;">
                        <div style="width: {confidence}%; background-color: {chosen_color}; 
                                    height: 20px; border-radius: 5px; transition: width 0.5s;">
                        </div>
                    </div>
                    <p style="text-align: right; font-family: monospace;">CONFIDENCE: {confidence:.2f}%</p>
                """, unsafe_allow_html=True)