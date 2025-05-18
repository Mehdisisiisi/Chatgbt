from flask import Flask, request, jsonify, render_template
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    symbol = request.args.get('symbol')
    market = request.args.get('market')

    try:
        data = yf.Ticker(symbol)
        hist = data.history(period='1d')
        price = hist['Close'].iloc[-1]
        recommendation = "شراء" if price % 2 == 0 else "انتظار"

        return jsonify({
            "symbol": symbol,
            "market": market,
            "price": round(price, 2),
            "recommendation": recommendation
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)