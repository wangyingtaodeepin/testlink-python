#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Testlink API Sample Python 3.1.2 getProjects() - Client implementation
# 
import xmlrpc.client
import os

class TestlinkAPIClient:        
    # substitute your server URL Here
    SERVER_URL = os.getenv("XMLRPC_PATH") or "https://*****************/lib/api/xmlrpc/v1/xmlrpc.php"
      
    def __init__(self):
        self.server = xmlrpc.client.ServerProxy(self.SERVER_URL)
        self.devKey = os.getenv("TESTLINKTOKEN") or "**********************************"

    def getInfo(self):
        return self.server.tl.about()

    def getProjects(self):
        return self.server.tl.getProjects(dict(devKey=self.devKey))

    def getClientTL(self):
        return self.server.tl

client = TestlinkAPIClient()
tlclient = client.getClientTL()

args = {}
args["devKey"] = client.devKey
args["testplanname"] = "pythontest"
args["testprojectname"] = "LSTest"

client = TestlinkAPIClient()
tlclient = client.getClientTL()

print(client.getInfo())
print("-" * 80)
print(tlclient.getTestPlanByName(args))
