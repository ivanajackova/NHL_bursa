
import os   #Importuje Python knihovny pro práci s proměnnými prostředí
import sys  #Importuje Python knihovny pro práci s parametry příkazové řádky (`sys.argv`)



def main():
    #Definuje funkci main(), která se použije, když se skript spustí jako program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nhl_bursa.settings') #Říká Djangu: „Použij nastavení ze souboru `settings.py` ve složce `nhl_bursa`.
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    #Pokusí se importovat funkci execute_from_command_line, která umožní vykonat příkaz jako např. python manage.py runserver.

if __name__ == '__main__':
    main()
    #Tento blok zajistí, že se funkce `main()` spustí jen tehdy, když je `manage.py` spuštěn přímo, ne když je importován z jiného souboru.