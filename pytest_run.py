# -*- coding: utf-8 -*-

"""
pytest 批量跑脚本入口
"""


import os
import time
import pytest


def run_test(*args, allure_report_path="report_allure"):
    now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
    pytest.main(list(args) + [
        "--self-contained-html",
        "--capture=tee-sys",
        "--alluredir", f"{allure_report_path}/{now}"
    ])
    time.sleep(1)

    os.system(f"allure generate ./{allure_report_path}/{now} -o ./{allure_report_path}/{now}/result --clean")


if __name__ == "__main__":
    # run_test("-m=P0 or P1")
    run_test()
