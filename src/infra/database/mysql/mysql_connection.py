from playhouse.db_url import connect

from src.utils.env import env

db = connect(env.DATABASE_URL)
