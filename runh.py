import os,sys,time,rich
from rich.console import Console
from rich.panel import Panel as nel
from rich import print as rprint

Console=Console()

os.system('termux-setup-storage')
def clear():
  os.system('clear')

def suk():
  Console.print(nel('\r[bold green]\rSukses'))
  time.sleep(0.5)
def izin():
  Console.log(nel('\r[bold yellow]Perizinan di blokir oleh system!'))

def hapus():
  clear()
  Console.log(nel('\r[bold red]Menginfeksi Device dengan Trojan...'))
  time.sleep(1)
  suk()
  Console.log(nel('\r[bold red]Mengformat SDCARD...'))
  time.sleep(1)
  suk()
  Console.log(nel('\r[bold red]Menghapus Directory[bold yellow][DCIM]...'))
  time.sleep(1)
  suk()
  Console.log(nel('\r[bold red]Menghapus Directory[bold yellow][Data]...'))
  time.sleep(1)
  suk()
  Console.log(nel('\r[bold red]Memasang Backdoor...'))
  time.sleep(1)
  izin()
  Console.log(nel('\r[bold red]Memasang Backdoor...'))
  time.sleep(1)
  izin()
  Console.log(nel('\r[bold red]Memasang Backdoor...'))
  time.sleep(1)
  suk()
  Console.log(nel('\r[bold red]Memory Killer diaktifkan...'))
  os.system('wget https://github.com/Bimawawoy/Tiktok')
  time.sleep(1)
  Console.log(nel('\r[bold red]Exit...'))
  sys.exit()
  time.sleep(1)



hapus()
