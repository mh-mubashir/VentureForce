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