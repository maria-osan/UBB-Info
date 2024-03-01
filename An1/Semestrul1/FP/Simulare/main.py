from domain.validators import ValidateImobil
from repository.imobil_repo import ImobilFileRepo
from service.imobil_service import ImobilService
from ui.console import Console

repo_file_imobil = ImobilFileRepo('imobile.txt')
validare_imobil = ValidateImobil
service_imobil = ImobilService(repo_file_imobil, validare_imobil)

ui_console = Console(service_imobil)

ui_console.agentie_imobiliara()
