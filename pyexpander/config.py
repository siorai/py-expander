import babelfish

# Local directory settings.
TV_PATH = '/home/siorai/Downloads/Transmission/Organized/TV'
MOVIE_PATH = '/home/siorai/Downloads/Transmission/Organized/Movies'
APP_PATH = '/home/siorai/Downloads/Transmission/Organized/Programs'
MUSIC_PATH = '/home/siorai/Downloads/Transmission/Organized/Music'
OTHER_PATH = '/home/siorai/Downloads/Transmission/Organized/Other'
DEFAULT_PATH = '/home/siorai/Downloads/Transmission/Organized/'

# Log settings.
LOGFILE = 'pyexp.log'

# Extraction settings.
EXTRACTION_FILES_MASK = '770'
EXTRACTION_TEMP_DIR_NAME = '_extracted'
EXTRACTION_EXECUTABLE = '7z'

# Subtitle settings.
SHOULD_FIND_SUBTITLES = True
# A map between each language and its favorite subliminal providers (None for all providers).
LANGUAGES_MAP = {
    babelfish.Language('heb'): ['subscenter'],
    babelfish.Language('eng'): []
}

# Upload settings.
SHOULD_UPLOAD = False
UPLOAD_TO = 'Google'
ACD_CLI_PATH = '/usr/bin/acd_cli'
DEFAULT_VIDEO_EXTENSION = '.mkv'
SUBTITLES_EXTENSIONS = ['.srt']
LANGUAGE_EXTENSIONS = ['.he', '.en']
# Lists.
EXTENSIONS_WHITE_LIST = ['.srt', '.mkv', '.avi', '.mp4', '.mov', '.m4v', '.wmv']
NAMES_BLACK_LIST = ['sample']

# Remote settings.

# Amazon directory settings.
AMAZON_TV_PATH = '/amazon/tv/path'
AMAZON_MOVIE_PATH = '/amazon/movies/path'
ORIGINAL_NAMES_LOG = '/var/log/original_names.log'

# Google Drive settings.
KEYFILE = '/home/siorai/Python/GoogleDriveFtw!-fc20e0f60d1b.json'
CLIENT_EMAIL = 'seedbox@virtual-plexus-92702.iam.gserviceaccount.com'
DELEGATED_EMAIL = 'paul@ladancesafe.org'

