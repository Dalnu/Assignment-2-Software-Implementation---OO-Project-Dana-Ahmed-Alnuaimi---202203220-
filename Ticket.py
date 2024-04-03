from datetime import datetime
from typing import Union
from Exhibition import Exhibition
from SpecialEvent import SpecialEvent


class Ticket:
    """Represents a ticket purchased by a visitor."""

    def __init__(self, price: float, ticket_type: str, visitor: 'Visitor', event: Union[Exhibition, SpecialEvent],
                 purchase_date: datetime):
        # Initialize the Ticket object with provided attributes.
        self.price = price  # Price of the ticket
        self.ticket_type = ticket_type  # Type of the ticket
        self.visitor = visitor  # Visitor who purchased the ticket
        self.event = event  # Event associated with the ticket (Exhibition or SpecialEvent)
        self.purchase_date = purchase_date  # Date and time when the ticket was purchased

    def getPrice(self):
        # Getter method for price attribute
        return self.price
    def setPrice(self, price):
        # Setter method for price attribute
        self.price = price

    def getTicketType(self):
        # Getter method for ticket_type attribute
        return self.ticket_type
    def setTicketType(self, ticket_type):
        # Setter method for ticket_type attribute
        self.ticket_type = ticket_type

    def getVisitor(self):
        # Getter method for visitor attribute
        return self.visitor
    def setVisitor(self, visitor):
        # Setter method for visitor attribute
        self.visitor = visitor

    def getEvent(self):
        # Getter method for event attribute
        return self.event
    def setEvent(self, event):
        # Setter method for event attribute
        self.event = event

    def getPurchaseDate(self):
        # Getter method for purchase_date attribute
        return self.purchase_date
    def setPurchaseDate(self, purchase_date):
        # Setter method for purchase_date attribute
        self.purchase_date = purchase_date
