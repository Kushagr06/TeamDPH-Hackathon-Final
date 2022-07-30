from flask import Flask, redirect,render_template,request, url_for
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

#ignore ssl certifications
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def getinfo(keys):
  url='https://api.test.esamudaay.com/api/v1/businesses/'+keys+'/report'

  html = urllib.request.urlopen(url, context=ctx).read()

  soup = BeautifulSoup(html, 'html.parser')
# Retrieve all the info
  maintext=soup.prettify()
  info=json.loads(maintext)
  return info




app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
  if request.method=='POST':
    ans=request.form['id']
    print(ans)
    return redirect(url_for('post_result',ans=ans))
  return render_template('index.html')

@app.route("/result")
def post_result():
  ans=request.args.get('ans',None)
  print(ans)
  info= getinfo(ans)
  print(info)  
  return render_template('result.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)