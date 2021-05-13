from flask import Flask, flash, render_template, request, redirect, send_file
import os
app = Flask(__name__, template_folder="uploadpage/")


@app.route("/", methods=["GET", "POST"])
def homepage():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        print()
        f = request.files['audiofile']
        if f.filename == '':
            redirect(request.url)
        if f.filename .split(".", 1)[1].lower() == "mp3":
            f.save(os.getcwd() + "/files/audiofile.mp3")

        txtfile = request.files['Textfile']
        if txtfile.filename == '':
            redirect(request.url)
        if txtfile.filename .split(".", 1)[1].lower() == "txt":
            txtfile.save(os.getcwd() + "/files/txtfile.txt")
        csv = open(os.getcwd() + "/files/result.csv", "wb")

        return send_file(csv, attachment_filename="result.csv", mimetype='text/csv')


if __name__ == "__main__":
    app.run(debug=True)
