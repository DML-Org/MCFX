import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '7031536'))
API_HASH = environ.get('API_HASH', 'fada850e5a6155f164c80e61d0ff0b82')
BOT_TOKEN = environ.get('BOT_TOKEN', "5054199554:AAEavlYuOf9tpfjmZudptP3gM4Mcj1V7v7s")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/2d381c9b5c2621335040d.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1717130632, 800435685').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001634360035 -1001617496862 -1001634238211 -1001234165493 -1001500007497 -1001495495666 -1001526514350 -1001563481034 -1001591057296 -1001517152612 -1001327911524 -1001513015963 -1001522595979 -1001490893135 -1001592057255 -1001512849718 -1001554735797 -1001580679295 -1001501243958 -1001510203790 -1001157941824 -1001562323229 -1001511629430 -1001515590697 -1001548763346 -1001680901377 -1001501157756 -1001581241095 -1001658353601 -1001533767277 -1001598699420 -1001159803049 -1001212125293').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001415345069')
auth_grp = environ.get('AUTH_GROUP', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://dinukacreation:dinukacreation@cluster0.bhepukk.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "tgdinuka")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001593272391'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MovieClubFamily_Chat')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "ɴᴀᴍᴇ: <code>{file_name}</code> \n\nJoin Now: [MCF FilterX Bot](https://t.me/MovieClubFamily)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 Title: {title} \n🎭 Genres: {genres}\n📆 Year: {year}\n🌟 Rating: {rating}/ 10 (based on {votes} user ratings.)\n☀️ Languages : {languages}\n📀 RunTime: {runtime} Minutes\n📆 Release Info : {release_date}\n🎛 Countries : {countries}\n\n┏━━━━•❅•°•❈•°•❅•━━━━┓\n🇱🇰𝐌𝐨𝐯𝐢𝐞𝐂𝐥𝐮𝐛 𝐅𝐚𝐦𝐢𝐥𝐲™🎭\n┗━━━━•❅•°•❈•°•❅•━━━━┛")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'Clicksfly.com')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'b22bac22c1c3aad163918ac98dbc831ca127410b')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/ClickAdd_MCF/7"

   # Custom Caption Under Button #
CAPTION_BUTTON = "Subscribe Premium"
CAPTION_BUTTON_URL = "https://t.me/MovieClubUpdates/17112"

   # Auto Delete For Bot Sending Files #
