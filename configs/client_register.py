class ClientRegister:
    def __init__(self, ip, reception_port, password, online, in_call):
        self._ip = ip
        self._reception_port = reception_port
        self._password = password
        self._online = online
        self._in_call = in_call
    
    def get_ip(self):
        return self._ip

    def get_reception_port(self):
        return self._reception_port
    
    def get_status(self):
        return self._online
    
    def get_password(self):
        return self._password
    
    def get_in_call(self):
        return self._in_call

    def set_online_status(self, online):
        self._online = online 

    def set_reception_port(self, reception_port):
        self._reception_port = reception_port
    
    def set_in_call(self, truth_value):
        self._in_call = truth_value