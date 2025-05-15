my_dict = {"name": "Mohina","age": 18,"education": {"university": "New Uzbekistan University","major": "AI & Robotics"}}

has_nested = any(isinstance(val, dict) for val in my_dict.values())

print("Nested dictionary found!" if has_nested else "No nested dictionary found.")