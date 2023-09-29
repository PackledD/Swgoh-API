from loaders.base_loader import BaseLoader


class BaseLocalLoader(BaseLoader):
    def __init__(self):
        super().__init__()

    def load(self, *args):
        pass
