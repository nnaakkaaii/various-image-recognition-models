import argparse
from typing import Any, Callable, Dict

from . import (cosine_scheduler, linear_scheduler, step_scheduler)

schedulers: Dict[str, Callable[[Any, argparse.Namespace], Any]] = {
    'cosine_scheduler': cosine_scheduler.create_scheduler,
    'linear_scheduler': linear_scheduler.create_scheduler,
    'step_scheduler': step_scheduler.create_optimizer,
}

scheduler_options: Dict[str, Callable[[argparse.ArgumentParser], argparse.ArgumentParser]] = {
    'cosine_scheduler': lambda x: x,
    'linear_scheduler': lambda x: x,
    'step_scheduler': step_scheduler.scheduler_modify_commandline_options,
}
