import socket
import platform
from time import sleep
from os import getcwd
from platform import system
from rich import print as rprint
from rich.progress import Progress
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
import psutil
from binascii import hexlify
from base64 import b64decode, b64encode

class Base:
    def __init__(self):
        pass

    def local_ip(self):
        localhost = socket.gethostname()
        local_ip = socket.gethostbyname(localhost)
        rprint(f"[bold blue]Hostname: {localhost}[bold blue]")
        rprint(f"[bold blue]local IP: {local_ip}[bold blue]")

    def ip(self):
        addrs = psutil.net_if_addrs()
        for interface, addr_list in addrs.items():
            rprint(f"\n[bold blue]Interface: {interface}[bold blue]")
            for addr in addr_list:
                if addr.family == socket.AF_INET:
                    rprint(f"[bold blue]  IPv4 Address: {addr.address}[bold blue]")
                elif addr.family == socket.AF_INET6:
                    rprint(f"[bold blue]  IPv6 Address: {addr.address}[bold blue]")

    def sys_info(self):
        rprint(f"[bold blue] Версия системы: {platform.platform()}[bold blue]")
        rprint(f"[bold blue] Machine: {platform.machine()}[bold blue]")
        rprint(f"[bold blue] Текущая директория: {getcwd()}[bold blue]")

    def full_info_system(self):
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        rprint(f"[bold blue] ОС: {platform.system()}[bold blue]")
        rprint(f"[bold blue] Версия ОС: {platform.release()}[bold blue]")
        rprint(f"[bold blue] Архитектура: {platform.machine()}[bold blue]")
        rprint(f"[bold blue] Процессор: {platform.processor()}[bold blue]")
        rprint(f"[bold blue] Полная инфо ОС: {platform.platform()}[bold blue]")
        rprint(f"[bold blue] CPU usage: {psutil.cpu_percent(interval=1)} %[bold blue]")
        rprint(f"[bold blue] Total RAM: {ram.total / (1024**3):.2f} GB[bold blue]")
        rprint(f"[bold blue] Used RAM: {ram.used / (1024**3):.2f} GB[bold blue]")
        rprint(f"[bold blue] Total Disk: {disk.total / (1024**3):.2f} GB[bold blue]")
        rprint(f"[bold blue] Free Disk: {disk.free / (1024**3):.2f} GB[bold blue]")
    
class Blocker:
    def __init__(self):
        self.resident = "127.0.0.1"
        self.bloks = []
        self.console = Console()
        plat = system()
        if plat == "Windows":
            self.plat = r"C:\Windows\System32\drivers\etc\hosts"
        elif plat == "Linux" or plat == "Mac":
            self.plat =  r"/etc/hosts"
 
    def unblock_site(self):
        try:
            ndex = 0
            site = input("Введите ссылку: ")
            host = self.plat
            with open(host, "r") as file:
                content = file.readlines()
                ndex = content.index(f"{self.resident} {site}\n")
                line_to_delete = ndex+1

            progress = Progress()
            progress.start()
            try:
                task2 = progress.add_task("[green]В процессе...", total=1000)
                while not progress.finished:
                    progress.update(task2, advance=1.7)
                    sleep(0.002)
            except PermissionError as e:
                rprint(f"[bold red]Error: {e}[bold red]")
            finally:
                progress.stop()

            with open(host, 'r', ) as f:
                lines = f.readlines()
            new_lines = []
            for i, line in enumerate(lines):
                if i != line_to_delete - 1:
                    new_lines.append(line)

            with open(host, 'w') as f:
                f.writelines(new_lines)
        except PermissionError as e:
            rprint(f"[bold red]Error: {e}[bold red]")
        
        except ValueError as er:
            rprint(f"[bold red]Error: {er}[bold red]")

    def block_site(self):
        site = input("Введите ссылку: ")
        self.bloks.append(site)
        host = self.plat
        progress = Progress()
        progress.start()
        try:
            task2 = progress.add_task("[green]В процессе...", total=1000)
            while not progress.finished:
                progress.update(task2, advance=1.6)
                sleep(0.002)
        finally:
            progress.stop()
        try:
            with open(host, "r+") as file:
                content = file.read()
                for site in self.bloks:
                    if site in content:
                        pass
                    else:
                        file.write(f"{self.resident} {site}\n")
        except PermissionError as e:
            rprint(f"[bold red]Error: {e}[bold red]")
            rprint(f"[bold red]Run with admin rights[bold red]")

    def get_blocks(self):
        num = 0
        host = self.plat
        table = Table(title="Заблокированные сайты")
        table.add_column("номер", justify="center", style="green")
        table.add_column("сайт", justify="left", style="red")
        
        with open(host, "r") as file:
            content = file.readlines()
        for i in range(len(content)):
            con = content[i].split(" ")
            if "#" in con[0] or con[0] == '\n':
                pass
            else:
                try:
                    table.add_row(f"{num}", con[1])
                except IndexError:
                    pass
                num+=1
        self.console.print(table)

class Decoder:
    def __init__(self):
        pass

    def to_two(self):
        choice = Prompt.ask("Перевести..", choices=["из", "в"], default="в")
        try:
            if choice == "из":
                promt = input("Введите текст: ")
                byte_list = [int(promt[i:i+8], 2) for i in range(0, len(promt), 8)]
                binary_text = bytes(byte_list).decode("utf-8")
                rprint(f"[bold green] Ваш код в тексте: {binary_text} [bold green]")
            elif choice == "в":
                promt = input("Введите текст: ")
                binary_text = ' '.join(format(byte,"08b") for byte in promt.encode())
                rprint(f"[bold green] Ваш текст в двоично коде: {binary_text} [bold green]")
        except Exception as e:
            rprint(f"[bold red] Error: произошла ошибка, убедитесь что вы верно ввели текст/код и повторите попытку [bold red]")
            rprint(f"[bold red] Error: {e} [bold red]")
    
    def to_base64(self):
        choice = Prompt.ask("Перевести..", choices=["из", "в"], default="в")
        try:
            if choice == "из":
                promt = input("Введите код: ")
                b64_text = b64decode(promt).decode("utf-8")
                rprint(f"[bold green] Ваш код B64 в тексте: {b64_text} [bold green]")
            elif choice == "в":
                promt = input("Введите текст: ")
                b64_bytes = b64encode(promt.encode("utf-8"))
                b64_text = b64_bytes.decode()
                rprint(f"[bold green] Ваш текст в B64: {b64_text} [bold green]")
        except Exception as e:
            rprint(f"[bold red] Error: произошла ошибка, убедитесь что вы верно ввели текст/код и повторите попытку [bold red]")
            rprint(f"[bold red] Error: {e} [bold red]")
    
    def to_hex(self):
        
        choice = Prompt.ask("Перевести..", choices=["из", "в"], default="в")
        try:
            if choice == "из":
                promt = input("Введите код: ")
                hex_string = bytes.fromhex(promt).decode('utf-8')
                rprint(f"[bold green] Ваш код HEX в тексте: {hex_string} [bold green]")
            elif choice == "в":
                promt = input("Введите текст: ")
                hex_str = hexlify(promt.encode()).decode()
                rprint(f"[bold green] Ваш текст в HEX: {hex_str} [bold green]")
        except Exception as e:
            rprint(f"[bold red] Error: произошла ошибка, убедитесь что вы верно ввели текст/код и повторите попытку [bold red]")
            rprint(f"[bold red] Error: {e} [bold red]")
