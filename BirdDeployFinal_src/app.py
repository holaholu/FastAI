import json
import gradio as gr
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

# 1) Load class labels
with open('classes.json', 'r') as f:
    classes = json.load(f)

# 2) Load the full model saved from Kaggle (Sequential backbone + head)
model = torch.load('bird_model_full.pth', map_location='cpu', weights_only=False)
model.eval()

# 3) Preprocessing (match training size; normalization can be kept simple for now)
preprocess = transforms.Compose([
    transforms.Resize((192, 192)),
    transforms.ToTensor(),
])

def predict(img: Image.Image):
    """
    Take a PIL image, return class probabilities as a dict.
    """
    x = preprocess(img).unsqueeze(0)  # shape: (1, 3, 192, 192)

    with torch.no_grad():
        logits = model(x)
        probs = F.softmax(logits, dim=1)[0]

    return {label: float(probs[i]) for i, label in enumerate(classes)}

title = "Bird or Forest Detector"
description = "A simple image classifier to determine if an image contains a bird or a forest. Trained on the fast.ai 'Is it a bird?' tutorial."

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(),
    title=title,
    description=description,
)

demo.launch()