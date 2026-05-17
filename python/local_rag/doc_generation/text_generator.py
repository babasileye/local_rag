import requests


class TextGenerator:
    """
    A class to generate text content using an Ollama model.
    """

    def __init__(self, model_name:str, ollama_url:str)->None:
        """
        Initializes the text generator.
        Args:
            model_name (str): The name of the Ollama model to use for generating content.
            ollama_url (str): The URL of the Ollama API endpoint.
        """
        self.model_name = model_name
        self.ollama_url = ollama_url

    def __call__(self, prompt:str) -> str:
        """
        Generates content using the specified Ollama model.
        Args:
            prompt (str): The prompt to send to the Ollama model.
        Returns:
            str: The generated content from the Ollama model.
        """
        print(f"Generating text with model '{self.model_name}' for prompt: {prompt[:50]}...")
        print(f"Sending request to Ollama API at {self.ollama_url}...")
        response = requests.post(
            self.ollama_url,
            json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False,
            }
        )
        if response.status_code != 200:
            raise Exception(f"Generation failed: {response.status_code} - {response.text}")

        print("Text generation successful.")

        payload = response.json()
        generated_text = payload.get("response", "")
        if generated_text:
            return generated_text.strip()

        raise Exception(f"Ollama response did not contain text. Payload: {payload}")
