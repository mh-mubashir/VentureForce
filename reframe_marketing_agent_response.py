import requests
import json

def get_ventureforce_response(instruction, input_text):
    # Make API call to your deployed VentureForce model
    response = requests.post(
        "https://your-ngrok-url.ngrok-free.app/generate",
        headers={"Content-Type": "application/json"},
        json={
            "instruction": instruction,
            "input_text": input_text,
            "max_new_tokens": 1024
        }
    )
    return response.json()["generated_text"]

def get_marketing_plan(instruction, input_text):
    # Step 1: Get response from VentureForce model
    ventureforce_response = get_ventureforce_response(instruction, input_text)
    
    # Step 2: Create the marketing plan prompt
    marketing_plan_prompt = create_marketing_plan_prompt(instruction, input_text, ventureforce_response)
    
    # Step 3: Send to general AI model (e.g., OpenAI's API)
    # Replace with your preferred general AI model API call
    general_ai_response = send_to_general_ai_model(marketing_plan_prompt)
    
    return general_ai_response

# Example usage
instruction = "Venture Force - A Multi Agent Framework for Early Age Startups"
input_text = "I want to create a startup that helps small businesses with AI-powered customer service"
marketing_plan = get_marketing_plan(instruction, input_text)
print(marketing_plan)