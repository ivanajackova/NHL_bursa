from pathlib import Path  #Importuje třídu Path z Python knihovny pathlib, která slouží pro práci s cestami k souborům a složkám.
import os


BASE_DIR = Path(__file__).resolve().parent.parent  #v Pythonu (a konkrétně v Django) nastavuje proměnnou BASE_DIR tak, aby ukazovala na kořenovou složku projektu – tedy tam, kde je typicky soubor manage.py.



SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-@z5_t66(z^@ao!8au^%%_%vqokyn$crs0s_lv*d!jiov=g^n%-') #nastavuje tajný klíč pro Django aplikaci, který je nezbytný pro bezpečnost.


DEBUG = 'RENDER' not in os.environ #způsob, jak zapínat nebo vypínat režim ladění (DEBUG) podle prostředí,vývoj vs. produkce

ALLOWED_HOSTS = []  #prázdný seznam povolených hostitelů.
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


INSTALLED_APPS = [   #definice všech aplikací, které chcem ve svém Django projektu používat.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nhl_bursa.albums',
    'nhl_bursa.marketplace',
    'nhl_bursa.users',
    'nhl_bursa.messaging',
]




AUTH_USER_MODEL = 'users.CustomUser'
MIDDLEWARE = [  #Middleware je řetězec tříd, které Django spouští při každém požadavku/odpovědi – např. ochrana proti útokům, přihlašování, cookies, zprávy atd.
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # přidat tento řádek
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nhl_bursa.urls' #„Použij soubor urls.py ve složce nhl_bursa jako hlavní směrovač (router) URL adres.“

TEMPLATES = [  #nastavení HTML šablon
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nhl_bursa.wsgi.application'



import dj_database_url  #importuje externí Python knihovnu dj-database-url, která slouží ke snadné konfiguraci databáze v Django projektech – obzvlášť při nasazení na servery jako Render


DATABASES = {    #říká Djangu, jakou databázi má použít pro ukládání dat
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if 'DATABASE_URL' in os.environ:   #přepnutí databáze na produkční prostředí
    DATABASES['default'] = dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )


AUTH_PASSWORD_VALIDATORS = [  #nastavuje ověřování síly hesla
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', #Zabraňuje použití hesla, které je příliš podobné uživatelskému jménu, e-mailu nebo jinému údaji
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', #Vyžaduje minimální délku hesla (standardně 8 znaků)
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', #Blokuje běžná hesla jako 123456, password...
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', #Zakazuje hesla složená pouze z čísel
    },
]



LANGUAGE_CODE = 'en-us' #Nastavuje výchozí jazyk celé aplikace.

TIME_ZONE = 'UTC' #Určuje výchozí časové pásmo, které Django používá uvnitř aplikace.

USE_I18N = True #Zapíná mezinárodní podporu, aplikace podporuje různé jazyky

USE_TZ = True #Django bude pracovat s časem včetně časových zón, zobrazí čas podle nastavené zóny


STATIC_URL = '/static/' #Konfiguruje statické soubory v Django (např. CSS, JavaScript, obrázky).Určuje veřejnou URL adresu, odkud se budou statické soubory načítat ve webovém prohlížeči.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #Určuje složku, do které se při nasazení zkopírují všechny statické soubory z aplikací.


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' #Určuje výchozí typ pole pro primární klíče (id) v modelech, pokud to výslovně neuvedeš.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' #
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #Toto nastavení je povinné pro nasazení na Render, aby CSS/JS fungovalo správně. Říká Djangu, aby používal WhiteNoise k obsluze statických souborů.
