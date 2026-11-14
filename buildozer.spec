[app]
title = Ahmed
package.name = ahmed
package.domain = org.ahmed
source.dir = .
source.include_exts = py,html,css,js,json,png,jpg
version = 1.0.0
requirements = python3,flask,requests,urllib3,certifi,idna,charset-normalizer,werkzeug,jinja2,markupsafe,itsdangerous,click,blinker
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# إعدادات الـ WebView (أهم جزء)
p4a.bootstrap = webview
p4a.port = 8080

[buildozer]
log_level = 2
warn_on_root = 1
