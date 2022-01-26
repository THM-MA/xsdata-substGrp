from dataclasses import dataclass
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TArtifact(TBaseElement):
    class Meta:
        name = "tArtifact"
