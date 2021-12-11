from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
word= " "
define=""
pronunciation=""
wordType=""
@app.route('/',methods=["POST","GET"])
def makeWord():
    if request.method=="POST":
        word = request.form["w"]
        define = request.form["define"]
        pronunciation = request.form["sound"]
        wordType= request.form["type"]
        return redirect(url_for("result", word=word,pronunciation=pronunciation,define=define,wordType=wordType))
    else:
    	return render_template("index.html")
@app.route("/result/<word>/<pronunciation>/<wordType>/<define>")
def result(word,pronunciation,define,wordType):
	return render_template("result.html", content=define,word=word,type=wordType,pron=pronunciation)

if __name__ == "__main__":
	app.run(debug=True)