from services.csv_service import CSVService


def main():
    csv_service = CSVService()

    print("=" * 60)
    print("ALL PRODUCTS")
    print("=" * 60)

    products = csv_service.load_products()
    print(products)

    print("\n" + "=" * 60)
    print("GET PRODUCT BY ID")
    print("=" * 60)

    product = csv_service.get_product_by_id("P1005")
    print(product)


if __name__ == "__main__":
    main()
