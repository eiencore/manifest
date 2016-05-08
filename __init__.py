import os
import urllib

if os.path.isdir(".repo/manifests"):
    urllib.urlretrieve("https://alpha.release.core-os.net/amd64-usr/current/version.txt", ".repo/manifests/version.txt")
