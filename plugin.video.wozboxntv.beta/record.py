import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os
import datetime
import time
import utils, recordings
import default
import net
from hashlib import md5  
import json  

ADDON      = xbmcaddon.Addon(id='plugin.video.wozboxntv.beta')
#print 'record.py: sys.argv= %s' %(str(repr(sys.argv)))
program  = sys.argv[0]
cat      = sys.argv[1]
startTime= sys.argv[2]
endTime  = sys.argv[3]
duration = sys.argv[4]
title    = sys.argv[5]
argv6    = sys.argv[6]
argv7    = sys.argv[7]
nameAlarm= sys.argv[8]

try: 
	#print os.environ
	print os.environ['OS']  #put in LOG
except: pass
"""
Windows Vista x32
19:13:31 T:7064  NOTICE: Starting Kodi (14.0 Git:20141223-ad747d9). Platform: Windows NT x86 32-bit
19:13:31 T:7064  NOTICE: Using Release Kodi x32 build
19:13:31 T:7064  NOTICE: Kodi compiled Dec 23 2014 by MSVC 180030723 for Windows NT x86 32-bit version 6.0 (0x06000000)
19:13:31 T:7064  NOTICE: Running on LG Electronics E300-A.C4HGV with Windows Vista SP2, kernel: Windows NT x86 32-bit version 6.0
19:13:31 T:7064  NOTICE: Host CPU: Intel(R) Core(TM)2 Duo CPU T8100 @ 2.10GHz, 2 cores available
19:13:31 T:7064  NOTICE: Desktop Resolution: 1280x800 32Bit at 60Hz

21:14:02 T:6420  NOTICE: {'TMP': 'C:\\Users\\Antibes\\AppData\\Local\\Temp', 'COMPUTERNAME': 'ANTIBES-PC', 'USERDOMAIN': 'Antibes-PC', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'PROCESSOR_IDENTIFIER': 'x86 Family 6 Model 23 Stepping 6, GenuineIntel', 'PROGRAMFILES': 'C:\\Program Files', 'PROCESSOR_REVISION': '1706', 'SYSTEMROOT': 'C:\\Windows', 'PATH': 'C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Program Files\\ATI Technologies\\ATI.ACE\\Core-Static;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\Kodi\\system\\;C:\\Program Files\\Kodi\\system\\players\\dvdplayer\\;C:\\Program Files\\Kodi\\system\\players\\paplayer\\;C:\\Program Files\\Kodi\\system\\cdrip\\;C:\\Program Files\\Kodi\\system\\python\\;C:\\Program Files\\Kodi\\system\\webserver\\;C:\\Program Files\\Kodi\\', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'TEMP': 'C:\\Users\\Antibes\\AppData\\Local\\Temp', 'PROCESSOR_ARCHITECTURE': 'x86', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'SESSIONNAME': 'Console', 'HOMEPATH': '\\Users\\Antibes', 'PYTHONOPTIMIZE': '1', 'USERNAME': 'Antibes', 'LOGONSERVER': '\\\\ANTIBES-PC', 'LOCALAPPDATA': 'C:\\Users\\Antibes\\AppData\\Local', 'PROGRAMDATA': 'C:\\ProgramData', 'TRACE_FORMAT_SEARCH_PATH': '\\\\NTREL202.ntdev.corp.microsoft.com\\4F18C3A5-CA09-4DBD-B6FC-219FDD4C6BE0\\TraceFormat', 'PYTHONPATH': 'C:\\Program Files\\Kodi\\system\\python\\DLLs;C:\\Program Files\\Kodi\\system\\python\\Lib', 'KODI_PROFILE_USERDATA': 'C:\\Users\\Antibes\\AppData\\Roaming\\Kodi\\userdata\\', 'KODI_HOME': 'C:\\Program Files\\Kodi', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'CONFIGSETROOT': 'C:\\Windows\\ConfigSetRoot', 'FP_NO_HOST_CHECK': 'NO', 'WINDIR': 'C:\\Windows', 'APPDATA': 'C:\\Users\\Antibes\\AppData\\Roaming', 'HOMEDRIVE': 'C:', 'SYSTEMDRIVE': 'C:', 'PYTHONHOME': 'C:\\Program Files\\Kodi\\system\\python', 'NUMBER_OF_PROCESSORS': '2', 'PROCESSOR_LEVEL': '6', 'DFSTRACINGON': 'FALSE', 'OS': 'win32', 'PUBLIC': 'C:\\Users\\Public', 'USERPROFILE': 'C:\\Users\\Antibes'}
21:14:02 T:6420  NOTICE: win32

Linux Ubuntu x64
01:02:48 T:139721866180544  NOTICE: Starting Kodi (14.1 Git:38e4046). Platform: Linux x86 64-bit
01:02:48 T:139721866180544  NOTICE: Using Release Kodi x64 build
01:02:48 T:139721866180544  NOTICE: Kodi compiled Jan 30 2015 by GCC 4.8.2 for Linux x86 64-bit version 3.13.11 (199947)
01:02:48 T:139721866180544  NOTICE: Running on Ubuntu 14.04.1 LTS, kernel: Linux x86 64-bit version 3.13.0-44-generic
01:02:48 T:139721866180544  NOTICE: FFmpeg statically linked, version: 2.4.6-xbmc-2.4.6-Helix
01:02:48 T:139721866180544  NOTICE: Host CPU: Intel(R) Core(TM) i5-2520M CPU @ 2.50GHz, 4 cores available

01:03:29 T:139720487057152  NOTICE: {'LC_NUMERIC': 'en_US.UTF-8', 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/hans', 'QT4_IM_MODULE': 'xim', 'LC_MEASUREMENT': 'en_US.UTF-8', 'XDG_CURRENT_DESKTOP': 'Unity', 'KODI_BIN_HOME': '/usr/lib/kodi', 'LC_PAPER': 'en_US.UTF-8', 'QT_IM_MODULE': 'ibus', 'LOGNAME': 'hans', 'USER': 'hans', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games', 'XDG_VTNR': '7', 'HOME': '/home/hans', 'DISPLAY': ':0', 'LANG': 'en_GB.UTF-8', 'SHELL': '/bin/bash', 'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0', 'XAUTHORITY': '/home/hans/.Xauthority', 'LANGUAGE': 'en_GB:en', 'SESSION_MANAGER': 'local/ThinkPad-X220:@/tmp/.ICE-unix/1329,unix/ThinkPad-X220:/tmp/.ICE-unix/1329', 'LC_MONETARY': 'en_US.UTF-8', 'QT_QPA_PLATFORMTHEME': 'appmenu-qt5', 'LC_IDENTIFICATION': 'en_US.UTF-8', '__GL_SYNC_TO_VBLANK': '1', 'TEXTDOMAIN': 'im-config', 'COMPIZ_CONFIG_PROFILE': 'ubuntu', 'SESSION': 'ubuntu', 'SESSIONTYPE': 'gnome-session', 'IM_CONFIG_PHASE': '1', 'GIO_LAUNCHED_DESKTOP_FILE_PID': '9034', 'GPG_AGENT_INFO': '/run/user/1000/keyring-h9aWdK/gpg:0:1', 'CLUTTER_IM_MODULE': 'xim', 'SELINUX_INIT': 'YES', 'GIO_LAUNCHED_DESKTOP_FILE': '/usr/share/applications/kodi.desktop', 'XDG_RUNTIME_DIR': '/run/user/1000', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'LC_ADDRESS': 'en_US.UTF-8', 'COMPIZ_BIN_PATH': '/usr/bin/', 'PYTHONCASEOK': '1', 'SSH_AUTH_SOCK': '/run/user/1000/keyring-h9aWdK/ssh', 'GDMSESSION': 'ubuntu', 'XMODIFIERS': '@im=ibus', 'TEXTDOMAINDIR': '/usr/share/locale/', 'KODI_HOME': '/usr/share/kodi', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/', 'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0', 'TZ': ':Europe/Copenhagen', 'XDG_SESSION_ID': 'c1', 'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-6OJtsNUdQb', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 'SDL_VIDEO_ALLOW_SCREENSAVER': '1', 'GTK_IM_MODULE': 'ibus', 'DESKTOP_SESSION': 'ubuntu', 'UPSTART_SESSION': 'unix:abstract=/com/ubuntu/upstart-session/1000/1139', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg', 'GTK_MODULES': 'overlay-scrollbar:unity-gtk-module', '__GL_YIELD': 'USLEEP', 'GDM_LANG': 'en_GB', 'LC_TELEPHONE': 'en_US.UTF-8', 'PAPERSIZE': 'letter', 'INSTANCE': '', 'PWD': '/home/hans', 'JOB': 'dbus', 'LC_NAME': 'en_US.UTF-8', 'XDG_MENU_PREFIX': 'gnome-', 'LC_TIME': 'en_US.UTF-8', 'OS': 'Linux', 'XDG_SEAT': 'seat0'}
01:03:29 T:139720487057152  NOTICE: Linux

Android Tab Simulator
01:16:17 T:18446744072499033024  NOTICE: Starting Kodi (14.1 Git:2015-01-30-38e4046-dirty). Platform: Android ARM 32-bit
01:16:17 T:18446744072499033024  NOTICE: Using Release Kodi x32 build
01:16:17 T:18446744072499033024  NOTICE: Kodi compiled Jan 30 2015 by GCC 4.8.0 for Android ARM 32-bit API level 14 (API level 14)
01:16:17 T:18446744072499033024  NOTICE: Running on samsung SM-G900F with Android 4.4.2 API level 19, kernel: Linux ARM 32-bit version 3.10.30-android-x86-hd+
01:16:17 T:18446744072499033024  NOTICE: FFmpeg version: 14.0-Helix-87-g38e4046-xbmc-2.4.6-Helix
01:16:17 T:18446744072499033024  NOTICE: Host CPU: ARMv7 processor rev 1 (v7l), 0 cores available
01:16:17 T:18446744072499033024  NOTICE: Product: kltexx, Device: klte, Board: MSM8974 - Manufacturer: samsung, Brand: samsung, Model: SM-G900F, Hardware: unknown
01:16:17 T:18446744072499033024  NOTICE: ARM Features: Neon enabled

01:36:16 T:18446744072513306048  NOTICE: {'force_s3tc_enable': 'true', 'XBMC_ANDROID_SYSTEM_LIBS': '/vendor/lib:/system/lib:/system/lib/arm:/data/downloads', 'EXTERNAL_STORAGE': '/storage/sdcard', 'LOOP_MOUNTPOINT': '/mnt/obb', 'ANDROID_SOCKET_zygote': '9', 'BOOTCLASSPATH': '/system/framework/core.jar:/system/framework/conscrypt.jar:/system/framework/okhttp.jar:/system/framework/core-junit.jar:/system/framework/bouncycastle.jar:/system/framework/ext.jar:/system/framework/framework.jar:/system/framework/framework2.jar:/system/framework/telephony-common.jar:/system/framework/voip-common.jar:/system/framework/mms-common.jar:/system/framework/android.policy.jar:/system/framework/services.jar:/system/framework/apache-xml.jar:/system/framework/webviewchromium.jar', 'ANDROID_PROPERTY_WORKSPACE': '8,0', 'PATH': '/sbin:/vendor/bin:/system/sbin:/system/bin:/system/xbin:/system/xbin/bstk', 'HOME': '/storage/sdcard/Android/data/org.xbmc.kodi/files', '__GL_SYNC_TO_VBLANK': '1', 'ANDROID_STORAGE': '/storage', 'LD_LIBRARY_PATH': '/vendor/lib:/system/lib:/system/lib/arm:/data/downloads', 'ANDROID_ASSETS': '/system/app', 'ANDROID_BOOTLOGO': '1', 'XBMC_ANDROID_LIBS': '/data/app-lib/org.xbmc.kodi-1', 'PYTHONNOUSERSITE': '1', 'PYTHONOPTIMIZE': '', 'XBMC_ANDROID_APK': '/data/app/org.xbmc.kodi-1.apk', 'PYTHONPATH': '', 'ANDROID_DATA': '/data', 'BIONIC_DNSCACHE': '1', 'KODI_HOME': '/data/data/org.xbmc.kodi/cache/apk/assets', 'KODI_BIN_HOME': '/data/data/org.xbmc.kodi/cache/apk/assets', '__GL_YIELD': 'USLEEP', 'ANDROID_ROOT': '/system', 'PYTHONHOME': '/data/app/org.xbmc.kodi-1.apk/assets/python2.6', 'ASEC_MOUNTPOINT': '/mnt/asec', 'OS': 'Linux'}
01:36:16 T:18446744072513306048  NOTICE: Linux

"""

def rtmpdumpFilename():
	if ADDON.getSetting('DebugRecording')=='false': #dont update Paltform if debugging recordings
		try:
			Platform = recordings.FindPlatform()
			ADDON.setSetting('osplatform','')
			if Platform == 'Windows NT x86 32-bit':
				ADDON.setSetting('os','11')
			elif Platform == 'Windows NT x86 64-bit':
				ADDON.setSetting('os','11')
			elif Platform == 'Android ARM 32-bit':
				ADDON.setSetting('os','0')
			elif Platform == 'Android x86 32-bit':
				ADDON.setSetting('os','1')
			elif Platform == 'Linux x86 64-bit':
				ADDON.setSetting('os','7')
			elif Platform == 'Linux x86 32-bit':
				ADDON.setSetting('os','6')
			else:
				print 'record.py Your platform= %s has not been set automatically!' % repr(Platform)  # Put in LOG
		except:
			pass
			print 'record.py Failed to automatically update platform!'  # Put in LOG
		ADDON.setSetting('osplatform',ADDON.getSetting('os'))
		print 'Running on: %s' % repr( ADDON.getSetting('runningon'))
		if 'OpenELEC' in ADDON.getSetting('runningon'):
			ADDON.setSetting('os','12')
		if 'samsung' in ADDON.getSetting('runningon'):
			ADDON.setSetting('os','13')
		if 'WOZTEC' in ADDON.getSetting('runningon'):
			ADDON.setSetting('os','13')
		if 'MBX' in ADDON.getSetting('runningon'): 
			ADDON.setSetting('os','13')
		if 'Genymotion' in ADDON.getSetting('runningon'): 
			ADDON.setSetting('os','13')
		#if 'Ubuntu' in ADDON.getSetting('runningon'):  # ONLY TEST
		#	ADDON.setSetting('os','13')
	quality = ADDON.getSetting('os')
	if quality == '0':
		return 'androidarm/rtmpdump'
	elif quality == '1':
		return 'android86/rtmpdump'
	elif quality == '2':
		return 'atv1linux/rtmpdump'
	elif quality == '3':
		return 'atv1stock/rtmpdump'
	elif quality == '4':
		return 'atv2/rtmpdump'
	elif quality == '5':
		return 'ios/rtmpdump'
	elif quality == '6':
		return 'linux32/rtmpdump'
	elif quality == '7':
		return 'linux64/rtmpdump'
	elif quality == '8':
		return 'osx106/rtmpdump'
	elif quality == '9':
		return 'osx107/rtmpdump'
	elif quality == '10':
		return 'pi/rtmpdump'
	elif quality == '11':
		return 'win/rtmpdump.exe'
	elif quality == '12':
		return '/usr/bin/rtmpdump'
	elif quality == '13':
		return '/data/local/tmp/rtmpdump'   # '/system/bin/rtmpdump'  # HOTFIX Android - rtmpdump moved to /system/bin (& library to /system/lib)
	else:
		print 'record.py Your platform= %s has not been set automatically!' % repr(Platform)  # Put in LOG
		return

LoopCountMax = int(ADDON.getSetting('LoopCount'))

rtmpdumpEXEp = rtmpdumpFilename()
quality = ADDON.getSetting('os')
if quality == '13':
	osplatform = ADDON.getSetting('osplatform')
	print 'record.py: osplatform= %s' % osplatform
	try:
		import shutil
		os.chmod(rtmpdumpEXEp, 0777)
	except:
		pass
	try:
		if osplatform == 0:
			osplatformexe = 'androidarm/rtmpdump'
			#osplatformlib = 'androidarm/librtmp.so'
		else:
			osplatformexe = 'android86/rtmpdump'
			#osplatformlib = 'android86/librtmp.so.0'
		print 'record.py: try to copy %s --> %s' % (osplatformexe,rtmpdumpEXEp)
		shutil.copyfile(os.path.join(ADDON.getAddonInfo('path'),'rtmpdump',osplatformexe),rtmpdumpEXEp)		
		print 'record.py: copied %s --> %s' % (osplatformexe,rtmpdumpEXEp)
	except:
		pass
		print 'record.py: copied FAILED %s --> %s' % (osplatformexe,rtmpdumpEXEp)
	try:
		os.chmod(rtmpdumpEXEp, 0777) 
	except:
		pass
		print 'record.py: set 0777 FAILED %s --> /system/bin/rtmpdump' % osplatformexe
	"""
	try:
		os.chmod('/system/lib/librtmp.so', 0777)
	except:
		pass
		print 'record.py: set 0777 FAILED %s --> /system/lib/librtmp.so' % osplatformlib
	try:
		os.chmod('/system/lib/librtmp.so.0', 0777)
	except:
		pass
		print 'record.py: set 0777 FAILED %s --> /system/lib/librtmp.so.0' % osplatformlib
	try:
		print 'record.py: try to copied %s --> /system/lib/librtmp.so(.0)' % osplatformlib
		if osplatform == 0:
			shutil.copyfile(os.path.join(ADDON.getAddonInfo('path'),'rtmpdump',osplatformlib),'/system/lib/librtmp.so') 
		else:
			shutil.copyfile(os.path.join(ADDON.getAddonInfo('path'),'rtmpdump',osplatformlib),'/system/lib/librtmp.so.0') 
		print 'record.py: copied %s --> /system/lib/librtmp.so(.0)' % osplatformlib
	except:
		pass
		print 'record.py: copy FAILED %s --> /system/lib/librtmp.so(.0)' % osplatformlib
	try:
		if osplatform == 0:
			os.chmod('/system/lib/librtmp.so', 0777)
	except:
		pass
		print 'record.py: set 0777 FAILED %s --> /system/lib/librtmp.so' % osplatformlib
	try:
		if not osplatform == 0:
			os.chmod('/system/lib/librtmp.so.0', 0777)
	except:
		pass
		print 'record.py: set 0777 FAILED %s --> /system/lib/librtmp.so.0' % osplatformlib
"""
	rtmpdumpEXE = rtmpdumpEXEp
else:
	rtmpdumpEXE = os.path.join(ADDON.getAddonInfo('path'),'rtmpdump',rtmpdumpEXEp)
print 'record.py: rtmpdumpEXE= %s' % repr(rtmpdumpEXE)
print 'record.py: os.path.exists(rtmpdumpEXE)= %s' % repr(os.path.exists(rtmpdumpEXE))
xbmc.log('stats os.F_OK: %s' % os.access(rtmpdumpEXE, os.F_OK))
xbmc.log('stats os.W_OK: %s' % os.access(rtmpdumpEXE, os.W_OK))
xbmc.log('stats os.X_OK: %s' % os.access(rtmpdumpEXE, os.X_OK))

if not xbmc.getCondVisibility('system.platform.windows'):
	if os.access(rtmpdumpEXE, os.X_OK):
		print 'Permissions ------ 0777 ----- GREAT !!'  # Put in LOG
	else:
		print 'Permissions -----------------   BAD !!'  # Put in LOG
		for dirpath, dirnames, filenames in os.walk(os.path.join(ADDON.getAddonInfo('path'),'rtmpdump')):
			for filename in filenames:
				path = os.path.join(dirpath, filename)
				try:
					os.chmod(path, 0777) 
					print 'Permissions set with: CHMOD 0777 !!'  # Put in LOG
				except: pass

if os.access(rtmpdumpEXE, os.X_OK):
	#print 'os.access(/home/hans/.xbmc/addon/plugin.video.wozboxntv.beta/rtmpdump/linux32/rtmpdump, os.X_OK)= OK'
	RecordingDisabled = False
else:
	time.sleep(1)
	#print 'os.access(/home/hans/.xbmc/addon/plugin.video.wozboxntv.beta/rtmpdump/linux32/rtmpdump, os.X_OK)= FAIL'
	recordings.updateRecordingPlanned(nameAlarm, '[COLOR red]Set this program executable:[/COLOR] %s' % (rtmpdumpEXE))
	utils.notification('Recording %s [COLOR red]NOT possible! Set this program executable:[/COLOR] %s' % (title,rtmpdumpEXE))
	time.sleep(1000)
	RecordingDisabled = True

#print 'record.py: nameAlarm= %s' % (str(repr(nameAlarm)))
#print 'record.py: LoopCountMax= %s' % (str(repr(LoopCountMax)))
recordPath = xbmc.translatePath(os.path.join(ADDON.getSetting('record_path')))
print 'record.py: recordPath= %s' %recordPath

def libPath():
	quality = ADDON.getSetting('os')
	print 'record.py: quality= %s' %quality
	if quality == '0':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'androidarm')
	elif quality == '1':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'android86')
	elif quality == '2':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'atv1linux')
	elif quality == '3':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'atv1stock')
	elif quality == '4':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'atv2')
	elif quality == '5':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'ios')
	elif quality == '6':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'linux32')
	elif quality == '7':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'linux64')
	elif quality == '8':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'osx106')
	elif quality == '9':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'osx107')
	elif quality == '10':
		return os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', 'pi')
	elif quality == '11':
		return 'None'   
	elif quality == '12':
		return '/usr/bin/'
	elif quality == '13':
		LIBpath = '/data/data/org.xbmc.kodi/lib/'
		print 'record.py: os.path.exists(%s)= %s' % (repr(LIBpath),repr(os.path.exists(LIBpath)))
		print 'record.py: os.path.exists(%s)= %s' % (repr(LIBpath + 'librtmp.so'),repr(os.path.exists(LIBpath + 'librtmp.so')))
		return LIBpath

if xbmc.getCondVisibility('system.platform.linux'):
    for dirpath, dirnames, filenames in os.walk(os.path.join(ADDON.getAddonInfo('path'),'rtmpdump')):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            os.chmod(path, 0777) 
def runCommand(cmd, LoopCount, libpath = None, module_path = './'):
	print 'record.py: cmd= %s' % repr(cmd)
	print 'record.py: LoopCount= %s' % repr(LoopCount)
	print 'record.py: libpath= %s' % repr(libpath)
	print 'record.py: module_path= %s' % repr(module_path)
	from subprocess import Popen, PIPE, STDOUT
	# get the list of already defined env settings
	env = os.environ
	print 'record.py: env= %s' % env
	if LoopCount == 0:
		if (libpath):
			print 'record.py: libpath1= %s' %repr(libpath)
			# add the additional env setting
			envname = "LD_LIBRARY_PATH"
			if (env.has_key(envname)):
				env[envname] = env[envname] + ":" + libpath
			else:
				env[envname] = libpath

			envname = "DYLD_LIBRARY_PATH"
			if (env.has_key(envname)):
				env[envname] = env[envname] + ":" + libpath
			else:
				env[envname] = libpath

		if (env.has_key('PYTHONPATH')):
			env['PYTHONPATH'] = env['PYTHONPATH']+':' + module_path
		else:
			env['PYTHONPATH'] = module_path
                    
	#try:
		#print 'env[PYTHONPATH]        = ' + env['PYTHONPATH']
		#print 'env[LD_LIBRARY_PATH]   = ' + env['LD_LIBRARY_PATH']
		#print 'env[DYLD_LIBRARY_PATH] = ' + env['DYLD_LIBRARY_PATH']
	#except:
		#pass
	print 'record.py: cmd1= %s' %repr(cmd)
	print 'record.py: env= %s' %repr(env)
	try:
		subpr = Popen(cmd, shell=True, env=env, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
		print 'record.py: subpr= %s' %(repr(subpr))
		Pname = str(repr(subpr))
		print 'record.py: Pname= %s' %(repr(Pname))
		#ADDON = xbmcaddon.Addon(id='plugin.video.wozboxntv.beta')
		#ADDON.setSetting('LastRecordProcess', Pname)

		
		#print "waiting for recording to stop.0.."
		x = subpr.stdout.read()
		while subpr.poll() == None:
			#ADDON.setSetting('LastRecordProcess', 'Waiting for recording to stop...' + Pname)
			#print "waiting for recording to stop.1.."
			time.sleep(2)
			#print "waiting for recording to stop.2..."
			x = subpr.stdout.read()
		#ADDON.setSetting('LastRecordProcess', '')
	except:
		pass
		print 'ERROR record.py: Basic recording function failed!'  # Put in LOG
		utils.notification('[COLOR red]ERROR record.py: Basic recording function failed![/COLOR]')
		recordings.updateRecordingPlanned(nameAlarm, '[COLOR red]ERROR record.py: Basic recording function failed![/COLOR]' + title)
		time.sleep(1000)


net=net.Net()

datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
cookie_path = os.path.join(datapath, 'cookies')

loginurl = 'http://www.ntv.mx/index.php?' + recordings.referral()+ 'c=3&a=0'
username = ADDON.getSetting('user')
password = md5(ADDON.getSetting('pass')).hexdigest()


data     = {'email': username,
                                        'psw2': password,
                                        'rmbme': 'on'}
headers  = {'Host':'www.ntv.mx',
                                        'Origin':'http://www.ntv.mx',
                                        'Referer':'http://www.ntv.mx/index.php?' + recordings.referral()+ 'c=3&a=0'}
                                        
#create cookie
html = net.http_POST(loginurl, data, headers)
cookie_jar = os.path.join(cookie_path, "ntv.lwp")
if os.path.exists(cookie_path) == False:
        os.makedirs(cookie_path)
net.save_cookies(cookie_jar)

#set cookie to grab url
net.set_cookies(cookie_jar)

Retry = True
LoopCount = 0
import locking
try:
	nowHM=datetime.datetime.today().strftime('%H:%M:%S')
except:
	pass
try:
	#locking.recordUnlock(title)
	#A new recording unlocks all previous - otherwise the retry feature will make some fuzz
	locking.recordUnlockAll()
except:
	pass
try:
	locking.recordLock(nameAlarm)
except:
	pass
#print 'record.py: title= %s' % repr(title)
while (Retry == True) and (LoopCount < LoopCountMax) and (locking.isRecordLocked(nameAlarm)):
	nowHM=datetime.datetime.today().strftime('%H:%M:%S')
	#print 'record.py0: title= %s, LoopCount= %s at %s' % (repr(title),repr(LoopCount),nowHM)
	url      = 'http://www.ntv.mx/index.php?' + recordings.referral()+ 'c=6&a=0&mwAction=content&xbmc=1&mwData={"id":%s,"type":"tv"}' % cat
	link     = net.http_GET(url,headers={"User-Agent":"NTV-XBMC-" + ADDON.getAddonInfo('version')}).content
	data     = json.loads(link)
	playchannelName = default.ChannelName(cat)
	if playchannelName == '':
		playchannel = str(cat) 
	else:
		playchannel = playchannelName
	try:
		rtmp     = data['src']
	except:
		pass
		utils.notification('Recording [COLOR red]NOT possible! No data on channel[/COLOR] %s' % (playchannel))
		recordings.updateRecordingPlanned(nameAlarm, 'Recording [COLOR red]NOT possible! No data on channel[/COLOR] '+ playchannel + " - " + title + ' at ' + nowHM)
		#nowHM=datetime.datetime.today().strftime('%H:%M:%S')
		#print 'record.py1: title= %s, LoopCount= %s at %s' % (repr(title),repr(LoopCount),nowHM)
		time.sleep(10)
		#nowHM=datetime.datetime.today().strftime('%H:%M:%S')
		#print 'record.py2: title= %s, LoopCount= %s at %s' % (repr(title),repr(LoopCount),nowHM)
		rtmp = ''
	#nowHM=datetime.datetime.today().strftime('%H:%M:%S')
	#print 'record.py3: title= %s, LoopCount= %s at %s' % (repr(title),repr(LoopCount),nowHM)
	#utils.notification('Recording %s [COLOR orange]LOOP %s[/COLOR]' % (title, nowHM))
	if rtmp == '' :
		Retry = True
		LoopCount += 1
		LoopCountMax = int(ADDON.getSetting('LoopCount'))
		nowHM=datetime.datetime.today().strftime('%H:%M:%S')
		#print 'record.py4: title= %s, LoopCount= %s at %s' % (repr(title),repr(LoopCount),nowHM)
	else:
		nowHM=datetime.datetime.today().strftime('%H:%M:%S')
		#print 'record.py5: title= %s, LoopCount= %s at %s' % (repr(title),repr(LoopCount),nowHM)
		rtmp  = '%s' % (rtmp)
		cmd  =  os.path.join(ADDON.getAddonInfo('path'),'rtmpdump', rtmpdumpFilename())
		cmd += ' --stop ' + str(duration) 
		cmd += ' --live '
		#cmd += ' --flv "' + recordPath + '['+datetime.datetime.today().strftime('%Y-%m-%d %H-%M')+ ' ' +str(LoopCount) +'] - ' + playchannel + ' - ' + re.sub('[,:\\/*?\<>|"]+', '', title) + '.flv"'
		filetitle = title.replace('?', '')
		filetitle = filetitle.replace(':', ' -')
		filetitle = filetitle.replace('/', '')
		filetitle = filetitle.replace('+', '')
		filetitle = filetitle.replace('\\', '')
		filetitle = re.sub('[,:\\/*?\<>|"]+', '', filetitle)
		filetitle = " ".join(filetitle.split())  # Remove extra spaces from filename
		cmd += ' --flv "' + recordPath + filetitle + ' ['+datetime.datetime.today().strftime('%Y-%m-%d %H-%M')+ ' ' +str(LoopCount) +' ' + playchannel  +'].flv"'
		cmd += ' --rtmp "' + rtmp
		cmd += '"'
	
		nowHM=datetime.datetime.today().strftime('%H:%M')
		
		if LoopCount == 0 and not RecordingDisabled:
			utils.notification('Recording %s [COLOR green]started %s[/COLOR]' % (title, nowHM))
			recordings.updateRecordingPlanned(nameAlarm, '[COLOR green]Started ' + nowHM + '[/COLOR] ' + title)
		else:
			LoopNr = str(LoopCount)
			if not RecordingDisabled:
				utils.notification('Recording %s [COLOR orange]RESTARTED# %s %s[/COLOR]' % (title, LoopNr, nowHM))
				recordings.updateRecordingPlanned(nameAlarm, '[COLOR orange]Restarted# %s %s[/COLOR] %s' % (LoopNr, nowHM, title))
		
		if ADDON.getSetting('os')=='11':
				#print 'libpath= None os=11'
				runCommand(cmd, LoopCount, libpath=None)
		else:
				libpath = libPath()
				#print 'libpath= %s' % libpath
				runCommand(cmd, LoopCount, libpath=libpath)

		nowP = recordings.parseDate(datetime.datetime.today())
		endTimeO =  recordings.parseDate(endTime)
		time_tuple = endTimeO.timetuple()
		timestamp = time.mktime(time_tuple) - 120
		endTimeM = datetime.datetime.fromtimestamp(timestamp)
		endTimeP =  recordings.parseDate(endTimeM)
		nowHM=datetime.datetime.today().strftime('%H:%M')
		if 	endTimeP > nowP and not RecordingDisabled:
			recordings.updateRecordingPlanned(nameAlarm, '[COLOR red]Completed Early ' + nowHM + '[/COLOR] ' + title)
			startTime = nowP
			Retry = True
			LoopCount += 1
			LoopCountMax = int(ADDON.getSetting('LoopCount'))
		else:
			if not RecordingDisabled:
				recordings.updateRecordingPlanned(nameAlarm, '[COLOR green]Complete ' + nowHM + '[/COLOR] ' + title)
			Retry = False

if not RecordingDisabled:
	utils.notification('Recording %s [COLOR red]complete[/COLOR]' % title)
locking.recordUnlock(nameAlarm)
