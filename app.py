from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Dhaka, Bangladesh",
    "salary": 'BDT. 10,00,00'
  },
  {
    "id": 2,
    "title": "Flutter Developer",
    "location": "Dhaka, Bangladesh",
  },
  {
    "id": 3,
    "title": "Data Engnieer",
    "location": "Dhaka, Bangladesh",
    "salary": 'BDT. 9,00,00'
  },
  {
    "id": 4,
    "title": "Frontend Engnieer",
    "location": "Remote",
    "salary": 'BDT. 7,00,00'
  },
]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, companyname="Geonics")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
