from datetime import datetime
from Exhibition import Exhibition


class Tour:
    """Represents a tour organized by the museum."""

    def __init__(self, date: datetime, group_size: int, guide: str, exhibition: Exhibition, duration: str):
        # Initialize the Tour object with provided attributes.
        self.date = date  # Date and time when the tour takes place
        self.group_size = group_size  # Size of the tour group
        self.guide = guide  # Guide leading the tour
        self.exhibition = exhibition  # Exhibition associated with the tour
        self.duration = duration  # Duration of the tour

    def getDate(self):
        # Getter method for date attribute
        return self.date
    def setDate(self, date):
        # Setter method for date attribute
        self.date = date

    def getGroupSize(self):
        # Getter method for group_size attribute
        return self.group_size
    def setGroupSize(self, group_size):
        # Setter method for group_size attribute
        self.group_size = group_size

    def getGuide(self):
        # Getter method for guide attribute
        return self.guide
    def setGuide(self, guide):
        # Setter method for guide attribute
        self.guide = guide

    def getExhibition(self):
        # Getter method for exhibition attribute
        return self.exhibition
    def setExhibition(self, exhibition):
        # Setter method for exhibition attribute
        self.exhibition = exhibition

    def getDuration(self):
        # Getter method for duration attribute
        return self.duration
    def setDuration(self, duration):
        # Setter method for duration attribute
        self.duration = duration

    def startTour(self):
        # Method to start the tour
        print(f"The tour of {self.exhibition.getTitle()} starts at {self.date}")

    def endTour(self):
        # Method to end the tour
        print(f"The tour of {self.exhibition.getTitle()} ends.")

    def changeGuide(self, new_guide):
        # Method to change the guide leading the tour
        self.guide = new_guide
        print(f"The guide for the tour of {self.exhibition.getTitle()} has been changed to {new_guide}.")
