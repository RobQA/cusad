class TestGroup:
    def __init__(self, test_group_name, test_cases):
        print("Test: " + test_group_name + " is running")
        for test_case in test_cases:
            test_case.run()
        print("Test: " + test_group_name + " completed successfully")

