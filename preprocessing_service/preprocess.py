import json
import argparse

def preprocess(input_path, output_path):
    # Read input data
    with open(input_path, 'r') as f:
        data = json.load(f)
    
    # Simulate preprocessing
    processed_data = {"processed_data": f"transformed({data})"}
    
    # Write output data
    with open(output_path, 'w') as f:
        json.dump(processed_data, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocessing Service')
    parser.add_argument('--input_path', type=str, required=True, help='Path to input data')
    parser.add_argument('--output_path', type=str, required=True, help='Path to output processed data')
    
    args = parser.parse_args()
    
    preprocess(args.input_path, args.output_path)
