#!/usr/bin/envpython
# -*- coding:utf-8-*-

"""
Descriptions
"""
import os
import time
from common.unilogging import logger


def ping_server(server, timeout=500):
    """
    这个函数会尝试ping指定的服务器，如果连续10次ping通，则函数会返回。

    Args:
        server (str): 要ping的服务器的地址。
        timeout (int, optional): 超时时间，单位为秒。默认为500秒。

    Tip:
        服务器连续10次ping通，函数会返回；超过timeout秒，函数会抛出TimeoutError异常。

    Returns:
        None
    """
    logger.info("This is log info!")
    time.sleep(0.2)
    logger.warning("This is log warning!")
    time.sleep(0.2)
    logger.critical("This is log critical!")
    time.sleep(0.2)
    logger.error("This is log error!")
    time.sleep(0.2)
    logger.debug("This is log debug!")
    time.sleep(0.2)
    start_time = time.time()
    success_count = 0
    while time.time() - start_time < timeout:
        response = os.system("ping -n 1 " + server)
        if response == 0:
            success_count += 1
            if success_count >= 10:
                logger.info(f'服务器 {server} 连续10次ping通，脚本将退出。')
                return
            else:
                logger.debug(f'服务器 {server} ping通，继续尝试...')
        else:
            success_count = 0
            logger.debug(f'服务器 {server} 无法ping通，继续尝试...')
        time.sleep(2)  # 每2秒尝试一次
    raise TimeoutError(f'超过 {timeout} 秒，服务器 {server} 未连续ping通10次。')
