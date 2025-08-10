# SessionKit

## Class Diagram
![alt text](https://i.postimg.cc/G3F9bf8W/Screenshot-2025-08-10-at-11-56-28-PM.png)

## Usage
```python
from sessions.core import SessionManager
from sessions.config import SessionConfig

config = SessionConfig()
sessionManager = SessionManager(config)
```

Initialize SessionConfig with params
```python
from sessions.core import SessionManager
from sessions.config import SessionConfig
config = config = SessionConfig(
    store=RedisStore(host="localhost", port=6379, db=0, cluster_nodes=None),  # Backend store for session data
    serializer=JSONSerializer(),  # Handles serialization of session data
    id_generator=SecureRandomGenerator(),  # Generates unique session IDs
    ttl_in_sec=86400,  # Session time-to-live in seconds
    cookie_name="session_id",  # Name of the session cookie
    cookie_max_age=86400,  # Max age of the cookie in seconds
    cookie_path="/",  # Path scope of the cookie
    cookie_domain=None,  # Domain for which the cookie is valid
    cookie_secure=True,  # Cookie only sent over HTTPS
    cookie_httponly=True,  # Cookie not accessible via JavaScript
    cookie_samesite="lax",  # Controls cross-site cookie behavior
    rolling=False,  # Whether to reset expiry on every request
    increase_interval_on_touch=10000,  # Interval for extending TTL on touch (if rolling is True)
    save_uninitialized=False  # Save new sessions that are unmodified
)
sessionManager = SessionManager(config)
```
