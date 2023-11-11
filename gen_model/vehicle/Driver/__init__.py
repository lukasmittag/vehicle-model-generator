#!/usr/bin/env python3

"""Driver model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointString,
    DataPointUint16,
    Model,
)

from vehicle.Driver.Identifier import Identifier


class Driver(Model):
    """Driver model.

    Attributes
    ----------
    AttentiveProbability: sensor
        Probability of attentiveness of the driver.

        Value range: [0, 100]
        Unit: percent
    DistractionLevel: sensor
        Distraction level of the driver will be the level how much the driver is distracted, by multiple factors. E.g. Driving situation, acustical or optical signales inside the cockpit, phone calls.

        Value range: [0, 100]
        Unit: percent
    FatigueLevel: sensor
        Fatigueness level of driver. Evaluated by multiple factors like trip time, behaviour of steering, eye status.

        Value range: [0, 100]
        Unit: percent
    HeartRate: sensor
        Heart rate of the driver.

    Identifier: branch
        Identifier attributes based on OAuth 2.0.

    IsEyesOnRoad: sensor
        Has driver the eyes on road or not?

    EmotionDetection: sensor


    """

    def __init__(self, name, parent):
        """Create a new Driver model."""
        super().__init__(parent)
        self.name = name

        self.AttentiveProbability = DataPointFloat("AttentiveProbability", self)
        self.DistractionLevel = DataPointFloat("DistractionLevel", self)
        self.FatigueLevel = DataPointFloat("FatigueLevel", self)
        self.HeartRate = DataPointUint16("HeartRate", self)
        self.Identifier = Identifier("Identifier", self)
        self.IsEyesOnRoad = DataPointBoolean("IsEyesOnRoad", self)
        self.EmotionDetection = DataPointString("EmotionDetection", self)
