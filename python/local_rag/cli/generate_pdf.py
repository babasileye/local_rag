import argparse

from local_rag.doc_generation.create_prompt import create_prompt
from local_rag.doc_generation.text_generator import TextGenerator
from local_rag.doc_generation.text_to_pdf import text_to_pdf
from local_rag.models.llm_name_factory import get_llm_name

OLLAMA_URL = "http://localhost:11434/api/generate"


def main():
    """
    Main function to generate a PDF document based on a specified topic.
    This function parses command-line arguments, creates a prompt for the specified topic,
    generates text using the specified Ollama model, and converts the generated text to a PDF file.
    """
    parser = argparse.ArgumentParser(description="Generate a PDF document on a specified topic.")
    parser.add_argument("--topic", type=str, help="The topic for the PDF document.")
    parser.add_argument("--max_length", type=int, default=1000, help="The maximum length of the generated document in words.")
    parser.add_argument("--output", type=str, default="output.pdf", help="The path to the output PDF file.")
    parser.add_argument("--model", type=str, default="mistral", help="The key of the model to use for generation (e.g., 'mistral', 'llama').")  
    args = parser.parse_args() 
    topic = args.topic
    max_length = args.max_length
    output_path = args.output
    model_key = args.model
    prompt = create_prompt(topic, max_length)
    model_name = get_llm_name(model_key)
    text_generator = TextGenerator(model_name=model_name, ollama_url=OLLAMA_URL)
    text = text_generator(prompt)
    text_to_pdf(text, output_path)
