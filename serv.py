from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    # Create a DummyAuthorizer object to manage user permissions
    authorizer = DummyAuthorizer()

    # Add a user with username 'YOUR_NAME', password '12345',
    # and the home directory '/Users/YOUR_NAME' with specific permissions
    # authorizer.add_user('YOUR_NAME', '12345', '/Users/YOUR_NAME', perm='elradfmwMT')

    # Add an anonymous user with home directory "DATAPATH" and specific permissions
    authorizer.add_anonymous(homedir="DATAPATH", perm="elradfmwMT")

    # Create an instance of FTPHandler
    handler = FTPHandler

    # Assign the authorizer to the handler
    handler.authorizer = authorizer

    # Set a custom banner message for the FTP server
    handler.banner = "pyftpdlib based ftpd ready."

    # Define the address and port for the FTP server to listen on (port 21)
    address = ('', 21)

    # Create an FTPServer instance bound to the defined address using the handler
    server = FTPServer(address, handler)

    # Limit the maximum number of simultaneous connections to 256
    server.max_cons = 256

    # Limit the maximum number of simultaneous connections per IP address to 5
    server.max_cons_per_ip = 5

    # Start serving FTP requests indefinitely
    server.serve_forever()


if __name__ == '__main__':
    main()
