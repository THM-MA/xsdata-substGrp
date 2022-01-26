# xsdata-substGrp
Testcase for XSDATA "Unknown property" parser error on XSD substitutionGroup.

# Error description

The XS schema contains a substitutionGroup Element named "di:DiagramElement" that is not detected during model generation. The substitutionGroup allows either an BPMNShape or a BPMNEdge element to be assigned to assigned BPMNPlane. 

BPMNDiagram -> BPMNPlane |-> BPMNShape
                         |-> BPMNEdge

However the assigment can ot be found in the model class of BPMNPlane

    __NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


    @dataclass
    class Bpmnplane(Plane):
        class Meta:
            name = "BPMNPlane"
            namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

        bpmn_element: Optional[QName] = field(
            default=None,
            metadata={
                "name": "bpmnElement",
                "type": "Attribute",
            }
        )

When parsing a valid BPMN XML file using the generated models an "Unknown property" occurs.

A working example with full details (schema, generated model, parser code,name of substitutionGroup) can be found on GitHub:

https://github.com/THM-MA/xsdata-substGrp

The documentation 21.8 (2021-08-03) mentions „Updated fields derived from xs:substitutionGroups to optional”. May this be the problem?

Any help is highly appreciated.

Thanks
Thomas


# Schemas
Business Process Model and Notation (BPMN) for business processes diagrams.

Source: https://www.omg.org/spec/BPMN/2.0.2/

![substitutionGroup="di:DiagramElement"](https://github.com/THM-MA/xsdata-substGrp/blob/main/images/substitutionGroup.png)


# Models generated using XSDATA
    xsdata .\schemas\BPMN20.xsd --package .\models --structure-style clusters --relative-imports 

# Exapmle Python XML parser file
    from pathlib import Path
    from xsdata.formats.dataclass.parsers import XmlParser
    from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler

    # Models
    from models.definitions import Definitions

    filename = Path("example.xml").absolute()
    parser = XmlParser(handler=XmlEventHandler)
    definitions = parser.parse(str(filename), Definitions) # Unknown property BPMNShape


# Exapmle XML file
    <?xml version="1.0" encoding="UTF-8"?>
    <bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:modeler="http://camunda.org/schema/modeler/1.0" id="Definitions_1uipr0j" targetNamespace="http://bpmn.io/schema/bpmn" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd">
        <bpmn:process id="Process_19gu2sk" isExecutable="true">
            <bpmn:startEvent id="Event_11lw8y6"/>
        </bpmn:process>
        <bpmndi:BPMNDiagram id="BPMNDiagram_1">
            <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_19gu2sk">
                <bpmndi:BPMNShape id="Event_11lw8y6_di" bpmnElement="Event_11lw8y6">
                    <dc:Bounds x="152" y="82" width="36" height="36"/>
                </bpmndi:BPMNShape>
            </bpmndi:BPMNPlane>
        </bpmndi:BPMNDiagram>
    </bpmn:definitions>
