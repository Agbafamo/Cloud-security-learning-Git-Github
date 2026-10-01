#user_password = "password123" 

#secure_password = user_password.replace("password123", "[REDACTED]")

#print(f"User password is: {secure_password}")

#email = "admin@example.com"

#if email.find("@") !=-1:
#    print("Valid email address")

# Password = input("Enter password:")

# if len(Password) < 8:
#     print("Password must be at least 8 characters long.")
# elif Password.isalnum() == True:
#     print("Password must contain at least one letter and one number.")
# else:
#     print("Password is valid.")

# user_password = "password123"

# Password = input("Enter password:")

# if Password == user_password:
#     print("Access granted.")
# else:
#     print("Access denied.")

# server = ["server1", "server2", "server3"]

# for Servers in server:
#     print(f"Connecting to {Servers}...")

# numbers = ""

# user_input = input("Enter a positive number:")

# while not user_input.isdigit() or int(user_input) <= 0:
#     user_input = input("Invalid input. Please enter a positive number:")

#     if user_input == "Done":
#         break

# login_attempt = [1, 2, 3, 5, 6, 7, 9, 8, 10, 12, 32, 45,]

# high_activity_days = [attempt for attempt in login_attempt if attempt >=10]
# print("High Activity Days:", high_activity_days)

# user_info = {
#     "username": "admin",
#     "password": "lesoto123",
#     "last_login": "2023-06-01",
#     "Website": "www.example.com"
# }

# for key, value in user_info.items():
#     print(f"{key}: {value}")

# Nested dictionary for user credentials
# user_credentials = {
#     "admin": {"password": "lesoto123", "last_login": "2023-06-01"},
#     "user1": {"password": "user123", "last_login": "2023-06-02"},
# }

# print(user_credentials ["user1"]["password"])

set1 = {"192.168.1.1", "10.10.0.1"}

set2 = {"192.168.0.1", "10.10.0.1"}

# # common_ips = set1 | set2

# common_ips = set1 - set2
# print("Common IP addresses:", common_ips)

# logs = [
#     {"username": "admin", "ip": "192.168.1.1", "status": "success"},
#     {"username": "user1", "ip": "192.168.0.5", "status": "failure"},
#     {"username": "user2", "ip": "192.168.0.10", "status": "success"},
#     {"username": "alex", "ip": "192.168.101.0", "status": "failure"},
#     {"username": "bob", "ip": "192.168.100.1", "status": "success"},
#     {"username": "charlie", "ip": "192.168.102.1", "status": "success"},
#     {"username": "david", "ip": "192.168.103.1", "status": "failure"}
# ]

# unique_ips = {log["ip"] for log in logs}
# print("Unique IP addresses:", unique_ips)


# special_ip = "192.168.0.0"
# if special_ip in unique_ips:
#     print(f"Special IP {special_ip} found in logs.")
# else:
#     print(f"Special IP not found in logs.")


# #Number of failed login attempts

# logs = [
#     {"username": "admin", "ip": "192.168.1.1", "status": "success"},
#     {"username": "user1", "ip": "192.168.0.5", "status": "failure"},
#     {"username": "user2", "ip": "192.168.0.10", "status": "success"},
#     {"username": "alex", "ip": "192.168.101.0", "status": "failure"},
#     {"username": "bob", "ip": "192.168.100.1", "status": "success"},
#     {"username": "charlie", "ip": "192.168.102.1", "status": "success"},
#     {"username": "david", "ip": "192.168.103.1", "status": "failure"},
#     {"username": "admin", "ip": "192.168.1.1", "status": "success"},
#     {"username": "user1", "ip": "192.168.0.5", "status": "failure"},
#     {"username": "alex", "ip": "192.168.101.0", "status": "failure"}
# ]


# failed_attempts ={}


# for log in logs:
#     if log["status"] == "failure":
#         username =log["username"]
#         if username not in failed_attempts:
#             failed_attempts[username] = 0
#         failed_attempts[username] += 1
# print("Failed login attempts per user:" , failed_attempts)


****Basic Authentication System****

