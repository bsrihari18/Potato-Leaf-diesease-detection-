import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import gradio as gr

# -------------------------------
# DEVICE
# -------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -------------------------------
# LOAD MODEL (SAME STRUCTURE)
# -------------------------------
model = models.mobilenet_v2(pretrained=False)
model.classifier[1] = nn.Linear(model.last_channel, 3)

# Load trained weights
model.load_state_dict(torch.load("plant_disease_model.pth", map_location=device))

model = model.to(device)
model.eval()

# MUST match training dataset
class_names = train_data.classes   # ✅ Correct way

# If running separately, manually paste:
# class_names = ['Early Blight', 'Late Blight', 'Healthy']


# TRANSFORM (same as test)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# -------------------------------
# PREDICTION FUNCTION
# -------------------------------
def predict_image(image):

    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        probs = torch.softmax(outputs, dim=1)[0]

    result = {class_names[i]: float(probs[i]) for i in range(len(class_names))}
    return result

# -------------------------------
# GRADIO UI
# -------------------------------
interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="🌿 Plant Disease Detection",
    description="Upload a leaf image to detect disease using MobileNetV2"
)

# -------------------------------
# LAUNCH
# -------------------------------
interface.launch()