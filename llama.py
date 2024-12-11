# llama.py

class Llama2:
    @staticmethod
    def get_employee_position(employee_id):
        # Mock data retrieval from Llama 2
        employees = {
            1: 'X',
            2: 'Y',
            3: 'Z'
        }
        return employees.get(employee_id, None)

class Llama3:
    @staticmethod
    def get_leave_data(employee_id):
        # Mock data retrieval from Llama 3
        employees_leave_data = {
            1: {'totalLeaves': 10, 'usedLeaves': 4},
            2: {'totalLeaves': 12, 'usedLeaves': 5},
            3: {'totalLeaves': 8, 'usedLeaves': 2}
        }
        return employees_leave_data.get(employee_id, None)
