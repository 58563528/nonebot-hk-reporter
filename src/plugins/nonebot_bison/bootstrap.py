from nonebot import get_driver

from .config.config_legacy import start_up as legacy_db_startup
from .config.db import upgrade_db
from .scheduler.manager import init_scheduler


@get_driver().on_startup
async def bootstrap():
    # legacy db
    legacy_db_startup()
    # new db
    await upgrade_db()
    # init scheduler
    await init_scheduler()
