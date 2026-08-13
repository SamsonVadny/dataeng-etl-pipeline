from etl.extract import extract_product, extract_users
from etl.transform import transform_products, transform_users
from etl.load import load_to_db

def run_pipeline():
    print('Starting Pipeline')

    product_df = extract_product()
    user_df = extract_users()

    print('Starting Transformations')

    product_df = transform_products(product_df)
    user_df = transform_users(user_df)

    print('Starting to DB')

    load_to_db(product_df, 'products')
    load_to_db(user_df, 'users')

    print('ETL Pipeline Completed')


if __name__ == '__main__':
    run_pipeline()
