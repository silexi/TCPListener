
# TCPListener

## Project Description

TCPListener is a simple TCP server that binds to a specified IP address and port. It listens for incoming TCP connections, receives data from clients, and processes it. The project consists of two Python scripts: `main.py` to start the listener and `listenport.py` to handle the TCP connection and data processing.

## Project Structure

- **main.py**: The entry point of the application, responsible for initiating the TCP listener.
- **listenport.py**: Contains the logic for setting up the TCP server, accepting connections, and handling data received from clients.

## Features
- Listens on a specified IP address and port.
- Handles multiple client connections.
- Receives and processes incoming data.
- Automatically closes connections after data is received.

## Technologies Used
- Python 3
- `socket` library (for networking)
- `select` library (for managing multiple connections)

## Installation Steps

1. **Clone the repository:**
   - Clone this repository to your local machine.

2. **Running the Script:**
   - Start the TCP listener by running:
     ```sh
     python main.py
     ```

   - The `main.py` script will start the listener on `127.0.0.1` (localhost) by default.

3. **Customizing IP and Port:**
   - You can customize the IP and Port by modifying the `main.py` script:
     ```python
     LP.start(IP="your_ip_address", PORT=your_port_number)
     ```
   - Replace `"your_ip_address"` and `your_port_number` with the desired IP and port.

## Example Usage

1. **Start the TCP Listener:**
   - By default, the listener will start on `127.0.0.1:443`.
   - You can connect to it using any TCP client, send data, and observe the server processing the data.

2. **Data Reception and Processing:**
   - The listener will print out received data and wait for a semicolon (`;`) to indicate the end of the data stream.
   - Once all data is received, the connection will close.

## Potential Enhancements
- Add support for SSL/TLS to secure the connection.
- Implement logging for better debugging and monitoring.
- Allow configuration via command-line arguments instead of hardcoding IP and port.

## Support and Contact
If you have any questions or suggestions, feel free to contact the project maintainer at [kilicbartu@gmail.com](mailto:kilicbartu@gmail.com).
