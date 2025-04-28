import os
import chainlit as cl
from dotenv import load_dotenv
import semantic_kernel as sk
from semantic_kernel.planning.sequential_planner import SequentialPlanner

from utils.github_ai_client import add_github_ai
from skills.InventorySkill import InventorySkill
from skills.ProductFAQSkill import ProductFAQSkill

# Load env
load_dotenv()

# Build Kernel
kernel = sk.Kernel()
add_github_ai(kernel)

inventory_skill = InventorySkill()
product_skill = ProductFAQSkill()

kernel.import_skill(inventory_skill, skill_name="Inventory")
kernel.import_skill(product_skill, skill_name="ProductFAQ")
kernel.import_semantic_skill_from_directory("skills", "ChatRouter")

planner = SequentialPlanner(kernel)

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content
    plan = await planner.create_plan_async(user_input)

    print("🛠️ Plan:\n", plan.generated_plan.strip())

    answer_ctx = await kernel.run_async(plan)
    final_answer = answer_ctx.result.strip()

    await cl.Message(content=final_answer).send()
