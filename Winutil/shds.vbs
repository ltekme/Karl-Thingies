Option Explicit

' Function to prompt the user and handle countdown logic
Function PromptUser(prompt, countdown)
    Dim wshShell, startTime, elapsedTime, result
    Set wshShell = CreateObject("WScript.Shell")
    startTime = Timer ' Get the current time
    elapsedTime = 0
    
    Do While elapsedTime < countdown
        If wshShell.AppActivate("Shutdown Warning") Then
            ' Activate the prompt window if it's minimized or behind other windows
            wshShell.SendKeys("%{TAB}")
        End If
        
        elapsedTime = Timer - startTime ' Calculate elapsed time
        
        If elapsedTime >= countdown Then
            result = vbNo ' Default action after the countdown
        Else
            result = wshShell.Popup(prompt, countdown, "Shutdown Warning", vbYesNo + vbExclamation)
        End If

        If result = vbYes Or result = vbNo Then Exit Do ' Exit loop when user selects Yes or No
        
        WScript.Sleep 200 ' Delay for 200 milliseconds
    Loop
    
    PromptUser = (result = vbYes)
End Function

' Function to perform the shutdown
Sub Shutdown()
    ' MsgBox "Shutdown placeholder for testing", vbInformation, "Shutdown"
    CreateObject("WScript.Shell").Run "shutdown.exe /s /f /t 5", 0, False
End Sub

' Main script logic
Dim prompt, countdown
prompt = "Do you wish to continue using this machine for the next 30 minutes?"
countdown = 60

If Not PromptUser(prompt, countdown) Then
    Shutdown
End If