import asyncio
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

class AdvancedComfyUIBot(ComfyUIBot):
    def __init__(self):
        super().__init__()
        self.setup_advanced_handlers()
    
    def setup_advanced_handlers(self):
        # Add more handlers for different models, styles, etc.
        self.application.add_handler(CommandHandler("models", self.list_models))
        self.application.add_handler(CommandHandler("style", self.style_command))
    
    async def list_models(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """List available models"""
        models = ["SD1.5", "SDXL", "Anime", "Realistic"]
        keyboard = [[model] for model in models]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Choose a model:",
            reply_markup=reply_markup
        )