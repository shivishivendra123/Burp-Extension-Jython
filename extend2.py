# Burp imports
from burp import IBurpExtender, ITab, IContextMenuFactory,IBurpExtenderCallbacks
from java.io import PrintWriter
from burp import  IHttpRequestResponse
# Jython specific imports for the GUI
from javax import swing
from java.awt import BorderLayout
from java.util import ArrayList
import java.awt.Component;
import java.io.OutputStream;
import java.util.List;
import java.util.Map;
import array
# stdlib
import ast
# from urllib.parse import urlparse, parse_qs
import sys
import threading
import json

# For easier debugging, if you want.
# https://github.com/securityMB/burp-exceptions
try:
    from exceptions_fix import FixBurpExceptions
except ImportError:
    pass

class BurpExtender(IBurpExtender, ITab, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):

        # Required for easier debugging:
        # sys.stdout = callbacks.getStdout()

        # Keep a reference to our callbacks object
        self.callbacks = callbacks

        # Obtain an extension helpers object
        self.helpers = callbacks.getHelpers()

        # Set our extension name
        self.callbacks.setExtensionName("Tester")

        stdout = PrintWriter(callbacks.getStdout(),True)
        res = self.callbacks.getSiteMap('http://quotes.toscrape.com');
        # sitemap  = self.callbacks.getSiteMap('http://quotes.toscrape.com')
        __to__be = []
        __get__directory = []
        direc_dict = {}
        __response__dic = {}
        for i in res:
            request = self.helpers.bytesToString(i.getRequest())
    
            __to__be.append(i.getUrl())

        # print(__to__be)
        string_url = "http://quotes.toscrape.com:80/"
        for i in  range(len(__to__be)):
            if(i == 0):
                __get__directory.append('/')
            else:
                f = str(__to__be[i])
                c =f.replace(string_url,'')
                fi = c.split('/')[0]
                __get__directory.append(fi)

        __get__directory = set(__get__directory)
        __get__directory = list(__get__directory)
        print(__get__directory)
        if "/" in __get__directory:
            __get__directory.remove("/")
        __get__directory.remove('')

        direc = {}
        direc['root']= {}
        direc['root'][string_url] = {}
        for i in __get__directory:
            direc[str(i)] = {}
        # print(direc)
        # print(__get_root_directory)
        # for i in __get__directory:
        #     if(i==0):
        #         direc_dict[i] = i
        #     else:
        #         for key in direc_dict:
        #             if key in i:
        #                 direc_dict[key].append(i)
        #                 break
        #             else:
        #                 continue
        #
        # direc_dict["http://quotes.toscrape.com:80"] = {}
        # # print(direc_dict)
        #
        # direc = direc_dict
        for i in __to__be:
                for key in direc:
                    if(str(key) in str(i)):
                        direc[str(key)][str(i)] = {}
                        direc[str(key)][str(i)]['Method'] = " "
                        direc[str(key)][str(i)]['Params'] = " "
        # print(direc)
        with open('data.txt', 'w') as outfile:
            json.dump(direc, outfile)
        # Create a context menttu
        # callbacks.registerContextMenuFactory(self)

        # Create the tab
    #     self.tab = swing.JPanel(BorderLayout())
    #
    #     # Create a split panel
    #     splitPane = swing.JSplitPane(swing.JSplitPane.VERTICAL_SPLIT)
    #
    #     # Create the top panel containing the text area
    #     box = swing.Box.createVerticalBox()
    #
    #     # Make the text area
    #     row = swing.Box.createHorizontalBox()
    #     textPanel = swing.JPanel()
    #     self.textArea = swing.JTextArea('', 15, 100)
    #     self.textArea.setLineWrap(True)
    #     scroll = swing.JScrollPane(self.textArea)
    #     row.add(scroll)
    #     box.add(row)
    #
    #      # Make a button
    #     row = swing.Box.createHorizontalBox()
    #     row.add(swing.JButton('Mind Map!'))
    #                       # actionPerformed=self.handleButtonClick))
    #     box.add(row)
    #
    #     # Set the top pane
    #     splitPane.setTopComponent(box)
    #
    #     # Bottom panel for the response.
    #     box = swing.Box.createVerticalBox()
    #
    #     # Make the text box for the HTTP response
    #     row = swing.Box.createHorizontalBox()
    #         # self.responseTextArea = swing.JTextArea('', 15, 100)
    #         # self.responseTextArea.setLineWrap(True)
    #     # scroll = swing.JScrollPane(self.responseTextArea)
    #     # row.add(scroll)
    #     # box.add(row)
    #
    #     # Set the bottom pane
    #     splitPane.setBottomComponent(box)
    #
    #     # Start the divider roughly in the middle
    #     splitPane.setDividerLocation(250)
    #
    #     # Add everything to the custom tab
    #     self.tab.add(splitPane)
    #
    #     # Add the custom tab to Burp's UI
    #     callbacks.addSuiteTab(self)
    #     return
    #
    # # Implement ITab
    # def getTabCaption(self):
    #     """Return the text to be displayed on the tab"""
    #     return "B2MM"
    #
    # def getUiComponent(self):
    #     """Passes the UI to burp"""
    #     return self.tab
    #
    # # Implement IContextMenuFactory
    def createMenuItems(self, invocation):
        """Adds the extension to the context menu that
        appears when you right-click an object.
        """
        self.context = invocation
        itemContext = invocation.getSelectedMessages()

        # Only return a menu item if right clicking on a
        # HTTP object
        if itemContext > 0:

            # Must return a Java list
            menuList = ArrayList()
            menuItem = swing.JMenuItem("Send to B2CC",
                                        actionPerformed=self.handleHttpTraffic)
            menuList.add(menuItem)
            return menuList
        return None
    #
    # def handleHttpTraffic(self, event):
    #     """Calls the function to write the HTTP object to
    #     the request text area, and then begins to parse
    #     the HTTP traffic for use in other functions.
    #     """
    #
    #     # Writes to the top pane text box
    #     self.writeRequestToTextBox()
    #
    #
    # def writeRequestToTextBox(self):
    #     """Writes HTTP context item to RequestTransformer
    #     tab text box.
    #     """
    #     httpTraffic = self.context.getSelectedMessages()
    #     httpRequest =  httpTraffic
    #     # request = ''.join(httpRequest)
    #     self.textArea.text = self.context.getSelectedMessages()
        # print(self.callbacks.getSiteMap("http://quotes.toscrape.com"))
    # def handleButtonClick(self, event):
    #     """Attempts to make an HTTP request for the
    #     object in the text area.
    #     """
    #
    #     # Get data about the request that was right clicked
    #     host = self.httpService.host
    #     port = self.httpService.port
    #     protocol = self.httpService.protocol
    #     protoChoice = True if protocol.lower() == 'https' else False
    #
    #     # Parse the text area that should contain an HTTP
    #     # request.
    #     requestInfo = self.helpers.analyzeRequest(self.textArea.text)
        # headers = requestInfo.getHeaders()
        # bodyOffset = requestInfo.bodyOffset
        # body = self.textArea.text[bodyOffset:]
        #
        # # Build the request to be sent
        # request = self.helpers.buildHttpMessage(headers, body)

        # Need to make the HTTP request in new thread to
        # prevent the GUI from locking up while the
        # request is being made.
#         t = threading.Thread(
#             target=self.makeRequest,
#             args=[host, port, protoChoice, request]
#         )
#         t.daemon = True
#         t.start()
#
#     def makeRequest(self, host, port, protoChoice, request):
#         """Makes an HTTP request and writes the response to
#         the response text area.
#         """
#         resp = self.callbacks.makeHttpRequest(
#             host,           # string
#             port,           # int
#             protoChoice,    # bool
#             request         # bytes
#         )
#         self.responseTextArea.text = resp.tostring()
#
# try:
#     FixBurpExceptions()
# except:
#     pass
