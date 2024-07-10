import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20473138"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7e7a511bec31d0189e296f74a7655322")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://tipendra26:VDsprixpEKHlgSRV@cluster0.sbg8yo4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
