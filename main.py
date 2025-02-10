import wget
path = "C:\\Users\\Stables\\Downloads"
link = "https://github.com/abbodi1406/vcredist/releases/download/v0.86.0/VisualCppRedist_AIO_x86_x64.exe"
link2='https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-24.3.1-win10-win11-mar20-vega-polaris.exe'
entrada=input("gostaria de baixar o pacoto AIO do vc++ ?[Y/N]")
if entrada == "Y":
 wget.download(link , out="C:\\Users\\Stables\\Downloads") 
 print("\nta ai meu patrao!")
else:
 print("Beleza, meu rei!")

