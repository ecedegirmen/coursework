import socket

hostname = "example.net"

# Do not modify this function
def make_http_request(ip, port):
  global hostname
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((ip, port))
  client.send(
      bytes(f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n", encoding="utf-8"))
  response = client.recv(8192)
  return response.decode()


# Write your code below here for A08
# Note: You shouldn't need to import anything else besides socket which is already included

# 1- Firstly, find the function to return an ip address from whatever the hostname is
# (This variable is defined at the top of this file if you want to play with it)
# Hint: This is meant for you to use Google to figure out.


# 2- Next, call make_http_request with the correct parameters and then print the response
# Note: This response should look a lot like the in-class example of "curl", and start with
# "HTTP/1.1 200 OK". Rememeber, we're making an HTTP request, so from that you should
# be able to figure out what port to use.


# ANSWER - Using "example.net"
ip = socket.gethostbyname(hostname)

port = 80 # default for all websites

response = make_http_request(ip, port)
print(response)


