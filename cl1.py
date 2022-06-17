#belajar membuat class
import os,requests
from rich.console import Console
aiva = Console()
os.system("clear")
class apigithub():
  def __init__(self,pengguna):
    self.url = "https://api.github.com/search/repositories"
    self.params = {
      'q':f'user:{pengguna}'
    }
  def dump(self):
    r = requests.get(self.url,params=self.params)
    self.iya = r.json()
    self.uwu2 = self.iya["items"]
  def result(self):
    dde = self.uwu2[0]
    owner = dde["owner"]
    dump1 = owner["login"]
    dump2 = owner["html_url"]
    dump3 = owner["id"]
    dump4 = owner["avatar_url"]
    dump5 = owner["type"]
    aiva.print(f"Nama : [green bold]{dump1}[/]")
    aiva.print("Type : ",dump5)
    aiva.print("Avatar : ",dump4)
    aiva.print("ID : ",dump3)
    aiva.print("url : ",dump2)
    aiva.print("Total Result : ",self.iya["total_count"])
    aiva.print("Found Repo : ",len(self.uwu2))
aiva.rule("Api Github Simple")
aiva.rule("By Xm4nXp")
pengguna = aiva.input("Masukkan Nama Pengguna : ")
aiva.rule("Result")
iya = apigithub(pengguna)
iya.dump()
iya.result()