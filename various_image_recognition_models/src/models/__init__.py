import argparse
from typing import Callable, Dict

from .abstract_model import AbstractModel

models: Dict[str, Callable[[argparse.Namespace], AbstractModel]] = {
}

model_options: Dict[str, Callable[[argparse.ArgumentParser], argparse.ArgumentParser]] = {
}
