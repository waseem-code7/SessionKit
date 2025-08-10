import uuid

from sessions_kit.id_generators.base import SessionIDGenerator


class SecureRandomGenerator(SessionIDGenerator):
    """UUID-based session ID generator"""

    def generate(self) -> str:
        return str(uuid.uuid4())