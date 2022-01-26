from dataclasses import dataclass, field
from typing import List
from .diagram_element import DiagramElement
from .node import Node

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Plane(Node):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    diagram_element: List[DiagramElement] = field(
        default_factory=list,
        metadata={
            "name": "DiagramElement",
            "type": "Element",
        }
    )
