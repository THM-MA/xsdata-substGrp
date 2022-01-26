# xsdata-substGrp
Testcase for XSDATA "Unknown property" parser error on XSD substitutionGroup.

# Schemas
Business Process Model and Notation (BPMN) for business processes diagrams.

Source: https://www.omg.org/spec/BPMN/2.0.2/

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
