

from flask import Flask, request, render_template_string
import time

app = Flask(__name__)

def pattern_search(txt, pat):

    m = len(txt)
    n = len(pat)

    for i in range(m):

        if txt[i:n+i] == pat:
            return i

    return -1

html = """

<!DOCTYPE html>

<html>

<head>

<title>Pattern Search</title>

<style>

body{
background:#f2f2f2;
font-family:Arial;
text-align:center;
padding:50px;
}

.box{
width:500px;
margin:auto;
background:white;
padding:30px;
border-radius:10px;
box-shadow:0px 0px 10px gray;
}

input{
width:90%;
padding:10px;
margin:10px;
}

button{
padding:10px 20px;
background:blue;
color:white;
border:none;
border-radius:5px;
}

</style>

</head>

<body>

<div class="box">

<h2>Pattern Searching Web App</h2>

<form method="POST">

<input
type="text"
name="text"
placeholder="Enter Text"
required>

<br>

<input
type="text"
name="pattern"
placeholder="Enter Pattern"
required>

<br>

<button type="submit">

Search

</button>

</form>

{% if result != None %}

<hr>

<h3>
Pattern Position :
{{result}}
</h3>

<h3>
Execution Time :
{{exec_time}}
</h3>

<h3>
Text Length :
{{txtlen}}
</h3>

<h3>
Pattern Length :
{{patlen}}
</h3>

{% endif %}

</div>

</body>

</html>

"""

@app.route(
"/",
methods=["GET","POST"]
)

def home():

    result=None
    exec_time=None
    txtlen=None
    patlen=None

    if request.method=="POST":

        txt=request.form["text"]

        pat=request.form["pattern"]

        start=time.time()

        result=pattern_search(
        txt,
        pat
        )

        end=time.time()

        exec_time=round(
        end-start,
        8
        )

        txtlen=len(txt)

        patlen=len(pat)

    return render_template_string(
    html,
    result=result,
    exec_time=exec_time,
    txtlen=txtlen,
    patlen=patlen
    )

app = app

