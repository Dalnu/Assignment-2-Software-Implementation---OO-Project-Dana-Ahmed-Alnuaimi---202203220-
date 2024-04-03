from typing import List


class SpecialEvent:
    """Represents a special event organized by the museum."""

    def __init__(self, title: str, location: str, duration: str, ticket_price: float, performers: List[str]):
        # Initialize the SpecialEvent object with provided attributes.
        self.title = title  # Title of the special event
        self.location = location  # Location of the special event
        self.duration = duration  # Duration of the special event
        self.ticket_price = ticket_price  # Ticket price for the special event
        self.performers = performers  # List of performers at the special event

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

    def getTicketPrice(self):
        # Getter method for ticket_price attribute
        return self.ticket_price
    def setTicketPrice(self, ticket_price):
        # Setter method for ticket_price attribute
        self.ticket_price = ticket_price

    def getPerformers(self):
        # Getter method for performers attribute
        return self.performers
    def setPerformers(self, performers):
        # Setter method for performers attribute
        self.performers = performers
