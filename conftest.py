#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
description: 全局固件
"""

# import pytest
# from envlib.env.envlogging import logger
# from envlib.env.app import Env
# from resources.data import PLATFORM_PORT, REST_USERNAME, REST_PASSWORD
#
#
# @pytest.fixture(scope="session", autouse=True)
# def login_app():
#     """例如自动登陆平台
#
#     :return:
#     """
#
#     logger.info(f"全局预置：开始使用{REST_USERNAME}/{REST_PASSWORD}账号登陆{PLATFORM_PORT}平台")
#     with Env(PLATFORM_PORT, REST_USERNAME, REST_PASSWORD):
#         logger.info(f"全局预置：初始化社区配置")
#         ManageOrgan.initialize_area(bind=True)
#         yield
#
#         logger.info("会话退出登陆")
