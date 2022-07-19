contacts = {
    "number": 4,
    "students": [
        {"name": "Sarah Holderness", "email": "sarah@example.com"},
        {"name": "Harry Potter", "email": "Harry@example.com"},
        {"name": "Hermione Granger", "email": "Hermione@example.com"},
        {"name": "Ron Weasley", "email": "Ron@example.com"},
    ],
}

for student in contacts["students"]:
    print(student["email"])
