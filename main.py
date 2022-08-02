from flask import Flask, render_template, request
import bot

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def form():
    link = request.form['link']
    productCount = request.form['productCount']
    excelFileName = request.form['excelFileName']
    
    bot.getProductsCode(link,productCount,excelFileName)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)