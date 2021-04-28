__all__ = ['Scraper_CS', 'Scraper_Fundinfo', 'Scraper_Morningstar_CH', 'Scraper_DIV',
           'Scraper_Swisscanto', 'Scraper_UBS_CH', 'Scraper_UBS_AST','CSV_Collector',
           'Scraper_Tramondo', 'Scraper_Morningstar_DE','Scraper_UBS_SWISS',
           'Scraper_Fundsquare', 'Scraper_CS_FX', 'Scraper_SwissFundData']
from .Scraper_CS import cs
from .Scraper_Fundinfo import fundinfo
from .Scraper_Morningstar_CH import morningstar_CH
from .Scraper_DIV import div
from .Scraper_Swisscanto import swisscanto
from .Scraper_UBS_AST import ubs_AST
from .Scraper_UBS_CH import ubs_CH
from .Scraper_UBS_SWISS import ubs_swiss
from .Scraper_Tramondo import tramondo
from .Scraper_Morningstar_DE import morningstar_DE
from .Scraper_Fundsquare import fundsquare
from .Scraper_CS_FX import cs_fx
from .Scraper_SwissFundData import SwissFundData
from .CSV_Collector import collector



