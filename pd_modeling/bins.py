import sys

# ESTOS BINS SON LOS DE LA CLASE, TENEMOS QUE CREAR LOS NUESTROS (NO SE COMO)
bins = {
    "customer_age": [
        {
            "label": "(-inf, 37)",
            "max": 37
        },
        {
            "label": "(37, 40)",
            "max": 40
        },
        {
            "label": "(40, 46)",
            "max": 46
        },
        {
            "label": "(46, 58)",
            "max": 58
        },
        {
            "label": "(58, inf)",
            "max": sys.maxsize
        },
    ],
    "months_at_address": [
        {
            "label": "(-inf, 23)",
            "max": 23
        },
        {
            "label": "(23, 83)",
            "max": 83
        },
        {
            "label": "(83, inf)",
            "max": sys.maxsize
        },
    ],
    "income": [
        {
            "label": "(-inf, 29000)",
            "max": 29000
        },
        {
            "label": "(29000, 33000)",
            "max": 33000
        },
        {
            "label": "(33000, 42000)",
            "max": 42000
        },
        {
            "label": "(42000, 47000)",
            "max": 47000
        },
        {
            "label": "(47000, inf)",
            "max": sys.maxsize
        },
    ],
    "months_with_bank": [
        {
            "label": "(-inf, 12)",
            "max": 12
        },
        {
            "label": "(12, 45)",
            "max": 45
        },
        {
            "label": "(45, 71)",
            "max": 71
        },
        {
            "label": "(71, inf)",
            "max": sys.maxsize
        },
    ],
    "balance": [
        {
            "label": "(-inf, 558)",
            "max": 558
        },
        {
            "label": "(558, 1254)",
            "max": 1254
        },
        {
            "label": "(1254, 1597)",
            "max": 1597
        },
        {
            "label": "(1597, inf)",
            "max": sys.maxsize
        },
    ]
}