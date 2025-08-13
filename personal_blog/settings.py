import os
from dotenv import load_dotenv
load_dotenv()

run_development = os.environ["RUN_DEV_SETTINGS"].strip().lower() in ('true', '1', 't')
if run_development:
    from .dev_settings import *
else:
    from .prod_settings import *