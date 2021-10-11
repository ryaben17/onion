"""
This file contains classes to handle sessions.
"""
import json
import requests

class Session():
    """
    This class handles the session, storing cookies and allowing for requests.
    It also loads the configuration for Tor connections
    """

    # Initialize the session to an empty value
    _session = None
    _cookies = None
    _headers = {}

    def __init__(self, tor: bool = False, cookies: dict = None, headers: dict = None) -> None:
        self.session = tor
        self.cookies = cookies
        self.headers = headers

    @property
    def headers(self):
        return self._headers


    @headers.setter
    def headers(self, headers):
        self._headers.update(headers)

        if self.session:
            self.session.headers = self._headers

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, cookies: dict = None) -> dict:
        # set the cookies
        self._cookies = cookies
        
        # check if there is any session yet, and if there is, set
        # the cookies.
        if self.session and cookies:
            self.session.cookies = self._cookies

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, tor: bool = False) -> requests.Session:
        if self._session:
            print("Session already created!\n Creating new Session...")

        # create a new session
        session = requests.session()

        # if we need a Tor session, we will use a proxy for our
        # connection send the packets over it.
        if tor:
            session.proxies = {
                "https": 'socks5h://localhost:9050',
                "http": 'socks5h://localhost:9050'
            }

        self._session = session
        return self._session


