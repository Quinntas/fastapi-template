from typing import Dict, Any


class Context:
    def __init__(self,
                 state: Dict[str, Any] = None
                 ):
        self.state = state or {}
