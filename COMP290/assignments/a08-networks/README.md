# Python Sockets and HTTP | Coursework

[Research portfolio](https://github.com/ecedegirmen/research-portfolio) · [Repository directory](https://github.com/ecedegirmen/research-portfolio/blob/main/docs/repository-directory.md)

**Context:** COMP 290 networking exercise  
**Tools:** Python standard library (`socket`)

This exercise explores DNS resolution, TCP connections, and sending a basic HTTP GET request.

## Files

| File | Purpose |
| --- | --- |
| [main.py](main.py) | Original exercise scaffold and instructions |
| [answer.py](answer.py) | Answer script that resolves the hostname, connects on port 80, and prints the response |

## Run the answer script

With Python 3 and network access:

```bash
python3 answer.py
```

The script uses a plain HTTP connection and reads one response chunk of up to 8,192 bytes. It is a learning example, not a general-purpose web client; HTTPS and complete response handling are outside its scope.

The repository retains the supplied course scaffold alongside my answer.
