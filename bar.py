import time
from git import RemoteProgress
from tqdm import tqdm

class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=''):
        if (cur_count < 30.0):
            self.pbar.colour = "red"
        if (cur_count > 30.0 and cur_count < 50.0):
            self.pbar.colour = "#FFA500"
        if(cur_count > 50.1 and cur_count < 75.0):
            self.pbar.colour = "yellow"
        if (cur_count > 75.1 and cur_count < 99.0):
            self.pbar.colour = "#3CB043"
        if (cur_count < 100.0):
            self.pbar.colour = "white"
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()




