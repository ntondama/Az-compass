from components.header import render_header
from components.sidebar import render_sidebar
from pages.product_master import show_product_master


def main():

    render_header()

    render_sidebar()

    show_product_master()


if __name__ == "__main__":
    main()
