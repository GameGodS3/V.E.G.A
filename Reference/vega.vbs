Set Vega = Wscript.CreateObject("SAPI.SpVoice")
set wshshell = wscript.CreateObject("wscript.shell")

dim Input

Vega.speak "Please type, what you want to open"
Input=inputbox("Please type what you want to open")

if Input = "google" OR Input="Google" then
Vega.speak "Opening Google"
wshshell.run "www.google.com"

else if Input = "control panel" OR Input="Control Panel" OR Input="Control panel" then
Vega.speak "Opening Control Panel"
wshshell.run "control panel"

else if Input = "bye" then
end if