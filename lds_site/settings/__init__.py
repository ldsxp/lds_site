import socket

# 根据主机名来判断是否在发布环境
if socket.gethostname() == 'lds_server':
    from .product import *  # noqa @UnusedWildImport
else:
    from .develop import *  # noqa @UnusedWildImport
