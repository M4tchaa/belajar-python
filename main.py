from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "https://www.minecraft.net/en-us"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.prettify()) #tester