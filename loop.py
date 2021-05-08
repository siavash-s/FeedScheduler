from typing import MutableSet
import publisher
from pydantic import BaseModel
from time import sleep
from logging import getLogger


class MainLoop:
    def __init__(self, publisher_: publisher.Publisher, channel_set: MutableSet, publish_interval: int):
        self.publisher = publisher_
        self.channel_set = channel_set
        self.exit_flag = False
        self.publish_interval = publish_interval

    def loop(self):
        while not self.exit_flag:
            channels = list(self.channel_set)
            getLogger().info(f"publishing {channels}")
            for channel in channels:
                self.publisher.publish(Task(link=channel).json())
            else:
                sleep(self.publish_interval)

    def exit(self):
        self.exit_flag = True
        self.publisher.close()


class Task(BaseModel):
    link: str
