from flask import Flask, render_template, request, redirect, url_for

import requests
from requests.exceptions import HTTPError

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

@app.route('/query',methods=["POST","GET"])
def queryDictionary():
    if request.method=="POST":
        queryWord = request.form["q"]
        try:
                response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+queryWord)
                response.raise_for_status()
    		# access JSOn content
                jsonResponse = response.json()[0]
                
                word = jsonResponse["word"]
                
                meaning = jsonResponse["meanings"][0]
                
                define = meaning["definitions"][0]["definition"]
                
                pronunciation = jsonResponse["phonetic"]
                
                wordType= meaning["partOfSpeech"]
                
                return render_template("result.html", content=define,word=word,type=wordType,pron=pronunciation)

        except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
        except Exception as err:
                print(f'Other error occurred: {err}')
    else:
    	return render_template("query.html")

@app.route("/result/<word>/<pronunciation>/<wordType>/<define>")
def result(word,pronunciation,define,wordType):
	return render_template("result.html", content=define,word=word,type=wordType,pron=pronunciation)

if __name__ == "__main__":
	app.run(debug=False)