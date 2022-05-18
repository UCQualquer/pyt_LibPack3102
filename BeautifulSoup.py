from bs4 import BeautifulSoup as bs
from typing import Union as Union

class BeautifulSoup(bs):
    def __init__(self, data: Union[str, bytes], parser = 'html.parser', **kwargs):
        if issubclass(type(data), bytes):
            data = data.decode()

        super().__init__(data, parser, **kwargs)