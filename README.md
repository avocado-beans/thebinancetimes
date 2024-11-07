# Binance Times - Telegram Bot

**Binance Times** is a Telegram bot that listens for new coin listing announcements from a Chinese Telegram channel. The bot forwards the posts with minimal latency, allowing you to get an early notification of upcoming coin listings. This project is purely educational and does not execute actual trades.

## Features

- **Real-time Notifications**: The bot listens for new coin listing announcements from a specific Chinese Telegram channel.
- **Low Latency**: The bot is designed to forward the posts with minimal delay, ensuring you receive the information as quickly as possible.
- **Educational Purpose**: The bot does not perform any live trading but serves as an educational tool to learn about automation, Telegram bots, and cryptocurrency market dynamics.
  
## How It Works

1. **Listen for Announcements**: The bot continuously monitors a specific Telegram channel for new announcements regarding token listings.
2. **Forward Announcements**: Once a new token is announced, the bot forwards the details to a designated Telegram group or user.
3. **Uniswap/PancakeSwap Pre-listing**: Based on the announcement, users can manually purchase the token from liquidity pools like Uniswap or PancakeSwap *before* the token is officially listed on major exchanges.
4. **No Trades Executed**: This bot does not interact 

## Setup 

```bash
git clone https://github.com/avocado-beans/binance-times.git
cd binance-times
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080
```
