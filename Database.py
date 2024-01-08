import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "2000140100890":
        {
            "name": "Shivam",
            "branch": "CS",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2024-01-05 00:54:34"
        },
    "2000140101230":
        {
            "name": "venus",
            "branch": "CS",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2024-01-05 00:54:34"
        },
    "963852":
        {
            "name": "Arun",
            "branch": "Computer Science And Engineering",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-01-05 00:54:34"
        },
    "20001401001007":
        {
            "name": "tarun",
            "branch": "CS",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2024-01-05 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
