# ==========================================
# CONFIGURAÇÃO DO BOT
# ==========================================

# Capital usado apenas na simulação
CAPITAL_USD = 1000

# Valor máximo de cada operação simulada
MAX_TRADE_USD = 100

# Lucro mínimo em dólares
MIN_PROFIT_USD = 1

# Lucro líquido mínimo em %
MIN_PROFIT_PERCENT = 0.30

# Volume mínimo diário da moeda
MIN_VOLUME_USD = 1000000

# Liquidez mínima na DEX
MIN_LIQUIDITY_USD = 500000

# Taxa estimada da CEX
CEX_FEE_PERCENT = 0.10

# Reserva para custos DEX/gas/slippage
DEX_COST_PERCENT = 0.30

# Moedas que o bot vai procurar
COINS = [
    "ETH",
    "BTC",
    "SOL",
    "BNB",
    "AVAX",
    "LINK"
]

# Stablecoin usada na comparação
QUOTE = "USDT"
