# SessionKit
A robust session management library for FastAPI that supports Redis-based storage with customizable session configuration. It features secure cookie handling, pluggable ID generation, and optional rolling sessions for flexible state management.

## Current Version
0.1

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
    rolling=False,  # Whether to reset expiry on every request (adds increase_interval_on_touch to exipiry time)
    increase_interval_on_touch=10000,  # Interval for extending TTL on touch (if rolling is True)
    save_uninitialized=False  # Save new sessions that are unmodified
)
sessionManager = SessionManager(config)
```

Use session object like a dictionary
```python
@router.post("/v1/login", status_code=status.HTTP_200_OK)
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(),  auth_service: AuthService = Depends(get_auth_service)):
    try:
        session: Session = request.state.session
        response = auth_service.verify_credentials(form_data.username, form_data.password)
        session["user"] = response.get("user")
        return {"Status": "Success"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=str(e))

@router.post("/v1/logout", status_code=status.HTTP_200_OK)
def logout(request: Request):
    try:
        session: Session = request.state.session
        session.destroy()
        return {"Status": "Success"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=str(e))
