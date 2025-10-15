import re
from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()

@register.filter
def youtube_embed(value):
    """
    Converte URL do YouTube em URL para iframe embed.
    Funciona mesmo com parâmetros extras como listas ou start_radio.
    """
    parsed_url = urlparse(value)
    query = parse_qs(parsed_url.query)
    video_id = query.get('v')
    if video_id:
        return f"https://www.youtube.com/embed/{video_id[0]}?autoplay=0"
    # fallback para youtu.be
    match = re.search(r'youtu\.be/([\w-]+)', value)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}?autoplay=0"
    return ""
