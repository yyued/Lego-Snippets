# http://www.seanbehan.com/how-to-create-a-date-time-snippet-in-sublime-text-2-dynamic-signature-with-time-stamp
# http://net.tutsplus.com/tutorials/python-tutorials/how-to-create-a-sublime-text-2-plugin/

import datetime, getpass
import sublime, sublime_plugin

class SignatureCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	self.startloc = self.view.sel()[-1].end()
        signature = "%s" % (datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
        self.view.insert(edit, self.startloc, signature)