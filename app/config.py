from decouple import Csv, config
from web3 import Web3

PERM_GOERLI = "perm_goerli"

PERM_GOERLI_UPPER = PERM_GOERLI.upper()

# auth key for server-server auth
API_KEY = config("API_KEY", default=None)
ENABLED_NETWORKS = config(
    "ENABLED_NETWORKS",
    default=PERM_GOERLI,
    cast=Csv(),
)
CONFIRMATION_BLOCKS: int = config("CONFIRMATION_BLOCKS", default=15, cast=int)
TRANSACTION_TIMEOUT = config("TRANSACTION_TIMEOUT", default=900, cast=int)

NETWORKS = {
    PERM_GOERLI: dict(
        ETH1_ENDPOINT=config(f"{PERM_GOERLI_UPPER}_ETH1_ENDPOINT", default=""),
        IS_POA=True,
        MAX_FEE_PER_GAS=config(
            f"{PERM_GOERLI_UPPER}_MAX_FEE_PER_GAS_GWEI",
            default=150,
            cast=lambda x: Web3.toWei(x, "gwei"),
        ),
        CONTRACT_ADDRESS="0x176Bf5626C6e9Cd82a13CD69997fA58c633fcF7B",
        PRIVATE_KEY=config(
            f"{PERM_GOERLI_UPPER}_PRIVATE_KEY",
            default=None,
        ),
    ),
}
