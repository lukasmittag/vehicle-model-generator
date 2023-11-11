#!/usr/bin/env python3

"""Played model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from velocitas_sdk.model import (
    DataPointString,
    Model,
)


class Played(Model):
    """Played model.

    Attributes
    ----------
    Album: sensor
        Name of album being played

    Artist: sensor
        Name of artist being played

    Source: actuator
        Media selected for playback

        Allowed values: UNKNOWN, SIRIUS_XM, AM, FM, DAB, TV, CD, DVD, AUX, USB, DISK, BLUETOOTH, INTERNET, VOICE, BEEP
    Track: sensor
        Name of track being played

    URI: sensor
        User Resource associated with the media

    """

    def __init__(self, name, parent):
        """Create a new Played model."""
        super().__init__(parent)
        self.name = name

        self.Album = DataPointString("Album", self)
        self.Artist = DataPointString("Artist", self)
        self.Source = DataPointString("Source", self)
        self.Track = DataPointString("Track", self)
        self.URI = DataPointString("URI", self)
