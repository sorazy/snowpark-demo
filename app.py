from flask import Flask, jsonify
from snowflake.snowpark import Session

app = Flask(__name__)

@app.route('/')
def index():
    session = Session.builder.configs({
        "account": "your_account.snowflakecomputing.com",
        "user": "your_user",
        "password": "your_password",
        "role": "SYSADMIN",
        "warehouse": "COMPUTE_WH",
        "database": "SNOWFLAKE_SAMPLE_DATA",
        "schema": "TPCH_SF1"
    }).create()

    df = session.table("ORDERS").limit(5)
    result = df.collect()
    return jsonify([row.as_dict() for row in result])