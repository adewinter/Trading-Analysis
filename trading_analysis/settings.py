# Django settings for trading_analysis project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'anton',                      # Or path to database file if using sqlite3.
        'USER': 'anton',                      # Not used with sqlite3.
        'PASSWORD': 'qsczse',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True
PROJECT_ROOT = os.path.split(os.path.abspath(__file__))[0]
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_media')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_l_-zu$)*eoa98uw4st($#n2)mmagr977eoa%%=nr86gk6ecyi'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'trading_analysis.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'financials',
    'market_data',
#    'debug_toolbar',
#    'south',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

MARKET_DATA_PATH = '/home/wbnigeria/Desktop/trading_analysis/market_data'
FINANCE_DATA_PATH = '/home/wbnigeria/Desktop/trading_analysis/fin_data'

INTERNAL_IPS = ('127.0.0.1',)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


######################## CUSTOM #########################
FIN_COMPANY_LIST = [
    ('A E C I LIMITED', 'AFE'),
    ('ABSA BANK LIMITED', 'ABSP'),
    ('ABSA CAPITAL', 'ACPL'),
    ('ABSA GROUP LIMITED', 'AMAGB'),
    ('ACUCAP PROPERTIES LIMITED', 'ACP'),
    ('ADAPTIT HOLDINGS LIMITED', 'ADI'),
    ('ADCOCK INGRAM HOLDINGS LIMITED', 'AIP'),
    ('ADCORP HOLDINGS LIMITED', 'ADR'),
    ('ADVTECH LIMITED', 'ADH'),
    ('AFGRI LIMITED', 'AFR'),
    ('AFRICAN AND OVERSEAS ENTERPRISES LD', 'AOO'),
    ('AFRICAN BANK INVESTMENTS LIMITED', 'ABL'),
    ('AFRICAN MEDIA ENTERTAINMENT LIMITED', 'AME'),
    ('AFRICAN OXYGEN LIMITED', 'AFX'),
    ('AFRICAN RAINBOW MINERALS LIMITED', 'ARI'),
    ('AFRIMAT LIMITED', 'AFT'),
    ('AFROCENTRIC INVESTMENT CORP LIMITED', 'ACT'),
    ('AG INDUSTRIES LIMITED', 'AGI'),
    ('ALEXANDER FORBES PREF SHARE INV LTD', 'AFP'),
    ('ALLIED ELECTRONICS CORPORATION LTD', 'ATN'),
    ('ALLIED TECHNOLOGIES LIMITED', 'ALT'),
    ('AMALGAMATED APPLIANCE HOLDINGS LD', 'AMA'),
    ('AMALGAMATED ELECTRONICS CORP LTD', 'AER'),
    ('ANDULELA INVESTMENT HOLDINGS LTD', 'AND'),
    ('ANGLO AMERICAN PLAT LTD', 'AMS'),
    ('ANGLO AMERICAN PLC', 'AGL'),
    ('ANGLOGOLD ASHANTI LIMITED', 'ANG'),
    ('ANOORAQ RESOURCES CORPORATION', 'ARQ'),
    ('AQUARIUS PLATINUM LIMITED', 'AQP'),
    ('ARB HOLDINGS LIMITED', 'ARH'),
    ('ARCELORMITTAL SOUTH AFRICA LIMITED', 'ACL'),
    ('ARGENT INDUSTRIAL LIMITED', 'ART'),
    ('ARROWHEAD PROPERTIES LIMITED A', 'AWA'),
    ('ARROWHEAD PROPERTIES LIMITED B', 'AWB'),
    ('ASPEN PHARMACARE HOLDINGS LIMITED', 'APN'),
    ('ASSORE LIMITED', 'ASR'),
    ('ASTRAL FOODS LIMITED', 'ARL'),
    ('ASTRAPAK LIMITED', 'APK'),
    ('AUSTRO GROUP LIMITED', 'ASO'),
    ('AVENG LIMITED', 'AEG'),
    ('AVI LIMITED', 'AVI'),
    ('AVUSA LTD', 'AVU'),
    ('AWETHU BREWERIES LIMITED', 'AWT'),
    ('BARLOWORLD LIMITED', 'BAW'),
    ('BASIL READ HOLDINGS LIMITED', 'BSR'),
    ('BAUBA PLATINUM LIMITED', 'BAU'),
    ('BELL EQUIPMENT LIMITED', 'BEL'),
    ('BETTABETA CIS', 'BBET'),
    ('BHP BILLITON PLC', 'BIL'),
    ('BLUE LABEL TELECOMS LIMITED', 'BLU'),
    ('BONATLA PROPERTY HOLDINGS LIMITED', 'BNT'),
    ('BOWLER METCALF LIMITED', 'BCF'),
    ('BRAIT SE', 'BRAIT'),
    ('BRIAN PORTER HOLDINGS LIMITED', 'POTP'),
    ('BRIMSTONE INVESTMENT CORPORATION LD', 'BRT'),
    ('BRITISH AMERICAN TOBACCO PLC', 'BTI'),
    ('BUILDMAX LIMITED', 'BDM'),
    ('BUSINESS CONNEXION GROUP LIMITED', 'BCX'),
    ('CADIZ HOLDINGS LIMITED', 'CDZ'),
    ('CAFCA LIMITED', 'CAC'),
    ('CAPE EMPOWERMENT LIMITED', 'CAP'),
    ('CAPEVIN INVESTMENTS LIMITED', 'CVI'),
    ('CAPITAL & COUNTIES PROPERTIES PLC', 'CCO'),
    ('CAPITAL PROPERTY FUND', 'CPL'),
    ('CAPITAL SHOPPING CENTRES GROUP PLC', 'CSO'),
    ('CAPITEC BANK HOLDINGS LIMITED', 'CPI'),
    ('CARGO CARRIERS LIMITED', 'CRG'),
    ('CASHBUILD LIMITED', 'CSB'),
    ('CAXTON CTP PUBLISHERS & PRINTERS LD', 'CAT'),
    ('CENTRAL RAND GOLD LIMITED', 'CRD'),
    ('CERAMIC INDUSTRIES LIMITED', 'CRM'),
    ('CIPLA MEDPRO SOUTH AFRICA LIMITED', 'CMP'),
    ('CITY LODGE HOTELS LIMITED', 'CLH'),
    ('CITY OF JHB METROP MUNICIPALITY', 'JOZI'),
    ('CLICKS GROUP LIMITED', 'CLS'),
    ('CLIENTELE LIMITED', 'CLI'),
    ('CLOVER INDUSTRIES LIMITED', 'CLR'),
    ('COAL OF AFRICA LIMITED', 'CZA'),
    ('COLLIERS SOUTH AFRICA HOLDINGS LTD', 'COL'),
    ('COMAIR LIMITED', 'COM'),
    ('COMBINED MOTOR HOLDINGS LIMITED', 'CMH'),
    ('COMMAND HOLDINGS LIMITED', 'CMA'),
    ('COMPAGNIE FINANCIERE RICHEMONT SA', 'CFR'),
    ('COMPU-CLEARING OUTSOURCING LIMITED', 'CCL'),
    ('CONDUIT CAPITAL LIMITED', 'CND'),
    ('CONSOLIDATED INFRASTRUCTURE GRP LTD', 'CIL'),
    ('CONTROL INSTRUMENTS GROUP LIMITED', 'CNL'),
    ('CONVERGENET HOLDINGS LIMITED', 'CVN'),
    ('CORONATION FUND MANAGERS LIMITED', 'CML'),
    ('CORWIL INVESTMENTS LIMITED', 'CRW'),
    ('COUNTRY BIRD HOLDINGS LIMITED', 'CBH'),
    ('CROOKES BROTHERS LIMITED', 'CKS'),
    ('CULLINAN HOLDINGS LIMITED', 'CUL'),
    ('DATACENTRIX HOLDINGS LIMITED', 'DCT'),
    ('DATATEC LIMITED', 'DTC'),
    ('DECILLION LIMITED', 'DEC'),
    ('DELRAND RESOURCES LIMITED', 'DRN'),
    ('DELTA EMD LIMITED', 'DTA'),
    ('DEUTSCHE BANK AG', 'DEUT'),
    ('DEUTSCHE BANK AG LONDON', 'DBETN'),
    ('DIGICORE HOLDINGS LIMITED', 'DGC'),
    ('DIPULA INCOME FUND LTD', 'DIF'),
    ('DISCOVERY HOLDINGS LIMITED', 'DSY'),
    ('DISTELL GROUP LIMITED', 'DST'),
    ('DISTRIB. AND WAREHOUSING NETWORK LD', 'DAW'),
    ('DORBYL LIMITED', 'DLV'),
    ('DRDGOLD LIMITED', 'DRDD'),
    ('EASTERN PLATINUM LIMITED', 'EPS'),
    ('EFFICIENT GROUP LIMITED', 'EFG'),
    ('ELB GROUP LIMITED', 'ELR'),
    ('ELLIES HOLDINGS LIMITED', 'ELI'),
    ('EMIRA PROPERTY FUND', 'EMI'),
    ('EOH HOLDINGS LIMITED', 'EOH'),
    ('EQSTRA HOLDINGS LIMITED', 'EQS'),
    ('ESORFRANKI LIMITED', 'ESR'),
    ('EVRAZ HIGHVELD STEEL & VANADIUM LTD', 'EHS'),
    ('EXCELLERATE HOLDINGS LIMITED', 'EXL'),
    ('EXXARO RESOURCES LIMITED', 'EXX'),
    ('FAIRVEST PROPERTY HOLDINGS LIMITED', 'FVT'),
    ('FAMOUS BRANDS LIMITED', 'FBR'),
    ('FARITEC HOLDINGS LIMITED', 'FRT'),
    ('FERRUM CRESCENT LIMITED', 'FCR'),
    ('FIRESTONE ENERGY LIMITED', 'FSE'),
    ('FIRST URANIUM CORPORATION', 'FIU'),
    ('FIRSTRAND LIMITED', 'FSR'),
    ('FOORD COMPASS LIMITED', 'FCPD'),
    ('FORBES & MANHATTAN COAL CORP', 'FMC'),
    ('FORTRESS INCOME FUND LIMITED', 'FORT'),
    ('FOUNTAINHEAD PROPERTY TRUST', 'FPT'),
    ('GIJIMA GROUP LIMITED', 'GIJ'),
    ('GOLD FIELDS LIMITED', 'GOGOF'),
    ('GOLD ONE INTERNATIONAL LIMITED', 'GDO'),
    ('GOLIATH GOLD MINING LIMITED', 'GGM'),
    ('GRAND PARADE INVESTMENTS LIMITED', 'GPL'),
    ('GREAT BASIN GOLD LIMITED', 'GBG'),
    ('GRINDROD LIMITED', 'GND'),
    ('GROUP FIVE LIMITED', 'GRF'),
    ('GROWTHPOINT PROPERTIES LIMITED', 'GRT'),
    ('HARMONY GOLD MINING COMPANY LIMITED', 'HAPS'),
    ('HOLDSPORT LIMITED', 'HSP'),
    ('HOSKEN CONSOLIDATED INVESTMENTS LTD', 'HCI'),
    ('HOSPITALITY PROPERTY FUND LIMITED', 'HPA'),
    ('HOWDEN AFRICA HOLDINGS LIMITED', 'HWN'),
    ('HUDACO INDUSTRIES LIMITED', 'HDC'),
    ('HULAMIN LIMITED', 'HLM'),
    ('HWANGE COLLIERY COMPANY LIMITED', 'HWHWA'),
    ('HYPROP INVESTMENTS LIMITED', 'HYP'),
    ('IFA HOTELS AND RESORTS LIMITED', 'IFH'),
    ('ILIAD AFRICA LIMITED', 'ILA'),
    ('ILLOVO SUGAR LIMITED', 'ILV'),
    ('IMPALA PLATINUM HOLDINGS LIMITED', 'IMPO'),
    ('IMPERIAL HOLDINGS LIMITED', 'IPL'),
    ('INFRASORS HOLDINGS LIMITED', 'IRA'),
    ('INGENUITY PROPERTY INVESTMENTS LTD', 'ING'),
    ('INSIMBI REFRACTORY & ALLOY SUP LTD', 'ISB'),
    ('INTERTRADING LIMITED', 'ITR'),
    ('INVESTEC BANK LIMITED', 'INVS'),
    ('INVESTEC BANK LTD', 'INLP'),
    ('INVESTEC LIMITED', 'INL'),
    ('INVESTEC PLC', 'INP'),
    ('INVESTEC PROPERTY FUND LIMITED', 'IPF'),
    ('INVICTA HOLDINGS LIMITED', 'IVT'),
    ('ITALTILE LIMITED', 'ITE'),
    ('ITRIX CIS', 'ITXUK'),
    ('JASCO ELECTRONICS HOLDINGS LIMITED', 'JSC'),
    ('JCI LIMITED', 'JCD'),
    ('JD GROUP LIMITED', 'JDG'),
    ('JSE LIMITED', 'JSE'),
    ('JUBILEE PLATINUM PLC', 'JUJLP'),
    ('KAGISO MEDIA LIMITED', 'KGM'),
    ('KAIROS INDUSTRIAL HOLDINGS LIMITED', 'KIR'),
    ('KAP INTERNATIONAL HOLDINGS LIMITED', 'KAP'),
    ('KAYDAV GROUP LIMITED', 'KDV'),
    ('KEATON ENERGY HOLDINGS LIMITED', 'KEH'),
    ('KELLY GROUP LIMITED', 'KEL'),
    ('KUMBA IRON ORE LIMITED', 'KIO'),
    ('LEWIS GROUP LIMITED', 'LEW'),
    ('LIBERTY HOLDINGS LIMITED', 'LBH'),
    ('LIFE HEALTHCARE GROUP HOLDINGS LTD', 'LHC'),
    ('LITHA HEALTHCARE GROUP LIMITED', 'LHG'),
    ('LONDON FINANCE AND INVEST. GRP PLC', 'LOJM'),
    ('LONMIN PLC', 'LOLMI'),
    ('M CUBED HOLDINGS LIMITED', 'MCU'),
    ('MARSHALL MONTEAGLE PLC', 'MMP'),
    ('MASONITE (AFRICA) LIMITED', 'MAS'),
    ('MASSMART HOLDINGS LIMITED', 'MSM'),
    ('MAZOR GROUP LIMITED', 'MZR'),
    ('MEDICLINIC INTERNATIONAL LIMITED', 'MDC'),
    ('MERAFE RESOURCES LIMITED', 'MRF'),
    ('MERCANTILE BANK HOLDINGS LIMITED', 'MTL'),
    ('METAIR INVESTMENTS LIMITED', 'MTA'),
    ('METMAR LIMITED', 'MML'),
    ('METROFILE HOLDINGS LIMITED', 'MFL'),
    ('MICROMEGA HOLDINGS LIMITED', 'MMG'),
    ('MINE WASTE SOLUTIONS (PTY) LTD', 'MWNT'),
    ('MIRANDA MINERAL HOLDINGS LIMITED', 'MMH'),
    ('MIX TELEMATICS LIMITED', 'MIX'),
    ('MMI HOLDINGS LIMITED', 'MMI'),
    ('MOBILE INDUSTRIES LIMITED', 'MOB'),
    ('Mondi Limited', 'MND'),
    ('Mondi plc', 'MNP'),
    ('MORVEST BUSINESS GROUP LIMITED', 'MOR'),
    ('MPACT LIMITED', 'MPT'),
    ('MR PRICE GROUP LIMITED', 'MPC'),
    ('MTN GROUP LIMITED', 'MTN'),
    ('MURRAY & ROBERTS HOLDINGS LIMITED', 'MUR'),
    ('MUSTEK LIMITED', 'MST'),
    ('MVELAPHANDA GROUP LIMITED', 'MVG'),
    ('MVELASERVE LIMITED', 'MVS'),
    ('NAMPAK LIMITED', 'NPK'),
    ('NASPERS LIMITED', 'NPN'),
    ('NEDBANK GROUP LIMITED', 'NED'),
    ('NEDBANK LIMITED', 'NEDB'),
    ('NEDBANK LTD', 'NBKP'),
    ('NET 1 UEPS TECHNOLOGIES INC', 'NT1'),
    ('NETCARE LIMITED', 'NTC'),
    ('NEW AFRICA INVESTMENT LIMITED', 'NAI'),
    ('NEW CORPCAPITAL LIMITED', 'NCA'),
    ('NEW EUROPE PROPERTY INVESTMENTS PLC', 'NEP'),
    ('NEW GOLD ISSUER LIMITED', 'GLD'),
    ('NEWFUNDS COLLECTIVE INVEST SCHEME', 'NFS'),
    ('NICTUS BEPERK', 'NCS'),
    ('NORTHAM PLATINUM LIMITED', 'NHM'),
    ('NU-WORLD HOLDINGS LIMITED', 'NWL'),
    ('OANDO PLC', 'UNTP'),
    ('OCEANA GROUP LIMITED', 'OCE'),
    ('OCTODEC INVESTMENTS LIMITED', 'OCT'),
    ('OLD MUTUAL PLC', 'OLOML'),
    ('OMNIA HOLDINGS LIMITED', 'OMN'),
    ('OPTIMUM COAL HOLDINGS LIMITED', 'OPT'),
    ('ORION REAL ESTATE LIMITED', 'ORE'),
    ('PALABORA MINING COMPANY LIMITED', 'PAM'),
    ('PALLINGHURST RESOURCES LIMITED', 'PGL'),
    ('Pamodzi Gold Limited', 'PZG'),
    ('PAN AFRICAN RESOURCES PLC', 'PAN'),
    ('PBT GROUP LIMITED', 'PBT'),
    ('PEREGRINE HOLDINGS LIMITED', 'PGR'),
    ('PETMIN LIMITED', 'PET'),
    ('PHUMELELA GAMING & LEISURE LIMITED', 'PHM'),
    ('PICK N PAY HOLDINGS LIMITED', 'PWK'),
    ('PICK N PAY STORES LIMITED', 'PIK'),
    ('PINNACLE TECHNOLOGY HOLDINGS LTD', 'PNC'),
    ('PIONEER FOOD GROUP LIMITED', 'PFG'),
    ('PLATFIELDS LIMITED', 'PLL'),
    ('PREMIUM PROPERTIES LIMITED', 'PMM'),
    ('PRETORIA PORTLAND CEMENT COMPANY LD', 'PPC'),
    ('PRIMESERV GROUP LIMITED', 'PMV'),
    ('PROP INDEX TRACKER COL INV SCHEME', 'PTX'),
    ('PROTECH KHUTHELE HOLDINGS LIMITED', 'PKH'),
    ('PSG FINANCIAL SERVICES LIMITED', 'PGFP'),
    ('PSG GROUP LIMITED', 'PSG'),
    ('PURPLE CAPITAL LIMITED', 'PPE'),
    ('PUTPROP LIMITED', 'PPR'),
    ('RAINBOW CHICKEN LIMITED', 'RBW'),
    ('RAND MERCHANT INSURANCE HLDGS LTD', 'RMI'),
    ('RANDGOLD & EXPLORATION COMPANY LTD', 'RNG'),
    ('RAUBEX GROUP LIMITED', 'RBX'),
    ('REAL AFRICA HOLDINGS LIMITED', 'RAH'),
    ('REBOSIS PROPERTY FUND LIMITED', 'REB'),
    ('RECM AND CALIBRE LIMITED', 'REC'),
    ('REDEFINE PROP INTERNATIONAL LTD', 'RIN'),
    ('REDEFINE PROPERTIES LIMITED', 'RDF'),
    ('REINET INVESTMENTS S.C.A', 'REI'),
    ('REMGRO LIMITED', 'REM'),
    ('RESILIENT PROPERTY INCOME FUND LTD', 'RES'),
    ('RESOURCE GENERATION LIMITED', 'RSG'),
    ('REUNERT LIMITED', 'RLO'),
    ('REX TRUEFORM CLOTHING COMPANY LTD', 'RTO'),
    ('RMB EXCHANGE TRADED NOTES', 'RMBETN'),
    ('RMB HOLDINGS LIMITED', 'RMH'),
    ('ROCKWELL DIAMONDS INCORPORATED', 'RDI'),
    ('ROLFES HOLDINGS LIMITED', 'RLF'),
    ('ROYAL BAFOKENG PLATINUM LIMITED', 'RBP'),
    ('SA CORPORATE REAL ESTATE FUND', 'SAC'),
    ('SABMILLER PLC', 'SOSAB'),
    ('SABVEST LIMITED', 'SBV'),
    ('SACOIL HOLDINGS LIMITED', 'SCL'),
    ('SANLAM LIMITED', 'SLM'),
    ('SANTAM LIMITED', 'SNT'),
    ('SANTOVA LOGISTICS LIMITED', 'SNV'),
    ('SANYATI HOLDINGS LIMITED', 'SAN'),
    ('SAPPI LIMITED', 'SAVVI'),
    ('SASFIN HOLDINGS LIMITED', 'SFN'),
    ('SASOL LIMITED', 'SOL'),
    ('SATRIX COLLECTIVE INVESTMENT SCHEME', 'STX2'),
    ('SATRIX COLLECTIVE INVESTMENT SCHEME', 'STX'),
    ('SEA KAY HOLDINGS LIMITED', 'SKY'),
    ('SEARDEL INVESTMENT CORPORATION LTD', 'SER'),
    ('SECUREDATA HOLDINGS LIMITED', 'SDH'),
    ('SEKUNJALO INVESTMENTS LIMITED', 'SKJ'),
    ('SENTULA MINING LIMITED', 'SNU'),
    ('SEPHAKU HOLDINGS LIMITED', 'SEP'),
    ('SHOPRITE HOLDINGS LIMITED', 'SHP'),
    ('SIMMER AND JACK MINES LIMITED', 'SIIF'),
    ('SOUTH AFRICAN COAL MINING HLDGS LTD', 'SAH'),
    ('SOUTH OCEAN HOLDINGS LIMITED', 'SOH'),
    ('SOVEREIGN FOOD INVESTMENTS LIMITED', 'SOV'),
    ('SPANJAARD LIMITED', 'SPA'),
    ('SPUR CORPORATION LIMITED', 'SUR'),
    ('SQUARE ONE SOLUTIONS GROUP LIMITED', 'SQE'),
    ('STANDARD BANK GROUP LIMITED', 'SBK'),
    ('STANDARD BANK OF SOUTH AFRICA LD', 'SCIB'),
    ('STANLIB COLLECTIVE INVESTMENTS LTD', 'STNCIS'),
    ('STD BANK OF SA RETAIL DEPOSIT NOTES', 'SBR'),
    ('STEFANUTTI STOCKS HOLDINGS LTD', 'SSK'),
    ('STEINHOFF INTERNATIONAL HOLDINGS LD', 'SHF'),
    ('STEINHOFF INVESTMENT HOLDINGS LD', 'SHFF'),
    ('STERLING WATERFORD CCN SPV 4', 'CBN013'),
    ('SUN INTERNATIONAL LIMITED', 'SUI'),
    ('SUPER GROUP LIMITED', 'SPG'),
    ('SYCOM PROPERTY FUND', 'SYC'),
    ('SYNERGY INCOME FUND LIMITED', 'SIFL'),
    ('TASTE HOLDINGS LIMITED', 'TAS'),
    ('TAWANA RESOURCES NL', 'TAW'),
    ('TELKOM SA LIMITED', 'TKG'),
    ('THABEX LIMITED', 'TBX'),
    ('THE BIDVEST GROUP LIMITED', 'BVT'),
    ('THE DB X-TRACKER COL INVEST SCHEME', 'DBX'),
    ('THE DON GROUP LIMITED', 'DON'),
    ('THE FOSCHINI GROUP LIMITED', 'TFG'),
    ('THE SPAR GROUP LIMITED', 'SPP'),
    ('THE ZSHARES ETF SCHEME', 'ZRNETF'),
    ('TIGER BRANDS LIMITED', 'TIIH'),
    ('TONGAAT HULETT LIMITED', 'THGL'),
    ('TRACKHEDGE (PTY) LIMITED', 'THG'),
    ('TRADEHOLD LIMITED', 'TDH'),
    ('TRANS HEX GROUP LIMITED', 'TSX'),
    ('TRANSPACO LIMITED', 'TPC'),
    ('TREMATON CAPITAL INVESTMENTS LTD', 'TMT'),
    ('TRENCOR LIMITED', 'TRE'),
    ('TRUWORTHS INTERNATIONAL LIMITED', 'TRU'),
    ('TSOGO SUN HOLDINGS LIMITED', 'TSH'),
    ('URANIUM ONE INC', 'UUU'),
    ('VALUE GROUP LIMITED', 'VLE'),
    ('VERIMARK HOLDINGS LIMITED', 'VMK'),
    ('VILLAGE MAIN REEF LIMITED', 'VIL'),
    ('VIVIDEND INCOME FUND LIMITED', 'VIF'),
    ('VODACOM GROUP LIMITED', 'VOD'),
    ('VUKILE PROPERTY FUND LIMITED', 'VKE'),
    ('VUNANI PROPERTY INVESTMENT FUND LTD', 'VPF'),
    ('WESCOAL HOLDINGS LIMITED', 'WSL'),
    ('WESIZWE PLATINUM LIMITED', 'WEZ'),
    ('WILSON BAYLY HOLMES-OVCON LIMITED', 'WBO'),
    ('WINHOLD LIMITED', 'WNH'),
    ('WITWATERSRAND CONS GOLD RESOURCES', 'WGR'),
    ('WOOLWORTHS HOLDINGS LIMITED', 'WOWOW'),
    ('YORK TIMBER HOLDINGS LIMITED', 'YRK'),
    ('ZCI LIMITED', 'ZCI'),
    ('ZEDER INVESTMENTS LIMITED', 'ZED'),
    ('ZURICH INSURANCE COMPANY S A LTD', 'ZSA')]
