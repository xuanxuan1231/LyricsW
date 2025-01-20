"""
    这是一个示例插件
"""
from PyQt5 import uic
from loguru import logger
from datetime import datetime
from .ClassWidgets.base import PluginBase, SettingsBase, PluginConfig  # 导入CW的基类

from PyQt5.QtWidgets import QHBoxLayout
from qfluentwidgets import LineEdit
from flask import Flask, request

# 自定义小组件
WIDGET_CODE = 'widgets_lyrics.ui'
WIDGET_NAME = 'LyricsWidget'
WIDGET_WIDTH = 245


class Plugin(PluginBase):  # 插件类
    def __init__(self, cw_contexts, method):  # 初始化
        super().__init__(cw_contexts, method)  # 调用父类初始化方法

        self.method.register_widget(WIDGET_CODE, WIDGET_NAME, WIDGET_WIDTH)  # 注册小组件到CW
        self.cfg = PluginConfig(self.PATH, 'config.json')  # 实例化配置类

    flaskapp = Flask(__name__)

    @flaskapp.route('/component/lyrics/lyrics', methods=['POST'])
    def lyrics(self):
        self.method.change_widget_content(WIDGET_CODE, WIDGET_NAME, '')
        request.get_json()

    def execute(self):  # 自启动执行部分
        global flaskapp
        flaskapp.run(port=50063)
        # 小组件自定义（照PyQt的方法正常写）
        self.test_widget = self.method.get_widget(WIDGET_CODE)  # 获取小组件对象

    def update(self, cw_contexts):  # 自动更新部分
        super().update(cw_contexts)  # 调用父类更新方法