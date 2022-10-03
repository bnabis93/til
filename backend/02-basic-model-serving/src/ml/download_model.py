"""Save ImageNet pretrained resnet model.

- Author: bono
- Email: qhsh9713@gmail.com
"""
import torch
import torchvision.models as models

# Initialize model
model = models.resnet50(pretrained=True)

# Set model to eval mode
model.eval()


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
compiled_model = torch.jit.script(model)
torch.jit.save(compiled_model, "resnet50.pt")
