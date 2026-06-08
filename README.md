# 🚀 Solana Meme Coin Trading Bot

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Solana](https://img.shields.io/badge/Solana-Web3-9945FF.svg)](https://solana.com)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4.svg)](https://core.telegram.org/bots)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Automated trading bot for Solana meme coins. Monitors new token launches on **Raydium** and **Pump.fun** DEXes in real time, filters by liquidity and momentum criteria, and executes swaps via **Jupiter Aggregator** — all controlled through a full **Telegram control panel**.

---

## ✨ Features

- 🔍 **Real-time scanning** of new token launches on Raydium & Pump.fun
- 📊 **Smart filters** — liquidity, holder count, age, and price momentum
- ⚡ **Auto buy/sell** via Jupiter Aggregator (best on-chain price routing)
- 📱 **Full Telegram panel** — monitor positions, adjust settings, stop/start bot
- 🛡️ **Risk management** — per-trade SOL cap, daily loss limit, rug-pull detection
- 📈 **Live P&L tracking** — real-time profit/loss per token and daily summary
- 🔄 **24/7 ready** — runs on DigitalOcean / any Linux VPS with PM2

---

## 📱 Telegram Commands

| Command | Description |
|---------|-------------|
| `/start` | Start bot & show menu |
| `/status` | Running status + open positions |
| `/balance` | SOL wallet balance |
| `/pnl` | Profit/loss report |
| `/buy <token> <amount>` | Manual buy |
| `/sell <token>` | Manual sell |
| `/stop` | Pause auto-trading |
| `/settings` | View current config |

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.10+ (async) |
| Blockchain | Solana Web3.py + Solders |
| Swap routing | Jupiter Aggregator API v6 |
| Market data | DexScreener API |
| Bot control | python-telegram-bot v20 |
| Deployment | DigitalOcean + PM2 |

---

## 🚀 Quick Start

### 1. Clone & install

```bash
git clone https://github.com/fikrigoldbot/Solana-bot.git
cd Solana-bot
pip install -r requirements.txt
```

### 2. Configure

```bash
cp config.example.py config.py
# Edit config.py with your credentials
```

### 3. Run

```bash
# Development
python main.py

# Production (24/7 with PM2)
pm2 start main.py --interpreter python3 --name solana-bot
pm2 save
```

---

## ⚙️ Configuration

```python
# config.py
TELEGRAM_TOKEN    = "your_bot_token"        # from @BotFather
TELEGRAM_CHAT_ID  = "your_chat_id"          # from @userinfobot
WALLET_PRIVATE_KEY = "your_solana_key"      # base58 private key
RPC_URL           = "https://api.mainnet-beta.solana.com"

# Trading parameters
MAX_SOL_PER_TRADE     = 0.1    # max SOL spent per buy
DAILY_LOSS_LIMIT_SOL  = 0.5    # bot stops if daily loss exceeds this
TAKE_PROFIT_PERCENT   = 50     # sell at +50%
STOP_LOSS_PERCENT     = 20     # sell at -20%

# Token filters
MIN_LIQUIDITY_USD     = 5000   # min pool liquidity in USD
MAX_TOKEN_AGE_MINUTES = 30     # only buy tokens under 30 min old
MIN_PRICE_CHANGE_5M   = 5      # min +5% momentum in last 5 minutes
```

---

## 📁 Project Structure

```
Solana-bot/
├── main.py           # Entry point
├── bot.py            # Core trading logic & Telegram handler
├── config.example.py # Configuration template
├── requirements.txt  # Dependencies
└── README.md
```

---

## ⚠️ Disclaimer

This project is for educational purposes only. Meme coin trading involves significant financial risk — only use funds you can afford to lose entirely. This is not financial advice.

---

## 👤 Author

**Fikri Abd al-Hamid** — Python Developer | Bot Engineer | Automation Specialist

- 📧 fikriteacher@gmail.com
- 🔗 [GitHub — fikrigoldbot](https://github.com/fikrigoldbot)
- 🤖 Also see: [Gold Trading Bot (XAUUSD)](https://github.com/fikrigoldbot/Gold-Signal-Bot)
