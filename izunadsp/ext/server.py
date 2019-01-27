from typing import Dict, Any

import izunadsp
from izunadsp import Manager


class DSPServer:
    def __init__(self):
        self._config: Dict[str, Dict[str, Any]] = {}

    def config(self, part: str, setting: str, value: Any):
        if part not in self._config:
            self._config[part] = {
                "enabled": True
            }

        self._config[part][setting] = value

    def get_manager(self):
        manager = Manager()
        for name, part in self._config.items():
            if part["enabled"]:
                part_obj = getattr(izunadsp, name)
                for setting, value in part.items():
                    if setting == "enabled":
                        continue

                    if hasattr(part_obj, "set_" + setting):
                        getattr(part_obj, "set_" + setting)(value)
                    else:
                        setattr(part_obj, setting, value)
                manager.register_part(part_obj)

        return manager
