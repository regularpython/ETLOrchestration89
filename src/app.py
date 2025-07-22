import json

from sqlalchemy import text

from src.source.Database.database_connection import engine


# import requests


def lambda_handler(event, context):
    print(event)
    data = json.loads(event['Records'][0]['body'])

    order_id = '12345'
    user_id = '1111'
    total_amount = '250'
    payment_method = 'Online'
    status = 'Success'

    insert_query = text("""
                    INSERT INTO batch89.orders (order_id, user_id, total_amount, payment_method, status)
                    VALUES (:order_id, :user_id, :total_amount, :payment_method, :status);
                """)
    with engine.connect() as connection:
        connection.execute(insert_query, {"order_id": order_id, "user_id": user_id,
                                          "total_amount": total_amount, "payment_method": payment_method,
                                          "status": status})
        connection.commit()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "Data": data
        }),
    }
