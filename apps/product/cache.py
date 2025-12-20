import hashlib
from django.core.cache import cache

PRODCUST_VER_KEY = 'products:ver'

def get_products_ver() -> int:
    ver = cache.get(PRODCUST_VER_KEY)

    if ver is None:
        cache.set(PRODCUST_VER_KEY, 1 ,timeout=None)
        return 1
    return int(ver)

def bump_products_ver() -> None:
    try:
        cache.incr(PRODCUST_VER_KEY)
    except Exception:
        cache.set(PRODCUST_VER_KEY, 2, timeout=None)

def build_cache_key(prefix : str, request) -> str:
    raw = request.get_full_path().encode("utf-8")
    h = hashlib.md5(raw).hexdigest()
    ver = get_products_ver()
    return f"{prefix}:v{ver}:{h}"