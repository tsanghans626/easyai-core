import picologging as logging

from litestar.plugins.structlog import StructlogPlugin

logging.basicConfig()

logger = logging.getLogger()
struct_log = StructlogPlugin()
