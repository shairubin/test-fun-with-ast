

def _translate_api(self, query, from_lang, to_lang):

    # Build request
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "appid": f"{self.appid}",
        "q": f"{query}",
        "from": from_lang,
        "to": to_lang,
        "salt": f"{salt}",
        "sign": f"{sign}",
    }

    # Send request
    time.sleep(1 / self.qps)


