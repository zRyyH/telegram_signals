import telebot


class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

        if not self.bot_token or self.bot_token == "SEU_TOKEN_AQUI":
            raise ValueError("❌ Configure o bot_token no arquivo config.json")

        if not self.chat_id or self.chat_id == "SEU_CHAT_ID_AQUI":
            raise ValueError("❌ Configure o chat_id no arquivo config.json")

        self.bot = telebot.TeleBot(self.bot_token)

    def enviar_mensagem(self, mensagem: str):
        try:
            self.bot.send_message(self.chat_id, mensagem)
            return True
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
            return False
