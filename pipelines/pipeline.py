import random
from kfp import dsl
from kfp.dsl import component

@component
def preprocessing_component(env: str = "Local"):
    import random
    import logging

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info(f"[Preprocessing] ENV: {env}")
    random_int = random.randint(1, 100)
    logger.info(f"[Preprocessing] Random integer: {random_int}")

@component
def training_component(env: str = "Local"):
    import random
    import logging

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info(f"[Training] ENV: {env}")
    random_int = random.randint(1, 100)
    logger.info(f"[Training] Random integer: {random_int}")

@dsl.pipeline(name="two-step-pipeline", description="A pipeline with preprocessing and training steps.")
def two_step_pipeline(env: str = "Local"):
    """
    Pipeline with two components: preprocessing and training.
    """
    # Step 1: Preprocessing
    step_preprocessing = preprocessing_component(env=env)

    # Step 2: Training (depends on preprocessing)
    step_training = training_component(env=env).after(step_preprocessing)

if __name__ == "__main__":
    from kfp import compiler

    # Compile the pipeline to a YAML
    compiler.Compiler().compile(
        pipeline_func=two_step_pipeline,
        package_path="pipeline_compiled.yaml"
    )
    print("Pipeline compiled! Upload 'pipeline_compiled.yaml' on Kubeflow UI.")
