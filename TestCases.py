from datetime import datetime  # Importing the datetime module for handling date and time
from Artwork import Artwork  # Importing the Artwork class from the Artwork module
from Exhibition import Exhibition  # Importing the Exhibition class from the Exhibition module
from SpecialEvent import SpecialEvent  # Importing the SpecialEvent class from the SpecialEvent module
from Ticket import Ticket  # Importing the Ticket class from the Ticket module
from Visitor import Visitor  # Importing the Visitor class from the Visitor module
from Tour import Tour  # Importing the Tour class from the Tour module

# Test cases for Artwork class
print("Test cases for Artwork class:")
# Creating an instance of the Artwork class
artwork1 = Artwork("The Falcon of Quraish", "Mattar Bin Lahej", datetime(2011, 1, 1), "Symbolic representation", "Emirati Art Gallery")
# Printing attributes of the artwork instance
print(f"Title: {artwork1.getTitle()}")
print(f"Artist: {artwork1.getArtist()}")
print(f"Date: {artwork1.getDate()}")
print(f"Significance: {artwork1.getSignificance()}")
print(f"Location: {artwork1.getLocation()}")

# Test cases for Exhibition class
print("\nTest cases for Exhibition class:")
# Creating instances of Artwork class for Exhibition
artwork2 = Artwork("My Dubai", "Abdul Qader Al Rais", datetime(2008, 1, 1), "Abstract cityscape", "Special Exhibition")
artwork3 = Artwork("Desert Symphony", "Hassan Sharif", datetime(2005, 1, 1), "Mixed media", "Special Exhibition")
artworks_list = [artwork2, artwork3]
# Creating an instance of the Exhibition class
exhibition1 = Exhibition("Emirati Art Exhibition", "Exhibition Hall 2", "2 months", artworks_list, "Dr. Ali")
# Printing attributes of the exhibition instance
print(f"Title: {exhibition1.getTitle()}")
print(f"Location: {exhibition1.getLocation()}")
print(f"Duration: {exhibition1.getDuration()}")
print(f"Curator: {exhibition1.getCurator()}")
exhibition1.addArtwork(artwork1)
print(f"Number of artworks: {len(exhibition1.getArtworks())}")

# Test cases for SpecialEvent class
print("\nTest cases for SpecialEvent class:")
# Creating an instance of the SpecialEvent class
special_event1 = SpecialEvent("Concert", "Outdoor Stage", "1 day", 50.0, ["Emirati Singer 1", "Emirati Singer 2"])
# Printing attributes of the special event instance
print(f"Title: {special_event1.getTitle()}")
print(f"Location: {special_event1.getLocation()}")
print(f"Duration: {special_event1.getDuration()}")
print(f"Ticket Price: {special_event1.getTicketPrice()}")
print(f"Performers: {special_event1.getPerformers()}")

# Test cases for Ticket class
print("\nTest cases for Ticket class:")
# Creating instances of Visitor and Ticket classes
visitor1 = Visitor("Dana", 24, "dana@example.com")
ticket1 = Ticket(63.0, "Adult", visitor1, exhibition1, datetime.now())
# Printing attributes of the ticket instance
print(f"Price: {ticket1.getPrice()}")
print(f"Ticket Type: {ticket1.getTicketType()}")
print(f"Visitor: {ticket1.getVisitor().getName()}")
print(f"Event: {ticket1.getEvent().getTitle()}")
print(f"Purchase Date: {ticket1.getPurchaseDate()}")

# Test cases for Visitor class
print("\nTest cases for Visitor class:")
# Purchase ticket for visitor and printing visitor details
visitor1.purchaseTicket(ticket1)
print(f"Name: {visitor1.getName()}")
print(f"Age: {visitor1.getAge()}")
print(f"Email: {visitor1.getEmail()}")
print(f"Tickets Purchased: {[ticket.getTicketType() for ticket in visitor1.getTicketsPurchased()]}")
visitor1.setAge(25)
print(f"Visitor's Age: {visitor1.getAge()}")

# Test cases for Tour class
print("\nTest cases for Tour class:")
# Creating an instance of the Tour class
tour1 = Tour(datetime(2024, 3, 30), 20, "Tour Guide A", exhibition1, "2 hours")
# Starting and changing the guide for the tour
tour1.startTour()
tour1.changeGuide("Tour Guide B")
