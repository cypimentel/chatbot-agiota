# app/messaging/renderer.py
from datetime import date

def money_br(v: float) -> str:
    # formatação simples pt-BR
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def date_br(d: date) -> str:
    return d.strftime("%d/%m/%Y")

def first_name(full_name: str) -> str:
    return (full_name.split()[:1] or [""])[0].title()

def render(template: str, *, full_name: str, amount: float, due_date: date, pix: str | None, link: str | None) -> str:
    return template.format(
        first_name=first_name(full_name),
        amount=money_br(amount),
        due_date=date_br(due_date),
        pix=pix or "(Pix ainda não disponível)",
        link=link or "(link ainda não disponível)",
    )
