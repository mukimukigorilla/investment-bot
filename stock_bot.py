import yfinance as yf

stocks = {
    "Rocket Lab": "RKLB",
    "AST SpaceMobile": "ASTS",
    "IonQ": "IONQ"
}

report = "🚀 AI投資レポート\n"
report += "=" * 40 + "\n\n"

for company, ticker in stocks.items():

    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")

    current = hist["Close"].iloc[-1]
    previous = hist["Close"].iloc[0]

    change = ((current - previous) / previous) * 100

    report += f"【{company}】\n"
    report += f"株価: ${current:.2f}\n"
    report += f"5日変化率: {change:.2f}%\n"

    if change > 10:
        report += "評価: 🔥非常に強い\n"
    elif change > 5:
        report += "評価: 📈上昇中\n"
    else:
        report += "評価: 👀様子見\n"

    report += "\n"

with open("investment_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print(report)
print("✅ investment_report.txt を作成しました")
