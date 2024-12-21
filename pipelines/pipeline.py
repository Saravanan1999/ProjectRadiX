import kfp
from kfp import dsl

# Load component definitions
generate_input_op = dsl.load_component_from_file('components/generate_input_component.yaml')
preprocess_op = dsl.load_component_from_file('components/preprocess_component.yaml')
train_op = dsl.load_component_from_file('components/train_component.yaml')

@dsl.pipeline(
    name='Direct Data Processing Pipeline',
    description='A pipeline that generates input data, preprocesses it, and then trains a model.'
)
def direct_data_pipeline():
    # Step 1: Generate Input Data
    generate_input = generate_input_op()
    
    # Step 2: Preprocessing
    preprocessing = preprocess_op(
        input_data=generate_input.outputs['input_data']
    )
    
    # Step 3: Training
    training = train_op(
        processed_data=preprocessing.outputs['processed_data']
    )
