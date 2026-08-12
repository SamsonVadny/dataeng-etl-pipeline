from etl.extract import extract_product, extract_users
from etl.transform import transform_products, transform_users
from etl.load import load_to_postgres

def run_pipeline():
    print('Starting Pipeline')

    product_df = extract_product()
    user_df = extract_users()

    print('Starting Transformations')

    product_df = transform_products(product_df)
    user_df = transform_users(user_df)

    print('Starting to Postgres')

    load_to_postgres(product_df, 'products')
    load_to_postgres(user_df, 'users')

    print('ETL Pipeline Completed')


if __name__ == '__main__':
    run_pipeline()