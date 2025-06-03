import code
import os
import sys
import time
import traceback
import warnings
def _get_module(name):
    try:
        return __import__(name)
    except ImportError:
        return None
def _get_mpl_backend():
    import matplotlib as mpl
    return mpl.get_backend()
def _get_pyplot():
    import matplotlib.pyplot as plt
    return plt
def _get_ipython():
    try:
        import IPython
        return IPython
    except ImportError:
        return None
def _get_ipython_shell():
    ipython = _get_ipython()
    if ipython is None:
        return None
    return ipython.get_ipython()
def _get_ipython_user_ns():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_ns
def _get_ipython_user_global_ns():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_global_ns
def _get_ipython_user_module():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_module
def _get_ipython_user_module_dict():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_module.__dict__
def _get_ipython_user_ns_dict():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_ns
def _get_ipython_user_global_ns_dict():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_global_ns
def _get_ipython_user_ns_keys():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_ns.keys()
def _get_ipython_user_global_ns_keys():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_global_ns.keys()
def _get_ipython_user_ns_items():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_ns.items()
def _get_ipython_user_global_ns_items():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_global_ns.items()
def _get_ipython_user_ns_values():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_ns.values()
def _get_ipython_user_global_ns_values():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return ipython_shell.user_global_ns.values()
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
def _get_ipython_user_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_ns)
def _get_ipython_user_global_ns_dir():
    ipython_shell = _get_ipython_shell()
    if ipython_shell is None:
        return None
    return dir(ipython_shell.user_global_ns)
