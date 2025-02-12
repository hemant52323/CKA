from flask import Flask
import calendar
from datetime import date

app = Flask(__name__)

@app.route('/')
def show_calendar():
    dat = date.today()
    year_cur = dat.year
    month_cur = dat.month
    cal = calendar.month(year_cur, month_cur)
    return f"<pre>{cal}</pre>"  # Use <pre> to format the text properly

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

