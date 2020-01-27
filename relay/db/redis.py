import redis
from relay.common.utils import get_config


__clients = dict()


def init_redis(db):
    print (__clients)
    if db in __clients:
        raise ValueError("Duplicated redis db: {}".format(db))

    config_dict = get_config("REDIS")
    r = redis.StrictRedis(
        host=config_dict["HOST"],
        port=config_dict["PORT"],
        db=db
    )
    # for checking connection and db index
    r.ping()

    __clients[db] = r


def get_redis(db):
    client = __clients.get(db)
    if client is None:
        raise ValueError("Unkown redis db: {}".format(db))
    return client
