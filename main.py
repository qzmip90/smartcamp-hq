import asyncio
import os
from semantic_kernel import Kernel
from semantic_kernel.planning.sequential_planner import SequentialPlanner
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from skills.ProductFAQSkill import ProductFAQSkill
from dotenv import load_dotenv

from utils.github_ai_client import add_github_ai
from skills.InventorySkill import InventorySkill

# Load environment variables
load_dotenv()

# Kernel setup
kernel = Kernel()
add_github_ai(kernel)

# Import skills
inventory_skill = InventorySkill()
product_skill = ProductFAQSkill() 
kernel.import_skill(inventory_skill, skill_name="Inventory")
kernel.import_skill(product_skill, skill_name="ProductFAQ") 
router_skill = kernel.import_semantic_skill_from_directory("skills", "ChatRouter")

# Planner setup
planner = SequentialPlanner(kernel)

async def smartcamp_chat():
    while True:
        user_input = input("🟢 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        plan = await planner.create_plan_async(user_input)
        print(f"🛠️ Plan:\n{plan.generated_plan.strip()}")

        answer_ctx = await kernel.run_async(plan)
        print(f"🤖 {answer_ctx.result.strip()}")

if __name__ == "__main__":
    asyncio.run(smartcamp_chat())
