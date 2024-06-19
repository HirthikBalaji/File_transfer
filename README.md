# FTP Server with Streamlit Client UI

This project implements an FTP server using Python's `ftplib` and provides a client-side graphical user interface (GUI) powered by Streamlit. The combination allows users to interact with the FTP server using a simple web-based interface.

## Features

- **FTP Server**: Implements an FTP server capable of handling basic file operations such as upload, download, rename, and delete.
- **Streamlit Client UI**: Provides a user-friendly web interface for interacting with the FTP server.
- **Authentication**: Supports basic authentication mechanisms for accessing the FTP server.
- **File Operations**: Allows users to browse directories, upload files, download files.

## Prerequisites

- Python 3.x installed on your system.
- Dependencies listed in `requirements.txt`. Install them using:

  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. **Start the FTP Server**:
   - Run `python serv.py`. By default, the server starts on port 21.

2. **Start the Streamlit Client UI**:
   - Run `streamlit run main.py`. This will launch the Streamlit application in your default web browser.

3. **Accessing the Client UI**:
   - Open the URL provided by Streamlit in your web browser (typically `http://localhost:8501`).

4. **Using the Client UI**:
   - Enter the FTP server details (host, port, username, password) in the Streamlit UI.
   - Navigate through directories, upload, download.

## Configuration

- **Server Configuration**:
  - Modify `serv.py` to change server settings such as port number and root directory.
  - Update authentication details in `serv.py` if required.

- **Client UI Customization**:
  - Adjust layout and functionality in `main.py` based on specific needs.
  - Modify UI elements in `main.py` to enhance user experience.

## Additional Notes

- Ensure firewall settings allow incoming and outgoing connections on the FTP server port (default: 21).
- This project is intended for educational purposes and may require additional security hardening for production environments.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
