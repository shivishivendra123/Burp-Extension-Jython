from burp import IBurpExtender
from java.io import PrintWriter
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("Test")
        stdout = PrintWriter(callbacks.getStdout(),True)
        stdout.println("Hello")
        return
