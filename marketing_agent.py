import requests
import json

def create_marketing_plan_prompt(instruction, user_input, model_response):
    prompt = f"""
    You are a specialized Marketing Strategist working with the VentureForce Multi-Agent Framework. The VentureForce AI has analyzed a startup concept and provided initial insights. Your task is to expand this into a comprehensive marketing plan.

    ORIGINAL REQUEST TO VENTUREFORCE:
    Instruction: {instruction}
    Input: {user_input}

    VENTUREFORCE AI RESPONSE:
    {model_response}

    Based on the VentureForce AI's response above, develop a detailed, actionable marketing plan that includes:

    1. TARGET AUDIENCE ANALYSIS
    - Define 2-3 primary customer personas with demographics, needs, and pain points
    - Identify key market segments and their potential value

    2. BRAND POSITIONING
    - Unique Value Proposition (UVP)
    - Brand voice, personality, and core messaging
    - Key differentiators from competitors

    3. MARKETING CHANNEL STRATEGY
    - Primary digital marketing channels (social media, content, email, etc.)
    - Content strategy for each channel
    - Paid vs. organic approach

    4. CUSTOMER ACQUISITION FUNNEL
    - Awareness stage tactics
    - Consideration stage engagement
    - Conversion optimization strategies
    - Retention and referral programs

    5. METRICS & KPIs
    - Key performance indicators to track
    - Growth targets (3-month, 6-month, 1-year)
    - Budget allocation recommendations

    6. IMPLEMENTATION TIMELINE
    - 90-day action plan with key milestones
    - Resource requirements

    Format your response as a structured marketing plan that the startup founder can immediately use to guide their marketing efforts. Be specific and actionable while maintaining alignment with the VentureForce AI's original analysis.
    """
    return prompt

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