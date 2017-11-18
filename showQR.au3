#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.9.19 (Beta)
 Author: raoyi

 Script Function:
	Show a image in a borderless window

#ce ----------------------------------------------------------------------------

#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>

$imgsize = Number(IniRead(@ScriptDir&"\CreateQR.ini", "Config", "imgsize", "200"))
$wait = Number(IniRead(@ScriptDir&"\CreateQR.ini", "Config", "wait", "5"))
$imgadd = IniRead(@ScriptDir&"\CreateQR.ini","Config","imgadd", "QRcode.jpg")

If $cmdline[0] = 0 Then
	$sec = 30000
	$timeout = 30000
Else
	$timeout = $cmdline[1] * 1000
EndIf

If $cmdline[0] < 2 Then
	While 1
		Run("CreateQR.exe")
		Sleep($wait * 1000)
		If FileExists($imgadd) Then
			GUIDelete()
			Global $n, $msg
				GUICreate("My GUI picture", $imgsize, $imgsize, @DesktopWidth-$imgsize, 0, $WS_POPUP + $WS_BORDER )
				GUISetBkColor(0xE0FFFF)
				$n = GUICtrlCreatePic($imgadd, 0, -1, $imgsize, $imgsize)
				GUISetState()
			Sleep($timeout)
		Else
			MsgBox(0,"Error","QRcode Image is lost!")
		EndIf
	WEnd
Else
	Run("CreateQR.exe")
	Sleep($wait * 1000)
	If FileExists($imgadd) Then
			GUIDelete()
			Global $n, $msg
				GUICreate("My GUI picture", $imgsize, $imgsize, (@DesktopWidth-$imgsize)/2, (@DesktopHeight-$imgsize)/2, $WS_POPUP + $WS_BORDER )
				GUISetBkColor(0xE0FFFF)
				$n = GUICtrlCreatePic($imgadd, 0, -1, $imgsize, $imgsize)
				GUISetState()
		While 1
			Sleep($timeout)
			If $cmdline[$cmdline[0]] = 0 Then
				Shutdown(1)
			EndIf
		WEnd
	Else
		MsgBox(0,"Error","QRcode Image is lost!")
	EndIf
EndIf
