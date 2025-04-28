import os
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

def add_github_ai(kernel):
    kernel.add_service(
        OpenAIChatCompletion(
            model_id=os.getenv("MODEL_ID"),
            api_key=os.getenv("API_KEY"),
            endpoint=os.getenv("API_ENDPOINT"),
        ),
        service_id="chat"
    )
