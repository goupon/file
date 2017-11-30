import httplib
import urllib,urllib2,re,sys
import cookielib,os,string,cookielib,StringIO,gzip
import os,time,base64,logging
from t0mm0.common.net import Net
import xml.dom.minidom
import xbmcaddon,xbmcplugin,xbmcgui
try: import simplejson as json
except ImportError: import json
import cgi
import datetime
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import SoupStrainer
import urlresolver

PLUGIN = xbmcaddon.Addon(id='plugin.video.MegaKhmerDubbed')
addon_name = 'plugin.video.MegaKhmerDubbed'

KHMERAVE ='http://www.khmeravenue.com/'
KHMERSTREAM ='http://www.khmerstream.net/'
MERLKON ='http://www.merlkon.net/'
KMERDRA = 'http://www.khmerdrama.com/'
JOLCHET7 ='http://www.khmotion.com/'
VIDEO4U ='http://www.video4khmer19.com/'
FILM4KH ='http://www.ckh7.com/'
KHDRAMA ='http://www.khdrama24.com/'
HOTKHMER ='http://www.khmerkomsan.co/'
KHMERALL = 'http://www.khmer6.ga/'
K8MER = 'http://asialakorn.com/'
TUBE_KHMER ='http://www.khmer.video/'
PHUMIKHMER = 'http://phumikhmer.media/'
PHUMIKHMER1 ='http://phumikhmer.club/'
PHUMIKHMER2 ='http://www.phumikhmer1.com/'
LAKORNKHMER = 'http://lakhoan.com/'

USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1"
datapath = xbmc.translatePath('special://profile/addon_data/'+addon_name)
cookiejar = os.path.join(datapath,'khmerstream.lwp')
ADDON_PATH = PLUGIN.getAddonInfo('path')
sys.path.append( os.path.join( ADDON_PATH, 'resources', 'lib' ) )
from net import Net
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import CommonFunctions #For VIMEO
common = CommonFunctions
net = Net()

pluginhandle = int(sys.argv[1])

# example of how to get path to an image

fanart = os.path.join(ADDON_PATH, 'resources', 'images','fanart.jpg')
TubekhmerImage = os.path.join(ADDON_PATH, 'resources', 'images','tk.jpg')

def OpenURL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link 

def OpenSoup(url):
    req = urllib2.Request(url)
    req.add_unredirected_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0')
    response = urllib2.urlopen(req).read()
    return response

def HOME():
        addDir('ASIALAKOR',K8MER,80,'http://asialakorn.com/wp-content/uploads/2015/05/123.png')
        addDir('CKH7',FILM4KH,40,'http://www.ckh7.com/uploads/custom-logo.png')
        addDir('KHDRAMA',KHDRAMA,50,'http://www.khdramas24.com/img/khdram.png')	
        addDir('KHMOTION',JOLCHET7,20,'http://2.bp.blogspot.com/-VvXKIY58csE/WBWJzk8EYeI/AAAAAAAABNc/CTJKHQnXVj4X-hXYeG_-JsepSAYOa0FFwCK4B/s1600/new%2Blogo.png')
        addDir('KOMSAN',HOTKHMER,60,'http://www.khmerkomsan.co/templates/default/img/KhmerKomsan.png')
        addDir('LAKHOAN',LAKORNKHMER,100,'http://2.bp.blogspot.com/-nT9gH29nfCc/VTfq8tvfM9I/AAAAAAAACjU/2NGWGjNh8_Y/s1600/lakhaonlogo%2Bcopy.png')
        addDir('MERLKON',MERLKON,10,'http://www.merlkon.net/wp-contents/uploads/logo.jpg')
        addDir('NIYEAYKHMER',KHMERALL,130,'https://pbs.twimg.com/profile_images/484906745483886592/UppABZdI_400x400.png')
        addDir('TUBE-PHUMI KHMER ',TUBE_KHMER,90,TubekhmerImage+'')
        addDir('VIDEO4U',VIDEO4U,30,'http://www.video4khmer19.com/templates/kulenkiri/images/header/logo.png')


############## ASIALAKOR SITE ******************
		
def K8MERS():
        addDir('Chinese Drama',K8MER+'category/home/chinese-series/',81,'http://phumikhmerblog.files.wordpress.com/2017/05/6.jpg')
        addDir('Thai Drama',K8MER+'category/home/thai-lakorn/',81,'https://phumikhmerblog.files.wordpress.com/2017/07/form-thai-movie.png?w=300')
        addDir('Korean Drama',K8MER+'category/home/korea-drama/',81,'http://www.khmer89.com/uploads/thumbs/3d40ad547-1.jpg')		
		
				
def INDEX_K8MER(url):
         html = OpenSoup(url)
         try:
             html = html.encode("UTF-8")
         except: pass
         soup = BeautifulSoup(html.decode('utf-8'))
         div_index = soup('div',{"class":"item-thumbnail"})
         for link in div_index:
             vLink = BeautifulSoup(str(link))('a')[0]['href']
             vLink = vLink.encode("UTF-8",'replace')
             print vLink
             vTitle = BeautifulSoup(str(link))('img')[0]['title']
             vTitle = vTitle.encode("UTF-8",'replace')
             print vTitle
             vImage = BeautifulSoup(str(link))('img')[0]['src']
             print vImage
             addDir(vTitle,vLink,85,vImage)
         pages=re.compile('"nextLink":"(.+?)",').findall(html)
         for pageurl in pages:
            addDir("[B][COLOR blue]%s >>[/B][/COLOR]"% 'NEXT PAGE',pageurl.replace("\/",'/'),81,"")
			
def EPISODE_K8MER(url,name):
         html = OpenSoup(url)
         addLink(name,url,3,'')
         try:
             html = html.encode("UTF-8")
         except: pass
         soup = BeautifulSoup(html.decode('utf-8'))
         epis = soup('a',{"class":"btn btn-sm btn-default "})
         for link in epis:
             vLink = BeautifulSoup(str(link))('a')[0]['href']
             print vLink
             vTitle = BeautifulSoup(str(link))('a')[0]['title']
             print vTitle
             addLink(vTitle,vLink,3,'')	
		
		
########## START MERLKON ***********

def MERLKONS():#10
        addDir('Chinese Modern (KA)',KHMERAVE+'genre/modern-series/',13,'http://phumikhmerblog.files.wordpress.com/2017/05/6.jpg')
        addDir('Chinese Ancient (KA)',KHMERAVE+'genre/ancient-series/',13,'https://phumikhmerblog.files.wordpress.com/2017/05/phumikhmer.jpg')
        addDir('Chinese Modern (KS)',KHMERSTREAM+'genre/modern-chinese/',12,'http://phumikhmerblog.files.wordpress.com/2017/05/6.jpg')
        addDir('Chinese Ancient (KS)',KHMERSTREAM+'genre/ancient-chinese/',12,'https://phumikhmerblog.files.wordpress.com/2017/05/phumikhmer.jpg')
        addDir('Korean Ancient',KHMERSTREAM+'genre/ancient-korean/',12,'http://www.khmer89.com/uploads/thumbs/c8810789c-1.jpg')
        addDir('Korean Moderm',KHMERSTREAM+'genre/korean/',12,'http://www.khmer89.com/uploads/thumbs/3d40ad547-1.jpg')
        addDir('Mayura',MERLKON+'dubbed/mayura/',11,'https://phumikhmerblog.files.wordpress.com/2017/07/form-thai-movie.png?w=300')      
        addDir('Thai Drama',MERLKON+'genre/modern-thai/',11,'http://www.phumi-thai9.com/images/subcat/2674/5007.jpg')
        addDir('Thai Boran',MERLKON+'genre/thai-boran/',11,'https://phumikhmerblog.files.wordpress.com/2017/06/form-thai-movie.png')
        addDir('Thai Horror',MERLKON+'genre/horror/',11,'https://phumikhmerblog.files.wordpress.com/2017/06/1b3d0-logo.png')
        addDir('Thai Air',KMERDRA+'thai-lakorn',14,'http://www.khmerdrama.com/wp-content/uploads/2017/02/kd-logo.png')	
		
def INDEX_MERLKON(url):
        html = OpenSoup(url)
        try:   
           html =html.encode("UTF-8")
        except: pass
        soup = BeautifulSoup(html.decode('utf-8'))
        div_index = soup('div',{'style':"float:left;width:100%; height:125px;overflow:hidden;padding:4px;border: 1px solid silver; background-color:#ffffff"})
        for link in div_index:
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('a')[0]['title']
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            vTitle = vTitle.encode("UTF-8",'replace')
            addDir(vTitle,vLink,15,vImage)
        match5=re.compile('<div class=\'wp-pagenavi\'>\n(.+?)\n</div>').findall(html)
        if(len(match5)):
           pages=re.compile('<a class=".+?" href="(.+?)">(.+?)</a>').findall(match5[0])
           for pageurl,pagenum in pages:
               addDir(" Page " + pagenum,pageurl.encode("utf-8"),11,"")                        
    
        xbmcplugin.endOfDirectory(pluginhandle)

def INDEX_KHMERSTREAM(url):
        html = OpenSoup(url)
        try:   
           html =html.encode("UTF-8")
        except: pass
        soup = BeautifulSoup(html.decode('utf-8'))
        div_index = soup('div',{'style':"float:left;width:100%; height:125px;overflow:hidden;padding:4px;border: 1px solid silver; background-color:#ffffff"})
        for link in div_index:
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('a')[0]['title']
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            vTitle = vTitle.encode("UTF-8",'replace')
            addDir(vTitle,vLink,15,vImage)
        match5=re.compile('<div class=\'wp-pagenavi\'>\n(.+?)\n</div>').findall(html)
        if(len(match5)):
           pages=re.compile('<a class=".+?" href="(.+?)">(.+?)</a>').findall(match5[0])
           for pageurl,pagenum in pages:
               addDir(" Page " + pagenum,pageurl.encode("utf-8"),12,"")                        
    
        xbmcplugin.endOfDirectory(pluginhandle)

def INDEX_KHMERAVE(url):    
        html = OpenSoup(url)
        try:   
           html =html.encode("UTF-8")
        except: pass
        soup = BeautifulSoup(html.decode('utf-8'))
        div_index = soup('div',{'style':"float:left;width:100%; height:125px;overflow:hidden;padding:4px;border: 1px solid silver; background-color:#ffffff"})
        for link in div_index:
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('a')[0]['title']
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            vTitle = vTitle.encode("UTF-8",'replace')
            addDir(vTitle,vLink,15,vImage)
        match5=re.compile('<div class=\'wp-pagenavi\'>\n(.+?)\n</div>').findall(html)
        if(len(match5)):
           pages=re.compile('<a class=".+?" href="(.+?)">(.+?)</a>').findall(match5[0])
           for pageurl,pagenum in pages:
               addDir(" Page " + pagenum,pageurl.encode("utf-8"),13,"")                        
    
        xbmcplugin.endOfDirectory(pluginhandle)

def EPISODE_MERLKON(url,name):
        link = OpenURL(url)
        addLink(name,url,3,'')
        match=re.compile('<a href="(.+?)"><span class="part">(.+?)</span></a>').findall(link)     
        if(len(match) == 0):
          match=re.compile('<a href="(.+?)"><span style=".+?">(.+?)</span></a>').findall(link)
        for vLink, vLinkName in match:
            addLink(vLinkName,vLink,3,'')
        xbmcplugin.endOfDirectory(pluginhandle)		
		
def INDEX_KMERDRA(url):    
        html = OpenSoup(url)
        try:   
           html =html.encode("UTF-8")
        except: pass
        soup = BeautifulSoup(html.decode('utf-8'))
        div_index = soup('div',{'style':"width:100%; height:105px;overflow:hidden;padding:4px;border: 1px solid silver; background-color:#ffffff"})
        for link in div_index:
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('img')[0]['alt']
            vTitle = vTitle.encode("UTF-8",'replace')
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            addDir(vTitle,vLink,16,vImage)
        match5=re.compile('<div class=\'wp-pagenavi\'>\n(.+?)\n</div>').findall(html)
        if(len(match5)):
           pages=re.compile('<a class=".+?" href="(.+?)">(.+?)</a>').findall(match5[0])
           for pageurl,pagenum in pages:
               addDir(" Page " + pagenum,pageurl.encode("utf-8"),14,"")                 
        xbmcplugin.endOfDirectory(pluginhandle)
		
def EPISODE_KMERDRA(url,name):
        link = OpenURL(url)
        try:
             link = link.encode("UTF-8")
        except: pass
        match=re.compile('{\s*"file":\s*"(.+?)",\s*"title":\s*"(.+?)",\s*"description":\s*".+?",\s*"image":\s*"(.+?)"').findall(link)			
        if(len(match) > 0):      
         for vLink,vLinkName,vImage in match:                 
          addLink(vLinkName,vLink,4,vImage)				
        
         
######## START VIDEO4U ***************
def VIDEO4YOU():#30
        addDir('Chinese Drama',VIDEO4U+'khmer-movie-category/chinese-series-drama-watch-online-free-catalogue-506-page-1.html',31,'https://phumikhmerblog.files.wordpress.com/2017/05/phumikhmer.jpg')   
        addDir('Chinese Cont',VIDEO4U+'khmer-movie-category/chinese-series-drama-to-be-continued-catalogue-2673-page-1.html',31,'http://phumikhmerblog.files.wordpress.com/2017/05/6.jpg')   
        addDir('Khmer Drama',VIDEO4U+'khmer-movie-category/khmer-drama-watch-online-free-catalogue-504-page-1.html',31,'http://www.khmer89.com/uploads/thumbs/060e552ce-1.jpg')
        addDir('Korean Drama',VIDEO4U+'khmer-movie-category/korean-drama-watch-online-free-catalogue-507-page-1.html',31,'http://www.khmer89.com/uploads/thumbs/3d40ad547-1.jpg')
        addDir('Thai Drama',VIDEO4U+'khmer-movie-category/thai-lakorn-drama-watch-online-free-catalogue-537-page-1.html',31,'http://www.phumi-thai9.com/images/subcat/2674/5007.jpg')
        addDir('Thai Cont',VIDEO4U+'khmer-movie-category/thai-lakorn-drama-to-be-continued-catalogue-2674-page-1.html',31,'https://phumikhmerblog.files.wordpress.com/2017/06/1b3d0-logo.png')		
        addDir('Chinese Movie',VIDEO4U+'khmer-movie-category/chinese-movie-watch-online-free-catalogue-505-page-1.html',31,'http://file.hotkhmer.com/wp-content/uploads/2017/02/Komsan9-108-300x300.jpg')  
        addDir('Thai Movie',VIDEO4U+'khmer-movie-category/thai-movie-watch-online-free-catalogue-525-page-1.html',31,'http://file.hotkhmer.com/wp-content/uploads/2017/02/Komsan9-34-300x300.jpg')
        addDir('Khmer Movie',VIDEO4U+'khmer-movie-category/thai-movie-watch-online-free-catalogue-503-page-1.html',31,'http://www.khmer89.com/uploads/thumbs/4c9cf04ce-1.jpg')
		
def INDEX_VIDEO4U(url):
        html = OpenSoup(url)
        try:   
           html =html.encode("UTF-8")
        except: pass
        soup = BeautifulSoup(html.decode('utf-8'))
        div_index = soup('div',{'class':"cat-thumb"})
        for link in div_index:
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('img')[0]['title']
            vTitle = vTitle.encode("UTF-8",'replace')
            addDir(vTitle,vLink,35,vImage)
        try:
           paging = soup('div',{'class':'pagination'})
           pages = BeautifulSoup(str(paging[0]))('a')
           for p in pages:
             psoup = BeautifulSoup(str(p))
             pageurl = psoup('a')[0]['href']
             pagenum = psoup('a')[0].contents[0].replace("&gt;",">").replace("&lt;","<")
             addDir(" Page " + pagenum.encode("utf-8") ,pageurl,31,"")
        except:pass  
     
def EPISODE_VIDEO4U(url,name):
    #try:
        link = OpenSoup(url)
        try:
            link =html.encode("UTF-8")
        except: pass
        newlink = ''.join(link.splitlines()).replace('\t','')
        soup = BeautifulSoup(newlink)
        listcontent=soup.findAll('div', {"id" : "content-center"})
        for item in listcontent[0].findAll('div', {"class" : "movie-thumb"}):
			vname=item.a.img["alt"]
			vname = vname.encode("UTF-8",'replace')   
			vurl=item.a["href"]
			vimg=item.a.img["src"]
			addLink(vname,vurl,3,vimg)

        for item in listcontent[0].findAll('li'):
             if(item.a!=None):
				pageurl=item.a["href"]
				pagenum=item.a.contents[0].replace("&gt;",">").replace("&lt;","<")
				addDir("Page " + pagenum,pageurl,35,"")
	 
def EPISODE4U(url,name):        
        link = OpenURL(url)
        match=re.compile('<div class=".+?"><div class="movie-thumb"><a href="(.+?)"><img src="(.+?)" alt=".+?" title="(.+?)" width="180" height="170"').findall(link)
        counter = 1
        if (len(match) >= 1):
           for vLink,Vimage,vLinkName in match:
               counter += 1
               addLink(vLinkName,vLink,3,Vimage)
        match5=re.compile('<div class="pagination">(.+?)</div>').findall(link)
        if(len(match5)):
           pages=re.compile('<a href="(.+?)">(.+?)</a>').findall(match5[0])
           for pageurl,pagenum in pages:
               addDir(" Page " + pagenum.encode("utf-8"),pageurl,35,"")     
           xbmcplugin.endOfDirectory(pluginhandle)


############## START KHMOTION **********
def JOLCHET():####MODE===20
        addDir('Chinese Drama',JOLCHET7+'search/label/Chinese%20Drama?&max-results=20',21,'http://phumikhmerblog.files.wordpress.com/2017/05/6.jpg')
        addDir('Thai Drama',JOLCHET7+'search/label/Thai%20Drama?&max-results=20',21,'https://phumikhmerblog.files.wordpress.com/2017/07/form-thai-movie.png?w=300')
        addDir('Korean Drama',JOLCHET7+'search/label/Korean%20Drama?&max-results=20',21,'http://www.khmer89.com/uploads/thumbs/3d40ad547-1.jpg')		

def INDEX_J(url):     
        link = OpenURL(url)
        try:
            link =link.encode("UTF-8")
        except: pass
        match=re.compile('<h2 class=\'post-title entry-title index\' itemprop=\'name headline\'>\n<a href=\'(.+?)\' itemprop=\'url\'>(.+?)</a>\n</h2>\n<meta content=\'(.+?)\'').findall(link)
        for vurl,vname,vimage in match:
            addDir(vname,vurl,25,vimage)
        pages=re.compile('<span id=\'.+?\'>\n<a class=\'.+?\' href=\'([^"]+?)\' id=\'.+?\' title=\'.+?\'>(.+?)</a>\n</span>').findall(link)
        for pageurl,pagenum in pages:
               addDir("[B][COLOR blue]<<<%s>>>[/B][/COLOR]"% pagenum,pageurl,21,"")                        
        xbmcplugin.endOfDirectory(pluginhandle)
  
def EPISODE_J(url,name):    
        link = OpenURL(url)
        try:
             link = link.encode("UTF-8")
        except: pass
        match=re.compile('{\s*"file":\s*"(.+?)",\s*"title":\s*"(.+?)",').findall(link)     
        if(len(match) > 0):      
         for vLink,vLinkName in match:                 
          addLink(vLinkName,vLink,4,'')          


############## START FILM2US **********           
def FILM2US():
        addDir('Chinese Drama',FILM4KH+'category.php?cat=chinese-drama',41,'https://phumikhmerblog.files.wordpress.com/2017/05/phumikhmer.jpg')
        addDir('Chinese Movie',FILM4KH+'category.php?cat=chinese-movie',41,'http://file.hotkhmer.com/wp-content/uploads/2017/02/Komsan9-108-300x300.jpg')
        addDir('Korean Drama',FILM4KH+'category.php?cat=korean-drama',41,'http://www.khmer89.com/uploads/thumbs/c8810789c-1.jpg')
        #addDir('Korean Movie',FILM4KH+'khmer-korean-movie-dubbed',41,'http://www.khmer89.com/uploads/thumbs/3d40ad547-1.jpg')
        #addDir('Khmer Drama',FILM4KH+'khmer-drama-dubbed',41,'http://www.khmer89.com/uploads/thumbs/060e552ce-1.jpg')
        #addDir('Khmer Movie',FILM4KH+'khmer-movie-dubbed',41,'http://www.khmer89.com/uploads/thumbs/4c9cf04ce-1.jpg')
        addDir('Thai Drama',FILM4KH+'category.php?cat=thai-drama',41,'https://phumikhmerblog.files.wordpress.com/2017/07/form-thai-movie.png?w=300')
        addDir('Thai Movie',FILM4KH+'category.php?cat=thai-movie',41,'http://file.hotkhmer.com/wp-content/uploads/2017/02/Komsan9-34-300x300.jpg')
        #addDir('Philippian Movie',FILM4KH+'khmer-philipian-movie-dubbed',41,'http://www.movie2khmer.com/images/cover/Glamorosa.jpg')

def INDEX_FILM2US(url):
         html = OpenSoup(url)
         try:
             html = html.encode("UTF-8")
         except: pass
         soup = BeautifulSoup(html.decode('utf-8'))
         div_index = soup('div',{"class":"col-xs-6 col-md-3"})
         for link in div_index:
             vLink = BeautifulSoup(str(link))('a')[0]['href']
             print vLink
             vTitle = BeautifulSoup(str(link))('img')[0]['alt']
             #print vTitle
             vTitle = vTitle.encode("UTF-8",'replace')
             vImage = BeautifulSoup(str(link))('img')[0]['src']
             print vImage.encode("UTF-8")
             addDir(vTitle,vLink,45,vImage)
         try:
           paging = soup('ul',{'class':'pagination'})
           pages = BeautifulSoup(str(paging[0]))('a')
           for p in pages:
             psoup = BeautifulSoup(str(p))
             pageurl = psoup('a')[0]['href']
             pagenum = psoup('a')[0].contents[0].replace("&laquo;",">").replace("&raquo;","<")
             addDir(" Page " + pagenum.encode("utf-8") ,('http://www.ckh7.com/' + pageurl.encode("utf-8")),41,"")		 
         except:pass	   

def EPISODE_FILM2US(url,name):    
        link = OpenURL(url)
        try:
             link = link.encode("UTF-8")
        except: pass
        match=re.compile('{\s*"file":\s*"(.+?)",\s*"title":\s*"(.+?)",').findall(link)     
        if(len(match) > 0):      
         for vLink,vLinkName in match:                 
          addLink(vLinkName,vLink,4,'')	


############## START KHDRAMA **********
def KHDRAMA2():
        addDir('Chinese Drama',KHDRAMA+'watch-khmer-chinese-drama-video',51,'https://phumikhmerblog.files.wordpress.com/2017/05/phumikhmer.jpg')
        addDir('Chinese Movie',KHDRAMA+'watch-khmer-chinese-movie-video',51,'http://file.hotkhmer.com/wp-content/uploads/2017/02/Komsan9-108-300x300.jpg')
        addDir('Korean Drama',KHDRAMA+'watch-khmer-korean-drama-video',51,'http://www.khmer89.com/uploads/thumbs/c8810789c-1.jpg')
        addDir('Korean Movie',KHDRAMA+'watch-khmer-korean-movie-video',51,'http://www.khmer89.com/uploads/thumbs/3d40ad547-1.jpg')
        addDir('Khmer Movie',KHDRAMA+'watch-khmer-movie-video',51,'http://www.khmer89.com/uploads/thumbs/4c9cf04ce-1.jpg')
        addDir('Thai Drama',KHDRAMA+'watch-khmer-thai-lakorn-video',51,'https://phumikhmerblog.files.wordpress.com/2017/07/form-thai-movie.png?w=300')
        addDir('Thai Movie',KHDRAMA+'watch-khmer-thai-movie-video',51,'http://file.hotkhmer.com/wp-content/uploads/2017/02/Komsan9-34-300x300.jpg')
        addDir('Philippian Movie',KHDRAMA+'watch-khmer-philippian-movie-video',51,'http://www.movie2khmer.com/images/cover/Glamorosa.jpg')     
		
def INDEX_KHDRAMA(url):
    html = OpenSoup(url)
    soup = BeautifulSoup(html.decode('utf-8'))
    video_list = soup('div',{'class':"col-lg-3 col-md-3 col-sm-4 col-xs-6 hero-feature text-center"})
    for link in video_list:
        vLink = BeautifulSoup(str(link))('a')[1]['href']
        vTitle = BeautifulSoup(str(link))('a')[1]['title']
        vImage = BeautifulSoup(str(link))('img')[0]['src']
        addDir(vTitle,vLink,55,vImage)
    match5=re.compile('<ul class="pagination catalogue-pagination">(.+?)</ul>').findall(html)
    if(len(match5)):
        pages=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(match5[0])
        for pageurl,pagenum in pages:
            addDir(" Page " + pagenum,pageurl.encode("utf-8"),51,"")
    xbmcplugin.endOfDirectory(pluginhandle)  

def EPISODE_KHDRAMA(url,name):
        html =urllib2.urlopen(url).read()
        soup = BeautifulSoup(html.decode('utf-8'))
        episodes = soup('div',{'class':"col-lg-3 col-md-3 col-sm-4 col-xs-6 hero-feature text-center"})
        for link in episodes:
            vLink = BeautifulSoup(str(link))('a')[1]['href']
            vTitle = BeautifulSoup(str(link))('a')[1]['title']
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            addLink(vTitle,vLink,3,vImage)
        match5=re.compile('<ul class="pagination catalogue-pagination">(.+?)</ul>').findall(html)
        if(len(match5)):
            pages=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(match5[0])
            for pageurl,pagenum in pages:
                addDir(" Page " + pagenum,pageurl.encode("utf-8"),55,"")
        xbmcplugin.endOfDirectory(pluginhandle)    		



################KHMERKOMSAN#######################
def KHMERKOMSAN():#60
        addDir('Chinese Drama',HOTKHMER+'category.php?cat=chinese-drama-dubbed',61,'https://phumikhmerblog.files.wordpress.com/2017/07/nisay-sne-dav-tep-paladin3.png?w=300')   
        addDir('Khmer Drama',HOTKHMER+'category.php?cat=khmer-drama-dubbed',61,'https://3.bp.blogspot.com/-3gQZwS2lRoo/WEqr-XcJI1I/AAAAAAAAAWU/1BgKfBiBbSMAO3kug3tzB4GK_qg89JuJgCLcB/s320/Pheakdey-Sne-Tvei-Phob.jpg')
        addDir('Korean Drama',HOTKHMER+'category.php?cat=Korean-Drama',61,'http://www.citykhmer.net/uploads/articles/872201fe.jpg')
        addDir('Thai Lakorn',HOTKHMER+'category.php?cat=thai-lakorn-dubbed',61,'https://phumikhmerblog.files.wordpress.com/2017/07/form-thai-movie1.png?w=300')

def INDEX_KHMERKOMSAN(url):
        html = OpenSoup(url)
        try:   
           html =html.encode("UTF-8")
        except: pass
        soup = BeautifulSoup(html.decode('utf-8'))
        div_index = soup('div',{'class':"col-lg-3 col-md-3 col-sm-3 col-xs-6"})
        for link in div_index:            
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            vTitle = BeautifulSoup(str(link))('img')[0]['title']
            vTitle = vTitle.encode("UTF-8",'replace')
            addDir(vTitle,vLink,65,vImage)
        pages=re.compile('<li class="">\r\n\s*<a href="(.+?)">&raquo;</a>').findall(html)
        if(len(pages)):
          for pageurl in pages:
              addDir("[B][COLOR blue]<< Next Page >>[/B][/COLOR]",('http://www.khmerkomsan.co/' + pageurl.encode("utf-8")),61,"")
			  
def EPISODE_KHMERKOMSAN(url,name):    
        link = OpenURL(url)        
        match=re.compile('{\s*"file":\s*"(.+?)",\s*"title":\s*"(.+?)",').findall(link)     
        if(len(match) > 0):      
         for vLink,vLinkName in match:                 
             addLink(vLinkName,vLink,4,'')
        else: 
         match=re.compile('[^>]*{"idGD":\s*"([^"]+?)"').findall(link)
         print 'MATCHIFRAM: %s' % match
         if(len(match) > 0):
           EPlink = match[0].replace("0!?^0!?A"," ")       
           match = EPlink.split(' ')   
           counter = 0      
           for vLink in match:
               counter += 1 
               addLink(name.encode("utf-8") + " part " + str(counter), 'https://docs.google.com/file/d/%s' % vLink,4,'')
         else:
           match=re.compile('<div id="Playerholder">\r\n\t\t\t<iframe [^>]*src="([^"]+?)"').findall(link)
           print 'MATCHPLAY: %s' % match
           if(len(match) > 0):      
            for vLink in match:
              addLink(name.encode("utf-8"),vLink,4,'')	

######## START NIYEAYKHMER ***************
def KONKHMERALL():
        addDir('Chinese Drama',KHMERALL+'search/label/China%20Drama',131,'https://3.bp.blogspot.com/-SjZaQI6pdFo/WWhKHZWhnFI/AAAAAAAAC4A/yabRNxzqiAIx3D1GdHOXJj_TGGKdhaQygCLcBGAs/s227/Dav%2BTep%2BNisay%2BSne.PNG')
        addDir('Korean Drama',KHMERALL+'search/label/Korean%20Drama',131,'http://www.citykhmer.net/uploads/articles/872201fe.jpg')
        addDir('Thai Drama',KHMERALL+'search/label/Thai%20Drama',131,'https://4.bp.blogspot.com/-HkNWcGitdmw/WVCcX0ptfTI/AAAAAAAACmg/MxOnP7dDBSoP4sEuwNd4MdC_fW1qzTmVQCLcBGAs/s227/Komlang%2BAkum%2BChrek%2BSne.PNG')


def INDEX_KONKHMERALL(url):
    #try:
        html = OpenSoup(url)
        try:
            html = html.encode("UTF-8")
        except: pass
        soup = BeautifulSoup(html.decode('utf-8'))
        video_list = soup('div',{'class':'post-outer'})
        for link in video_list:
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('a')[0].contents[0]
            vTitle = vTitle.encode("UTF-8",'replace')
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            print vImage.encode("UTF-8")
            addDir(vTitle,vLink,135,vImage)
        label="" #re.compile("/label/(.+?)\?").findall(url)[0]
        print label
        pagenum=re.compile("PageNo=(.+?)").findall(url)
        print pagenum
        prev="0"
        if(len(pagenum)>0):
              prev=str(int(pagenum[0])-1)
              pagenum=str(int(pagenum[0])+1)

        else:
              pagenum="2"
        nexurl=buildNextPage(pagenum,label)

        if(int(pagenum)>2 and prev=="1"):
              urlhome=url.split("?")[0]+"?"
              addDir("[B][COLOR blue]<< Back Page >>[/B][/COLOR]",urlhome,131,"")
        elif(int(pagenum)>2):
              addDir("[B][COLOR blue]<< Back Page >>[/B][/COLOR]",buildNextPage(prev,label),131,"")
        if(nexurl!=""):
              addDir("[B][COLOR green]<< Next Page >>[/B][/COLOR]",nexurl,131,"")
        
        xbmcplugin.endOfDirectory(pluginhandle)	

def buildNextPage(pagenum,label):
	pagecount=str((int(pagenum) - 1) * 18)
	url=KHMERALL+"feeds/posts/summary?start-index="+pagecount+"&max-results=1&alt=json-in-script&callback=finddatepost"
	link = OpenSoup(url)
	try:
		link =link.encode("UTF-8")
	except: pass
	match=re.compile('"published":\{"\$t":"(.+?)"\}').findall(link)
	if(len(match)>0):
		tsvalue=urllib.quote_plus(match[0][0:19]+match[0][23:29])
		newurl=KHMERALL+"search/label/"+label+"?updated-max="+tsvalue+"&max-results=18#PageNo="+pagenum
	else:
		newurl=""
	return newurl

def EPISODE_KONKHMERALL(url,name):    
        link = OpenURL(url)		
        match=re.compile('{\s*"file":\s*"(.+?)",\s*"title":\s*"(.+?)",\s*"description":\s*".+?",\s*"image":\s*"(.+?)"').findall(link)		
        if(len(match) > 0):      
         for vLink,vLinkName,vImage in match:                 
          addLink(vLinkName,vLink,4,vImage)
		  
        match=re.compile('{\s*"file":\s*"(.+?)",\s*"title":\s*"(.+?)",\s*"description": "",\s*"image":\s*"(.+?)"').findall(link)		
        if(len(match) > 0):      
         for vLink,vLinkName,vImage in match:                 
          addLink(vLinkName,vLink,4,vImage) 		  
		  
        else: 
         match=re.compile('<li class="v-item active" data-source=".+?" data-vid="(.+?)">').findall(link)
         if(len(match) > 0):
           counter = 0      
           for vLink in match:
               counter += 1 
               addLink(name.encode("utf-8") + " part " + str(counter),('https://vid.me/e/'+ vLink),4,'')
         else:
          match=re.compile(' playlist: "(.+?)",').findall(link)
          if(len(match) > 0):
           List = (urllib2.unquote(match[0]).decode("utf8"))
           link = OpenURL(List)
           OpenXML(link)
          else: 
           match=re.compile('<li class="v-item " data-vid="(.+?)">').findall(link)
           if(len(match) > 0):
            counter = 0      
            for vLink in match:
               counter += 1 
               addLink(name.encode("utf-8") + " part " + str(counter),('http://www.mp4upload.com/embed-%s.html'% vLink),4,'')
           else:
             addLink(name,url,3,'')
        xbmcplugin.endOfDirectory(pluginhandle)	
		  

######## START TUBEKHMER, PHUMIKHMER ***************
def TUBEKHMER():   
        addDir('PHUMI-MEDIA',PHUMIKHMER+'page/1/',92,'https://4.bp.blogspot.com/-OlhlObrvgSc/WKLHP0Ii2YI/AAAAAAAAC0Q/-lBVlE1h24QOll92L10agxH3Ax6rqxryQCLcB/s300/400.PNG')
        addDir('PHUMI-CLUB',PHUMIKHMER1+'category/thai-lakorn/',93,'http://1.bp.blogspot.com/-i6AYFwrqk5A/WBP85TWifNI/AAAAAAAACYc/tJWxkJFCkpEpYMVxUaqOpDcbffBkw2ixgCK4B/s1600/PhumiKhmer-logo-2017-web.PNG')
        addDir('PHUMIKHMER1',PHUMIKHMER2+'newvideos.php?&page=1',94,'http://www.phumikhmer1.com/templates/default/img/phumikhmer-logo.png')		
        addDir('TUBEKHMER',TUBE_KHMER+'search/label/Thai%20Lakorn?&max-results=15',91,'http://1.bp.blogspot.com/-ptat91ZIzbw/V5wk9Br2GRI/AAAAAAAAAXM/keCw24Msw8wELtZhPiRZ-E9bf6cWTQeTQCK4B/s1600/H-90.gif')
		
def INDEX_PHUMIKHMER(url):     
    #try:
        html = OpenSoup(url)
        try:
            html =html.encode("UTF-8")
        except: pass
        #html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html.decode('utf-8'))
        video_list = soup('div',{'class':'td-module-thumb'})
        for link in video_list:
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('a')[0]['title']
            vTitle = vTitle.encode("UTF-8",'replace')
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            addDir(vTitle,vLink,95,vImage)
        pagecontent=soup.findAll('div', {"class" : re.compile("page-nav*")})
        if(len(pagecontent)>0):
            for item in pagecontent[0].findAll('a', {"class" : ["page", "last"]}):
				addDir("page " + item.contents[0],item["href"],92,"")
				
def buildNextPage2(pagenum,label):
	pagecount=str((int(pagenum) - 1) * 18)
	url=PHUMIKHMER+"feeds/posts/summary/?start-index="+pagecount+"&max-results=1&alt=json-in-script&callback=finddatepost"
	link = OpenURL(url)
	try:
		link =link.encode("UTF-8")
	except: pass
	match=re.compile('"published":\{"\$t":"(.+?)"\}').findall(link)
	print match
	if(len(match)>0):
		tsvalue=urllib.quote_plus(match[0][0:19]+match[0][23:29])
		newurl=PHUMIKHMER+"search/label/"+label+"?updated-max="+tsvalue+"&max-results=18#PageNo="+pagenum
	else:
		newurl=""
	return newurl				
	
def INDEX_TUBEKHMER(url):     
    #try:
        html = OpenSoup(url)
        try:
            html = html.encode("UTF-8")
        except: pass
        soup = BeautifulSoup(html.decode('utf-8'))
        video_list = soup('div',{'class':'post-outer'})
        for link in video_list:
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('a')[0].contents[0]
            vTitle = vTitle.encode("UTF-8",'replace')
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            print vImage.encode("UTF-8")
            addDir(vTitle,vLink,95,vImage)
        label="" #re.compile("/label/(.+?)\?").findall(url)[0]
        print label
        pagenum=re.compile("PageNo=(.+?)").findall(url)
        print pagenum
        prev="0"
        if(len(pagenum)>0):
              prev=str(int(pagenum[0])-1)
              pagenum=str(int(pagenum[0])+1)

        else:
              pagenum="2"
        nexurl=buildNextPage3(pagenum,label)

        if(int(pagenum)>2 and prev=="1"):
              urlhome=url.split("?")[0]+"?"
              addDir("[B][COLOR blue]<< Back Page >>[/B][/COLOR]",urlhome,91,"")
        elif(int(pagenum)>2):
              addDir("[B][COLOR blue]<< Back Page >>[/B][/COLOR]",buildNextPage3(prev,label),91,"")
        if(nexurl!=""):
              addDir("[B][COLOR green]<< Next Page >>[/B][/COLOR]",nexurl,91,"")

        xbmcplugin.endOfDirectory(pluginhandle)	

def buildNextPage3(pagenum,label):
	pagecount=str((int(pagenum) - 1) * 18)
	url=TUBE_KHMER+"feeds/posts/summary?start-index="+pagecount+"&max-results=1&alt=json-in-script&callback=finddatepost"
	link = OpenSoup(url)
	try:
		link =link.encode("UTF-8")
	except: pass
	match=re.compile('"published":\{"\$t":"(.+?)"\}').findall(link)
	if(len(match)>0):
		tsvalue=urllib.quote_plus(match[0][0:19]+match[0][23:29])
		newurl=TUBE_KHMER+"search/label/"+label+"?updated-max="+tsvalue+"&max-results=18#PageNo="+pagenum
	else:
		newurl=""
	return newurl
	
def INDEX_PHUMIKHMER1(url):     
    #try:
        html = OpenSoup(url)
        try:
            html =html.encode("UTF-8")
        except: pass
        #html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html.decode('utf-8'))
        video_list = soup('div',{'class':'td-module-thumb'})
        for link in video_list:
            vLink = BeautifulSoup(str(link))('a')[0]['href']
            vTitle = BeautifulSoup(str(link))('a')[0]['title']
            vTitle = vTitle.encode("UTF-8",'replace')
            vImage = BeautifulSoup(str(link))('img')[0]['src']
            addDir(vTitle,vLink,95,vImage)
        pagecontent=soup.findAll('div', {"class" : re.compile("page-nav*")})
        if(len(pagecontent)>0):
            for item in pagecontent[0].findAll('a', {"class" : ["page", "last"]}):
				addDir("page " + item.contents[0],item["href"],93,"")
				
def buildNextPage4(pagenum,label):
	pagecount=str((int(pagenum) - 1) * 18)
	url=PHUMIKHMER1+"feeds/posts/summary/?start-index="+pagecount+"&max-results=1&alt=json-in-script&callback=finddatepost"
	link = OpenURL(url)
	try:
		link =link.encode("UTF-8")
	except: pass
	match=re.compile('"published":\{"\$t":"(.+?)"\}').findall(link)
	print match
	if(len(match)>0):
		tsvalue=urllib.quote_plus(match[0][0:19]+match[0][23:29])
		newurl=PHUMIKHMER1+"search/label/"+label+"?updated-max="+tsvalue+"&max-results=18#PageNo="+pagenum
	else:
		newurl=""
	return newurl		
	
def INDEX_PHUMIKHMER2(url):     
         html = OpenSoup(url)
         try:
             html = html.encode("UTF-8")
         except: pass
         soup = BeautifulSoup(html.decode('utf-8'))
         div_index = soup('div',{"class":"heading"})
         for link in div_index:
             vLink = BeautifulSoup(str(link))('a')[0]['href']
             vTitle = BeautifulSoup(str(link))('img')[0]['alt']
             vTitle = vTitle.encode("UTF-8",'replace')
             vImage = BeautifulSoup(str(link))('img')[0]['src']
             print vImage.encode("UTF-8")
             addDir(vTitle,vLink,95,vImage)
         try:
           paging = soup('ul',{'class':'pagination'})
           pages = BeautifulSoup(str(paging[0]))('li')
           for p in pages:
             psoup = BeautifulSoup(str(p))
             pageurl = psoup('a')[0]['href']
             pagenum = psoup('a')[0].contents[0].replace("&laquo;",">").replace("&raquo;","<")
             addDir(" Page " + pagenum.encode("utf-8") ,('http://phumikhmer1.com/' + pageurl.encode("utf-8")),94,"")		 
         except:pass	
	
def EPISODE_TUBEKHMER(url,name):
        link = OpenURL(url)
        try:
             link = link.encode("UTF-8")
        except: pass
        match=re.compile('{\s*"file":\s*"(.+?)",\s*"title":\s*"(.+?)",').findall(link)     
        if(len(match) > 0):      
         for vLink,vLinkName in match:                 
          addLink(vLinkName,vLink,4,'')	
	
		  
             
######## START LAKHOAN ***************
def LAKORNKHMERS():
        addDir('Chinese',LAKORNKHMER+'category/chinese/',101,'https://phumikhmerblog.files.wordpress.com/2017/05/phumikhmer.jpg')        
        addDir('Khmer',LAKORNKHMER+'category/khmer/',101,'http://www.khmer89.com/uploads/thumbs/4c9cf04ce-1.jpg')        
        addDir('Thai',LAKORNKHMER+'category/thai/',101,'https://phumikhmerblog.files.wordpress.com/2017/06/1b3d0-logo.png')
        

def INDEX_LAKORNKHMER(url):
    #try:
        link = GetContent(url)
        try:
            link =link.encode("UTF-8")
        except: pass
        newlink = ''.join(link.splitlines()).replace('\t','')
        #start=newlink.index('<div id="main">')
        #end=newlink.index('<!-- main -->')
        match=re.compile('<div class="arc-main">((.|\s)*?)<div id="page-sidebar">').findall(newlink)
        if(len(match) >= 1 and len(match[0]) >= 1):
                match=re.compile('<div class="img-th">((.|\s)*?)</h4>').findall(match[0][0])
                if(len(match) >= 1):
                        for vcontent in match:
                            #match1=re.compile('<a href="(.+?)" rel="bookmark"><img [^>]*src="(.+?)" class="attachment-thumbnail wp-post-image" alt="(.+?)"').findall(vcontent[0])
                            vlink=re.compile('<h4 class="post-tit"><a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(vcontent[0])
                            vurl=vlink[0][0]
                            vimage=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(vcontent[0])
                            if(len(vimage)>0):
                                vimage=vimage[0]
                            else:
                                vimage=""
                            vname=vlink[0][1]
                            #(vurl, vimage, vname)=match1[0]
                            try:
								vname=vname.encode("utf-8")
                            except:pass
                            addDir(vname.replace("Thai Lakorn &#8211;",""),vurl,105,vimage)
        match5=re.compile("<div class='wp-pagenavi'>((.|\s)*?)</div>").findall(newlink)
        if(len(match5) >= 1 and len(match5[0]) >= 1 ):
                pagelist =re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(match5[0][0])
                for pageurl,pagenum in pagelist:
					addDir("page " + pagenum.replace('Last \xc2\xbb','Last >>').replace('\xc2\xab',"Prev <<").replace("Prev << First","<< First").replace('\xc2\xbb',"Next >>"),pageurl,101,"")

    #except: pass
						
def EPISODE_LAKORNKHMER(url,name):
    #try:
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        framesrc=re.compile('<iframe id="gdVideoIframe" [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(newlink)
        if(len(framesrc)==0):
			framesrc=re.compile('<video id="html5Video" [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(newlink)
        match1=re.compile('<ul class="v-list" id="vList">(.+?)</ul>').findall(newlink)
        if(len(match1) > 0):

				match1=re.compile('data-vid="(.+?)" data-source="(.+?)">\s*<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>\s*<span class="v-title">(.+?)</span>').findall(match1[0])
				if(len(framesrc)>0 and framesrc[0].find("vimeo") > -1):
					vidurl="http://player.vimeo.com/video/%s"
				elif(len(framesrc)>0 and framesrc[0].find("totptnt") > -1):
					vidurl=framesrc[0].replace(framesrc[0].split("/")[-1],"")+"%s"
				elif(len(framesrc)>0 and framesrc[0].find("docs.google") > -1):
					vidurl="https://docs.google.com/file/d/%s/preview"
				else:
					vidurl=framesrc[0].replace(framesrc[0].split("/")[-1],"%s")
				for mcontent in match1:
					vLink,vtype,vimage,vLinkName=mcontent
					addLink(vLinkName.encode("utf-8"),vidurl%vLink,4,vimage)
        match=re.compile('\{\s*"file":\s*"(.+?)",\s*"title":\s*"(.+?)",\s*"description":').findall(link)
        if(len(match) >= 1):
                for mcontent in match:
                    vLink, vLinkName=mcontent
                    addLink(vLinkName.encode("utf-8"),vLink,4,'')
        else:
                match=re.compile('"file": "(.+?)",').findall(link)
                if(len(match) >= 1):
                        if(".xml" in match[0]):
                                newcontent=GetContent(strdomain+match[0].replace(" ","%20"))
                                ParseXml(newcontent)
                        elif (len(match) > 1):
                                counter = 0
                                for mcontent in match:
                                        counter += 1
                                        addLink(name.encode("utf-8") + " part " + str(counter),mcontent,4,"")
                        else:
                                addLink(name.encode("utf-8"),match[0],3,"")
                else:
                        match=re.compile('<embed [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)
                        if(len(match) >= 1):
                                if(match[0].find(".swf") > -1):
                                        match=re.compile('<iframe [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)
                                        if(len(match) >= 1):
                                              addLink(name.encode("utf-8"),match[0],4,"")
                                else:
                                        addLink(name.encode("utf-8"),match[0],4,"")
                        else:
                                match=re.compile("'flashvars','&#038;file=(.+?)'").findall(link)
                                if(len(match) >= 1):
                                        ParseXml(GetContent(match[0]).encode("utf-8"))
                                elif(len(re.compile('file: "(.+?)",').findall(link)) >=1):
                                        hasitem=ParseSeparate(newlink,'title: "(.+?)",','file: "(.+?)",')
                                else:
                                        hasitem=ParseSeparate(newlink,'{"title":"(.+?)","creator":','"levels":\[{"file":"(.+?)"}')
        if(len(match1) ==0):
			match=re.compile('<iframe [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)
			if(len(match) >= 1):
				addLink(name.encode("utf-8"),match[0],4,"")
        match=re.compile('\).setup\((.+?)\)').findall(newlink)
        if(len(match) > 0):
            epimatch =re.compile('urls:\s*\[(.+?)\]').findall(newlink)
            if(len(epimatch) > 0):
                epilist = epimatch[0].split(",")
                counter = 0
                for mcontent in epilist:
                     counter += 1
                     addLink(name.encode("utf-8") + " part " + str(counter),mcontent,4,"")           
    #except: pass		

def ParseXml(newcontent):
        try:
                xmlcontent=xml.dom.minidom.parseString(newcontent)
        except:
                ParsePlayList(newcontent)
                return ""
        if('<tracklist>' in newcontent):
                ParsePlayList(newcontent)
                channels = xmlcontent.getElementsByTagName('tracklist')
                items=xmlcontent.getElementsByTagName('track')
                for itemXML in items:
                        vname=itemXML.getElementsByTagName('title')[0].childNodes[0].data
                        vurl=itemXML.getElementsByTagName('location')[0].childNodes[0].data
                        addLink(vname.encode("utf-8"),vurl.encode("utf-8"),3,"")
        else:
                channels = xmlcontent.getElementsByTagName('channel')
                if len(channels) == 0:
                    channels = xmlcontent.getElementsByTagName('feed')
                items=xmlcontent.getElementsByTagName('item')
                for itemXML in items:
                        vname=itemXML.getElementsByTagName('title')[0].childNodes[0].data
                        vurl=itemXML.getElementsByTagName('media:content')[0].getAttribute('url')
                        addLink(vname.encode("utf-8"),vurl.encode("utf-8"),3,"")

def ParsePlayList(newcontent):
        newcontent=''.join(newcontent.splitlines()).replace('\t','')
        match=re.compile('<title>(.+?)</title>[^>]*<location>(.+?)</location>').findall(newcontent)
        for vcontent in match:
                (vname,vurl)=vcontent
                addLink(vname.encode("utf-8"),vurl.encode("utf-8"),3,"")				

def ParseSeparate(vcontent,namesearch,urlsearch):
        newlink = ''.join(vcontent.splitlines()).replace('\t','')
        match2=re.compile(urlsearch).findall(newlink)
        match3=re.compile(namesearch).findall(newlink)
        imglen = len(match3)
        if(len(match2) >= 1):
                for i in range(len(match2)):
                    if(i < imglen ):
                        namelink = match3[i]
                    else:
                        namelink ='part ' + str(i+1)
                    addLink(namelink.encode("utf-8"),match2[i],3,"")
                return True
        return False
						
def GetContent(url):
    try:
       print "xmlurl="+url
       net = Net()
       second_response = net.http_GET(url)
       return second_response.content
    except:	
       d = xbmcgui.Dialog()
       d.ok(url,"Can't Connect to site",'Try again in a moment')

############## END OF VIDEO SITE ****************** 		
		
def OpenXML(Doc):
    document = xml.dom.minidom.parseString(Doc)      
    items = document.getElementsByTagName('item')
    for itemXML in items:
     vname=itemXML.getElementsByTagName('title')[0].childNodes[0].data
     vpart=itemXML.getElementsByTagName('description')[0].childNodes[0].data
     vImage=itemXML.getElementsByTagName('jwplayer:image')[0].childNodes[0].data
     vurl=itemXML.getElementsByTagName('jwplayer:source')[0].getAttribute('file')     
     addLink(vpart.encode("utf-8"),vurl.encode("utf-8"),4,"")           

def VIDEOLINKS(url):              
           link=OpenNET(url)
           url = re.compile('Base64.decode\("(.+?)"\)').findall(link)
           if(len(url) > 0):
            host=url[0].decode('base-64')
            match=re.compile('<iframe frameborder="0" [^>]*src="(.+?)"[^>]*>').findall(host)[0]
            VIDEO_HOSTING(match)
            #Play_VIDEO(match)
           else:
           #match=re.compile("'file': '(.+?)',").findall(link)
            match=re.compile('<IFRAME SRC="\r\n(.+?)" [^>]*').findall(link)
            if(len(match) == 0):
             match=re.compile('file:\s*"([^"]+?)"').findall(link)# Good Link
             if(len(match) == 0):
              match=re.compile('<iframe [^>]*src="(.+?)"').findall(link)
              if(len(match) == 0):
                match=re.compile('<iframe frameborder="0" [^>]*src="(.+?)">').findall(link)
                if(len(match)==0):
                 match=re.compile('<IFRAME SRC="(.+?)" [^>]*').findall(link)
                 if(len(match) == 0):   
                   #match=re.compile('<iframe [^>]*src="(.+?)" [^>]*').findall(link)
                   match=re.compile("'file': '(.+?)',").findall(link)
                   if(len(match) == 0):
                    match=re.compile('<div class="video_main">\s*<iframe [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)
                    if(len(match) == 0):
                     match = re.compile("var flashvars = {file: '(.+?)',").findall(link)        
                     if(len(match) == 0):       
                      match = re.compile('swfobject\.embedSWF\("(.+?)",').findall(link)
                      if(len(match) == 0):
                       match = re.compile("'file':\s*'(.+?)'").findall(link)
                       if(len(match) == 0):
                        match = re.compile("file: '(.+?)'").findall(link)
                        if(len(match) == 0):
                         match = re.compile('"src": "(.+?)"').findall(link)
                         if(len(match) == 0):                    
                          match = re.compile('<iframe [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)
                          if(len(match)== 0):
                           match = re.compile('<source [^>]*src="([^"]+?)"').findall(link)
                           if(len(match) == 0):                    
                            match = re.compile('<script>\nvidId = \'(.+?)\'; \n</script>').findall(link)
                            for url in match:
                             vid = url[0].replace("['']", "")       
                             match ='https://docs.google.com/file/d/'+ (vid)+'/preview'
                             #REAL_VIDEO_HOST(match)
                             VIDEO_HOSTING(match)
                             print match
           VIDEO_HOSTING(match[0])
           print match
           xbmcplugin.endOfDirectory(pluginhandle)
   
def VIDEO_HOSTING(vlink):          
           if 'dailymotion' in vlink:                
                VideoURL = DAILYMOTION(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Dailymotion Loading selected video)")
                Play_VIDEO(VideoURL)
				
           elif 'facebook.com' in vlink:   
                VideoURL = FACEBOOK(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Facebook Loading selected video)")
                Play_VIDEO(VideoURL)
                
           elif 'google.com' in vlink:   
                VideoURL = DOCS_GOOGLE(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Google Loading selected video)")
                Play_VIDEO(VideoURL)
                
           elif 'vimeo' in vlink:
                 VideoURL = VIMEO(vlink)
                 print 'VideoURL: %s' % VideoURL
                 #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Vimeo Loading selected video)")
                 Play_VIDEO(VideoURL)

           elif 'vid.me' in vlink:                   
                VideoURL = VIDDME(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Vid.me Loading selected video)")
                Play_VIDEO(VideoURL)
				
           elif 'sendvid.com' in vlink:
                VideoURL = SENDVID(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Sendvid Loading selected video)")
                Play_VIDEO(VideoURL)
				
           elif 'viddme' in vlink:
                VideoURL = vlink
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Viddme Loading selected video)")
                Play_VIDEO(VideoURL)

           elif 'az665436' in vlink:
                VideoURL = vlink
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,AZ Loading selected video)")
                Play_VIDEO(VideoURL)

           elif 'd1wst0behutosd' in vlink:
                #link = OpenURL(vlink)   
                VideoURL = vlink
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,d1wst0behutosd Loading selected video)")
                Play_VIDEO(urllib2.unquote(VideoURL).decode("utf8"))# MP4
           #     Play_VIDEO(VideoURL)

           elif 'mp4upload.com' in vlink:
                VideoURL = MP4UPLOAD(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,MP4UPLOAD Loading selected video)")
                Play_VIDEO(VideoURL)
				
           elif 'videobam' in vlink:  
                VideoURL = VIDEOBAM(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Videobam Loading selected video)")                                
                Play_VIDEO(VideoURL)     

           elif 'sharevids.net' in vlink:
                VideoURL = vlink
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Sharevids Loading selected video)")
                Play_VIDEO(VideoURL)   
                    # d = xbmcgui.Dialog()
                    # d.ok('Not Implemented','Sorry videos on linksend.net does not work','Site seem to not exist')     
					
           elif 'videos4share.com' in vlink:
                VideoURL = vlink
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,videos4share Loading selected video)")
                #Play_VIDEO(VideoURL)
                Play_VIDEO(urllib2.unquote(VideoURL).decode("utf8"))# MP4
				
           elif 'youtu.be' in vlink:                   
                VideoURL = YOUTUBE(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Youtube Loading selected video)")            
                Play_VIDEO(VideoURL)     

           elif 'youtube' in vlink:                   
                VideoURL = YOUTUBE(vlink)
                print 'VideoURL: %s' % VideoURL
                #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Youtube Loading selected video)")
                Play_VIDEO(VideoURL)
           else:
                #if 'grayshare.net' in vlink:
                if 'share.net' in vlink:    
                    VideoURL = vlink
                    print 'VideoURL: %s' % VideoURL
                    Play_VIDEO(urllib2.unquote(VideoURL).decode("utf8"))    
                      # d = xbmcgui.Dialog()
                      # d.ok('Not Implemented','Sorry videos on linksend.net does not work','Site seem to not exist')                
               
                else:
                    print 'VideoURL: %s' % vlink
                    xbmc.executebuiltin("XBMC.Notification(Please wait!, video is loading...)")
                    Play_VIDEO(urllib2.unquote(vlink).decode("utf8"))
                    #VideoURL = urlresolver.HostedMediaFile(url=vlink).resolve()
                    #Play_VIDEO(VideoURL)

def OpenNET(url):
    try:
       net = Net(cookie_file=cookiejar)
       #net = Net(cookiejar)
       try:
            second_response = net.http_GET(url)
       except:
            second_response = net.http_GET(url.encode("utf-8"))
       return second_response.content
    except:
       d = xbmcgui.Dialog()
       d.ok(url,"Can't Connect to site",'Try again in a moment')
	

def Play_VIDEO(VideoURL):

    print 'PLAY VIDEO: %s' % VideoURL    
    item = xbmcgui.ListItem(path=VideoURL)
    return xbmcplugin.setResolvedUrl(pluginhandle, True, item)

###################### Resolver Start  ###################
def GetContent2(url,referr, cj):
    if cj is None:
        cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [(
        'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        ('Accept-Encoding', 'gzip, deflate'),
        ('Referer', referr),
        ('Content-Type', 'application/x-www-form-urlencoded'),
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0'),
        ('Connection', 'keep-alive'),
        ('Accept-Language', 'en-us,en;q=0.5'),
        ('Pragma', 'no-cache')]
    usock = opener.open(url)
    if usock.info().get('Content-Encoding') == 'gzip':
        buf = StringIO.StringIO(usock.read())
        f = gzip.GzipFile(fileobj=buf)
        response = f.read()
    else:
        response = usock.read()
    usock.close()
    return (cj, response)

def DAILYMOTION(SID):
        match=re.compile('(dailymotion\.com\/(watch\?(.*&)?v=|(embed|v|user|video)\/))([^\?&"\'>]+)').findall(SID)                
        SID = match[0][len(match[0])-1]
        vlink = 'http://www.dailymotion.com/embed/' + str(SID)
        link = OpenURL(vlink)
        matchFullHD = re.compile('"1080":.+?"url":"(.+?)"', re.DOTALL).findall(link)
        matchHD = re.compile('"720":.+?"url":"(.+?)"', re.DOTALL).findall(link)
        matchHQ = re.compile('"480":.+?"url":"(.+?)"', re.DOTALL).findall(link)
        matchSD = re.compile('"380":.+?"url":"(.+?)"', re.DOTALL).findall(link)
        matchLD = re.compile('"240":.+?"url":"(.+?)"', re.DOTALL).findall(link)
        if matchFullHD:
            VideoURL = urllib.unquote_plus(matchFullHD[0]).replace("\\", "/")
        elif matchHD:
            VideoURL = urllib.unquote_plus(matchHD[0]).replace("\\/", "/")
        elif matchHQ:
            VideoURL = urllib.unquote_plus(matchHQ[0]).replace("\\/", "/")
        elif matchSD:
            VideoURL = urllib.unquote_plus(matchSD[0]).replace("\\/", "/")
        elif matchLD:
            VideoURL = urllib.unquote_plus(matchLD[0]).replace("\\/", "/")
        return VideoURL

def DOCS_GOOGLE(Video_ID):
                docid=re.compile('/d/(.+?)/preview').findall(Video_ID)[0]
                cj = cookielib.LWPCookieJar()
                (cj,vidcontent) = GetContent2("https://docs.google.com/get_video_info?docid="+docid,"", cj) 
                html = urllib2.unquote(vidcontent)
                cookiestr=""
                for cookie in cj:
					cookiestr += '%s=%s;' % (cookie.name, cookie.value)
                try:
					html=html.encode("utf-8","ignore")
                except: pass
                stream_map = re.compile('fmt_stream_map=(.+?)&fmt_list').findall(html)
                if(len(stream_map) > 0):
					formatArray = stream_map[0].replace("\/", "/").split(',')
					for formatContent in formatArray:
						 formatContentInfo = formatContent.split('|')
						 qual = formatContentInfo[0]
						 vidlink = (formatContentInfo[1]).decode('unicode-escape')

                else:
						cj = cookielib.LWPCookieJar()
						newlink1="https://docs.google.com/uc?export=download&id="+docid  
						(cj,vidcontent) = GetContent2(newlink1,newlink, cj)
						soup = BeautifulSoup(vidcontent)
						downloadlink=soup.findAll('a', {"id" : "uc-download-link"})[0]
						newlink2 ="https://docs.google.com" + downloadlink["href"]
						vidlink=GetDirVideoUrl(newlink2,cj) 
                VideoURL = (vidlink+ ('|Cookie=%s' % cookiestr))
                return  VideoURL

def FACEBOOK (SID):
       req = urllib2.Request(SID)
       req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.3')
       response = urllib2.urlopen(req)
       link=response.read()
       response.close()
       vlink = 'http://www.facebook.com/video/video.php?v=' + str(link)
       #vlink = re.compile('"params","([\w\%\-\.\\\]+)').findall(link)[0]
       html = urllib.unquote(vlink.replace('\u0025', '%')).decode('utf-8')
       html = html.replace('\\', '')
       videoUrl = re.compile('(?:hd_src|sd_src)\":\"([\w\-\.\_\/\&\=\:\?]+)').findall(html)
       if len(videoUrl) > 0:    
           VideoURL =  videoUrl[0]
       else:
           VideoURL =  videoUrl
       return  VideoURL  

def MP4UPLOAD(SID):
       req = urllib2.Request(SID)
       req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.3')
       response = urllib2.urlopen(req)
       link=response.read()
       response.close()    
       VideoURL=re.compile('\'file\': \'(.+?)\'').findall(link)[0]
       return VideoURL

def SENDVID(SID):
        #Video_ID = urllib.unquote_plus(SID).replace("//", "http://")
        VID = urllib2.unquote(SID).replace("//", "http://")
        req = urllib2.Request(VID)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<source src="([^"]+?)"').findall(link)
        #match = re.compile('<meta property="og:video:secure_url" content="([^"]+?)"').findall(link)
        #VideoURL = (match[0]).decode("utf-8")
        VideoURL =  urllib2.unquote(match[0]).replace("//", "http://")
        return VideoURL

def VIDDME(Video_ID):
        SID=re.compile('vid.me/e/(.+)').findall(Video_ID)[0]
        URL = "https://vid.me/e/"+str(SID)
        VideoURL = media_url = urlresolver.resolve(URL)
        return VideoURL     

def VIDEOBAM(Video_ID):        
        req = urllib2.Request(Video_ID)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()               
        match=re.compile('"url"\s*:\s*"(.+?)","').findall(link)               
        for URL in match:
            if(URL.find("mp4") > -1):
               VideoURL = URL.replace("\\","")
        return VideoURL       

def VIMEO(Video_ID):
        SID=re.compile("//player.vimeo.com/video/(.+?)\?").findall(Video_ID)[0]
        VideoURL = 'plugin://plugin.video.vimeo/play/?video_id=' +SID
        return VideoURL
		
def VIMEO1(Video_ID):
        HomeURL = ("http://"+Video_ID.split('/')[2])
        if 'player' in Video_ID:
            vlink =re.compile("//player.vimeo.com/video/(.+?)\?").findall(Video_ID+'?')
        elif 'vimeo' in Video_ID:
              vlink =re.compile("//vimeo.com/(.+?)\?").findall(Video_ID+'?')
        #result = common.fetchPage({"link": "http://player.vimeo.com/video/%s/config?type=moogaloop&referrer=&player_url=player.vimeo.com&v=1.0.0&cdn_url=http://a.vimeocdn.com" % vlink[0],"refering": HomeURL})
        result = common.fetchPage({"link": "http://player.vimeo.com/video/%s?title=0&byline=0&portrait=0" % vlink[0],"refering": HomeURL})        
        print 'Result: %s' % result
        collection = {}
        if result["status"] == 200:
            html = result["content"]
            html = html[html.find('={"cdn_url"')+1:]
            html = html[:html.find('}};')]+"}}"
            #print html
            collection = json.loads(html)
            print 'Collection: %s' %collection
            #codec = collection["request"]["files"]["codecs"][0]
            #print codec            
            video = collection["request"]["files"]["progressive"]#[0]
            #isHD = collection["request"]["files"][video]
            print 'VideoCOLL1: %s' % video
            if(len(video) > 2):
            #if video.get("720p"):
                VideoURL = video[2]['url']
                print 'VideoSD: %s' % VideoURL
            #elif(len(video) > 1):
            #    VideoURL = video[1]['url']
            #    print 'VideoSD: %s' % VideoURL
            else: 
               VideoURL = video[0]['url']
               print 'VideoLD: %s' % VideoURL
        return VideoURL
		
def YOUTUBE(SID):
        match=re.compile('(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(SID)
        if(len(match) > 0):
             URL = match[0][len(match[0])-1].replace('v/','')
        else:   
             match = re.compile('([^\?&"\'>]+)').findall(SID)
             URL = match[1].replace('v=','')
        VideoURL = 'plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=' +URL.replace('?','')     
        return VideoURL
###################### Resolver End  ###################     

      
def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultImage", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fanart)
        liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
		
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="http://www.clker.com/cliparts/I/G/g/8/6/W/next.svg", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param    



params=get_params()
url=None
name=None
mode=None
play=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass	

		
sysarg=str(sys.argv[1]) 
if mode==None or url==None or len(url)<1:
        #OtherContent()
        HOME()
elif mode==3:
        VIDEOLINKS(url)
elif mode==4:
        VIDEO_HOSTING(url)
        
elif mode==10:
        MERLKONS()
elif mode==11:
        INDEX_MERLKON(url)       
elif mode==12:
        INDEX_KHMERSTREAM(url)
elif mode==13:
        INDEX_KHMERAVE(url)
elif mode==15:
        EPISODE_MERLKON(url,name)		
	
elif mode==14:
        INDEX_KMERDRA(url)
elif mode==16:
        EPISODE_KMERDRA(url,name)


elif mode==20:
        JOLCHET()
elif mode==21:
        INDEX_J(url)
elif mode==23:
        INDEX_JJ(url)        
elif mode==22:
        MOVIE_J(url)
elif mode==25:
        EPISODE_J(url,name)
elif mode==26:
        EPISODE_MOVIEJ(url,name)

elif mode==30:
        VIDEO4YOU()
elif mode==31:
        INDEX_VIDEO4U(url)
elif mode==35:
        EPISODE_VIDEO4U(url,name)

elif mode==40:
        FILM2US()
elif mode==41:
        INDEX_FILM2US(url)        
elif mode==45:
        EPISODE_FILM2US(url,name)
		
elif mode==50:
        KHDRAMA2()
elif mode==51:
        INDEX_KHDRAMA(url)
elif mode==55:
        EPISODE_KHDRAMA(url,name)       
elif mode==80:
        K8MERS()
elif mode==81:
        INDEX_K8MER(url)
elif mode==85:
        EPISODE_K8MER(url,name)
elif mode==90:
        TUBEKHMER()
elif mode==91:
        INDEX_TUBEKHMER(url)
elif mode==92:
        INDEX_PHUMIKHMER(url)	
elif mode==93:
        INDEX_PHUMIKHMER1(url)	
elif mode==94:
        INDEX_PHUMIKHMER2(url)		
elif mode==95:
        EPISODE_TUBEKHMER(url,name)

elif mode==100:
        LAKORNKHMERS()
elif mode==101:
        INDEX_LAKORNKHMER(url)
elif mode==105:
        EPISODE_LAKORNKHMER(url,name)
############## START KARAOKE
elif mode==110:
        MUSIC_MENU(url,name)
elif mode==111:
        MUSIC_VIDEO(url)
elif mode==115:
        MUSIC_EP(url,name)       
elif mode==200:
        PLAYLIST_VIDEOLINKS(url)

elif mode==120:
        KHMERLOVES_MENU(url)
elif mode==121:
        INDEX_KHMERLOVES(url)
elif mode==125:
        EPISODE_KHMERLOVES(url,name)        
################ END KARAOKE
elif mode==130:
        KONKHMERALL()
elif mode==131:
        INDEX_KONKHMERALL(url)
elif mode==135:
        EPISODE_KONKHMERALL(url,name)
elif mode==60:
        KHMERKOMSAN()
elif mode==61:
        INDEX_KHMERKOMSAN(url)
elif mode==62:
        INDEX_KHMERKOMSAN_MOVIE(url)
elif mode==65:
        EPISODE_KHMERKOMSAN(url,name)    

xbmcplugin.endOfDirectory(int(sysarg))
        
