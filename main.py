
movies = [
    {"name": "Avengers", "price": 200, "times": ["10:00 AM", "2:00 PM", "6:00 PM"]},
    {"name": "Interstellar", "price": 180, "times": ["11:00 AM", "3:00 PM", "7:00 PM"]},
    {"name": "Inception", "price": 150, "times": ["12:00 PM", "4:00 PM", "8:00 PM"]},
    {"name": "The Dark Knight", "price": 220, "times": ["1:00 PM", "5:00 PM", "9:00 PM"]},
    {"name": "Dhurandar 2", "price": 200, "times": ["2:00 PM", "5:00 PM", "9:00 PM"]}
]

cinemas = [
    {"name": "PVR INOX", "extra": 0},
    {"name": "INOX", "extra": 20},
    {"name": "Cinepolis", "extra": 40},
    {"name": "IMAX", "extra": 100}
]

seats = {}
bookings = {}
sales = []
count = 0


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def movieshow():
    print("\n--- MOVIES ---")

    for i in range(len(movies)):
        print(i + 1, movies[i]["name"], "- Rs.", movies[i]["price"])


def cinemashow():
    print("\n--- CINEMAS ---")

    for i in range(len(cinemas)):
        print(i + 1, cinemas[i]["name"], "- Extra Rs.", cinemas[i]["extra"])


def timeshow(movie):
    print("\n--- TIMINGS ---")

    for i in range(len(movie["times"])):
        print(i + 1, movie["times"][i])


def seatshow(key):

    if key not in seats:
        seats[key] = set()

    print("\n--- SEATS ---")
    print("X = booked\n")

    for i in range(1, 21):
        if i in seats[key]:
            print("[X]", end=" ")
        else:
            print("[" + str(i) + "]", end=" ")

        if i % 5 == 0:
            print()


def book():

    global count

    movieshow()
    m = int(input("\nChoose movie: "))

    if m < 1 or m > len(movies):
        print("Invalid movie.")
        return

    movie = movies[m - 1]

    cinemashow()
    c = int(input("\nChoose cinema: "))

    if c < 1 or c > len(cinemas):
        print("Invalid cinema.")
        return

    cinema = cinemas[c - 1]

    timeshow(movie)
    t = int(input("\nChoose timing: "))

    if t < 1 or t > len(movie["times"]):
        print("Invalid timing.")
        return

    time = movie["times"][t - 1]

    key = movie["name"] + cinema["name"] + time

    if key not in seats:
        seats[key] = set()

    if len(seats[key]) == 20:
        print("All seats are booked.")
        return

    seatshow(key)

    s = int(input("\nChoose seat number: "))

    if s < 1 or s > 20:
        print("Invalid seat.")
        return

    if s in seats[key]:
        print("Seat already booked.")
        return

    price = movie["price"] + cinema["extra"]

    print("\nTicket price:", price)

    coupon = int(input("Enter coupon number (0 for no coupon): "))

    discount = 0

    if coupon == 0:
        print("No coupon used.")

    elif gcd(coupon, 10) == 1:
        discount = 10
        print("10% discount applied.")

    else:
        print("Invalid coupon.")

    dis = price * discount // 100
    final = price - dis

    count = count + 1

    seats[key].add(s)

    bookings[count] = (
        movie["name"],
        cinema["name"],
        time,
        s,
        final
    )

    sales.append(final)

    print("\n==============================")
    print("       BOOKING CONFIRMED")
    print("==============================")
    print("Booking ID :", count)
    print("Movie      :", movie["name"])
    print("Cinema     :", cinema["name"])
    print("Timing     :", time)
    print("Seat       :", s)
    print("Price      : Rs.", price)
    print("Discount   : Rs.", dis)
    print("Final Price: Rs.", final)
    print("==============================")


def cancel():

    if len(bookings) == 0:
        print("\nNo bookings available.")
        return

    bid = int(input("\nEnter booking ID: "))

    if bid not in bookings:
        print("Booking not found.")
        return

    b = bookings[bid]

    movie = b[0]
    cinema = b[1]
    time = b[2]
    seat = b[3]
    amount = b[4]

    key = movie + cinema + time

    if seat in seats[key]:
        seats[key].remove(seat)

    del bookings[bid]

    if amount in sales:
        sales.remove(amount)

    print("Ticket cancelled successfully.")


def show():

    if len(bookings) == 0:
        print("\nNo bookings available.")
        return

    print("\n--- ALL BOOKINGS ---")

    for bid in bookings:

        b = bookings[bid]

        print("\nBooking ID :", bid)
        print("Movie      :", b[0])
        print("Cinema     :", b[1])
        print("Timing     :", b[2])
        print("Seat       :", b[3])
        print("Amount     : Rs.", b[4])


def search():

    if len(bookings) == 0:
        print("\nNo bookings available.")
        return

    bid = int(input("\nEnter booking ID: "))

    if bid in bookings:

        b = bookings[bid]

        print("\n--- BOOKING FOUND ---")
        print("Booking ID :", bid)
        print("Movie      :", b[0])
        print("Cinema     :", b[1])
        print("Timing     :", b[2])
        print("Seat       :", b[3])
        print("Amount     : Rs.", b[4])

    else:
        print("Booking not found.")


def report():

    if len(sales) == 0:
        print("\nNo sales yet.")
        return

    total = 0

    for x in sales:
        total = total + x

    high = sales[0]

    for x in sales:
        if x > high:
            high = x

    recent = []

    i = len(sales) - 1

    while i >= 0:
        recent.append(sales[i])
        i = i - 1

    print("\n--- SALES REPORT ---")
    print("Tickets sold :", len(sales))
    print("Total sales  : Rs.", total)
    print("Highest sale : Rs.", high)
    print("Recent sales :", recent)


def main():

    while True:

        print("\n==============================")
        print("         CINERESERVE")
        print("==============================")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Show Bookings")
        print("4. Search Booking")
        print("5. Sales Report")
        print("6. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            book()

        elif choice == 2:
            cancel()

        elif choice == 3:
            show()

        elif choice == 4:
            search()

        elif choice == 5:
            report()

        elif choice == 6:
            print("\nThank you for using CineReserve!")
            break

        else:
            print("Invalid choice.")


main()
