import requests,json,os,random
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
Aiva = Console()
class githubmanz():
  def __init__(self):
    self.total = []
    self.count = 0
    self.count2 = 0
    self.ra = random.randint(0,255)
  def tanya(self):
    os.system("clear")
    Aiva.print("""╔════════════════════════════════════════════════════════╗
║ [bold white]Author   :[/] [bold rgb(0,255,255)]Xm4nXp[/]                       [red bold] Github Tools[/]  ║
║ [bold white]Github   :[/] [bold rgb(0,255,255)][not underline]https://github.com/Xm4nXp[/][/]    ╔══════════════║
║ [bold white]Version  :[/] [bold rgb(0,255,255)]v1[/]                           ║
╚════════════════════════════════════════════════════════╝""",style=f"color({self.ra})" )
    print(""" 1.Search By User\n 2.Search By Query""")
    try:
      with ThreadPoolExecutor(max_workers=40) as rahman:
        tanya = int(Aiva.input(" \nPilih [yellow bold]>[/] "))
        if tanya == 1:
          rahman.submit(self.getinfo)
        elif tanya == 2:
          rahman.submit(self.getrepo)
    except ValueError:
      print("Maman Ganz")
  def getinfo(self):
    try:
      user = Aiva.input("User [yellow bold]>[/] ")
      url = f"https://api.github.com/users/{user}"
      r = requests.get(url)
      iya = r.json()
      okz = iya["created_at"]
      if r.status_code == 200:
        anjaz = [requests.get(url+"/followers").json(),requests.get(url+"/following").json(),requests.get(url+"/repos").json()]
        repo = anjaz[2][:2:]
        for mamanganteng in anjaz[2]:
          self.total.append(mamanganteng["html_url"])
       #   print(mamanganteng["html_url"])
        for y in anjaz[0]:
          iyaz = list(y["login"].split(" "))
          self.count += len(iyaz)
          for zxmanz in anjaz[1]:
             iyaz = list(zxmanz["login"].split(" "))
             self.count2 += len(iyaz)
        Aiva.print(f"""\nName           : [green bold]{iya['login']}[/]\nCreate Account : [green bold]{okz}[/]\nFollowers      : [green bold]{self.count} [/]\nFollowing      : [green bold]{self.count2} [/]\nUrl            : [green bold][not underline]{iya["html_url"]}[/] [/]""")
        Aiva.rule("Repository Found",style="red bold")
        Aiva.print(f"[green bold]{self.total}[/]")
        Aiva.rule("akhir",style="red bold")
      elif r.status_code == 404:
        print("User Tidak Ditemukan")
    except KeyError:
      print("Kesalahan Tidak Diketahui")
  def getrepo(self):
      print("MainTenance !")
if __name__ == "__main__":
  githubmanz().tanya()
