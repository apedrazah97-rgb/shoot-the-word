from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    def log_message(self, format, *args):
        pass  # silenciar logs

os.chdir(r'C:\Users\Andrea Pedraza\Desktop\Mini juegos')
print('Servidor corriendo en puerto 8282...')
HTTPServer(('', 8282), NoCacheHandler).serve_forever()
