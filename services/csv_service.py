import pandas as pd
from pathlib import Path


class CSVService:
    """
    Service class to perform CRUD operations on CSV files.
    """

    def __init__(self):
        # Project root directory
        self.project_root = Path(__file__).resolve().parent.parent

        # Data folder
        self.data_folder = self.project_root / "data"

        # CSV files
        self.products_file = self.data_folder / "products.csv"

    # --------------------------------------------------
    # Load Products
    # --------------------------------------------------

    def load_products(self):
        """
        Load all products from products.csv
        """
        try:
            return pd.read_csv(self.products_file)
        except FileNotFoundError:
            print("products.csv not found.")
            return pd.DataFrame()

    # --------------------------------------------------
    # Dashboard Methods
    # --------------------------------------------------

    def get_total_products(self):
        df = self.load_products()
        return len(df)

    def get_total_categories(self):
        df = self.load_products()
        return df["category"].nunique()

    def get_active_products(self):
        df = self.load_products()
        return len(df[df["status"] == "Active"])

    # --------------------------------------------------
    # Planning Workspace Methods
    # --------------------------------------------------

    def get_categories(self):
        """
        Return all unique product categories.
        """
        df = self.load_products()

        if df.empty:
            return []

        return sorted(
            df["category"].dropna().unique().tolist()
        )

    def get_products_by_category(self, category):
        """
        Return product names for a given category.
        """
        df = self.load_products()

        if df.empty:
            return []

        products = df[df["category"] == category]

        return sorted(
            products["product_name"].dropna().unique().tolist()
        )

    def get_all_products(self):
        """
        Return all product names.
        """
        df = self.load_products()

        if df.empty:
            return []

        return sorted(
            df["product_name"].dropna().unique().tolist()
        )

    # --------------------------------------------------
    # Product Details
    # --------------------------------------------------

    def get_product_by_id(self, product_id):
        """
        Get product details using Product ID
        """
        df = self.load_products()

        product = df[df["product_id"] == product_id]

        if product.empty:
            return None

        return product.to_dict(orient="records")[0]

    # --------------------------------------------------
    # CRUD Operations
    # --------------------------------------------------

    def add_product(self, product):
        """
        Add a new product.
        Product should be a dictionary.
        """
        df = self.load_products()

        new_df = pd.concat(
            [df, pd.DataFrame([product])],
            ignore_index=True
        )

        new_df.to_csv(
            self.products_file,
            index=False
        )

        return True

    def update_product_price(self, product_id, new_price):
        """
        Update product price.
        """
        df = self.load_products()

        if product_id not in df["product_id"].values:
            return False

        df.loc[
            df["product_id"] == product_id,
            "unit_price"
        ] = new_price

        df.to_csv(
            self.products_file,
            index=False
        )

        return True

    def delete_product(self, product_id):
        """
        Delete a product.
        """
        df = self.load_products()

        if product_id not in df["product_id"].values:
            return False

        df = df[df["product_id"] != product_id]

        df.to_csv(
            self.products_file,
            index=False
        )

        return True
