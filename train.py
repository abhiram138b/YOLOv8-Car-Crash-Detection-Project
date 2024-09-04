# train.py

def train_model(model, train_data, val_data):
    print("Training started...")
    model.train(data_path=train_data, epochs=50, batch_size=16, imgsz=640)
    print("Training completed.")
