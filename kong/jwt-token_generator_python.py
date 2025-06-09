import jwt
import time

payload = {
    "iss": "mykey",
    "exp": int(time.time()) + 3600  # 1 hour expiry
}

token = jwt.encode(payload, "mysecret", algorithm="HS256")
print(token)

