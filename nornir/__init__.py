import pkg_resources

from nornir.init_nornir import InitNornir, InitNornirAsync

__version__ = pkg_resources.get_distribution("nornir").version

__all__ = ("InitNornir", "InitNornirAsync", "__version__")
