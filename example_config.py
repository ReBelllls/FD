# Rename this to "config.py"

token = "BOT_TOKEN"
shard_count = 1  # ~ guilds // 1000
shard_ids = None  # ~ Optional

prefix = "#"

extensions = [
    "cogs.errors",
    "cogs.help",
    "cogs.admin",
    "cogs.backups",
    "cogs.templates",
    "cogs.pro",
    "cogs.blacklist",
    "cogs.basics",
    "cogs.stats"
]

support_guild = 522419810701803522

self_host = True
# The options below are not required if "self_host" is enabled

dbl_token = ""
