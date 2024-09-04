# test.py

def test_model(model, test_data):
    print("Testing started...")
    results = model.evaluate(data_path=test_data)
    print(f"Testing completed. mAP: {results['mAP']}")
