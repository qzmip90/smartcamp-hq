from semantic_kernel.skill_definition import sk_function

PRODUCT_INFO_FILE = "data/product_info.txt"

class ProductFAQSkill:

    @sk_function(description="Answer questions about tent products based on datasheet.")
    def GetProductAnswer(self, question: str) -> str:
        """Simple keyword search based Q&A."""
        try:
            with open(PRODUCT_INFO_FILE, "r") as f:
                data = f.read()

            question_lower = question.lower()

            if "trailmaster" in question_lower:
                return data.split("Alpine Explorer Tent")[0].strip()
            if "alpine explorer" in question_lower:
                return data.split("SkyView 2-Person Tent")[0].split("Alpine Explorer Tent")[1].strip()
            if "skyview" in question_lower:
                return data.split("SkyView 2-Person Tent")[1].strip()
            return "I could not find matching product information."
        except Exception as e:
            return f"Error accessing product info: {e}"
