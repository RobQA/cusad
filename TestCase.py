class TestCase:
    def __init__(self, test_case_name, test_steps, assertion):
        self.test_case_name = test_case_name
        self.test_steps = test_steps

    def run(self):
        print("Test: " + self.test_case_name + " is running")
        for step in self.test_steps:
            func = step['func']
            args = step['args']
            if args is None:
                func()
            else:
                func(*args)

        print("Test: " + self.test_case_name + " completed successfully")