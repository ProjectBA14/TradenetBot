# Tradenetbot

A modular Python CLI application for placing orders on the Binance USDT-M Futures Testnet / Demo environment.

This project supports:
- MARKET orders
- LIMIT orders
- BUY and SELL sides
- Input validation
- Structured logging
- Modular architecture
- Error handling

---

# Features

- Binance Futures Testnet support
- CLI-based order placement
- Logging to file
- Validation for:
  - order side
  - order type
  - quantity
  - price
- Reusable architecture
- Environment variable support using `.env`

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── trading.log
├── requirements.txt
├── README.md
└── .env
```

---

# Requirements

- Python 3.9+
- Binance Futures Testnet account
- Binance API Key + Secret

---

# Setup

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd trading_bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create `.env`

Create a `.env` file in the root folder:

Acquire the API key from the website provided https://testnet.binancefuture.com
```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
BINANCE_FUTURES_URL=https://demo-fapi.binance.com/fapi
```

---

# Binance Futures Testnet

Register and create API keys:

https://testnet.binancefuture.com

Official Binance Futures API Documentation:

https://developers.binance.com/docs/derivatives/usds-margined-futures/general-info

---

# Supported Order Types

Currently supported:
- MARKET
- LIMIT

Additional validation exists for:
- STOP
- STOP_MARKET
- TAKE_PROFIT
- TAKE_PROFIT_MARKET

However full implementation for advanced order types has not been implemented yet

---

# Usage

---

## MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## MARKET SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

## LIMIT BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

## LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000
```

---

# Example Output

```text
Order placed successfully!

ORDER RESPONSE

Order ID            : 13160908119
Symbol              : BTCUSDT
Status              : NEW
Order Type          : LIMIT
Side                : SELL
Quantity            : 0.001
Executed Quantity   : 0.000
Average Price       : 0.00
```

---

# Logging

Logs are written to:

```text
trading.log
```

Logs include:
- Binance connection events
- validated orders
- order preparation
- API requests
- API responses
- errors

Example log:

```text
2026-05-19 14:30:01 | INFO | Connected to Binance Futures Testnet
2026-05-19 14:30:02 | INFO | Validated order for BTCUSDT
2026-05-19 14:30:02 | INFO | Preparing LIMIT order
```

---

# Architecture Overview

The application follows a layered modular architecture.

---

## `cli.py`

Responsible for:
- CLI argument parsing
- user interaction
- displaying responses

---

## `orders.py`

Responsible for:
- business logic
- order preparation
- validation coordination
- trading rules

---

## `client.py`

Responsible for:
- Binance API communication
- authenticated requests
- Futures endpoint configuration

---

## `validators.py`

Responsible for:
- validating input
- enforcing trading constraints

---

## `logging_config.py`

Responsible for:
- centralized logging configuration

---

# Error Handling

The application handles:
- invalid order side
- invalid order type
- invalid quantity
- missing LIMIT price
- Binance API failures
- timestamp issues
- network failures

---

# Assumptions

- User has a Binance Futures Testnet account
- User has generated valid API credentials
- User has synchronized system time
- User has sufficient testnet balance

---

# Future Improvements

Potential future enhancements:
- STOP order support
- TAKE_PROFIT support
- OCO orders
- WebSocket market streaming
- position management
- Docker support
- automated trading strategies
- unit tests
- async requests
- richer logging
- prettier terminal UI

---

# Dependencies

```txt
python-binance
python-dotenv
```

---

