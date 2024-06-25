#!/usr/bin/envpython
# -*- coding:utf-8-*-

"""
统一logging模块
"""

import logging
import inspect
from loguru import logger


# 创建一个handler，用于将日志信息输出到控制台
class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

# logger.remove()  # 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
# logger.add(sys.stderr, level="INFO")  # 添加一个可以修改控制的handler


if __name__ == '__main__':
    logger.info("This is log info!")
    logger.warning("This is log warning!")
    logger.error("This is log error!")
    logger.debug("This is log debug!")

    # logger.add("test.log", backtrace=True, diagnose=True, rotation="500 MB")
