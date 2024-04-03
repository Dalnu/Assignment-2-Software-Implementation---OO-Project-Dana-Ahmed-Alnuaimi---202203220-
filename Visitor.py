from Ticket import Ticket


class Visitor:
    """Represents a visitor to the museum."""

    def __init__(self, name: str, age: int, email: str):
        # Initialize the Visitor object with provided attributes.
        self.name = name  # Name of the visitor
        self.age = age  # Age of the visitor
        self.email = email  # Email of the visitor
        self.tickets_purchased = []  # List of tickets purchased by the visitor

    def getName(self):
        # Getter method for name attribute
        return self.name
    def setName(self, name):
        # Setter method for name attribute
        self.name = name

    def getAge(self):
        # Getter method for age attribute
        return self.age
    def setAge(self, age):
        # Setter method for age attribute
        self.age = age

    def getEmail(self):
        # Getter method for email attribute
        return self.email
    def setEmail(self, email):
        # Setter method for email attribute
        self.email = email

    def getTicketsPurchased(self):
        # Getter method for tickets_purchased attribute
        return self.tickets_purchased
    def setTicketsPurchased(self, tickets_purchased):
        # Setter method for tickets_purchased attribute
        self.tickets_purchased = tickets_purchased

    def purchaseTicket(self, ticket: Ticket):
        # Add a purchased ticket to the list of tickets purchased by the visitor
        self.tickets_purchased.append(ticket)
