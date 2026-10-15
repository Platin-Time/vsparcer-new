from classes import Decoder, Base, Blocker
from rich import print as rprint
from rich.prompt import Prompt
from datetime import datetime
global log_root
log_root = False

def log__(logs, type):
    if log_root:
        match type:
            case "INFO":
                rprint(f"[green]{datetime.now()}: {type}: {logs} [green]")
            case "WARNING":
                rprint(f"[yellow]{datetime.now()}: {type}: {logs} [yellow]")
            case "ERROR":
                rprint(f"[red]{datetime.now()}: {type}: {logs} [red]")
            case "DEBUG":
                rprint(f"[grey]{datetime.now()}: {type}: {logs} [grey]")
            case _:
                rprint(f"[bold grey](type is undifined): {datetime.datetime.now()}: {logs} [bold grey]")
def main():
    log__("прогамма запущена","INFO")
    while True:
        rprint("[bold green]Список комманд: \n 1 - Декодер \n 2 - Блокировщик сайтов \n 3 - База \n 4 - Логи(для разраба) \n 5 - Выход [bold green]")
        promt = input("Ваш выбор: ")
        match promt: 
            case '1':
                decode = Decoder()
                decode_tf = True
                while decode_tf:
                    rprint("[bold green]Выбери действие \n 1 - Двоичный код \n 2 - HEX \n 3 - Base64 \n 4 - Выход в главное меню [bold green]")
                    promt1 = input("Ваш выбор: ")
                    match promt1:
                        case "1":
                            decode.to_two()
                            log__("Успешно","INFO")
                        case "2":
                            decode.to_hex()
                            log__("Успешно","INFO")
                        case "3":
                            decode.to_base64()
                            log__("Успешно","INFO")
                        case "4":
                            log__("Выход в главное меню","INFO")
                            decode_tf = False
                        case _:
                            rprint("[bold red]Error: Нет такого варианта[bold red]")
                            log__("Нету такого варианта","ERROR")
            case '2':
                block = Blocker()
                block_tf = True
                while block_tf:
                    rprint("[bold green]Выбери действие \n 1 - Заблокировать сайт \n 2 - Разблокировать сайт \n 3 - Список заблокированных сайтов \n 4 - Выход в главное меню [bold green]")
                    promt1 = input("Ваш выбор: ")
                    match promt1:
                        case "1":
                            block.block_site()
                            log__("Успешно","INFO")
                        case "2":
                            block.unblock_site()
                            log__("Успешно","INFO")
                        case "3":
                            block.get_blocks()
                            log__("Успешно","INFO")
                        case "4":
                            log__("Выход в главное меню","INFO")
                            block_tf = False
                        case _:
                            rprint("[bold red]Error: Нет такого варианта[bold red]")
                            log__("Нету такого варианта","ERROR")
            case '3':
                basa = Base()
                base_tf = True
                while base_tf:
                    rprint("[bold green]Выбери действие  \n 1 - Локальный IP-адрес \n 2 - IP-адрес \n 3 - Инфо о ОС \n 4 - Полная инфо о ОС \n 5 - Выход в главное меню[bold green]")
                    promt1 = input("Ваш выбор: ")
                    match promt1:
                        case "1":
                            basa.local_ip()
                            log__("Успешно","INFO")
                        case "2":
                            basa.ip()
                            log__("Успешно","INFO")
                        case "3":
                            basa.sys_info()
                            log__("Успешно","INFO")
                        case "4":
                            basa.full_info_system()
                            log__("Успешно","INFO")
                        case "5":
                            log__("Выход в главное меню","INFO")
                            base_tf = False
                        case _:
                            rprint("[bold red]Error: Нет такого варианта[bold red]")
                            log__("Нету такого варианта","ERROR")
            case '4':
                global log_root
                rprint(f"[bold red] Логи: {log_root}[bold red]")
                choice = Prompt.ask("Включить логи?", choices=["да", "нет"], default="нет")
                if choice == "да":
                    log_root = True
                    rprint("[bold red] Логи:[bold red]",f"[bold green]{log_root}[bold green]")
                elif choice == "нет":
                    log_root = False
                    rprint(f"[bold red] Логи:[bold red]",f"[bold red]{log_root}[bold red]")
            case '5':
                log__("Остановка программы","INFO")
                break
            case _:
                log__("Нету такого варианта","ERROR")

rprint("[bold red] 'VSPARCER' by PlatinTime [bold red]")
rprint("[red]   V1.0 [red]")

if __name__ == "__main__":
    main()
