#!/usr/bin/env python3

"""Infotainment model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    Model,
)

from vehicle.Cabin.Infotainment.HMI import HMI
from vehicle.Cabin.Infotainment.Media import Media
from vehicle.Cabin.Infotainment.Navigation import Navigation


class Infotainment(Model):
    """Infotainment model.

    Attributes
    ----------
    HMI: branch
        HMI related signals

    Media: branch
        All Media actions

    Navigation: branch
        All navigation actions

    """

    def __init__(self, name, parent):
        """Create a new Infotainment model."""
        super().__init__(parent)
        self.name = name

        self.HMI = HMI("HMI", self)
        self.Media = Media("Media", self)
        self.Navigation = Navigation("Navigation", self)
