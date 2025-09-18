# Configuration file for SpreadBot
# Copy this file to config.py and fill in your account details

config = {
    # Required: Your account details
    'account_index': 0,  # Replace with your account index
    'api_key_private_key': 'YOUR_PRIVATE_KEY_HERE',  # Replace with your API private key
    
    # Optional: API settings
    'api_key_index': 2,
    
    # Trading settings
    'market_index': 1,
    'order_size': 0.0002,
    'tick_size': 0.1,
    
    # Bot behavior
    'chase_interval': 0.2,
    'loss_threshold': 0.002,
    'profit_threshold': 0.0001,
    
    # Connection settings
    'reconnect_attempts': 5,
    'reconnect_delay': 5.0,
    'tx_delay': 0,
    'order_timeout': 30.0,
    'position_check_interval': 10.0,
    
    # Network settings
    'base_url': 'https://mainnet.zklighter.elliot.ai'
}
