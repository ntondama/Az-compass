from services.csv_service import CSVService


class ProductAgent:

    def __init__(self):
        self.csv_service = CSVService()

    def process(self, query: str):

        query = query.lower()

        # Show all products
        if "all products" in query:
            return self.csv_service.load_products()

        # Active products
        if "active" in query:
            df = self.csv_service.load_products()
            return df[df["status"] == "Active"]

        # Product by ID
        if query.startswith("product "):

            product_id = query.replace("product", "").strip().upper()

            product = self.csv_service.get_product_by_id(product_id)

            if product:
                return product

            return "Product not found."

        # Category search
        categories = [
            "dairy",
            "bakery",
            "grocery",
            "beverages",
            "snacks",
            "personal care",
            "home care",
        ]

        for category in categories:

            if category in query:

                df = self.csv_service.load_products()

                return df[
                    df["category"].str.lower() == category
                ]

        return (
            "I can help with:\n"
            "- Show all products\n"
            "- Show Dairy products\n"
            "- Show Grocery products\n"
            "- Show active products\n"
            "- Product P1005"
        )
