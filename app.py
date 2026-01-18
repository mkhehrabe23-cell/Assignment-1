from flask import Flask, request, render_template_string
import pandas as pd
import numpy as np
import re, smtplib
from email.message import EmailMessage

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>TOPSIS Web Service</title>
</head>
<body>
    <h2>TOPSIS Web Service</h2>
    <form method="POST" enctype="multipart/form-data">
        <label>File Name:</label>
        <input type="file" name="file" required><br><br>

        <label>Weights:</label>
        <input type="text" name="weights" placeholder="1,1,1,1" required><br><br>

        <label>Impacts:</label>
        <input type="text" name="impacts" placeholder="+,+,-,+" required><br><br>

        <label>Email ID:</label>
        <input type="email" name="email" required><br><br>

        <button type="submit">Submit</button>
    </form>
    <p style="color:red;">{{ message }}</p>
</body>
</html>
"""

def run_topsis(input_file, weights, impacts, output_file):
    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        raise Exception("Input file must have at least 3 columns")

    data = df.iloc[:, 1:]

    # Numeric check (FIXED)
    if not np.all(np.isfinite(data.values)):
        raise Exception("Criteria columns must be numeric")

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise Exception("Weights and impacts count must match criteria")

    for i in impacts:
        if i not in ["+", "-"]:
            raise Exception("Impacts must be + or -")

    norm = data / np.sqrt((data ** 2).sum(axis=0))

    weighted = norm * weights

    ideal_best, ideal_worst = [], []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    d_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = d_neg / (d_pos + d_neg)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)

def send_email(to_email, file_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "yourgmail@gmail.com"
    msg["To"] = to_email
    msg.set_content("Please find attached the TOPSIS result file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("yourgmail@gmail.com", "YOUR_APP_PASSWORD")
        server.send_message(msg)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]


        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return render_template_string(HTML_FORM, message="Invalid Email ID")

        if len(weights.split(",")) != len(impacts.split(",")):
            return render_template_string(
                HTML_FORM,
                message="Weights and impacts count must be equal"
            )

        input_path = "input.csv"
        output_path = "result.csv"

        file.save(input_path)

        try:
            run_topsis(input_path, weights, impacts, output_path)
            send_email(email, output_path)
            message = "Result file sent successfully to your email!"
        except Exception as e:
            message = str(e)

    return render_template_string(HTML_FORM, message=message)

#
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
