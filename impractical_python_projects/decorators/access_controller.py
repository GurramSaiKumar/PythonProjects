def access_control_decorator(access_level):
    def decorator(func):
        def wrapper(user):
            if user.get("access_level") >= access_level:
                return func(user)
            else:
                return "Access Denied"
        return wrapper
    return decorator

# Define user data with access levels.
users = [
    {"name": "Alice", "access_level": 3},
    {"name": "Bob", "access_level": 1},
    {"name": "Charlie", "access_level": 5}
]

# Apply access control decorators for different access levels.
@access_control_decorator(3)
def view_sensitive_data(user):
    return "This is sensitive data."

@access_control_decorator(5)
def modify_data(user):
    return "Data modification is allowed."

# Test the access control decorators with different users.
for user in users:
    print(user["name"])
    print("View Data:", view_sensitive_data(user))
    print("Modify Data:", modify_data(user))
    print()
