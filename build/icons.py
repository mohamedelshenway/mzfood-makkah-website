# -*- coding: utf-8 -*-
"""Minimal inline SVG icons (stroke, currentColor) — no icon font/library needed."""

def icon(name, size=24):
    paths = {
        "home": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/>',
        "chef": '<path d="M6 13a4 4 0 0 1 3-6.5A4 4 0 0 1 12 4a4 4 0 0 1 3 1.5A4 4 0 0 1 18 13"/><path d="M6 13h12v3a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3z"/><path d="M9 19h6"/>',
        "truck": '<rect x="1.5" y="7" width="13" height="9"/><path d="M14.5 10h4l4 4v2h-8z"/><circle cx="6" cy="18.5" r="1.6"/><circle cx="17.5" cy="18.5" r="1.6"/>',
        "users": '<circle cx="9" cy="8" r="3.2"/><path d="M2.5 20c0-4 3-6.5 6.5-6.5S15.5 16 15.5 20"/><circle cx="17" cy="9" r="2.6"/><path d="M15.7 13.6c2.6.4 4.3 2.5 4.3 6.4"/>',
        "whatsapp": '<path d="M4 20l1.3-4A8 8 0 1 1 9 19l-5 1z"/><path d="M8.2 9.6c.2 2.6 2.8 5.2 5.4 5.4.6 0 1.7-.1 1.9-.7.2-.5 0-1.9-.3-2.1-.3-.2-1.4-.7-1.7-.5-.2.1-.5.7-.7.8-.5.1-1.3-.4-1.9-1s-1.1-1.4-1-1.9c.1-.2.7-.5.8-.7.2-.3-.3-1.4-.5-1.7-.2-.3-1.6-.5-2.1-.3-.5.3-.6 1.3-.6 1.9z" fill="currentColor" stroke="none"/>',
        "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2C9.5 21 3 14.5 3 6a2 2 0 0 1 2-2z"/>',
        "pin": '<path d="M12 22s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/>',
        "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1"/>',
        "check": '<path d="M20 6L9 17l-5-5"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
        "map": '<path d="M9 3L3 6v15l6-3 6 3 6-3V3l-6 3-6-3z"/><path d="M9 3v15M15 6v15"/>',
        "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
        "star": '<path d="M12 3l2.6 5.7 6.2.6-4.7 4.1 1.4 6.1L12 16.7 6.5 19.5l1.4-6.1-4.7-4.1 6.2-.6z"/>',
    }
    d = paths.get(name, "")
    fill = "none"
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill}" '
            f'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{d}</svg>')
