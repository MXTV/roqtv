import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os,json,base64,plugintools,xbmc,news,pytz
from datetime import datetime as dtdeep
from dateutil.tz import tzlocal
import GoDev
import common,xbmcvfs,zipfile,downloader,extract
import xml.etree.ElementTree as ElementTree
import unicodedata
import time
import string
reload(sys)
dialog       =  xbmcgui.Dialog()
sys.setdefaultencoding('utf8')
SKIN_VIEW_FOR_MOVIES="515"
addonDir = plugintools.get_runtime_path()
global kontroll
global EPGColour
addon_id = "plugin.video.roqhosting"
background = "YmFja2dyb3VuZC5wbmc=" 
defaultlogo = "ZGVmYXVsdGxvZ28ucG5n" 
hometheater = "aG9tZXRoZWF0ZXIuanBn"
noposter = "bm9wb3N0ZXIuanBn"
theater = "dGhlYXRlci5qcGc="
addonxml = "YWRkb24ueG1s"
addonpy = "ZGVmYXVsdC5weQ=="
icon = "aWNvbi5wbmc="
fanart = "ZmFuYXJ0LmpwZw=="
supplier = "TGl2ZSBUVg=="
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png')) 
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.jpg')) 
APKS = base64.b64decode("aHR0cDovL2ZhYmlwdHYuY29tL2Fwa3MvbmV3YXBrcy50eHQ=")
HOME =  xbmc.translatePath('special://home/')
lehekylg= base64.b64decode("aHR0cDovL21lb3d5YXBtZW93LmNvbQ==")
pordinumber="8080"
message = "VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"
kasutajanimi=plugintools.get_setting("Username")
salasona=plugintools.get_setting("Password")
F1ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'F1.png'))
BASEURL = base64.b64decode("bmFkYQ==")
LOAD_LIVEchan = os.path.join( plugintools.get_runtime_path() , "resources" , "art/arch" )
loginurl   = base64.b64decode("JXM6JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,pordinumber,kasutajanimi,salasona)

def run():
    global pnimi
    global televisioonilink
    global LiveCats
    global PlayerAPI
    global filmilink
    global andmelink
    global uuenduslink
    global lehekylg
    global LOAD_LIVE
    global uuendused
    global vanemalukk
    global version
    version = int(get_live("MQ=="))
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    if not kasutajanimi:
        kasutajanimi = "NONE"
        salasona="NONE"
	
    uuendused=plugintools.get_setting(sync_data("dXVlbmR1c2Vk"))
    vanemalukk=plugintools.get_setting(sync_data("dmFuZW1hbHVraw=="))
    pnimi = get_live("T25lIFZpZXcg")
    LOAD_LIVE = os.path.join( plugintools.get_runtime_path() , "resources" , "art" )
    plugintools.log(pnimi+get_live("U3RhcnRpbmcgdXA="))
    televisioonilink = get_live("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9jYXRlZ29yaWVz")%(lehekylg,pordinumber,kasutajanimi,salasona)
    LiveCats = get_live("JXM6JXMvcGxheWVyX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmYWN0aW9uPWdldF9saXZlX2NhdGVnb3JpZXM=")%(lehekylg,pordinumber,kasutajanimi,salasona)
    PlayerAPI = get_live("JXM6JXMvcGxheWVyX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM=")%(lehekylg,pordinumber,kasutajanimi,salasona)
    filmilink = vod_channels("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM=")%(lehekylg,pordinumber,kasutajanimi,salasona)
    andmelink = vod_channels("JXM6JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==")%(lehekylg,pordinumber,kasutajanimi,salasona)
    params = plugintools.get_params()

    if params.get("action") is None:
        peamenyy(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def peamenyy(params):
    plugintools.log(pnimi+vod_channels("TWFpbiBNZW51")+repr(params))
    load_channels()
    if not lehekylg:
        plugintools.open_settings_dialog()

    channels = kontroll()
    if channels == 1 and GoDev.mode != 5 and GoDev.mode != 1:
        plugintools.log(pnimi+vod_channels("TG9naW4gU3VjY2Vzcw=="))
        plugintools.add_item( action=vod_channels("c2VjdXJpdHlfY2hlY2s="),  title=vod_channels(supplier) , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
    elif channels != 1 and GoDev.mode != 1:
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title="Step 1. Insert Login Credentials" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")), folder=False )	
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjazI="), title="Step 2. Click Once Login Is Input" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")), folder=False )	

def SPORT_LISTINGS(params):

	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A=')
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('href="http://www.wheresthematch.com/fixtures/(.+?).asp.+?class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em>.+?time-channel ">(.+?)</span>').findall(r)
	for game,team1,team2,gametime in match:
		a,b = gametime.split(" on ")
		plugintools.add_item (action="",  title='[COLOR white]'+team1+' vs '+team2+' - '+a+' [/COLOR]' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )
		plugintools.add_item (action="",  title='[COLOR yellowgreen][B]Watch on '+b+'[/B][/COLOR]' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )
		plugintools.add_item (action="",  title='------------------------------------------' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )

def LATESTAPKS(params):
	link = common.OPEN_XML(APKS).replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?ersion="(.+?)"').findall(link)
	for name,url,iconimage,fanart,description in match:
		GoDev.addXMLMenu('[COLOR white]' + name +'[/COLOR] [COLOR white]- version: [/COLOR]' + '[COLOR white]'+description+'[/COLOR]',url,15,iconimage,fanart,description)

def Listings(params):
	plugintools.add_item( action=vod_channels("U1BPUlRfTElTVElOR1M="),   title="UK Sport Listings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
	plugintools.add_item( action=vod_channels("R29EZXYuU3BvcnRDaG9pY2U="),   title="All Sport Listings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )

def Tools(params):
	plugintools.add_item( action=vod_channels("ZXhlY3V0ZV9haW5mbw=="),   title="Account Information", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
	plugintools.addItem('Run Speedtest','speed',9,GoDev.Images + 'speed.png',GoDev.Images + 'background.png')
	plugintools.add_item( action=vod_channels("R29EZXYuREN0ZXN0"),   title="Datacentre Speedtest" , thumbnail=GoDev.Images + 'speed.png', fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
	plugintools.add_item( action=vod_channels("TEFURVNUQVBLUw=="),   title="App Downloads" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
	plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title="Addon Settings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )
	plugintools.add_item( action=vod_channels("U2hvd05ld3M="), title="View Latest News Mesage" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("aWNvbi5wbmc=")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )

def ShowNews(params):
	TypeOfMessage="t"; (NewImage,NewMessage)=news.FetchNews(); 
	news.CheckNews(TypeOfMessage,NewImage,NewMessage,False); 

def TheDev(params):
    tvaAPI = base64.b64decode("JXM6JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==")%(lehekylg,pordinumber,kasutajanimi,salasona)
    link=open_url(tvaAPI)
    archivecheck = re.compile('"num":.+?,"name":"(.+?)".+?"stream_id":"(.+?)","stream_icon":"(.+?)".+?"tv_archive":(.+?).+?"tv_archive_duration":(.+?)}').findall(link)
    for kanalinimi,streamid,streamicon,tvarchive,archdays in archivecheck:
        if tvarchive == '1':
            streamicon = streamicon.replace('\/','/')
            archdays = archdays.replace('"','')
            plugintools.add_item( action=sync_data("dHZhcmNoaXZl"), title='[COLOR white]'+kanalinimi+'[/COLOR]' , thumbnail=streamicon, extra=streamid, page=archdays, fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")), isPlayable=False, folder=True )
            plugintools.set_view( plugintools.LIST )

def tvarchive(params):
	plugintools.set_view( plugintools.EPISODES )
	fmt = "%Y%m%d%H%M%S"
	date3 = dtdeep.now() - datetime.timedelta(int(params.get("page")))
	AweekAgo = date3.strftime(fmt)
	APIv2 = base64.b64decode("JXM6JXMvcGxheWVyX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmYWN0aW9uPWdldF9zaW1wbGVfZGF0YV90YWJsZSZzdHJlYW1faWQ9JXM=")%(lehekylg,pordinumber,kasutajanimi,salasona,params.get("extra"))
	data = json.load(urllib2.urlopen(APIv2))
	for x in data['epg_listings']:
		Title = x['title']
		Description = x['description']
		ChanID = x['channel_id']
		ShowTitle = base64.b64decode(Title)
		DesC = base64.b64decode(Description)
		start = x['start']
		end = x['end']
		format = '%Y-%m-%d %H:%M:%S'
		try:
			modend = dtdeep.strptime(end, format)
			modstart = dtdeep.strptime(start, format)
			modstart2 = dtdeep.strptime(start, format)
		except:
			modend = dtdeep(*(time.strptime(end, format)[0:6]))
			modstart = dtdeep(*(time.strptime(start, format)[0:6]))
		modend_ts = time.mktime(modend.timetuple())
		modstart_ts = time.mktime(modstart.timetuple())
		Duration=plugintools.get_setting("FinalDuration")
		if not Duration == 'Off':
			FinalDuration = Duration
		else:
			FinalDuration = int(modend_ts-modstart_ts) / 60
		try:
			ShowStart = dtdeep.strptime(start, '%Y-%m-%d %H:%M:%S').strftime("%Y%m%d%H%M%S")
		except:
			ShowStart = dtdeep(*(time.strptime(start, '%Y-%m-%d %H:%M:%S')[0:6])).strftime("%Y%m%d%H%M%S")
		TimeNow = pytz.timezone('UTC').localize(dtdeep.now()).astimezone(pytz.timezone('Europe/London'))
		TimeNow = TimeNow.replace(tzinfo=tzlocal())
		TimeNow = TimeNow.astimezone(pytz.timezone('Europe/London'))
		if 'USA/CA' in ChanID:
			modstart = pytz.timezone('UTC').localize(modstart).astimezone(pytz.timezone('Europe/London'))
			modstart = modstart.astimezone(pytz.timezone('America/New_York'))
		AweekAgo = (TimeNow - datetime.timedelta(int(params.get("page")))).strftime(fmt)
		try:
			Finalstart = dtdeep.strptime(start, '%Y-%m-%d %H:%M:%S').strftime("%Y-%m-%d:%H-%M")
		except:
			Finalstart = dtdeep(*(time.strptime(start, '%Y-%m-%d %H:%M:%S')[0:6])).strftime("%Y-%m-%d:%H-%M")
		Prefix = modstart.strftime("%a %d %H:%M")
		if ShowStart > AweekAgo:
			if ShowStart < TimeNow.strftime(fmt):
				catchupURL = base64.b64decode("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,params.get("extra"))
				ResultURL = catchupURL + str(Finalstart) + "&duration=%s"%(FinalDuration)
				kanalinimi = str('[COLOR white]'+Prefix+'[/COLOR]')+ " - " + '[COLOR gold]'+ShowTitle+'[/COLOR]'
				plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=ResultURL, thumbnail=params.get("thumbnail") , plot=DesC, fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def license_check(params):
	plugintools.log(pnimi+get_live("U2V0dGluZ3MgbWVudQ==")+repr(params))
	plugintools.open_settings_dialog()

def license_check2(params):
	d = urllib.urlopen(loginurl)
	FileInfo = d.info()['Content-Type']
	if not 'application/octet-stream' in FileInfo:
		dialog.ok('[COLOR white]Invalid Login[/COLOR]','[COLOR white]Incorrect login details found![/COLOR]','[COLOR white]Please check your spelling and case sensitivity[/COLOR]','[COLOR white]Check your password with the team otherwise[/COLOR]')
		plugintools.open_settings_dialog()
	else:
		xbmc.executebuiltin('Container.Refresh')

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def convertSize(size):
   import math
   if (size == 0):
       return '[COLOR lime]0 MB[/COLOR]'
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size,1024)))
   p = math.pow(1024,i)
   s = round(size/p,2)
   if size_name == "B" or "KB":
        return '[COLOR lime]%s %s' % (s,size_name[i]) + '[/COLOR]'
   if size_name == "GB" or "TB" or "PB" or "EB" or "ZB" or "YB":
        return '[COLOR red]%s %s' % (s,size_name[i]) + '[/COLOR]'
   if s >= 100:
        return '[COLOR red]%s %s' % (s,size_name[i]) + '[/COLOR]'
   if s < 50:
        return '[COLOR lime]%s %s' % (s,size_name[i]) + '[/COLOR]'
   if s >= 50:
        if i < 100:
            return '[COLOR orange]%s %s' % (s,size_name[i]) + '[/COLOR]'

def maintMenu(params):

	CACHE      =  xbmc.translatePath(os.path.join('special://home/cache',''))
	PACKAGES   =  xbmc.translatePath(os.path.join('special://home/addons','packages'))
	THUMBS     =  xbmc.translatePath(os.path.join('special://home/userdata','Thumbnails'))

	if not os.path.exists(CACHE):
		CACHE     =  xbmc.translatePath(os.path.join('special://home/temp',''))
	if not os.path.exists(PACKAGES):
		os.makedirs(PACKAGES)

	CACHE_SIZE_BYTE    = get_size(CACHE)
	PACKAGES_SIZE_BYTE = get_size(PACKAGES)
	THUMB_SIZE_BYTE    = get_size(THUMBS)
	
	CACHE_SIZE    = convertSize(CACHE_SIZE_BYTE)
	PACKAGES_SIZE = convertSize(PACKAGES_SIZE_BYTE)
	THUMB_SIZE    = convertSize(THUMB_SIZE_BYTE)

	startup_clean = plugintools.get_setting("acstartup")
	weekly_clean = plugintools.get_setting("clearday")

	if startup_clean == "false":
		startup_onoff = "[COLOR red]OFF[/COLOR]"
	else:
		startup_onoff = "[COLOR lime]ON[/COLOR]"
	if weekly_clean == "0":
		weekly_onoff = "[COLOR red]OFF[/COLOR]"
	else:
		weekly_onoff = "[COLOR lime]ON[/COLOR]"

	common.addItem('[COLOR white]Auto Clean Device[/COLOR]','url',19,ICON,FANART,'')
	common.addItem("[COLOR white]Clear Cache[/COLOR] - Current Size: " + str(CACHE_SIZE),BASEURL,20,ICON,FANART,'')
	common.addItem("[COLOR white]Delete Thumbnails [/COLOR] - Current Size: " + str(THUMB_SIZE),BASEURL,22,ICON,FANART,'')
	common.addItem("[COLOR white]Purge Packages [/COLOR] - Current Size: " + str(PACKAGES_SIZE),BASEURL,23,ICON,FANART,'')
	common.addItem('[COLOR white]Upload Log File[/COLOR]','url',27,ICON,FANART,'')
	common.addItem('[COLOR white]View Current or Old Log File[/COLOR]','url',18,ICON,FANART,'')
	common.addItem('[COLOR white]View the last error in log file[/COLOR]',BASEURL,24,ICON,FANART,'')
	common.addItem('[COLOR white]View all errors in the log file[/COLOR]',BASEURL,25,ICON,FANART,'')
	common.addItem('[COLOR white]Update Addons & Repos[/COLOR]',BASEURL,26,ICON,FANART,'')

def security_check(params):
	plugintools.add_item( action=vod_channels("VFZzZWFyY2g="),   title="Search Shows on Now" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
	plugintools.log(pnimi+sync_data("TGl2ZSBNZW51")+repr(params))
	request = urllib2.Request(televisioonilink, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
	u = urllib2.urlopen(request)
	tree = ElementTree.parse(u)
	rootElem = tree.getroot()
	for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
		kanalinimi = channel.find(get_live("dGl0bGU=")).text
		kanalinimi = base64.b64decode(kanalinimi)
		kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
		CatID = channel.find(get_live("Y2F0ZWdvcnlfaWQ=")).text
		ICON = os.path.join(LOAD_LIVE,sync_data("aWNvbi5wbmc="))
		if 'NHL' in kanalinimi.upper():
			ICON=os.path.join(LOAD_LIVE,sync_data("TkhMLnBuZw=="))
		if 'MLB' in kanalinimi.upper():
			ICON=os.path.join(LOAD_LIVE,sync_data("TUxCLnBuZw=="))
		if 'SPORTS' in kanalinimi.upper():
			ICON=os.path.join(LOAD_LIVE,sync_data("c3BvcnRzLnBuZw=="))
		plugintools.add_item( action=get_live("c3RyZWFtX3ZpZGVv"), title=kanalinimi , url=CatID , thumbnail=ICON , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) ,info_labels=kanalinimi, folder=True )

	plugintools.set_view( plugintools.LIST )

def stream_video(params):
	EPGColour=plugintools.get_setting("EPGColour")
	kasutajanimi=plugintools.get_setting("Username")
	salasona=plugintools.get_setting("Password")
	CatID = params.get(get_live("dXJs")) #description
	url = get_live("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9zdHJlYW1zJmNhdF9pZD0lcw==")%(lehekylg,pordinumber,kasutajanimi,salasona,CatID)
	xbmc.log(url)
	request = urllib2.Request(url, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
	u = urllib2.urlopen(request)
	tree = ElementTree.parse(u)
	rootElem = tree.getroot()
	for channel in tree.findall(sync_data("Y2hhbm5lbA==")): #channel
		kanalinimi = channel.find(get_live("dGl0bGU=")).text #title
		kanalinimi = base64.b64decode(kanalinimi)
		kanalinimi = kanalinimi.partition("[")
		striimilink = channel.find(get_live("c3RyZWFtX3VybA==")).text #stream_url
		pony = striimilink
		if ("%s:%s/enigma2.php")%(lehekylg,pordinumber)  in striimilink: 
			pony = striimilink.split(kasutajanimi,1)[1]
			pony = pony.split(salasona,1)[1]
			pony = pony.split("/",1)[1]			
		pilt = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text #desc_image
		kava = kanalinimi[1]+kanalinimi[2]
		kava = kava.partition("]")
		kava = kava[2]
		kava = kava.partition("   ")
		kava = kava[2]
		shou = get_live("W0NPTE9SIHdoaXRlXSVzWy9DT0xPUl0gW0NPTE9SICVzXSVzIFsvQ09MT1Jd")%(kanalinimi[0],EPGColour,kava)
		kirjeldus = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text #description
		if kirjeldus:
			kirjeldus = base64.b64decode(kirjeldus)
			nyyd = kirjeldus.partition("(")
			NowInfo = nyyd[2].partition(")")
			nyyd = sync_data("Tm93OiA=") +nyyd[0]
			jargmine = kirjeldus.partition(")\n")
			jargmine = jargmine[2].partition("(")
			jargmine = sync_data("TmV4dDog") +jargmine[0] #shou
			kokku = nyyd+jargmine
			if NowInfo:
				kokku = kokku+'\nNow:'+NowInfo[0]
		else:
			kokku = ""
		if pilt:
			plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=pilt, plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")), extra="", isPlayable=True, folder=False )
		else:
			plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=os.path.join(LOAD_LIVE,vod_channels("YWxsY2hhbm5lbHMucG5n")) , plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
	plugintools.set_view( plugintools.EPISODES )

def detect_modification(params):
    plugintools.add_item( action=vod_channels("Vk9Ec2VhcmNo"),   title="Search On Demand" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
    plugintools.add_item( action=vod_channels("UmVjZW50bHlBZGRlZA=="),   title="Recently Added" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
    plugintools.log(pnimi+vod_channels("Vk9EIE1lbnUg")+repr(params))
    request = urllib2.Request(filmilink, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        filminimi = channel.find(get_live("dGl0bGU=")).text
        filminimi = base64.b64decode(filminimi)
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=vod_channels("Z2V0X215YWNjb3VudA=="), title=filminimi , url=kategoorialink , thumbnail=os.path.join(LOAD_LIVE,sync_data("dm9kLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=True )
	
    plugintools.set_view( plugintools.LIST )

def open_url(url):
    try:
        req = urllib2.Request(url,headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
    except:quit()

def RecentlyAdded(params):
	plugintools.set_view( plugintools.MOVIES )
	Recent = base64.b64decode(b'JXM6JXMvcGxheWVyX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmYWN0aW9uPWdldF92b2Rfc3RyZWFtcw==')%(lehekylg,pordinumber,kasutajanimi,salasona)
	Load = json.load(urllib2.urlopen(Recent))
	now = datetime.datetime.now()
	diff = datetime.timedelta(days=7)
	future = now - diff
	Past = future.strftime("%Y-%m-%d %H:%M:%S")
	for x in Load:
		DateAdded = x['added']
		pealkiri = x['name']
		Icon = x['stream_icon']
		StreamID = x['stream_id']
		Ext = x['container_extension']
		Normal = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(DateAdded)))
		if Normal > Past:
			if StreamID:
				striimilink = vod_channels('JXM6JXMvbW92aWUvJXMvJXMvJXMuJXM=')%(lehekylg,pordinumber,kasutajanimi,salasona,StreamID,Ext)
				URL = vod_channels('JXM6JXMvcGxheWVyX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmYWN0aW9uPWdldF92b2RfaW5mbyZ2b2RfaWQ9JXM=')%(lehekylg,pordinumber,kasutajanimi,salasona,StreamID)
				Meta = json.load(urllib2.urlopen(URL))
				try:
					Plot = Meta['info']['plot']
				except:
					Plot = 'No plot Available'
				try:
					Genre = Meta['info']['genre']
				except:
					Genre = 'Unknown Genre'
				try:
					Director = Meta['info']['director']
				except:
					Director = 'No Director Specified'
				try:
					ReleaseDate = Meta['info']['releasedate']
				except:
					ReleaseDate = 'Release Date Not Found'
				try:
					Duration = Meta['info']['duration']
				except:
					Duration = 'Duration Not Found'
				kirjeldus = Duration+'\n'+Plot.encode("utf-8")+'\n'+Director.encode("utf-8")+'\n'+Genre.encode("utf-8")+'\n'+ReleaseDate
				if Icon:
					plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=Icon, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
				else:
					plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join(LOAD_LIVE,sync_data("dm9kLnBuZw==")), plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )

def VODsearch(params):
	SEARCH_LIST = base64.b64decode(b'JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX3N0cmVhbXMmY2F0X2lkPTA=')%(lehekylg,pordinumber,kasutajanimi,salasona)
	keyb = xbmc.Keyboard('', '[COLOR white]Search[/COLOR]')
	keyb.doModal()
	if (keyb.isConfirmed()):
		searchterm=keyb.getText()
		searchterm=string.capwords(searchterm)
	else:quit()
	link=open_url(SEARCH_LIST) 
	match = re.compile('<title>(.+?)</title><desc_image><!\[CDATA\[(.+?)\]\]></desc_image><description>(.+?)</description>.+?<stream_url><!\[CDATA\[(.+?)\]\]></stream_url>').findall(link)
	for pealkiri,pilt,kirjeldus,striimilink in match:
		pealkiri = base64.b64decode(pealkiri)
		pealkiri = pealkiri.encode("utf-8")
		if kirjeldus:
			kirjeldus = base64.b64decode(kirjeldus)
		if searchterm in pealkiri:
			if pilt:
				plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=pilt, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
			else:
				plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join("dm9kLnBuZw=="), plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )

def TVsearch(params):
	EPGColour=plugintools.get_setting("EPGColour")
	SEARCH_LIST = base64.b64decode(b'JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9zdHJlYW1zJmNhdF9pZD0w')%(lehekylg,pordinumber,kasutajanimi,salasona)
	keyb = xbmc.Keyboard('', '[COLOR white]Search[/COLOR]')
	keyb.doModal()
	if (keyb.isConfirmed()):
		searchterm=keyb.getText()
		searchterm=string.capwords(searchterm)
	else:quit()
	request = urllib2.Request(SEARCH_LIST, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
	u = urllib2.urlopen(request)
	tree = ElementTree.parse(u)
	rootElem = tree.getroot()
	for channel in tree.findall(sync_data("Y2hhbm5lbA==")): #channel
		kanalinimi = channel.find(get_live("dGl0bGU=")).text #title
		kanalinimi = base64.b64decode(kanalinimi)
		kanalinimi = kanalinimi.partition("[")
		striimilink = channel.find(get_live("c3RyZWFtX3VybA==")).text #stream_url
		pony = striimilink
		if ("%s:%s/enigma2.php")%(lehekylg,pordinumber) in striimilink:
			pony = striimilink.split(kasutajanimi,1)[1]
			pony = pony.split(salasona,1)[1]
			pony = pony.split("/",1)[1]			
		pilt = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text #desc_image
		kava = kanalinimi[1]+kanalinimi[2]
		kava = kava.partition("]")
		kava = kava[2]
		kava = kava.partition("   ")
		kava = kava[2]
		shou = get_live("W0NPTE9SIHdoaXRlXSVzWy9DT0xPUl0gW0NPTE9SICVzXSVzIFsvQ09MT1Jd")%(kanalinimi[0],EPGColour,kava)
		kirjeldus = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text #description
		if kirjeldus:
			kirjeldus = base64.b64decode(kirjeldus)
			nyyd = kirjeldus.partition("(")
			nyyd = sync_data("Tm93OiA=") +nyyd[0]
			jargmine = kirjeldus.partition(")\n")
			jargmine = jargmine[2].partition("(")
			jargmine = sync_data("TmV4dDog") +jargmine[0] #shou
			kokku = nyyd+jargmine
		else:
			kokku = ""
		if searchterm in kava:
			if pilt:
				plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=pilt, plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")), extra="", isPlayable=True, folder=False )
			else:
				plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=os.path.join(LOAD_LIVE,vod_channels("YWxsY2hhbm5lbHMucG5n")) , plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )

def get_myaccount(params):
    if vanemalukk == "true":
       pealkiri = params.get("title")
       vanema_lukk(pealkiri)
    purl = params.get("url")
    request = urllib2.Request(purl, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall("channel"):
        try:
            pealkiri = channel.find("title").text
            pealkiri = base64.b64decode(pealkiri)
            pealkiri = pealkiri.encode("utf-8")
            striimilink = channel.find("stream_url").text
            pilt = channel.find("desc_image").text
            kirjeldus = channel.find("description").text
            if kirjeldus:
               kirjeldus = base64.b64decode(kirjeldus)
            if pilt:
               plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=pilt, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
            else:
               plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join("dm9kLnBuZw=="), plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
        except:
            kanalinimi = channel.find("title").text
            kanalinimi = base64.b64decode(kanalinimi)
            kategoorialink = channel.find("playlist_url").text
            CatID = channel.find("category_id").text
            plugintools.add_item( action=get_live("Z2V0X215YWNjb3VudA=="), title=kanalinimi , url=kategoorialink , thumbnail=os.path.join(LOAD_LIVE,sync_data("dm9kLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) ,info_labels=kanalinimi, folder=True )

    plugintools.set_view( plugintools.EPISODES )

def run_cronjob(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    lopplink = params.get("url")
    if "http://"  not in lopplink: 
        lopplink = get_live("aHR0cDovLyVzOiVzL2VuaWdtYS5waHAvbGl2ZS8lcy8lcy8lcw==")%(lehekylg,pordinumber,kasutajanimi,salasona,lopplink)
        lopplink = lopplink[:-2]
        lopplink = lopplink + "ts"
    listitem = xbmcgui.ListItem(path=lopplink)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def sync_data(channel):
    video = base64.b64decode(channel)
    return video

def restart_service(params):
    lopplink = params.get(vod_channels("dXJs"))
    plugintools.play_resolved_url( lopplink )

def grab_epg():
	req = urllib2.Request(andmelink)
	req.add_header(sync_data("VXNlci1BZ2VudA==") , vod_channels("S29kaSBwbHVnaW4gYnkgTWlra00="))
	response = urllib2.urlopen(req)
	link=response.read()
	try:
		jdata = json.loads(link.decode('utf8'))
		response.close()
		if jdata:
			plugintools.log(pnimi+sync_data("amRhdGEgbG9hZGVk"))
			return jdata
	except ValueError, e:
		return False

def kontroll():
	try:
		randomstring = grab_epg()
		kasutajainfo = randomstring[sync_data("dXNlcl9pbmZv")]
		kontroll = kasutajainfo[get_live("YXV0aA==")]
		return kontroll
	except:
		return None
def get_live(channel):
    video = base64.b64decode(channel)
    return video
def execute_ainfo(params):
	data = json.load(urllib2.urlopen(PlayerAPI))
	today = datetime.date.today()
	x=data['user_info']
	Username = x['username']
	Status = x['status']
	Creation = x['created_at']
	Created = datetime.datetime.fromtimestamp(int(Creation)).strftime('%H:%M %d/%m/%Y')
	Current = x['active_cons']
	Max = x['max_connections']
	Expiry = x['exp_date']
	if Expiry == None:
		Expired = 'Never'
	else:
		Expired = datetime.datetime.fromtimestamp(int(Expiry)).strftime('%H:%M %d/%m/%Y')
	plugintools.add_item( action="",   title="[COLOR white]User: "+Username+"[/COLOR]", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
	plugintools.add_item( action="",   title="[COLOR white]Status: "+Status+"[/COLOR]", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
	plugintools.add_item( action="",   title="[COLOR white]Created: "+Created+"[/COLOR]", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
	plugintools.add_item( action="",   title="[COLOR white]Expires: "+Expired+"[/COLOR]", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
	plugintools.add_item( action="",   title="[COLOR white]Max connections: "+Max+"[/COLOR]", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
	plugintools.add_item( action="",   title="[COLOR white]Active connections: "+Current+"[/COLOR]", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )

	plugintools.set_view( plugintools.LIST )
def vanema_lukk(name):
        plugintools.log(pnimi+sync_data("UGFyZW50YWwgbG9jayA="))
        a = 'XXX', 'Adult', 'Adults','ADULT','ADULTS','adult','adults','Porn','PORN','porn','Porn','xxx'
        if any(s in name for s in a):
           xbmc.executebuiltin((u'XBMC.Notification("Parental Lock", "Channels may contain adult content", 2000)'))
           text = plugintools.keyboard_input(default_text="", title=get_live("UGFyZW50YWwgbG9jaw=="))
           if text==plugintools.get_setting(sync_data("dmFuZW1ha29vZA==")):
              return
           else:
              exit()
        else:
           name = ""
def check_user():
    plugintools.message(get_live("RVJST1I="),vod_channels("VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"))
    sys.exit()
def load_channels():
    statinfo = os.stat(LOAD_LIVE+"/"+get_live("YmFja2dyb3VuZC5wbmc="))

def vod_channels(channel):
    video = base64.b64decode(channel)
    return video

run()