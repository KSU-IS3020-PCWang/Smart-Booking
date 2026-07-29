class Booking:
    def __init__(self, title, date, consultant):
        self.title = title
        self.date = date
        self.consultant = consultant

    # Display booking information
    def show_booking(self):
        print(f"Appointment: {self.title}")
        print(f"Date: {self.date}")
        print(f"Consultant: {self.consultant}")

    # Check if two bookings overlap
    def overlaps(self, other_booking):
        return (
            self.date == other_booking.date and
            self.consultant == other_booking.consultant
        )


class BookingSystem:
    def __init__(self):
        self.bookings = []

    # Add a booking
    def add_booking(self, new_booking):
        for booking in self.bookings:
            if booking.overlaps(new_booking):
                print("Double booking detected!")
                return

        self.bookings.append(new_booking)
        print("Booking added successfully!")

    # Display all bookings
    def show_all_bookings(self):
        for booking in self.bookings:
            booking.show_booking()
            print("-" * 20)


# Create booking system
system = BookingSystem()

# Create bookings
booking1 = Booking(
    "Hair Appointment",
    "05/10/2026",
    "Clarissa"
)

booking2 = Booking(
    "Hair Consultation",
    "05/10/2026",
    "Clarissa"
)

booking3 = Booking(
    "Nail Appointment",
    "05/11/2026",
    "Clarissa"
)

# Add bookings
system.add_booking(booking1)
system.add_booking(booking2)
system.add_booking(booking3)

# Display all bookings
system.show_all_bookings()
