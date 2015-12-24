Set updateSession = CreateObject("Microsoft.Update.Session")
updateSession.ClientApplicationID = "MSDN Sample Script"

Set updateSearcher = updateSession.CreateUpdateSearcher()

Set searchResult = _
updateSearcher.Search("IsInstalled=0 and Type='Software' and IsHidden=0")

For I = 0 To searchResult.Updates.Count-1
    Set update = searchResult.Updates.Item(I)
Next

Set updatesToDownload = CreateObject("Microsoft.Update.UpdateColl")

For I = 0 to searchResult.Updates.Count-1
    Set update = searchResult.Updates.Item(I)
    addThisUpdate = false
    If update.InstallationBehavior.CanRequestUserInput = true Then
    Set nothing = "Nothing"
    Else
        If update.EulaAccepted = false Then
            strInput = "Y"
            If (strInput = "Y" or strInput = "y") Then
                update.AcceptEula()
                addThisUpdate = true
            Else
            End If
        Else
            addThisUpdate = true
        End If
    End If
    If addThisUpdate = true Then
        updatesToDownload.Add(update)
    End If
Next

If updatesToDownload.Count = 0 Then
Set nothing = "Nothing"
End If

Set downloader = updateSession.CreateUpdateDownloader()
downloader.Updates = updatesToDownload
downloader.Download()

Set updatesToInstall = CreateObject("Microsoft.Update.UpdateColl")

rebootMayBeRequired = false

For I = 0 To searchResult.Updates.Count-1
    set update = searchResult.Updates.Item(I)
    If update.IsDownloaded = true Then
        updatesToInstall.Add(update)
        If update.InstallationBehavior.RebootBehavior > 0 Then
            rebootMayBeRequired = true
        End If
    End If
Next

If updatesToInstall.Count = 0 Then
Set nothing = "Nothing"
End If

If rebootMayBeRequired = true Then
Set nothing = "Nothing"
End If
strInput = "Y"
If (strInput = "Y" or strInput = "y") Then
    Set installer = updateSession.CreateUpdateInstaller()
    installer.Updates = updatesToInstall
    Set installationResult = installer.Install()
End If
