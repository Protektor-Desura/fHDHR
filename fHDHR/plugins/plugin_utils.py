

from .plugin_config import Plugin_Config
from .plugin_db import Plugin_DB


class Plugin_Utils():

    def __init__(self, config, logger, db, plugin_name, plugin_manifest, modname):
        self.config = Plugin_Config(config, plugin_manifest["name"])
        self.db = Plugin_DB(db, plugin_manifest["name"])
        self.logger = logger
        self.namespace = plugin_manifest["name"].lower()
        self.plugin_name = plugin_name
        self.plugin_manifest = plugin_manifest
        self.origin = None
