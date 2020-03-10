import logging
import json
import fire

from utils import pretty_print, flatten_dict, replace_list_elements


logger = logging.getLogger(__name__)

class Main:
    @staticmethod
    def load(filename):
         with open(filename, "r") as file:
            content = file.read()
         return json.loads(content)

    @staticmethod
    @pretty_print(logger)
    def show(filename):
        return Main.load(filename)


    def flatten(self, filename):
        dictionary = self.load(filename)
        return flatten_dict(replace_list_elements(dictionary))

if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    fire.Fire(Main)
