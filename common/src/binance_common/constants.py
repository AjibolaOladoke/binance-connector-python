from enum import Enum


# TimeUnit Constants
class TimeUnit(Enum):
    MILLISECOND = "MILLISECOND"
    millisecond = "millisecond"
    MICROSECOND = "MICROSECOND"
    microsecond = "microsecond"


class WebsocketMode(Enum):
    SINGLE = "single"
    POOL = "pool"

AUTO_RECONNECT_INTERVAL_SECONDS = 23 * 3600
SUBSCRIBE_MESSAGE_DELAY_SECONDS = 0.5
DEFAULT_RECONNECT_ATTEMPTS = 3
MAX_RECONNECT_ATTEMPTS = 10
SUPPORTED_CONNECTION_EVENTS = {"open", "ping", "pong", "reconnect", "close", "error"}


# Algo constants
ALGO_REST_API_PROD_URL = ""

# Alpha constants
ALPHA_REST_API_PROD_URL = ""
ALPHA_WS_STREAMS_PROD_URL = "wss://nbstream.binance.com/w3w/wsa"

# Auto Invest constants
AUTO_INVEST_REST_API_PROD_URL = ""

# C2C constants
C2C_REST_API_PROD_URL = ""

# Convert constants
CONVERT_REST_API_PROD_URL = ""

# Copy Trading constants
COPY_TRADING_REST_API_PROD_URL = ""

# Crypto Loan constants
CRYPTO_LOAN_REST_API_PROD_URL = ""

# Derivatives Trading constants
DERIVATIVES_TRADING_REST_API_PROD_URL = ""

# Derivatives Trading (COIN-M Futures) constants
DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL = ""
DERIVATIVES_TRADING_COIN_FUTURES_REST_API_TESTNET_URL = (
    ""
)
DERIVATIVES_TRADING_COIN_FUTURES_WS_API_PROD_URL = (
    "wss://ws-dapi.binance.com/ws-dapi/v1"
)
DERIVATIVES_TRADING_COIN_FUTURES_WS_API_TESTNET_URL = (
    "wss://testnet.binancefuture.com/ws-dapi/v1"
)
DERIVATIVES_TRADING_COIN_FUTURES_WS_STREAMS_PROD_URL = "wss://dstream.binance.com"
DERIVATIVES_TRADING_COIN_FUTURES_WS_STREAMS_TESTNET_URL = (
    "wss://dstream.binancefuture.com"
)

# Derivatives Trading (USDS Futures) constants
DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL = ""
DERIVATIVES_TRADING_USDS_FUTURES_REST_API_TESTNET_URL = (
    ""
)
DERIVATIVES_TRADING_USDS_FUTURES_REST_API_DEMO_URL = ""
DERIVATIVES_TRADING_USDS_FUTURES_WS_API_PROD_URL = (
    "wss://ws-fapi.binance.com/ws-fapi/v1"
)
DERIVATIVES_TRADING_USDS_FUTURES_WS_API_TESTNET_URL = (
    "wss://testnet.binancefuture.com/ws-fapi/v1"
)
DERIVATIVES_TRADING_USDS_FUTURES_WS_STREAMS_PROD_URL = "wss://fstream.binance.com"
DERIVATIVES_TRADING_USDS_FUTURES_WS_STREAMS_TESTNET_URL = (
    "wss://fstream.binancefuture.com"
)

# Derivatives Trading (Options) constants
DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL = ""
DERIVATIVES_TRADING_OPTIONS_WS_STREAMS_PROD_URL = "wss://fstream.binance.com"

# Derivatives Trading (Portfolio Margin) constants
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL = ""
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_WS_STREAMS_PROD_URL = (
    "wss://fstream.binance.com/pm"
)

# Derivatives Trading (Portfolio Margin Pro) constants
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_PRO_REST_API_PROD_URL = ""
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_PRO_WS_STREAMS_PROD_URL = (
    "wss://fstream.binance.com/pm-classic"
)

# Dual Investment constants
DUAL_INVESTMENT_REST_API_PROD_URL = ""

# Fiat constants
FIAT_REST_API_PROD_URL = ""

# Gift Card constants
GIFT_CARD_REST_API_PROD_URL = ""

# Margin Trading constants
MARGIN_TRADING_REST_API_PROD_URL = ""
MARGIN_TRADING_WS_STREAMS_PROD_URL = "wss://stream.binance.com:9443"
MARGIN_TRADING_RISK_WS_STREAMS_PROD_URL = "wss://margin-stream.binance.com"

# Mining constants
MINING_REST_API_PROD_URL = ""

# NFT constants
NFT_REST_API_PROD_URL = ""

# Pay constants
PAY_REST_API_PROD_URL = ""

# Rebate constants
REBATE_REST_API_PROD_URL = ""

# Simple Earn constants
SIMPLE_EARN_REST_API_PROD_URL = ""

# Spot Constants
SPOT_REST_API_PROD_URL = ""
SPOT_REST_API_TESTNET_URL = ""
SPOT_REST_API_DEMO_URL = ""
SPOT_WS_API_PROD_URL = "wss://ws-api.binance.com:443/ws-api/v3"
SPOT_WS_API_TESTNET_URL = "wss://ws-api.testnet.binance.vision/ws-api/v3"
SPOT_WS_API_DEMO_URL = "wss://demo-ws-api.binance.com/ws-api/v3"
SPOT_WS_STREAMS_PROD_URL = "wss://stream.binance.com:9443"
SPOT_WS_STREAMS_TESTNET_URL = "wss://stream.testnet.binance.vision"
SPOT_WS_STREAMS_DEMO_URL = "wss://demo-stream.binance.com:9443"
SPOT_REST_API_MARKET_URL = ""
SPOT_WS_STREAMS_MARKET_URL = "wss://data-stream.binance.vision"

# Staking constants
STAKING_REST_API_PROD_URL = ""

# Stocks constants
STOCKS_REST_API_PROD_URL = ""
STOCKS_WS_STREAMS_PROD_URL = "wss://nbstream.binance.com/equity"

# Sub Account constants
SUB_ACCOUNT_REST_API_PROD_URL = ""

# VIP Loan constants
VIP_LOAN_REST_API_PROD_URL = ""

# Wallet constants
WALLET_REST_API_PROD_URL = ""

# W3W Prediction constants
W3W_PREDICTION_REST_API_PROD_URL = ""
