# ==========================================
# CONFIGURAÇÃO DO BOT
# ==========================================

# CEX utilizada no teste
# Você pode trocar depois por outra exchange
CEX = "kraken"

# Moedas que serão analisadas
COINS = [
    "BTC",
    "ETH",
    "SOL",
    "LINK",
    "AVAX"
]

# Moeda de referência
QUOTE = "USDT"


# ==========================================
# CAPITAL / OPERAÇÃO
# ==========================================

# Capital fictício utilizado no paper trading
CAPITAL_USD = 1000

# Valor máximo de cada operação simulada
MAX_TRADE_USD = 100


# ==========================================
# FILTROS DE OPORTUNIDADE
# ==========================================

# Lucro mínimo em %
MIN_PROFIT_PERCENT = 0.30

# Lucro mínimo em dólares
MIN_PROFIT_USD = 1.00

# Volume mínimo da CEX nas últimas 24h
MIN_VOLUME_USD = 1000000

# Liquidez mínima encontrada na DEX
MIN_LIQUIDITY_USD = 500000


# ==========================================
# CUSTOS
# ==========================================

# Taxa estimada da CEX
# Depois vamos substituir pela taxa real
CEX_FEE_PERCENT = 0.40

# Reserva para DEX + gas + slippage
# É uma estimativa conservadora neste primeiro teste
DEX_COST_PERCENT = 0.50


# ==========================================
# CONFIGURAÇÃO DEX
# ==========================================

DEX_QUOTES = [
    "USDT",
    "USDC"
]


# ==========================================
# PAPER TRADING
# ==========================================

# IMPORTANTE:
# False = nenhuma ordem real
LIVE_TRADING = False
