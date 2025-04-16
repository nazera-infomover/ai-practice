import subprocess

def get_model_response(prompt, model_name):
    """
    Sends the prompt to the specified Ollama model and returns the response.
    """
    result = subprocess.run(
        ["ollama", "run", model_name, prompt],  # Command to call Ollama
        capture_output=True,                    # Capture the output
        text=True                               # Treat output as text
    )
    return result.stdout.strip()  # Clean and return response

# Get user input
user_input = input("You: ").strip()

# Model to use
model_name = "deepseek-r1"

# Get response from model
response = get_model_response(user_input, model_name)

# Print the result
print(f"Deepseek Response: {user_input} → {response}")
