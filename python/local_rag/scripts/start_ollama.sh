echo "Starting Ollama server in the background..."
ollama serve > /var/log/ollama.log 2>&1 &

echo "Ollama server started. Pulling models..."
ollama pull mistral:latest
ollama pull llama3:latest

echo "Ollama models pulled. Current Ollama status:"
ollama list