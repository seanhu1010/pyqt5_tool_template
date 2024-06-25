#!/usr/bin/envpython
# -*- coding:utf-8-*-
"""
编译并生成可安装包
"""

import zipfile
import subprocess
from pathlib import Path


def get_current_script_directory():
    """
    Get the absolute path to the directory containing the current script.
    Returns:
        Path: The path to the current script's directory.
    """
    return Path(__file__).parent.resolve()


class Config:
    """
    配置类
    """

    def __init__(self):
        self.root_path = get_current_script_directory()  # 获取当前脚本的绝对路径
        self.main_file = self.root_path / 'main.py'  # 主执行文件
        self.binary_folder = self.root_path / "include"  # 依赖的二进制文件的文件夹
        self.output_dir = self.root_path / 'dist'  # 输出文件夹
        self.build_dir = self.root_path / 'build'  # 编译文件夹
        self.spec_dir = self.root_path / 'spec'  # spec文件夹
        self.release_dir = self.root_path / 'release'  # 发布文件夹
        self.ico_file = self.root_path / 'icon' / 'logo.ico'  # 图标文件
        self.license_file = self.root_path / 'release' / 'License.txt'  # License描述文件
        self.product_name = "TestTool"  # 产品名称
        self.product_version = "0.0.5"  # 产品版本


def freeze():
    """
    Compile your code to a standalone executable
    PyStand:后续可以参考PyStand的实现
    https://github.com/skywind3000/PyStand
    https://www.zhihu.com/question/48776632
    """
    pass


def builder(config):
    # 使用pyinstaller生成dist文件, --noconsole表示不显示控制台
    command = (f'pyinstaller -y --noconsole'
               f' --distpath {config.output_dir}'
               f' --workpath {config.build_dir}'
               f' --specpath {config.spec_dir}'
               f' --add-data "{config.binary_folder};."'
               f' --name {config.product_name}_{config.product_version}'
               f' --icon={config.ico_file}'
               f' {config.main_file}')
    try:
        subprocess.run(command, shell=False)
    except:
        print("生成dist文件失败。请先pip install pyinstaller==6.2.0！")
        return

    print("生成dist文件完成。")


def installer(config):
    print("生成安装包完成。")


def zipdir(path, ziph):
    # ziph 是 zipfile 的实例
    for file in Path(path).rglob('*'):
        if file.is_file():
            ziph.write(file, file.relative_to(path))


def create_zip(config):
    # 设置 zip 文件的名称
    zip_file_name = f"{config.product_name}_{config.product_version}.zip"

    # 设置要打包的目录
    dir_to_zip = config.output_dir / f"{config.product_name}_{config.product_version}"

    # 设置 zip 文件的保存目录
    release_dir = config.release_dir
    release_dir.mkdir(parents=True, exist_ok=True)

    # 创建 zip 文件
    zipf = zipfile.ZipFile(release_dir / zip_file_name, 'w', zipfile.ZIP_DEFLATED)

    # 将目录打包到 zip 文件
    zipdir(dir_to_zip, zipf)

    # 关闭 zip 文件
    zipf.close()
    print("生成release包完成。")


if __name__ == '__main__':
    config = Config()
    builder(config)
    create_zip(config)
