from flask import Flask,render_template,request
from mysql.connector import connect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
verifyotp = "0"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/verify")
def verify():
    return render_template("verifyemail.html")

@app.route("/verify1",methods=["POST","GET"])
def verify1():
    otp = random.randint(1111,9999)
    global verifyotp
    verifyotp = str(otp)
    print(verifyotp)
    x = False
    if request.method == "POST":
        email = request.form['email']
        x = True
    if x:
        print("Sending Email")
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        mailusername = "saivardhan.thimmisetty@gmail.com"
        mailpassword = "xqmd vmwz ibqy ijii"
        from_email = "saivardhan.thimmisetty@gmail.com"
        to_email = email
        subject = 'OTP for Login'
        body = f"The OTP for verification is {otp}"

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(mailusername, mailpassword)
        server.send_message(msg)
        server.quit()
        print("email Sent")
        return render_template("enterotp.html",email = email)
    else:
        return "Try Again"
    

@app.route("/verifyotp1",methods=["POST","GET"])
def verifyotp1():
    print("Verification started")
    print(verifyotp)
    print(type(verifyotp))
    x = False
    if request.method == "POST":
        otp = request.form['otp']
        email = request.form['mail']
        print(email)
        x = True
    else:
        return "Error Occured"
    if x:
        if otp == verifyotp:
            return "Otp Validated"
        else:
            return "try again"
        
if __name__ == "__main__":
    app.run(port=5008)
