from app import app
from commands import hello, getCovidStats
# Start your app
if __name__ == "__main__":
    app.start(port=3000)