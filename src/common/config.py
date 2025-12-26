
from dotenv import load_dotenv
import os

load_dotenv()

rds_access_protocol = os.getenv("RDS_ACCESS_PROTOCOL")
rds_username = os.getenv("RDS_USERNAME")
rds_password = os.getenv("RDS_PASSWORD")
rds_host = os.getenv("RDS_HOST")
rds_port = os.getenv("RDS_PORT")
rds_db_name = os.getenv("RDS_DB_NAME")
print(rds_access_protocol)