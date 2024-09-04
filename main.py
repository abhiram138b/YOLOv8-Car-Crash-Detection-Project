# main.py

from model import YOLOv8Model
from train import train_model
from test import test_model
from utils import load_data

# Load and prepare the dataset
train_data, val_data, test_data = load_data('path/to/dataset')

# Initialize YOLOv8 model
model = YOLOv8Model()

# Train the model
train_model(model, train_data, val_data)

# Test the model
test_model(model, test_data)
