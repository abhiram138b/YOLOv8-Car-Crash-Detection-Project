# utils.py

def load_data(data_dir):
    train_data = f"{data_dir}/train"
    val_data = f"{data_dir}/val"
    test_data = f"{data_dir}/test"
    
    return train_data, val_data, test_data
