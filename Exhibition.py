from datetime import datetime
from typing import List
from Artwork import Artwork


class Exhibition:
    """Represents an exhibition held at the museum."""

    def __init__(self, title: str, location: str, duration: str, artworks: List[Artwork], curator: str):
        # Initialize the Exhibition object with provided attributes.
        self.title = title  # Title of the exhibition
        self.location = location  # Location of the exhibition in the museum
        self.duration = duration  # Duration of the exhibition
        self.artworks = artworks  # List of artworks displayed in the exhibition
        self.curator = curator  # Curator responsible for the exhibition

    def getTitle(self):
        # Getter method for title attribute
        return self.title
    def setTitle(self, title):
        # Setter method for title attribute
        self.title = title

    def getLocation(self):
        # Getter method for location attribute
        return self.location
    def setLocation(self, location):
        # Setter method for location attribute
        self.location = location

    def getDuration(self):
        # Getter method for duration attribute
        return self.duration
    def setDuration(self, duration):
        # Setter method for duration attribute
        self.duration = duration

    def getArtworks(self):
        # Getter method for artworks attribute
        return self.artworks
    def setArtworks(self, artworks):
        # Setter method for artworks attribute
        self.artworks = artworks

    def getCurator(self):
        # Getter method for curator attribute
        return self.curator
    def setCurator(self, curator):
        # Setter method for curator attribute
        self.curator = curator

    def addArtwork(self, artwork):
        # Add an artwork to the exhibition
        self.artworks.append(artwork)
    def removeArtwork(self, artwork):
        # Remove an artwork from the exhibition
        self.artworks.remove(artwork)
