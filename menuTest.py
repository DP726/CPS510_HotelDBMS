import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

DB_FILE = "hotel.db"

def execute_sql(statements):
    """Execute one or more SQL statements safely."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        if isinstance(statements, list):
            for sql in statements:
                cursor.execute(sql)
        else:
            cursor.execute(statements)
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()

def drop_tables():
    sql = [
        "DROP TABLE IF EXISTS StaffHotelService;",
        "DROP TABLE IF EXISTS StaffHotelRoom;",
        "DROP TABLE IF EXISTS Booking;",
        "DROP TABLE IF EXISTS HotelService;",
        "DROP TABLE IF EXISTS HotelRoom;",
        "DROP TABLE IF EXISTS Staff;",
        "DROP TABLE IF EXISTS Guest;",
        "DROP TABLE IF EXISTS Hotel;",
        "DROP TABLE IF EXISTS Location;"
    ]
    execute_sql(sql)
    messagebox.showinfo("Success", "All tables dropped successfully.")

def create_tables():
    sql = [
        """CREATE TABLE IF NOT EXISTS Location (
            PostalCode TEXT PRIMARY KEY,
            StreetAddress TEXT NOT NULL,
            City TEXT NOT NULL,
            Province TEXT NOT NULL,
            Country TEXT NOT NULL
        );""",
        """CREATE TABLE IF NOT EXISTS Hotel (
            HotelID INTEGER PRIMARY KEY,
            HotelName TEXT NOT NULL,
            PostalCode TEXT NOT NULL,
            FOREIGN KEY (PostalCode) REFERENCES Location(PostalCode) ON DELETE CASCADE
        );""",
        """CREATE TABLE IF NOT EXISTS Staff (
            StaffID INTEGER PRIMARY KEY,
            HotelID INTEGER NOT NULL,
            Name TEXT NOT NULL,
            PhoneNumber TEXT NOT NULL UNIQUE,
            EmployeePosition TEXT NOT NULL,
            Salary INTEGER NOT NULL,
            Schedule DATE NOT NULL,
            FOREIGN KEY (HotelID) REFERENCES Hotel(HotelID) ON DELETE CASCADE
        );""",
        """CREATE TABLE IF NOT EXISTS Guest (
            GuestID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            PhoneNumber TEXT NOT NULL UNIQUE,
            Email TEXT NOT NULL UNIQUE,
            PostalCode TEXT NOT NULL,
            FOREIGN KEY (PostalCode) REFERENCES Location(PostalCode) ON DELETE CASCADE
        );""",
        """CREATE TABLE IF NOT EXISTS HotelRoom (
            RoomNumber INTEGER PRIMARY KEY,
            GuestID INTEGER,
            Type TEXT NOT NULL,
            Price REAL NOT NULL,
            Availability TEXT NOT NULL,
            FOREIGN KEY (GuestID) REFERENCES Guest(GuestID) ON DELETE CASCADE
        );""",
        """CREATE TABLE IF NOT EXISTS HotelService (
            ServiceID INTEGER PRIMARY KEY,
            RoomNumber INTEGER NOT NULL,
            GuestID INTEGER NOT NULL,
            ServiceName TEXT NOT NULL,
            Cost REAL NOT NULL,
            ServiceDescription TEXT NOT NULL,
            FOREIGN KEY (RoomNumber) REFERENCES HotelRoom(RoomNumber) ON DELETE CASCADE,
            FOREIGN KEY (GuestID) REFERENCES Guest(GuestID) ON DELETE CASCADE
        );""",
        """CREATE TABLE IF NOT EXISTS Booking (
            BookingID INTEGER PRIMARY KEY,
            GuestID INTEGER NOT NULL,
            RoomNumber INTEGER NOT NULL,
            BookingStatus TEXT NOT NULL,
            LengthOfStay INTEGER NOT NULL,
            PaymentMethod TEXT NOT NULL,
            BookingDate DATE NOT NULL,
            Receptionist TEXT,
            FOREIGN KEY (GuestID) REFERENCES Guest(GuestID) ON DELETE CASCADE,
            FOREIGN KEY (RoomNumber) REFERENCES HotelRoom(RoomNumber) ON DELETE CASCADE
        );""",
        """CREATE TABLE IF NOT EXISTS StaffHotelRoom (
            StaffID INTEGER NOT NULL,
            RoomNumber INTEGER NOT NULL,
            InteractionDate DATE NOT NULL,
            Details TEXT NOT NULL,
            PRIMARY KEY (StaffID, RoomNumber),
            FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE,
            FOREIGN KEY (RoomNumber) REFERENCES HotelRoom(RoomNumber) ON DELETE CASCADE
        );""",
        """CREATE TABLE IF NOT EXISTS StaffHotelService (
            StaffID INTEGER NOT NULL,
            ServiceID INTEGER NOT NULL,
            ServiceDate DATE NOT NULL,
            ServiceDetail TEXT NOT NULL,
            PRIMARY KEY (StaffID, ServiceID),
            FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE,
            FOREIGN KEY (ServiceID) REFERENCES HotelService(ServiceID) ON DELETE CASCADE
        );"""
    ]
    execute_sql(sql)
    messagebox.showinfo("Success", "All tables created successfully.")

def populate_tables():
    inserts = [
        # Locations
        "INSERT OR IGNORE INTO Location (PostalCode, StreetAddress, City, Province, Country) VALUES ('M6H5N3', '123 Bottelier Rd', 'Toronto', 'Ontario', 'Canada');",
        "INSERT OR IGNORE INTO Location (PostalCode, StreetAddress, City, Province, Country) VALUES ('M7H5N3', '123 Don Rd', 'Toronto', 'Ontario', 'Canada');",
        "INSERT OR IGNORE INTO Location (PostalCode, StreetAddress, City, Province, Country) VALUES ('8D3V4A', '123 Drake Rd', 'Montreal', 'Quebec', 'Canada');",
        "INSERT OR IGNORE INTO Location (PostalCode, StreetAddress, City, Province, Country) VALUES ('M5A1B2', '12 Doale Street', 'Toronto', 'Ontario', 'Canada');",
        "INSERT OR IGNORE INTO Location (PostalCode, StreetAddress, City, Province, Country) VALUES ('M2A1B2', '12 Oak Street', 'Toronto', 'Ontario', 'Canada');",
        # Hotels
        "INSERT OR IGNORE INTO Hotel (HotelID, HotelName, PostalCode) VALUES (1, 'Alpha', 'M6H5N3');",
        "INSERT OR IGNORE INTO Hotel (HotelID, HotelName, PostalCode) VALUES (2, 'Charlie','M7H5N3');",
        "INSERT OR IGNORE INTO Hotel (HotelID, HotelName, PostalCode) VALUES (3, 'Tango', '8D3V4A');",
        # Staff
        "INSERT OR IGNORE INTO Staff (StaffID, HotelID, Name, PhoneNumber, EmployeePosition, Salary, Schedule) VALUES (123, 1, 'Ricky Santos', '647-420-1738', 'Manager',67000, '2025-09-16');",
        "INSERT OR IGNORE INTO Staff (StaffID, HotelID, Name, PhoneNumber, EmployeePosition, Salary, Schedule) VALUES (2345, 2, 'Dojic Rafeal', '289-420-1738', 'Cleaner',87000, '2025-09-12');",
        "INSERT OR IGNORE INTO Staff (StaffID, HotelID, Name, PhoneNumber, EmployeePosition, Salary, Schedule) VALUES (345, 2, 'Obama Rafeal', '895-420-1738', 'President',187000, '2025-09-12');",
        "INSERT OR IGNORE INTO Staff (StaffID, HotelID, Name, PhoneNumber, EmployeePosition, Salary, Schedule) VALUES (258, 2, 'McDonald oConnel', '741-420-1738', 'Fooder',44000, '2025-09-12');",
        # Guests
        "INSERT OR IGNORE INTO Guest (GuestID, Name, PhoneNumber, Email, PostalCode) VALUES (1, 'Alice Green', '555-101-2020', 'alice.green@email.com','M5A1B2');",
        "INSERT OR IGNORE INTO Guest (GuestID, Name, PhoneNumber, Email, PostalCode) VALUES (2, 'Adam Bandler', '416-101-2020', 'badam@email.com','M2A1B2');",
        # Rooms
        "INSERT OR IGNORE INTO HotelRoom (RoomNumber, Type, Price, Availability, GuestID) VALUES (101, 'Single', 120.00, 'Booked', 1);",
        "INSERT OR IGNORE INTO HotelRoom (RoomNumber, Type, Price, Availability, GuestID) VALUES (102, 'Single', 120.00, 'Booked', 2);",
        "INSERT OR IGNORE INTO HotelRoom (RoomNumber, Type, Price, Availability, GuestID) VALUES (201, 'Double', 200.00, 'Available', NULL);",
        "INSERT OR IGNORE INTO HotelRoom (RoomNumber, Type, Price, Availability, GuestID) VALUES (202, 'Suite', 420.00, 'Available', NULL);",
        "INSERT OR IGNORE INTO HotelRoom (RoomNumber, Type, Price, Availability, GuestID) VALUES (302, 'Double', 200.00, 'Available', NULL);",
        # Services
        "INSERT OR IGNORE INTO HotelService (ServiceID, RoomNumber,GuestID, ServiceName, Cost, ServiceDescription) VALUES (1, 101, 1, 'Cleaning', 34.32, 'Room Cleaning');",
        "INSERT OR IGNORE INTO HotelService (ServiceID, RoomNumber,GuestID, ServiceName, Cost, ServiceDescription) VALUES (2, 101, 1, 'Food', 234.32, 'Dinner');",
        "INSERT OR IGNORE INTO HotelService (ServiceID, RoomNumber,GuestID, ServiceName, Cost, ServiceDescription) VALUES (3, 102, 2, 'Food', 234.32, 'Dinner');",
        # Bookings
        "INSERT OR IGNORE INTO Booking (BookingID, GuestID, RoomNumber, BookingStatus, LengthOfStay, PaymentMethod, BookingDate, Receptionist) VALUES (1, 1, 101, 'Confirmed',  3, 'Credit Card', '2025-09-19', NULL);",
        "INSERT OR IGNORE INTO Booking (BookingID, GuestID, RoomNumber, BookingStatus, LengthOfStay, PaymentMethod, BookingDate, Receptionist) VALUES (2, 2, 102, 'Confirmed',  4, 'Credit Card', '2025-10-19', NULL);",
        # Staff Interactions
        "INSERT OR IGNORE INTO StaffHotelRoom (StaffID, RoomNumber, InteractionDate, Details) VALUES (123, 101, '2025-09-19', 'Cleaned and changed linens for occupied double room.');",
        "INSERT OR IGNORE INTO StaffHotelRoom (StaffID, RoomNumber, InteractionDate, Details) VALUES (123, 102, '2025-09-19', 'Provided room service delivery of breakfast.');",
        "INSERT OR IGNORE INTO StaffHotelService (StaffID, ServiceID, ServiceDate, ServiceDetail) VALUES (123, 1, '2025-09-19', 'Provided room service delivery of breakfast.');"
    ]
    execute_sql(inserts)
    messagebox.showinfo("Success", "Tables populated successfully.")

def run_queries():
    # Clear previous results
    for widget in result_frame.winfo_children():
        widget.destroy()

    queries = [
        ("Lowest Price Rooms by Type",
         "SELECT MIN(Price) AS LowestPrice, Type FROM HotelRoom WHERE Availability = 'Available' GROUP BY Type ORDER BY LowestPrice ASC;"),
        ("Staff Activity Log",
         """
         SELECT s.Name AS StaffName, r.RoomNumber AS Location, sr.InteractionDate AS ActivityDate, sr.Details AS ActivityDetails, 'Room Interaction' AS ActivityType
         FROM StaffHotelRoom sr
         JOIN Staff s ON sr.StaffID = s.StaffID
         JOIN HotelRoom r ON sr.RoomNumber = r.RoomNumber
         UNION
         SELECT s.Name AS StaffName, hs.ServiceID AS Location, shs.ServiceDate AS ActivityDate, shs.ServiceDetail AS ActivityDetails, 'Service Interaction' AS ActivityType
         FROM StaffHotelService shs
         JOIN Staff s ON shs.StaffID = s.StaffID
         JOIN HotelService hs ON shs.ServiceID = hs.ServiceID
         ORDER BY StaffName, ActivityDate;
         """),
        ("Total Service Cost per Guest",
         "SELECT g.Name AS GuestName, SUM(hs.Cost) AS TotalServiceCost FROM HotelService hs JOIN Guest g ON hs.GuestID = g.GuestID GROUP BY g.Name ORDER BY TotalServiceCost DESC;"),
        ("Confirmed Bookings per Room Type",
         "SELECT hr.Type AS RoomType, COUNT(b.BookingID) AS ConfirmedBookingCount FROM Booking b JOIN Guest g ON b.GuestID = g.GuestID JOIN HotelRoom hr ON b.RoomNumber = hr.RoomNumber WHERE b.BookingStatus = 'Confirmed' GROUP BY hr.Type ORDER BY ConfirmedBookingCount DESC;"),
        ("Guests Spending Above Average",
         """
         SELECT g.Name AS GuestName, SUM(hs.Cost) AS TotalSpent
         FROM Guest g
         JOIN HotelService hs ON g.GuestID = hs.GuestID
         GROUP BY g.Name
         HAVING SUM(hs.Cost) > (
             SELECT AVG(TotalCost) FROM (
                 SELECT SUM(Cost) AS TotalCost FROM HotelService GROUP BY GuestID
             )
         );
         """)
    ]

    for title, query in queries:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [description[0] for description in cursor.description]

        group = tk.Frame(result_frame)
        group.pack(fill="x", padx=10, pady=10)

        tk.Label(group, text=title, font=("Arial", 12, "bold")).pack(anchor="w")

        tree = ttk.Treeview(group, columns=headers, show="headings", height=6)
        tree.pack(fill="x", expand=True)

        for h in headers:
            tree.heading(h, text=h)
            tree.column(h, width=130)

        for row in rows:
            tree.insert("", "end", values=row)

        conn.close()

def clear_results():
    for widget in result_frame.winfo_children():
        widget.destroy()

def add_custom_table():
    """Open dialog to create a custom table."""
    dialog = tk.Toplevel(root)
    dialog.title("Add Custom Table")
    dialog.geometry("500x400")
    dialog.resizable(True, True)

    tk.Label(dialog, text="Table Name:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)
    table_name_entry = tk.Entry(dialog, width=40)
    table_name_entry.pack(anchor="w", padx=10, pady=5)

    tk.Label(dialog, text="Columns (format: name TYPE [CONSTRAINT], ...)", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)
    columns_text = tk.Text(dialog, height=10, width=50)
    columns_text.pack(padx=10, pady=5, fill="both", expand=True)
    columns_text.insert("1.0", "id INTEGER PRIMARY KEY,\nname TEXT NOT NULL")

    def create_table_from_dialog():
        table_name = table_name_entry.get().strip()
        columns = columns_text.get("1.0", "end-1c").strip()

        if not table_name:
            messagebox.showerror("Error", "Table name cannot be empty.")
            return
        if not columns:
            messagebox.showerror("Error", "Columns cannot be empty.")
            return

        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Table '{table_name}' created successfully.")
            dialog.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    tk.Button(dialog, text="Create Table", command=create_table_from_dialog).pack(pady=10)

def delete_table():
    """Open dialog to delete an existing table."""
    dialog = tk.Toplevel(root)
    dialog.title("Delete Table")
    dialog.geometry("400x200")

    tk.Label(dialog, text="Select table to delete:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        return

    if not tables:
        messagebox.showinfo("Info", "No tables found in the database.")
        dialog.destroy()
        return

    table_var = tk.StringVar(value=tables[0])
    dropdown = ttk.Combobox(dialog, textvariable=table_var, values=tables, state="readonly", width=40)
    dropdown.pack(padx=10, pady=10)

    def delete_selected_table():
        table_name = table_var.get()
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete table '{table_name}'?"):
            try:
                conn = sqlite3.connect(DB_FILE)
                cursor = conn.cursor()
                cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"Table '{table_name}' deleted successfully.")
                dialog.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", str(e))

    tk.Button(dialog, text="Delete Table", command=delete_selected_table, bg="red", fg="white").pack(pady=10)

def see_tables():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = [row[0] for row in cursor.fetchall()]
        
        if not tables:
            messagebox.showinfo("Info", "No tables found in the database.")
            conn.close()
            return

        for table_name in tables:
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]

            group = tk.Frame(result_frame)
            group.pack(fill="x", padx=10, pady=10)

            tk.Label(group, text=table_name, font=("Arial", 12, "bold")).pack(anchor="w")

            tree = ttk.Treeview(group, columns=headers, show="headings", height=min(6, len(rows) + 1))
            tree.pack(fill="x", expand=True)

            for h in headers:
                tree.heading(h, text=h)
                tree.column(h, width=100)

            for row in rows:
                tree.insert("", "end", values=row)

        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))

def add_to_table():
    """Open dialog to add a record to a selected table."""
    dialog = tk.Toplevel(root)
    dialog.title("Add Record to Table")
    dialog.geometry("500x400")
    dialog.resizable(True, True)

    tk.Label(dialog, text="Select Table:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        return

    if not tables:
        messagebox.showinfo("Info", "No tables found in the database.")
        dialog.destroy()
        return

    table_var = tk.StringVar(value=tables[0])
    dropdown = ttk.Combobox(dialog, textvariable=table_var, values=tables, state="readonly", width=40)
    dropdown.pack(padx=10, pady=10)

    tk.Label(dialog, text="Enter Values (comma-separated):", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    attr_label = tk.Label(dialog, text="", justify="left", font=("Arial", 9))
    attr_label.pack(anchor="w", padx=10, pady=5)

    fields_frame = tk.Frame(dialog)
    fields_frame.pack(fill="x", padx=10, pady=5)
    entry_widgets = {} 

    def show_table_attributes(event=None):
        """Populate attr_label and fields_frame for the selected table.
        Clears previous widgets first so nothing stacks up."""
        table_name = table_var.get()
        attr_label.config(text="")
        for w in fields_frame.winfo_children():
            w.destroy()
        entry_widgets.clear()

        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()   
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
            return

        attr_lines = []
        for col in columns:
            cid, name, coltype, notnull, dflt, pk = col
            flags = []
            if pk: flags.append("PK")
            if notnull: flags.append("NOT NULL")
            if dflt is not None: flags.append(f"default={dflt}")
            attr_lines.append(f"{name} {coltype} {' '.join(flags)}".strip())
        attr_label.config(text="\n".join(attr_lines))

    dropdown.bind("<<ComboboxSelected>>", show_table_attributes)
    show_table_attributes()

    values_entry = tk.Entry(dialog, width=50)
    values_entry.pack(anchor="w", padx=10, pady=5)

    def insert_record():
        table_name = table_var.get()
        values = values_entry.get().strip()
        

        if not values:
            messagebox.showerror("Error", "Values cannot be empty.")
            return

        sql = f"INSERT INTO {table_name} VALUES ({values});"
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Record added to '{table_name}' successfully.")
            dialog.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    tk.Button(dialog, text="Add Record", command=insert_record).pack(pady=10)

def remove_to_table():
    """Open dialog to remove a record to a selected table."""
    dialog = tk.Toplevel(root)
    dialog.title("Delete Record to Table")
    dialog.geometry("500x400")
    dialog.resizable(True, True)

    tk.Label(dialog, text="Select Table:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        return

    if not tables:
        messagebox.showinfo("Info", "No tables found in the database.")
        dialog.destroy()
        return

    table_var = tk.StringVar(value=tables[0])
    dropdown = ttk.Combobox(dialog, textvariable=table_var, values=tables, state="readonly", width=40)
    dropdown.pack(padx=10, pady=10)

    tk.Label(dialog, text="Enter the Primary Key of the record you wish to delete (comma-separated):", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    attr_label = tk.Label(dialog, text="", justify="left", font=("Arial", 9))
    attr_label.pack(anchor="w", padx=10, pady=5)

    fields_frame = tk.Frame(dialog)
    fields_frame.pack(fill="x", padx=10, pady=5)
    entry_widgets = {} 

    def show_table_attributes(event=None):
        """Populate attr_label and fields_frame for the selected table.
        Clears previous widgets first so nothing stacks up."""
        table_name = table_var.get()
        attr_label.config(text="")
        for w in fields_frame.winfo_children():
            w.destroy()
        entry_widgets.clear()

        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()   
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
            return

        attr_lines = []
        for col in columns:
            cid, name, coltype, notnull, dflt, pk = col
            flags = []
            if pk: flags.append("PK")
            if notnull: flags.append("NOT NULL")
            if dflt is not None: flags.append(f"default={dflt}")
            attr_lines.append(f"{name} {coltype} {' '.join(flags)}".strip())
        attr_label.config(text="\n".join(attr_lines))

    dropdown.bind("<<ComboboxSelected>>", show_table_attributes)
    show_table_attributes()

    values_entry = tk.Entry(dialog, width=50)
    values_entry.pack(anchor="w", padx=10, pady=5)

    def delete_record():
        table_name = table_var.get()
        values = values_entry.get().strip()
        

        if not values:
            messagebox.showerror("Error", "Values cannot be empty.")
            return
        
        # Delete the appropriate record depending on the user's table and record selection
        if(table_name == "Hotel"):
            sql = f"DELETE FROM {table_name} WHERE HotelID = {values};"
        if(table_name == "Booking"):
            sql = f"DELETE FROM {table_name} WHERE BookingID = {values};"
        if(table_name == "Guest"):
            sql = f"DELETE FROM {table_name} WHERE GuestID = {values};"
        if(table_name == "HotelRoom"):
            sql = f"DELETE FROM {table_name} WHERE RoomNumber = {values};"
        if(table_name == "HotelService"):
            sql = f"DELETE FROM {table_name} WHERE ServiceID = {values};"
        if(table_name == "Staff"):
            sql = f"DELETE FROM {table_name} WHERE StaffID = {values};"
        if(table_name == "StaffHotelRoom"):
            list_of_values = values.split(",")
            sql = f"DELETE FROM {table_name} WHERE StaffID = {list_of_values[0]} AND RoomNumber = {list_of_values[1]};"
        if(table_name == "StaffHotelService"):
            list_of_values = values.split(",")
            sql = f"DELETE FROM {table_name} WHERE StaffID = {list_of_values[0]} AND ServiceID = {list_of_values[1]};"
        if(table_name == "Location"):
            sql = f"DELETE FROM {table_name} WHERE PostalCode = {values};"
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Record deleted from '{table_name}' successfully.")
            dialog.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    tk.Button(dialog, text="Delete Record", command=delete_record).pack(pady=10)

def update_to_table():
    """Open dialog to update a record to a selected table."""
    dialog = tk.Toplevel(root)
    dialog.title("Update Record to Table")
    dialog.geometry("500x400")
    dialog.resizable(True, True)

    tk.Label(dialog, text="Select Table:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        return

    if not tables:
        messagebox.showinfo("Info", "No tables found in the database.")
        dialog.destroy()
        return

    table_var = tk.StringVar(value=tables[0])
    dropdown = ttk.Combobox(dialog, textvariable=table_var, values=tables, state="readonly", width=40)
    dropdown.pack(padx=10, pady=10)

    tk.Label(dialog, text="Enter Values (comma-separated):", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    attr_label = tk.Label(dialog, text="", justify="left", font=("Arial", 9))
    attr_label.pack(anchor="w", padx=10, pady=5)

    fields_frame = tk.Frame(dialog)
    fields_frame.pack(fill="x", padx=10, pady=5)
    entry_widgets = {} 

    def show_table_attributes(event=None):
        """Populate attr_label and fields_frame for the selected table.
        Clears previous widgets first so nothing stacks up."""
        table_name = table_var.get()
        attr_label.config(text="")
        for w in fields_frame.winfo_children():
            w.destroy()
        entry_widgets.clear()

        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()   
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
            return

        attr_lines = []
        for col in columns:
            cid, name, coltype, notnull, dflt, pk = col
            flags = []
            if pk: flags.append("PK")
            if notnull: flags.append("NOT NULL")
            if dflt is not None: flags.append(f"default={dflt}")
            attr_lines.append(f"{name} {coltype} {' '.join(flags)}".strip())
        attr_label.config(text="\n".join(attr_lines))

    dropdown.bind("<<ComboboxSelected>>", show_table_attributes)
    show_table_attributes()

    values_entry = tk.Entry(dialog, width=50)
    values_entry.pack(anchor="w", padx=10, pady=5)

    def update_record():
        table_name = table_var.get()
        values = values_entry.get().strip()
        list_of_values = values.split(",")
        

        if not values:
            messagebox.showerror("Error", "Values cannot be empty.")
            return

        # Update the appropriate record depending on the user's table and record selection
        if(table_name == "Hotel"):
            sql = f"""UPDATE {table_name}
                    SET HotelName = '{list_of_values[1]}', PostalCode = '{list_of_values[2]}'
                    WHERE HotelID = {list_of_values[0]};"""

        if(table_name == "Booking"):
            sql = f"""UPDATE {table_name}
                    SET GuestID = '{list_of_values[1]}', RoomNumber = '{list_of_values[2]}', BookingStatus = '{list_of_values[3]}', LengthOfStay = '{list_of_values[4]}', PaymentMethod = '{list_of_values[5]}', BookingDate = '{list_of_values[6]}', Receptionist = '{list_of_values[7]}'
                    WHERE BookingID = {list_of_values[0]};"""
        if(table_name == "Guest"):
            sql = f"""UPDATE {table_name}
                    SET Name = '{list_of_values[1]}', PhoneNumber = '{list_of_values[2]}', Email = '{list_of_values[3]}', PostalCode = '{list_of_values[4]}'
                    WHERE GuestID = {list_of_values[0]};"""
        if(table_name == "HotelRoom"):
            sql = f"""UPDATE {table_name}
                    SET GuestID = '{list_of_values[1]}', Type = '{list_of_values[2]}', Price = '{list_of_values[3]}', Availability = '{list_of_values[4]}'
                    WHERE RoomNumber = {list_of_values[0]};"""
        if(table_name == "HotelService"):
            sql = f"""UPDATE {table_name}
                    SET RoomNumber = '{list_of_values[1]}', GuestID = '{list_of_values[2]}', ServiceName = '{list_of_values[3]}', Cost = '{list_of_values[4]}', ServiceDescription = '{list_of_values[5]}'
                    WHERE ServiceID = {list_of_values[0]};"""
        if(table_name == "Staff"):
            sql = f"""UPDATE {table_name}
                    SET HotelID = '{list_of_values[1]}', Name = '{list_of_values[2]}', PhoneNumber = '{list_of_values[3]}', EmployeePosition = '{list_of_values[4]}', Salary = '{list_of_values[5]}', Schedule = '{list_of_values[6]}'
                    WHERE StaffID = {list_of_values[0]};"""
        if(table_name == "StaffHotelRoom"):
            sql = f"""UPDATE {table_name}
                    SET InteractionDate = '{list_of_values[2]}', Details = '{list_of_values[3]}'
                    WHERE StaffID = {list_of_values[0]} AND RoomNumber = {list_of_values[1]};"""
        if(table_name == "StaffHotelService"):
            sql = f"""UPDATE {table_name}
                    SET ServiceDate = '{list_of_values[2]}', ServiceDetail = '{list_of_values[3]}'
                    WHERE StaffID = {list_of_values[0]} AND ServiceID = {list_of_values[1]};"""
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Record added to '{table_name}' successfully.")
            dialog.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    tk.Button(dialog, text="Update Record", command=update_record).pack(pady=10)

def search_to_table():
    """Open dialog to search a record to a selected table."""
    dialog = tk.Toplevel(root)
    dialog.title("Search Record to Table")
    dialog.geometry("500x400")
    dialog.resizable(True, True)

    tk.Label(dialog, text="Select Table:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        return

    if not tables:
        messagebox.showinfo("Info", "No tables found in the database.")
        dialog.destroy()
        return

    table_var = tk.StringVar(value=tables[0])
    dropdown = ttk.Combobox(dialog, textvariable=table_var, values=tables, state="readonly", width=40)
    dropdown.pack(padx=10, pady=10)

    tk.Label(dialog, text="Enter the Primary Key of the record you wish to search for (comma-separated):", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)

    attr_label = tk.Label(dialog, text="", justify="left", font=("Arial", 9))
    attr_label.pack(anchor="w", padx=10, pady=5)

    fields_frame = tk.Frame(dialog)
    fields_frame.pack(fill="x", padx=10, pady=5)
    entry_widgets = {} 

    def show_table_attributes(event=None):
        """Populate attr_label and fields_frame for the selected table.
        Clears previous widgets first so nothing stacks up."""
        table_name = table_var.get()
        attr_label.config(text="")
        for w in fields_frame.winfo_children():
            w.destroy()
        entry_widgets.clear()

        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()   
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
            return

        attr_lines = []
        for col in columns:
            cid, name, coltype, notnull, dflt, pk = col
            flags = []
            if pk: flags.append("PK")
            if notnull: flags.append("NOT NULL")
            if dflt is not None: flags.append(f"default={dflt}")
            attr_lines.append(f"{name} {coltype} {' '.join(flags)}".strip())
        attr_label.config(text="\n".join(attr_lines))

    dropdown.bind("<<ComboboxSelected>>", show_table_attributes)
    show_table_attributes()

    values_entry = tk.Entry(dialog, width=50)
    values_entry.pack(anchor="w", padx=10, pady=5)

    def search_record():
        table_name = table_var.get()
        values = values_entry.get().strip()
        

        if not values:
            messagebox.showerror("Error", "Values cannot be empty.")
            return
        
        # Search for the appropriate record depending on the user's table and record selection
        if(table_name == "Hotel"):
            sql = f"SELECT * FROM {table_name} WHERE HotelID = '{values}';"
        if(table_name == "Booking"):
            sql = f"SELECT * FROM {table_name} WHERE BookingID = '{values}';"
        if(table_name == "Guest"):
            sql = f"SELECT * FROM {table_name} WHERE GuestID = '{values}';"
        if(table_name == "HotelRoom"):
            sql = f"SELECT * FROM {table_name} WHERE RoomNumber = '{values}';"
        if(table_name == "HotelService"):
            sql = f"SELECT * FROM {table_name} WHERE ServiceID = '{values}';"
        if(table_name == "Staff"):
            sql = f"SELECT * FROM {table_name} WHERE StaffID = '{values}';"
        if(table_name == "StaffHotelRoom"):
            list_of_values = values.split(",")
            sql = f"SELECT * FROM {table_name} WHERE StaffID = '{list_of_values[0]}' AND RoomNumber = '{list_of_values[1]}';"
        if(table_name == "StaffHotelService"):
            list_of_values = values.split(",")
            sql = f"SELECT * FROM {table_name} WHERE StaffID = '{list_of_values[0]}' AND ServiceID = '{list_of_values[1]}';"
        if(table_name == "Location"):
            sql = f"SELECT * FROM {table_name} WHERE PostalCode = '{values}';"
        
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]
            group = tk.Frame(result_frame)
            group.pack(fill="x", padx=10, pady=10)
            tk.Label(group, text=table_name, font=("Arial", 12, "bold")).pack(anchor="w")
            tree = ttk.Treeview(group, columns=headers, show="headings", height=min(6, len(rows) + 1))
            tree.pack(fill="x", expand=True)
            for h in headers:
                tree.heading(h, text=h)
            tree.column(h, width=100)
            for row in rows:
                tree.insert("", "end", values=row)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    tk.Button(dialog, text="Search Record", command=search_record).pack(pady=10)

root = tk.Tk()
root.title("Hotel Database Manager")
root.geometry("800x600")

# All Buttons on the exe
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Clear Results", command=clear_results).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="See All Tables", command=see_tables).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Run Queries", command=run_queries).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Drop Tables", command=drop_tables).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Create Tables", command=create_tables).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Populate Tables", command=populate_tables).grid(row=1, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Add Custom Table", command=add_custom_table).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Delete Table", command=delete_table).grid(row=2, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Add Record Table", command=add_to_table).grid(row=2, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Delete Record Table", command=remove_to_table).grid(row=3, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Update Record Table", command=update_to_table).grid(row=3, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Search Record Table", command=search_to_table).grid(row=3, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Exit", command=root.quit).grid(row=4, column=1, padx=5, pady=5)

# UI for controls
result_container = tk.Frame(root)
result_container.pack(fill="both", expand=True)

canvas = tk.Canvas(result_container, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(result_container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

result_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=result_frame, anchor="nw")

def on_frame_config(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

result_frame.bind("<Configure>", on_frame_config)

def on_canvas_resize(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas_window = canvas.create_window((0, 0), window=result_frame, anchor="nw")
canvas.bind("<Configure>", on_canvas_resize)


root.mainloop()

