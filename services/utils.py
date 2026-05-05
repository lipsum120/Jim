from core.exceptions import NotFound

def get_or_404(entity, name: str = "Entity"):
    if not entity:
        raise NotFound(f"{name} not found")
    return entity
    