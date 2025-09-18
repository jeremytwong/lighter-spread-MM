# SpreadBot - Automated Trading Bot

A Python-based automated trading bot for the Lighter protocol that implements a spread trading strategy. Testnet doesn't have enough orders in book to capture spread.

## Features

- **Automated Order Management**: Places and manages buy/sell orders automatically
- **Position Management**: Monitors positions with configurable loss and profit thresholds
- **Real-time Market Data**: Uses WebSocket connections for live order book updates
- **Risk Management**: Implements stop-loss and take-profit mechanisms
- **Order Chasing**: Automatically adjusts order prices to stay competitive

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

1. Clone or download this repository
2. Install required dependencies:
```bash
pip install asyncio websockets lighter
```

## Configuration

1. Copy the example configuration file:
```bash
cp config_example.py config.py
```

2. Edit `config.py` with your account details:
```python
config = {
    'account_index': YOUR_ACCOUNT_INDEX,  # Your account index number
    'api_key_private_key': 'YOUR_PRIVATE_KEY',  # Your API private key
    # ... other settings
}
```

## Usage

1. Make sure your `config.py` file is properly configured
2. Run the bot:
```bash
python main.py
```

## Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| `account_index` | Your account index number | Required |
| `api_key_private_key` | Your API private key | Required |
| `api_key_index` | API key index | 2 |
| `market_index` | Market to trade | 1 |
| `order_size` | Order size in base currency | 0.0002 |
| `tick_size` | Minimum price increment | 0.1 |
| `chase_interval` | Order update interval (seconds) | 0.2 |
| `loss_threshold` | Stop-loss threshold | 0.002 |
| `profit_threshold` | Take-profit threshold | 0.0001 |
| `reconnect_attempts` | Max reconnection attempts | 5 |
| `reconnect_delay` | Reconnection delay (seconds) | 5.0 |
| `tx_delay` | Transaction delay (seconds) | 0 |
| `order_timeout` | Order timeout (seconds) | 30.0 |
| `position_check_interval` | Position check interval (seconds) | 10.0 |

## Trading Strategy

The bot implements the following strategy:

1. **Initial Order Placement**: Places a buy order slightly below the current ask price
2. **Order Chasing**: Adjusts buy order price to stay competitive with market
3. **Position Management**: When a position is opened:
   - Places a bid 0.02% above entry price
   - Monitors for 0.2% loss threshold (triggers market sell)
   - Manages take-profit orders at configured profit threshold
4. **Risk Management**: Automatically cancels conflicting orders and manages position exits

## Safety Features

- **Stop Loss**: Automatic market sell when loss threshold is reached
- **Order Timeout**: Cancels orders that haven't filled within timeout period
- **Position Validation**: Regular position checks via API
- **Error Handling**: Comprehensive error handling and logging

## Logging

The bot provides detailed logging including:
- Market data updates
- Order placements and fills
- Position changes
- Error conditions
- Connection status

## Important Notes

⚠️ **Risk Warning**: This bot trades real money. Always test with small amounts first and understand the risks involved.

⚠️ **API Security**: Never share your private keys or commit them to version control.

⚠️ **Market Risk**: Trading involves risk of loss. Past performance does not guarantee future results.

## Troubleshooting

### Common Issues

1. **Connection Failed**: Check your internet connection and API credentials
2. **Order Placement Failed**: Verify your account has sufficient balance
3. **WebSocket Disconnected**: The bot will automatically attempt to reconnect

### Getting Help

If you encounter issues:
1. Check the logs for error messages
2. Verify your configuration settings
3. Ensure your account has sufficient balance
4. Check that the market is active

## License

This project is for educational purposes. Use at your own risk.
