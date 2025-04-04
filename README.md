# VentureForce - Multi-Agent Framework

## Project Overview

VentureForce is a multi-agent framework designed to help early-stage startups convert their initial ideas into tangible deliverables. The framework employs specialized AI agents that work together in an entrepreneurial hierarchy, with each agent focusing on specific aspects of business development such as marketing, legal, technical, and financial planning.

## Current Implementation: Marketing Agent

This repository currently implements only the **Marketing Agent** component of the VentureForce framework. The current workflow:

1. The Marketing Agent (a finetuned LLM) processes the user's business idea and generates initial marketing insights
2. These insights are then passed to a general OpenAI model with specialized prompting
3. The OpenAI model expands the insights into a comprehensive marketing plan with detailed sections for brand positioning, target audience analysis, channel strategy, and more

```
User Request → Finetuned Marketing Agent → OpenAI Expansion → Complete Marketing Plan
```

## Finetuning Approach

The Marketing Agent model is finetuned using Unsloth, which provides 2x faster finetuning for Llama models:

- **Base Model**: `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit`
- **Optimization**: Using LoRA (Low-Rank Adaptation) to update only 1-10% of parameters
- **Configuration**:
  - Rank (r) = 16
  - Target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
  - 4-bit quantization for reduced memory usage
  - Gradient checkpointing optimized with Unsloth
- **Prompt Format**: Based on the Alpaca instruction format with instruction, input, and response sections

The model is optimized to generate concise but insightful marketing guidance for early-stage startups. The response is then expanded by the OpenAI model based on our specialized marketing plan prompt template.

## Deployment

The implementation includes:
1. A finetuned model accessible via Hugging Face
2. A FastAPI service deployed on Google Colab
3. Ngrok for exposing the API to external requests
4. A Python interface for managing the two-stage generation process

## Future Development

This is an ongoing project with plans to expand the framework with additional agents:

- **Legal Agent**: For legal documentation, compliance, and risk assessment
- **Technical Team**: For developing and deploying full stack applications
- **UI/UX Agent**: For designing user-friendly interfaces based on requirements
- **Financial Team**: For budget planning, forecasting, and financial strategies
- **Project Manager Agent**: For coordinating all agents and ensuring effective collaboration

## Usage

Basic usage involves sending a POST request to the API endpoint with:
- An instruction describing the task
- Input text with business details
- Optional parameters for generation

The resulting marketing plan is returned as JSON and can be directly used by startup founders to guide their marketing efforts.

## Contributors

- Ahad Imran
- Hamza Akmal
- Asad Ullah Waraich
- Muhammad Mubashir

---

*This project demonstrates how specialized, domain-specific LLM agents can work together to provide comprehensive support for startup founders, addressing the limitations of general-purpose LLMs with domain expertise.*