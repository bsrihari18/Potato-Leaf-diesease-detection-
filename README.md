# 🌿 Potato Leaf Disease Detection using Deep Learning

## 📌 Overview
This project is a deep learning-based web application that detects potato leaf diseases using a pretrained **MobileNetV2** model. The model classifies images into three categories and provides prediction confidence.

The application is deployed using **Gradio** and hosted on Hugging Face Spaces for real-time usage.

data source 
https://www.kaggle.com/datasets/rizwan123456789/potato-disease-leaf-datasetpld
---

## 🚀 Live Demo
👉 https://huggingface.co/spaces/u78677/plantDiseaseModel

---

## 🧠 Model Details
- Model: MobileNetV2 (Pretrained)
- Technique: Transfer Learning + Fine-Tuning
- Classes: 3 (e.g., Healthy, Early Blight, Late Blight)
- Framework: PyTorch

---

## 🧰 Tech Stack
- Python
- PyTorch
- Torchvision
- Gradio
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---


---

## ⚙️ Installation (Run Locally)

### 1. Clone the Repository
git clone https://github.com/bsrihari18/Potato-Leaf-diesease-detection-.git

cd Potato-Leaf-diesease-detection-
### 2. Install Dependencies
pip install -r requirements.txt
---

## 🖼️ Input
- Upload a potato leaf image (JPG/PNG)

<img width="1910" height="997" alt="image" src="https://github.com/user-attachments/assets/c101e773-56d2-45e9-99c8-e56151fdf39b" />


## 📊 Output
- Predicted disease class
- Confidence score for each class
- ![Uploading image.png…]()


---

## ⚠️ Important Notes
- Ensure `plant_disease_model.pth` is in the root directory
- Update class names correctly in `app.py` if needed:
- class_names = ['Healthy', 'Early Blight', 'Late Blight']


---

## ☁️ Deployment (Hugging Face Spaces)
This project is deployed using Gradio on Hugging Face.

### Steps:
1. Create a Space (Gradio)
2. Upload:
   - app.py  
   - requirements.txt  
   - model file (.pth)  
3. Hugging Face automatically deploys the app

---

---

## 🔮 Future Improvements
- Add more disease classes
- Improve model accuracy
- Mobile app integration
- Real-time camera detection

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork and improve the project.

---

## 📜 License
This project is licensed under the MIT License.
