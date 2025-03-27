from ray import serve
from ray.serve.llm import LLMConfig, LLMServer, LLMRouter

llm_config = LLMConfig(
    model_loading_config=dict(
        model_id="qwen-0.5b",
        model_source="Qwen/Qwen2.5-0.5B-Instruct",
        deployment_config=dict(
            autoscalling_config=dict(
                min_replcas=1, max_replicas=2,
            )
        ),
        # Pass the desired accelerator type 
        accelerator_type="P100"
    )
)