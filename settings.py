# 要修改游戏，只需修改settings.py中的一些值

class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)
