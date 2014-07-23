# http://www.seanbehan.com/how-to-create-a-date-time-snippet-in-sublime-text-2-dynamic-signature-with-time-stamp
# http://net.tutsplus.com/tutorials/python-tutorials/how-to-create-a-sublime-text-2-plugin/
# https://gist.github.com/uberbuilder/4657558
# http://www.cnblogs.com/restran/archive/2013/01/07/2850254.html

import datetime, getpass
import sublime, sublime_plugin

class AddDateTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S") } )

class AddDateStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%Y-%m-%d") } )

class AddTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%H:%M:%S") } )
