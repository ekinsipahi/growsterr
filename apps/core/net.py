"""Request helpers shared by the apps."""
import ipaddress


def _ip(value):
    try:
        return str(ipaddress.ip_address((value or "").strip()))
    except ValueError:
        return None


def client_ip(request):
    """The visitor's IP address: the first entry of X-Forwarded-For (Render's proxy sets it),
    else REMOTE_ADDR. None when neither holds a valid address, so a malformed header never
    reaches a GenericIPAddressField. Used for rate limits and dispute evidence."""
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if forwarded:
        ip = _ip(forwarded.split(",")[0])
        if ip:
            return ip
    return _ip(request.META.get("REMOTE_ADDR"))
