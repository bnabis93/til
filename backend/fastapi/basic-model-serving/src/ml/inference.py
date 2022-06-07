"""Inference image.

- Author: bono
- Email: qhsh9713@gmail.com
- Reference
https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project
"""
import cv2
import numpy as np
import torch


def preproces(image: np.uint8) -> np.float32:
    """Preprocessing image for imagenet model."""

    mean = np.array((0.486, 0.456, 0.406)).reshape((3, 1, 1))
    std = np.array((0.229, 0.224, 0.225)).reshape((3, 1, 1))

    resized_image = cv2.resize(image, (224, 224))
    resized_image = resized_image.astype(np.float32) / 255.0
    reshaped_image = resized_image.transpose((2, 0, 1))
    normed_image = (reshaped_image - mean) / (std)
    out = normed_image[np.newaxis, :]
    return out


def inference(image: np.uint8) -> str:
    """Input decoded image data."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    preprocesed_image = preproces(image)
    data = torch.tensor(preprocesed_image, dtype=torch.float32)
    model = torch.jit.load("src/ml/resnet50.pt", map_location=device)

    output = model(data)
    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    # Read the categories
    with open("./imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    return categories[top5_catid[0]]
