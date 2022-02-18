from dataclasses import dataclass


@dataclass
class Sample:

    id: int = 0
    name: str = None
    title: str = None
    description: str = None


    def __post_init__(self):
        self.id = int(self.id)

