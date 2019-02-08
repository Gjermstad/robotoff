from pathlib import Path
import os

PROJECT_DIR = Path(__file__).parent.parent
DATA_DIR = PROJECT_DIR / 'data'
CATEGORIES_PATH = DATA_DIR / 'categories.json'
DATASET_PATH = DATA_DIR / 'en.openfoodfacts.org.products.csv'
JSONL_DATASET_PATH = DATA_DIR / 'products.jsonl.gz'
JSONL_MIN_DATASET_PATH = DATA_DIR / 'products-min.jsonl.gz'
JSONL_DATASET_URL = "http://static.openfoodfacts.org/data/openfoodfacts-products.jsonl.gz"

DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_HOST = os.environ.get("DB_HOST", "localhost")

ELASTICSEARCH_HOSTS = os.environ.get("ELASTICSEARCH_HOSTS", "localhost:9200").split(",")
ELASTICSEARCH_TYPE = "document"

ELASTICSEARCH_CATEGORY_INDEX = 'category'
ELASTICSEARCH_PRODUCT_INDEX = 'product'
