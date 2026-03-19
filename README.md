# 🚀 Binance Futures Testnet Trading Bot

A robust, CLI-based trading bot designed for executing orders on the **Binance Futures Testnet**. This tool provides a safe environment for testing trading strategies with real-time market data without risking actual capital.

---

## ✨ Features

- 💹 **Binance Futures Support**: Specialized for futures trading.
- 🧪 **Testnet Integration**: Uses the Binance Testnet environment by default.
- 🛠️ **Multiple Order Types**: Support for both `MARKET` and `LIMIT` orders.
- ✅ **Input Validation**: Strict validation for symbols, order sides, types, quantities, and prices.
- 📝 **Detailed Logging**: Comprehensive logs for every action and API response.
- ⚙️ **Configurable**: Easy setup using environment variables.

---

## 📋 Prerequisites

Before you begin, ensure you have:
- **Python 3.8+** installed.
- A **Binance Testnet Account** (API Key & Secret). 
  - [Get them here](https://testnet.binancefuture.com/)

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/BinanceTradingBot.git
   cd BinanceTradingBot
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

1. Create a `.env` file in the root directory:
   ```bash
   # Windows (CMD)
   echo API_KEY=your_api_key_here > .env
   echo API_SECRET=your_api_secret_here >> .env
   
   # Linux/macOS or PowerShell
   touch .env
   ```

2. Add your Binance Testnet API credentials to `.env`:
   ```env
   API_KEY=your_binance_testnet_api_key
   API_SECRET=your_binance_testnet_api_secret
   ```

---

## 🚀 Usage

Run the bot using the command line with the following arguments:

### 📈 Market Order (Buy)
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### 📉 Limit Order (Sell)
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --qty 0.1 --price 2500
```

### 🔍 Command Line Arguments
| Argument | Type | Description |
| :--- | :--- | :--- |
| `--symbol` | `str` | Trading pair (e.g., `BTCUSDT`, `ETHUSDT`) |
| `--side` | `str` | Order side: `BUY` or `SELL` |
| `--type` | `str` | Order type: `MARKET` or `LIMIT` |
| `--qty` | `float`| Quantity to trade |
| `--price` | `float`| Required only for `LIMIT` orders |

---

## 📂 Project Structure

```text
BinanceTradingBot/
├── bot/
│   ├── client.py        # Binance API client initialization
│   ├── logging_config.py # Logger setup
│   ├── orders.py        # Order execution logic
│   └── validators.py    # Input validation rules
├── .env                 # Environment variables (API Keys)
├── cli.py               # Main entry point (CLI)
├── config.py            # Configuration loader
├── requirements.txt     # Project dependencies
└── trading_bot.log      # Runtime logs
```

---

## 📜 Logging

The bot logs all activities to `trading_bot.log`. This includes:
- Order requests sent to Binance.
- Successful order confirmations with `Order ID`, `Status`, and `Executed Qty`.
- API errors and validation failures.

---

## ⚠️ Disclaimer

This bot is for **educational and testing purposes only**. Always test your strategies on the Testnet before moving to a live production environment. The authors are not responsible for any financial losses.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

**Happy Trading! 💹**
