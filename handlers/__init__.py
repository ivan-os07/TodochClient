"""

Чтобы в main.py не делать этого
from handlers.start import router as start_router
from handlers.help import router as help_router
...

просто там где надо from handlers import *

"""

from .start import router as start_router
from .help import router as help_router
from .registration import router as register_router