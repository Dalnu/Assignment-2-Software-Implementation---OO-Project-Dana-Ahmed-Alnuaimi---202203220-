from datetime import datetime

class Artwork:
    """Represents an artwork in the museum's collection."""

    def __init__(self, title: str, artist: str, date: datetime, significance: str, location: str):
        # Initialize the Artwork object with provided attributes.
        self.title = title  # Title of the artwork
        self.artist = artist  # Artist who created the artwork
        self.date = date  # Date of creation
        self.significance = significance  # Historical significance of the artwork
        self.location = location  # Location of the artwork in the museum

    def getTitle(self):
        # Getter method for title attribute
        return self.title
    def setTitle(self, title):
        # Setter method for title attribute
        self.title = title

    def getArtist(self):
        # Getter method for artist attribute
        return self.artist
    def setArtist(self, artist):
        # Setter method for artist attribute
        self.artist = artist

    def getDate(self):
        # Getter method for date attribute
        return self.date
    def setDate(self, date):
        # Setter method for date attribute
        self.date = date

    def getSignificance(self):
        # Getter method for significance attribute
        return self.significance
    def setSignificance(self, significance):
        # Setter method for significance attribute
        self.significance = significance

    def getLocation(self):
        # Getter method for location attribute
        return self.location
    def setLocation(self, location):
        # Setter method for location attribute
        self.location = location
