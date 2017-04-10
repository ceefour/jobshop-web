from flask import Flask, render_template, flash, redirect, request, url_for
import subprocess
import os

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/")
def home():
    return render_template('home.html')
    #return "Hello World!"

@app.route("/jobshop", methods=['POST'])
def jobshop():
    # Windows
    # workdir = 'E:/project_amanah/S3/model-simulasi/SIMLIB'
    # command = 'E:/project_amanah/S3/model-simulasi/SIMLIB/jobshop.exe'
    # in_fname = 'E:/project_amanah/S3/model-simulasi/SIMLIB/jobshop.in'
    # outfile = 'E:/project_amanah/S3/model-simulasi/SIMLIB/jobshop.out'
    srcdir = os.path.dirname(os.path.abspath(__file__))
    workdir = srcdir + '/jobshop'
    command = workdir + '/jobshop.exe' if os.name == 'nt' else workdir + '/jobshop'
    in_fname = workdir + '/jobshop.in'
    outfile = workdir + '/jobshop.out'

    # check if the post request has the file part
    if 'infile' not in request.files:
        flash('Input file is required')
        return redirect(url_for('home'))
    file = request.files['infile']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('Input file is required')
        return redirect(url_for('home'))

    if file:
        file.save(in_fname)

        process = subprocess.Popen(command, cwd=workdir, shell=False, stdout=subprocess.PIPE)
        for line in process.stdout:
            print line
        process.wait()

        with open (outfile, "r") as myfile:
            jobshop_out = myfile.read()

        return render_template('jobshop.html', jobshop_out=jobshop_out)
    else:
        return "Unknown error"

if __name__ == "__main__":
    app.run()
