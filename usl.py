"""
    用户界面
"""
import os

from bll import GameController
from model import MoveDirection


class GameConsoleView:
    """
        负责处理界面逻辑
    """

    def __init__(self):
        self.__controller = GameController()

    def start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def __print_map(self):
        # 在终端中可以 清空界面
        os.system("clear")

        for line in self.__controller.map:
            for item in line:
                print(item, end=" ")
            print()

    def update(self):
        while True:
            str_input = input("请输入(wsad)：")
            self.__move_map(str_input)
            # 如果地图没有变化,则跳过
            if not self.__controller.is_change:continue
            self.__controller.generate_new_number()
            self.__print_map()
            if self.__controller.is_game_over():
                print("游戏结束喽")
                break

    def __move_map(self, str_input):
        if str_input == "w":
            self.__controller.move(MoveDirection.UP)
        elif str_input == "s":
            self.__controller.move(MoveDirection.DOWN)
        elif str_input == "a":
            self.__controller.move(MoveDirection.LEFT)
        elif str_input == "d":
            self.__controller.move(MoveDirection.RIGHT)

