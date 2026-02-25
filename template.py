# app/messaging/templates.py
TEMPLATES = {
    "D_MINUS_7": "Olá, {first_name}! Tudo bem? 😊\n"
                 "Passando pra lembrar que sua mensalidade de R$ {amount} vence em {due_date}.\n"
                 "Quer que eu te envie o Pix agora?",

    "D_MINUS_2": "Oi, {first_name}! Lembrete rápido: vence em {due_date} (R$ {amount}).\n"
                 "Pix copia e cola:\n{pix}\n"
                 "Se preferir, posso mandar link também: {link}",

    "D0": "Olá, {first_name}! Sua mensalidade vence hoje ({due_date}).\n"
          "Valor: R$ {amount}\n"
          "Pix:\n{pix}\n"
          "Link: {link}",

    "D_PLUS_3": "Oi, {first_name}. Vi que ainda ficou pendente desde {due_date} (R$ {amount}).\n"
                "Você prefere: pagar hoje, reagendar ou parcelar?",

    "PAID": "Pagamento confirmado ✅\n"
            "Obrigado, {first_name}! Qualquer coisa, estou por aqui.",

    "ASK_RECEIPT": "Perfeito, {first_name}! Você consegue me enviar o comprovante aqui pra eu confirmar?"
}
