import torch
import clip
from PIL import Image

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Load and preprocess the image
image = preprocess(Image.open("zero.jpg")).unsqueeze(0).to(device)

# Encode a text prompt
text = clip.tokenize([ " a photo consist of a man in swimming pool","A photo of a cat"]).to(device)

# Encode the image and the text
with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)

# Normalize the features
image_features /= image_features.norm(dim=-1, keepdim=True)
text_features /= text_features.norm(dim=-1, keepdim=True)

# Calculate the similarity between the image and each text prompt
similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)

# Print the similarity
print(similarity)