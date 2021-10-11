import yaml
import os

class Configuration():
    """
    Class to load and handle the configuration
    """
    _conf = None
    
    def __init__(self, filePath:str) -> None:
        self.conf = filePath

    @property
    def conf(self):
        return self._conf

    @conf.setter
    def conf(self, filePath: str) -> dict:
        if filePath and os.path.exists(filePath):

            if filePath.endswith('.yaml') or filePath.endswith('.yml'):
                with open(filePath, 'r') as f:
                    self._conf = yaml.safe_load(f)

                    return

        raise Exception(f"File '{filePath}' could not be found or open")