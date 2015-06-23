#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,base64,xmltosrt,os
from BeautifulSoup import BeautifulSoup
h = HTMLParser.HTMLParser()


versao = '1.0.9'
addon_id = 'plugin.video.brasiliptvonline'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.png'
 

###################################################MENUS############################################

	
def  menus():        		
	dialog = xbmcgui.Dialog()
	dialog.ok("BRASILIPTVONLINE", "          BRASILIPTV A SUA TV MAIS PERTO DE VOCÊ!")
	addDir('BRASILIPTVONLINE','-',3,'https://sites.google.com/site/logosiptv/capabrasiliptv.png')
	
	

def  categorias():
	addDir('EVENTOS ESPORTIVOS AO VIVO','http://logosbrasiliptv.ucoz.net/eventosesportivos.txt',6,'http://www.goltvaovivo.org/wp-content/uploads/2015/04/Programa%C3%A7%C3%A3o-Esportiva-Quarta.jpg')
	addDir('TV ABERTA','http://brasiliptv.xpg.uol.com.br/tvaberta.txt',6,'http://questoesinsanas.com/wp-content/uploads/2014/10/emissoras-de-tv_zpsa967c1d4.png')
	addDir('FILMES E SÉRIES','http://brasiliptv.xpg.uol.com.br/filmeseseries.txt',6,'http://www.geekonomics.com.br/wp-content/uploads/2015/02/capa-filmes-series-01.jpg')
	addDir('ESPORTES','http://logosbrasiliptv.ucoz.net/canaisdeesportes.txt',6,'https://forcapravencer.files.wordpress.com/2011/06/arteesportes.jpg')
	
	


def  categorias_alistar():
	addDir('','',6,'')
	addDir('','',6,'')	
	addDir('','',6,'')
	addDir('','',6,'')	
	addDir('','',6,'')
	addDir('','',6,'')
	addDir('','',6,'')	
	
	
def listar_canais(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Link: ' + rtmp
                  addLink(nome,rtmp,img)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")
	  
	  
def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def real_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.geturl()
	response.close()
	return link

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

def addDir(name,url,mode,iconimage,pasta=True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
	
	
############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################

              
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
iconimage=None


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

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)


###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################


if mode==None or url==None or len(url)<1:
    print ""
    menus()
	
elif mode==3:
	print ""
	categorias()

elif mode==5:
	print ""
	categorias_alistar()	
	
elif mode==6: 
	print ""
	listar_canais(url)

	

	


	
xbmcplugin.endOfDirectory(int(sys.argv[1]))
