from local_rag.models.llm_registry import LLM_REGISTRY

def get_llm_name(model_key: str) -> str:
    """
    Retrieves the full model name from the registry based on the provided key.
    Args:
        model_key (str): The key representing the desired model (e.g., "mistral", "llama").
    Returns:
        str: The full model name corresponding to the provided key.
    Raises:
        ValueError: If the provided model key is not found in the registry.
    """
    if model_key in LLM_REGISTRY:
        return LLM_REGISTRY[model_key]
    else:
        raise ValueError(f"Model '{model_key}' not found in registry. Available models: {list(LLM_REGISTRY.keys())}")
