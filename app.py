from flask import Flask, jsonify
from snowflake.snowpark import Session

app = Flask(__name__)

@app.route('/')
def index():
    snowflake_config = {
        "account": os.environ["SF_ACCOUNT"],
        "user": os.environ["SF_USER"],
        "password": os.environ["SF_PASSWORD"],
        "role": os.environ.get("SF_ROLE", "SYSADMIN"),
        "warehouse": os.environ["SF_WAREHOUSE"],
        "database": os.environ["SF_DATABASE"],
        "schema": os.environ["SF_SCHEMA"],
    }

    session = Session.builder.configs(snowflake_config).create()

    df = session.table("ORDERS").limit(5)
    result = df.collect()
    return jsonify([row.as_dict() for row in result])