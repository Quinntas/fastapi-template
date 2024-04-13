from datetime import datetime

from peewee import CharField, DateTimeField, AutoField, Model

from src.core.base_domain import BaseDomain
from src.infra.database.mysql.mysql_connection import db


class UserModel(Model):
    name = CharField(191, null=False)
    email = CharField(191, unique=True)
    password = CharField(191)

    id = AutoField(primary_key=True)
    pid = CharField(191, unique=True)
    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        db_table = "Users"


class UserDomain(BaseDomain):
    name: str
    email: str
    password: str
