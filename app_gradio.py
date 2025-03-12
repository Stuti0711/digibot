import gradio as gr
import requests
import os

# Load API Key from Environment Variable
HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

# Hugging Face Model API URL
MODEL_URL = "https://api-inference.huggingface.co/models/ramim36/Kolors-Virtual-Try-On"

def virtual_tryon(user_image, cloth_image):
    """Send images to Hugging Face model and return result."""
    if user_image is None or cloth_image is None:
        return "Please upload both user and cloth images."

    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    
    files = {
        "user_image": user_image,
        "cloth_image": cloth_image,
    }
    
    response = requests.post(MODEL_URL, headers=headers, files=files)

    if response.status_code == 200:
        return response.json()  # Return model output
    else:
        return {"error": "Failed to process request", "details": response.text}

# Gradio Interface
iface = gr.Interface(
    fn=virtual_tryon,
    inputs=[
        gr.Image(type="file", label="Upload User Image"),
        gr.Image(type="file", label="Upload Cloth Image"),
    ],
    outputs="json",
    title="Virtual Try-On",
    description="Upload a user image and a clothing image to try them on virtually.",
)

# Launch Gradio app
if __name__ == "__main__":
    iface.launch()
