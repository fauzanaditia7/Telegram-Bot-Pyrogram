import glob
import importlib
import sys
from os.path import dirname, basename, isfile
from bot.helper import MOD_LOAD, MOD_NOLOAD
from bot import LOGGER

def __list_all_modules():
    # This generates a list of modules in this
    # folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
        and not f.endswith("__main__.py")
    ]

    if MOD_LOAD or MOD_NOLOAD:
        to_load = MOD_LOAD
        if to_load:
            if not all(
                any(mod == module_name for module_name in all_modules)
                for mod in to_load
            ):
                LOGGER.error("Invalid Module name!")
                sys.exit()

        else:
            to_load = all_modules

        if MOD_NOLOAD:
            LOGGER.info("No load: %s", MOD_NOLOAD)
            return [item for item in to_load if item not in MOD_NOLOAD]

        return to_load

    return all_modules


importlib.import_module("bot.modules.__main__")
ALL_MODULES = sorted(__list_all_modules())
#LOGGER.info("Modules loaded: %s", str(ALL_MODULES))
LOGGER.info("".join(f"[{x}] " for x in sorted(__list_all_modules())))
__all__ = ALL_MODULES + ["ALL_MODULES"]