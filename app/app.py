from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
visits = Counter('webapp_visits_total', 'Total visits to the homepage')

@app.route("/")
def hello():
    visits.inc()
    return "Hello, Prometheus!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
