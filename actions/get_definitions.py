import json

import urbandict

from st2common.runners.base_action import Action

__all__ = [
    'GetDefinitionsAction'
]


class GetDefinitionsAction(Action):
    def run(self, term):
        result = urbandict.define(term)
        result = json.dumps(result)
        return result
