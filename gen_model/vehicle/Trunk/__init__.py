#!/usr/bin/env python3

"""Trunk model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointString,
    Model,
)


class Trunk(Model):
    """Trunk model.

    Attributes
    ----------
    Action: actuator


    """

    def __init__(self, name, parent):
        """Create a new Trunk model."""
        super().__init__(parent)
        self.name = name

        self.Action = DataPointString("Action", self)
