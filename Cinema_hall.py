class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall_obj):
        if type(hall_obj) == Hall:
            cls.hall_list.append(hall_obj)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        for row in range(1, rows + 1):
            self._seats[row] = {}
            for col in range(1, cols + 1):
                self._seats[row][col] = 'Free'

    def entry_show(self, movie_name, id,  time):
        show_info = (movie_name, id, time)
        self._show_list.append(show_info)
        self._allocate_seats(id)

    def _allocate_seats(self, id):
        if id not in self._seats:
            self._seats[id] = {}
            for row in range(1, self.rows + 1):
                self._seats[id][row] = {}
                for col in range(1, self.cols + 1):
                    self._seats[id][row][col] = 'Free'

    def book_seats(self, id, seat_list):
        if id not in self._seats:
            print(f"Invalid show ID: {id}")
            return

        for row, col in seat_list:
            if row < 1 or row > self.rows or col < 1 or col > self.cols:
                print(f"Invalid seat ({row}, {col}).")
                continue

            if self._seats[id][row][col] == 'Free':
                self._seats[id][row][col] = 'Booked'
                print(f"Seat ({row}, {col}) booked for show({show_id}).")
            else:
                print(f"Seat ({row}, {col}) is already booked.")

    def view_show_list(self):
        print("Shows running now hall:")
        for show_info in self._show_list:
            print(
                f"Movie Name: {show_info[0]} ID: {show_info[1]}  Time: {show_info[2]}")

    def view_available_seats(self, id):
        if id not in self._seats:
            print(f"Invalid show ID: {id}")
            return

        print(f"Available seats for show ID {id}:")
        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                if self._seats[id][row][col] == 'Free':
                    print(f"Seat ({row}, {col})")


hall1 = Hall(rows=5, cols=10, hall_no=1)
Star_Cinema.entry_hall(hall1)

hall1.entry_show(movie_name="Citizen 1", id=11, time="10:00 AM")
hall1.entry_show(movie_name="Citizen 2", id=22, time="2:00 PM")

while True:
    print("\n------------------------------------")
    print("Welcome to Star Cinema")
    print("------------------------------------")
    print("Options:")
    print("1: View All Shows Today")
    print("2: View Available Seats")
    print("3: Book Ticket")
    print("4: Exit")

    choice = int(input("Enter your Option: "))

    if choice == 1:
        hall1.view_show_list()

    elif choice == 2:
        show_id = int(input("Enter show ID: "))
        hall1.view_available_seats(show_id)

    elif choice == 3:
        show_id = int(input("Enter show ID: "))
        num_seats = int(input("Enter the number of seats to book: "))
        seat_list = []
        for _ in range(num_seats):
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            seat_list.append((row, col))

        hall1.book_seats(show_id, seat_list)

    elif choice == 4:
        break
