#!/usr/bin/env python3

"""Body model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointFloat,
    DataPointString,
    Model,
)

from vehicle.Body.Hood import Hood
from vehicle.Body.Horn import Horn
from vehicle.Body.Lights import Lights
from vehicle.Body.Mirrors import Mirrors
from vehicle.Body.Raindetection import Raindetection
from vehicle.Body.Trunk import Trunk
from vehicle.Body.Windshield import Windshield


class Body(Model):
    """Body model.

    Attributes
    ----------
    BodyType: attribute (string)
        Body type code as defined by ISO 3779.

    Hood: branch
        Hood status.

    Horn: branch
        Horn signals.

    Lights: branch
        All lights.

    Mirrors: branch
        All mirrors.

    Raindetection: branch
        Rainsensor signals.

    RearMainSpoilerPosition: actuator
        Rear spoiler position, 0% = Spoiler fully stowed. 100% = Spoiler fully exposed.

        Value range: [0, 100]
        Unit: percent
    RefuelPosition: attribute (string)
        Location of the fuel cap or charge port.

        Allowed values: FRONT_LEFT, FRONT_RIGHT, MIDDLE_LEFT, MIDDLE_RIGHT, REAR_LEFT, REAR_RIGHT
    Trunk: branch
        Trunk status.

    Windshield: branch
        Windshield signals.

    """

    def __init__(self, name, parent):
        """Create a new Body model."""
        super().__init__(parent)
        self.name = name

        self.BodyType = DataPointString("BodyType", self)
        self.Hood = Hood("Hood", self)
        self.Horn = Horn("Horn", self)
        self.Lights = Lights("Lights", self)
        self.Mirrors = Mirrors("Mirrors", self)
        self.Raindetection = Raindetection("Raindetection", self)
        self.RearMainSpoilerPosition = DataPointFloat("RearMainSpoilerPosition", self)
        self.RefuelPosition = DataPointString("RefuelPosition", self)
        self.Trunk = Trunk("Trunk", self)
        self.Windshield = Windshield("Windshield", self)
