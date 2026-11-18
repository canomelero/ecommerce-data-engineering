from dataclasses import dataclass


@dataclass(frozen=True)
class Dataset:
    filename: str
    table_name: str


DATASETS = (
    Dataset("olist_orders_dataset.csv", "orders"),
    Dataset("olist_customers_dataset.csv", "customers"),
    Dataset("olist_order_items_dataset.csv", "order_items"),
    Dataset("olist_products_dataset.csv", "products"),
    Dataset("olist_order_payments_dataset.csv", "order_payments"),
    Dataset("olist_sellers_dataset.csv", "sellers"),
    Dataset("olist_order_reviews_dataset.csv", "order_reviews"),
)