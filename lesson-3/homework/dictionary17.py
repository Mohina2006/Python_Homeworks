nested_dict = {
    "student1": {
        "name": "Mohina",
        "age": 18,
        "subjects": ["AI", "Robotics"]
    },
    "student2": {
        "name": "John",
        "age": 20,
        "subjects": ["Math", "Physics"]
    }
}
student_name = nested_dict["student1"]["name"]
print(student_name)
