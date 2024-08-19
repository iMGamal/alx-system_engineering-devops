import urllib.request
import urllib.parse
import json
import sys

def get_employee_name(employee_id):
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            with urllib.request.urlopen(url) as response:
                        response_data = response.read().decode('utf-8')
                                employee = json.loads(response_data)
                                        return employee.get('name')

                                    def get_todo_list(employee_id):
                                            url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
                                                with urllib.request.urlopen(url) as response:
                                                            response_data = response.read().decode('utf-8')
                                                                    todos = json.loads(response_data)
                                                                            return todos

                                                                        def main(employee_id):
                                                                                employee_name = get_employee_name(employee_id)
                                                                                    todos = get_todo_list(employee_id)

                                                                                        total_tasks = len(todos)
                                                                                            done_tasks = [todo for todo in todos if todo['completed']]
                                                                                                number_of_done_tasks = len(done_tasks)

                                                                                                    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
                                                                                                        for task in done_tasks:
                                                                                                                    print(f"\t {task['title']}")

                                                                                                                    if __name__ == "__main__":
                                                                                                                            if len(sys.argv) != 2:
                                                                                                                                        print("Usage: python script.py EMPLOYEE_ID")
                                                                                                                                                sys.exit(1)

                                                                                                                                                    try:
                                                                                                                                                                employee_id = int(sys.argv[1])
                                                                                                                                                    except ValueError:
                                                                                                                                                                print("EMPLOYEE_ID must be an integer")
                                                                                                                                                                        sys.exit(1)

                                                                                                                                                                            main(employee_id)
