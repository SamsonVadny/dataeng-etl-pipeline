import pandas as pd


def transform_products(product_df):
    df = product_df.copy()

    
    df['category'] = df['category'].apply(lambda x: x['name'] if isinstance(x, dict) else x)

    df = df.rename(columns={
        'id': 'product_id',
        'title': 'product_name',
        'price': 'product_price',
        'category': 'product_category',
        'description': 'description'
    })

    df = df[[
        'product_id', 'product_name', 'product_price', 'product_category', 'description'
    ]]

    df['product_price'] = df['product_price'].astype(float)

    return df


def transform_users(users_df):
    df = users_df.copy()

    df = df[[
        'id', 'email', 'name', 'role'
    ]]

    return df

