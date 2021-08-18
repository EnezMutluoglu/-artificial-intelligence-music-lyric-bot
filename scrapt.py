import string
import requests
from bs4 import BeautifulSoup

class hayirdir:
    def __init__(self):
        self.base_url = "https://www.lyricsfreak.com"

    def get_cata(self):
        letters = string.ascii_lowercase
        result=list(map(lambda letter:self.base_url+"/{}_top.html".format(letter),letters))
        return result

    def get_cataa(self,data):
        resultt=list(map(lambda dataa:self.base_url+"{}".format(dataa),data))
        return resultt

    def get_source(self,url):
        r=requests.get(url)
        if r.status_code==200:
            return BeautifulSoup(r.content,"lxml")
        return False

    def get_all_links(self,source):
        return source.find_all("a")

    def get_all_linkss(self,source):
        return source.find_all("a",class_='lf-link lf-link--primary')

    def get_all_linkss_song(self,source):
        return source.find_all("div",class_="lyrictxt js-lyrics js-share-text-content")


    def get_links(self):
        data = list()
        datat = ['/top/', '/top_new/', '/updates/', '/lyrics_submit.php', '/', '/', '/top_artists/',
                 '/about/privacy_policy.htm', '/about/tos.htm']
        for i in datat:
            data.append(i)
        categori = self.get_cata()

        for i in categori:
            source = self.get_source(i)
            source_filter = self.get_all_links(source)
            for i in datat:
                data.remove(i)



            for i in source_filter:
                data.append(i['href'])

        return data

    def get_song_list(self):
        data = self.get_links()

        sub_data = self.get_cataa(data)

        datat = ['/top/', '/top_new/', '/updates/', '/lyrics_submit.php', '/', '/', '/top_artists/',
                 '/about/privacy_policy.htm', '/about/tos.htm', '/a_top.html', '/b_top.html', '/b_top.html',
                 '/c_top.html',
                 '/d_top.html', '/e_top.html', '/f_top.html', '/g_top.html', '/h_top.html', '/i_top.html',
                 '/j_top.html', '/k_top.html',
                 '/l_top.html', '/m_top.html', '/n_top.html', '/o_top.html', '/p_top.html', '/r_top.html',
                 '/s_top.html',
                 '/t_top.html', '/u_top.html', '/v_top.html', '/y_top.html', '/z_top.html']

        datadata = list()

        for i in sub_data:
            if i != "https://www.lyricsfreak.com" + datat[0]:
                if i != "https://www.lyricsfreak.com" + datat[1]:
                    if i != "https://www.lyricsfreak.com" + datat[2]:
                        if i != "https://www.lyricsfreak.com" + datat[3]:
                            if i != "https://www.lyricsfreak.com" + datat[4]:
                                if i != "https://www.lyricsfreak.com" + datat[5]:
                                    if i != "https://www.lyricsfreak.com" + datat[6]:
                                        if i != "https://www.lyricsfreak.com" + datat[7]:
                                            if i != "https://www.lyricsfreak.com" + datat[8]:
                                                datadata.append(i)

        allin = list()
        f = open("data.txt", "w")
        for so in datadata:
            source = self.get_source(so)
            filter_source = self.get_all_linkss(source)
            for dev in filter_source:
                f.write(dev["href"]+"\n")





if __name__=='__main__':
    scraper=hayirdir()

    for d in range(30000):
        try:
            file = open("data.txt", "r",encoding="utf-8")
            for o in file:
                data = o
                base_url = "https://www.lyricsfreak.com"
                datas=scraper.get_source(base_url+data)
                datass=scraper.get_all_linkss_song(datas)
                f = open("datass.txt", "w")
                f.write(str(datass))
                f.close()
                files = open("datass.txt", "r")
                files.readline()
                files.readline()
                files.readline()
                for i in files:
                    print(i[0:len(i)-6])
                    f = open("song.txt", "a")
                    f.write(i[0:len(i)-6])
                f.write("\n")
                f.close()
        except:
            print(data)
            filee = open("data.txt", "r", encoding="utf-8")
            dat=filee.read()
            if data in dat:
                with open("data.txt", "r") as f:
                    lines = f.readlines()
                    with open("data.txt", "w") as f:
                        for line in lines:
                            if line!=data:
                                f.write(line)


