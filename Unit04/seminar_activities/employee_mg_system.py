from datetime import date, timedelta
from typing import Dict, List, Optional

class Employee:
    """Class to represent an employee and their leave details."""

    def __init__(self, employee_id: str, name: str, email: str,
                 department: str, salary: float, hire_date: date):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        self.hire_date = hire_date
        self.annual_leave_days = 20  # Standard annual leave days
        self.leave_balance = 20

    def get_details(self) -> str:
        """Return employee details as a formatted string."""
        return (f"Employee ID: {self.employee_id}\n"
                f"Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Department: {self.department}\n"
                f"Salary: ${self.salary:,.2f}\n"
                f"Hire Date: {self.hire_date}\n"
                f"Leave Balance: {self.leave_balance} days")

    def update_details(self, name: str = None, email: str = None,
                      department: str = None, salary: float = None) -> None:
        """Update employee details."""
        if name:
            self.name = name
        if email:
            self.email = email
        if department:
            self.department = department
        if salary:
            self.salary = salary

    def get_leave_balance(self) -> int:
        """Return current leave balance."""
        return self.leave_balance

    def deduct_leave(self, days: int) -> bool:
        """Deduct leave days from balance."""
        if days <= self.leave_balance:
            self.leave_balance -= days
            return True
        return False

    def restore_leave(self, days: int) -> None:
        """Restore leave days to balance (for rejected/cancelled requests)."""
        self.leave_balance = min(self.leave_balance + days, self.annual_leave_days)


class LeaveRequest:
    """Class to represent a leave request."""

    def __init__(self, request_id: str, employee_id: str,
                 start_date: date, end_date: date):
        self.request_id = request_id
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.num_days = self.calculate_days()
        self.status = "Pending"  # Status: Pending, Approved, Rejected
        self.request_date = date.today()

    def calculate_days(self) -> int:
        """Calculate number of leave days (excluding weekends)."""
        days = 0
        current = self.start_date
        while current <= self.end_date:
            # Monday = 0, Sunday = 6
            if current.weekday() < 5:  # Monday to Friday
                days += 1
            current += timedelta(days=1)
        return days

    def get_request_details(self) -> str:
        """Return leave request details as a formatted string."""
        return (f"Request ID: {self.request_id}\n"
                f"Employee ID: {self.employee_id}\n"
                f"Start Date: {self.start_date}\n"
                f"End Date: {self.end_date}\n"
                f"Number of Days: {self.num_days}\n"
                f"Status: {self.status}\n"
                f"Request Date: {self.request_date}")

    def get_status(self) -> str:
        """Return the current status of the request."""
        return self.status

    def update_status(self, status: str) -> None:
        """Update the status of the request."""
        if status in ["Pending", "Approved", "Rejected"]:
            self.status = status


class LeaveManager:
    """Class to manage leave requests for employees."""

    def __init__(self):
        self.leave_requests: Dict[str, LeaveRequest] = {}
        self.request_counter = 0

    def book_leave(self, employee: Employee, start_date: date,
                   end_date: date) -> Optional[str]:
        """Book leave for an employee. Returns request ID if successful."""
        if not self.validate_leave_dates(employee, start_date, end_date):
            return None

        self.request_counter += 1
        request_id = f"LR{self.request_counter:05d}"
        leave_request = LeaveRequest(request_id, employee.employee_id,
                                     start_date, end_date)

        if employee.deduct_leave(leave_request.num_days):
            leave_request.update_status("Approved")
            self.leave_requests[request_id] = leave_request
            return request_id
        else:
            return None

    def approve_leave(self, request_id: str) -> bool:
        """Approve a pending leave request."""
        if request_id in self.leave_requests:
            request = self.leave_requests[request_id]
            if request.status == "Pending":
                request.update_status("Approved")
                return True
        return False

    def reject_leave(self, request_id: str, employee: Employee) -> bool:
        """Reject a leave request and restore leave days."""
        if request_id in self.leave_requests:
            request = self.leave_requests[request_id]
            if request.status == "Pending" or request.status == "Approved":
                request.update_status("Rejected")
                employee.restore_leave(request.num_days)
                return True
        return False

    def get_employee_leaves(self, employee_id: str) -> List[LeaveRequest]:
        """Get all leave requests for a specific employee."""
        return [req for req in self.leave_requests.values()
                if req.employee_id == employee_id]

    def validate_leave_dates(self, employee: Employee, start_date: date,
                            end_date: date) -> bool:
        """Validate leave dates."""
        # Check if start date is before end date
        if start_date > end_date:
            print("Error: Start date cannot be after end date.")
            return False

        # Check if dates are in the future
        if start_date < date.today():
            print("Error: Leave dates must be in the future.")
            return False

        # Check if employee has sufficient leave balance
        temp_request = LeaveRequest("temp", employee.employee_id,
                                   start_date, end_date)
        if temp_request.num_days > employee.get_leave_balance():
            print(f"Error: Insufficient leave balance. Required: {temp_request.num_days}, "
                  f"Available: {employee.get_leave_balance()}")
            return False

        return True


class EmployeeDatabase:
    """Class to manage employee records."""

    def __init__(self):
        self.employees: Dict[str, Employee] = {}
        self.employee_counter = 0

    def add_employee(self, name: str, email: str, department: str,
                    salary: float, hire_date: date) -> str:
        """Add a new employee and return their employee ID."""
        self.employee_counter += 1
        employee_id = f"EMP{self.employee_counter:04d}"
        employee = Employee(employee_id, name, email, department,
                          salary, hire_date)
        self.employees[employee_id] = employee
        return employee_id

    def get_employee(self, employee_id: str) -> Optional[Employee]:
        """Get an employee by ID."""
        return self.employees.get(employee_id)

    def update_employee(self, employee_id: str, **kwargs) -> bool:
        """Update employee details."""
        if employee_id in self.employees:
            self.employees[employee_id].update_details(**kwargs)
            return True
        return False

    def delete_employee(self, employee_id: str) -> bool:
        """Delete an employee."""
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False

    def list_all_employees(self) -> List[Employee]:
        """Return a list of all employees."""
        return list(self.employees.values())


# Example usage and demonstration
if __name__ == "__main__":
    # Initialize systems
    db = EmployeeDatabase()
    leave_mgr = LeaveManager()

    # Add employees
    emp1_id = db.add_employee("Alice Johnson", "alice@company.com",
                              "Engineering", 75000, date(2020, 1, 15))
    emp2_id = db.add_employee("Bob Smith", "bob@company.com",
                              "Marketing", 65000, date(2021, 3, 20))
    emp3_id = db.add_employee("Carol Davis", "carol@company.com",
                              "HR", 70000, date(2019, 6, 10))

    print("=" * 60)
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 60)

    # Display employee details
    print("\n--- Employee Details ---")
    for emp_id in [emp1_id, emp2_id, emp3_id]:
        emp = db.get_employee(emp_id)
        print(f"\n{emp.get_details()}\n")

    # Book leave for Alice
    print("--- Booking Leave ---")
    req1 = leave_mgr.book_leave(db.get_employee(emp1_id),
                                date(2025, 11, 3), date(2025, 11, 7))
    if req1:
        print(f"Leave booked successfully: {req1}")
        print(f"Remaining balance: {db.get_employee(emp1_id).get_leave_balance()} days\n")

    # Try to book leave with insufficient balance
    print("--- Attempting to book excessive leave ---")
    req2 = leave_mgr.book_leave(db.get_employee(emp1_id),
                                date(2025, 12, 1), date(2025, 12, 31))
    if not req2:
        print("Leave booking failed due to insufficient balance.\n")

    # Display leave request details
    print("--- Leave Request Details ---")
    for leave_req in leave_mgr.get_employee_leaves(emp1_id):
        print(f"\n{leave_req.get_request_details()}\n")

    # Update employee details
    print("--- Updating Employee Details ---")
    db.update_employee(emp2_id, department="Sales", salary=72000)
    print(f"Updated {emp2_id}:")
    print(f"{db.get_employee(emp2_id).get_details()}\n")
