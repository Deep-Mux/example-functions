import json
from io import BytesIO

from PIL import Image
import torch
from torchvision import transforms

# Set up device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Labels
with open('data/imagenet_class_index.json') as f:
    classes = json.load(f)
    classes = dict((int(k), v[1]) for k, v in classes.items())

# Model
model = torch.hub.load('pytorch/vision', 'resnet18', pretrained=True)
model.eval()
model.to(device)

# Preprocessor
preprocessor = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def preprocess(data):
    input_image = Image.open(BytesIO(data))
    input_tensor = preprocessor(input_image)
    return input_tensor.unsqueeze(0).to(device)

def classify(data):
    tensor = preprocess(data)
    result = model(tensor)
    argmax = torch.argmax(result).item()
    print(argmax)
    return classes[argmax]
