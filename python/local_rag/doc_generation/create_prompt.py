

def create_prompt(topic:str, max_length:int) -> str:
    prompt = f"""
    You are a helpful assistant that generates an informative document on the topic: {topic}. 
    The document should be structured as introduction, body, and conclusion. 
    The maximum length of the document should be about {max_length} words.
    """
    return prompt
