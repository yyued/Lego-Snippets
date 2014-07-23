## About
LEGO Snippets in Sublime Text 2/3

## <a href="https://sublime.wbond.net/installation">How to install</a>
Get Package Control for Sublime Text 2/3. Installation is through the Sublime Text 2/3 console. The console is accessed via the ctrl+` shortcut or the View > Show Console menu. Once open, paste the appropriate Python code for your version of Sublime Text into the console.

### SUBLIME TEXT 2
```
import urllib2,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')
```
### SUBLIME TEXT 3
```
import urllib.request,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

1. Package Control: Add Repository `https://github.com/duowan/LEGO-Snippets`
2. Package Control: Install Package `LEGO Snippets`
3. Restart ST2/3 editor

### “Help! My snippets doesn’t work anymore in HTML/CSS files!”

By default, Emmet overrides Tab key behaviour and expands its own abbreviations instead native snippets. You can either disable this feature in user preferences (add `"disable_tab_abbreviations": true` setting into your _Settings — User_ file) and use `Ctrl+E` or `Ctrl+Alt+Enter` to expand Emmet abbeviations or move your snippets to Emmet as described [here](https://github.com/sergeche/emmet-sublime/issues/16#issuecomment-8427268). I’m investigating possibility to expand native snippets via Emmet Tab key handler.
