from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['debug'] = True

form = """
<!doctype html>


<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width 540px;
                height 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="rot">Rotate by:</label>
            <input name="rot" type="text" id="rot" value="0">
                <br><br>
            <textarea name="text">{0}</textarea>
            <input type ="submit">
        </form>
    </body>
</html>
"""        

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['post'])
def encrypt():
    text = str(request.form['text'])
    rot = int(request.form['rot'])
    
    encrypted = rotate_string(text, rot)
    #return "<h1>" + encrypted + "</h1>"
    return form.format(encrypted)

app.run()
    #store values of rot and text in local variables, converting data types as necessary.
    #encypt the value of the text parameter using rotate_string
    #return encrypted string in <h1> tags