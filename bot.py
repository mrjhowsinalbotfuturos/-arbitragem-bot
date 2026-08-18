import ccxt
import requests
import config


# ==============================
# BINANCE
# ==============================

exchange = ccxt.binance({
    "enableRateLimit": True
})


# ==============================
# BUSCAR BINANCE
# ==============================

def buscar_binance(moeda):

    simbolo = moeda + "/USDT"

    try:

        ticker = exchange.fetch_ticker(simbolo)

        return {
            "preco": ticker["last"],
            "volume": ticker.get("quoteVolume", 0)
        }

    except Exception as erro:

        print(
            f"Erro Binance {moeda}: {erro}"
        )

        return None


# ==============================
# BUSCAR DEXSCREENER
# ==============================

def buscar_dex(moeda):

    url = "https://api.dexscreener.com/latest/dex/search"

    params = {
        "q": moeda
    }

    try:

        resposta = requests.get(
            url,
            params=params,
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        pares = dados.get("pairs", [])

        melhores = []

        for par in pares:

            base = par.get(
                "baseToken",
                {}
            ).get(
                "symbol",
                ""
            ).upper()

            quote = par.get(
                "quoteToken",
                {}
            ).get(
                "symbol",
                ""
            ).upper()

            if base != moeda:
                continue

            if quote not in [
                "USDT",
                "USDC"
            ]:
                continue

            preco = par.get(
                "priceUsd"
            )

            liquidez = (
                par.get("liquidity") or {}
            ).get(
                "usd",
                0
            )

            volume = (
                par.get("volume") or {}
            ).get(
                "h24",
                0
            )

            if not preco:
                continue

            melhores.append({
                "preco": float(preco),
                "liquidez": float(
                    liquidez or 0
                ),
                "volume": float(
                    volume or 0
                )
            })

        if not melhores:

            return None

        melhores.sort(
            key=lambda x: x["liquidez"],
            reverse=True
        )

        return melhores[0]

    except Exception as erro:

        print(
            f"Erro DEX {moeda}: {erro}"
        )

        return None


# ==============================
# ANALISAR
# ==============================

def analisar(moeda):

    print()
    print("=" * 60)
    print(
        f"ANALISANDO {moeda}"
    )
    print("=" * 60)

    cex = buscar_binance(
        moeda
    )

    if not cex:

        print(
            "Nao foi possivel consultar Binance."
        )

        return

    dex = buscar_dex(
        moeda
    )

    if not dex:

        print(
            "Nao foi encontrado par DEX."
        )

        return

    preco_cex = cex["preco"]

    preco_dex = dex["preco"]

    # Spread considerando
    # compra na DEX
    # venda na CEX

    spread = (
        preco_cex /
        preco_dex -
        1
    ) * 100

    custos = (
        config.CEX_FEE_PERCENT +
        config.DEX_COST_PERCENT
    )

    lucro_liquido = (
        spread -
        custos
    )

    tamanho = min(
        config.CAPITAL_USD,
        config.MAX_TRADE_USD
    )

    lucro_usd = (
        tamanho *
        lucro_liquido /
        100
    )

    print(
        f"Preço Binance: "
        f"${preco_cex:.6f}"
    )

    print(
        f"Preço DEX: "
        f"${preco_dex:.6f}"
    )

    print(
        f"Spread bruto: "
        f"{spread:.4f}%"
    )

    print(
        f"Custos estimados: "
        f"{custos:.4f}%"
    )

    print(
        f"Lucro líquido estimado: "
        f"{lucro_liquido:.4f}%"
    )

    print(
        f"Lucro em ${tamanho:.2f}: "
        f"${lucro_usd:.4f}"
    )

    print(
        f"Liquidez DEX: "
        f"${dex['liquidez']:,.2f}"
    )

    print(
        f"Volume DEX 24h: "
        f"${dex['volume']:,.2f}"
    )

    print(
        f"Volume Binance 24h: "
        f"${cex['volume']:,.2f}"
    )

    # ==============================
    # FILTROS
    # ==============================

    motivos = []

    if dex["liquidez"] < config.MIN_LIQUIDITY_USD:

        motivos.append(
            "liquidez baixa"
        )

    if cex["volume"] < config.MIN_VOLUME_USD:

        motivos.append(
            "volume Binance baixo"
        )

    if lucro_liquido < config.MIN_PROFIT_PERCENT:

        motivos.append(
            "lucro abaixo do minimo"
        )

    if lucro_usd < config.MIN_PROFIT_USD:

        motivos.append(
            "lucro em USD abaixo do minimo"
        )

    print()

    if motivos:

        print(
            "RESULTADO: REJEITADA"
        )

        print(
            "Motivos:"
        )

        for motivo in motivos:

            print(
                f" - {motivo}"
            )

    else:

        print(
            "RESULTADO: "
            "OPORTUNIDADE PAPER"
        )

        print(
            "ATENCAO: "
            "nenhuma ordem real sera enviada."
        )


# ==============================
# INICIO
# ==============================

print()
print(
    "=========================================="
)

print(
    " BOT DE ARBITRAGEM - PAPER TRADING"
)

print(
    "=========================================="
)

print()

print(
    "Nenhuma ordem real sera executada."
)

print()

for moeda in config.COINS:

    analisar(
        moeda
    )
