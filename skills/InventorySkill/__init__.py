from semantic_kernel.skill_definition import sk_function
import sqlite3

DB_PATH = "data/inventory.db"

class InventorySkill:
    @sk_function(description="Get the stock of a specific item")
    def GetItemStock(self, item_id: str) -> str:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT quantity FROM inventory WHERE item_id = ?", (item_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return f"📦 Stock for {item_id}: {result[0]} units."
        return "❌ Item not found."

    @sk_function(description="List all inventory items")
    def GetAllInventory(self) -> str:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        conn.close()
        return "\n".join([str(row) for row in rows])
