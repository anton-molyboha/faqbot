from maubot import Plugin, MessageEvent
from maubot.handlers import command
from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper


class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("command_prefix")
        helper.copy("entries")


class FAQBot(Plugin):
    @classmethod
    def get_config_class(cls) -> type[BaseProxyConfig]:
        return Config

    async def start(self) -> None:
        self.config.load_and_update()
        self.log.info("Starting an instance with command prefix %s and %d entries",
                      self.config["command_prefix"], len(self.config["entries"]))

    @command.new(name=lambda self: self.config["command_prefix"])
    @command.argument("entry", "FAQ entry name or alias", pass_raw=True)
    async def faq(self, evt: MessageEvent, entry: str):
        if entry is None or entry == "":
            await evt.reply("Usage: !faq topic-in-question")
            return
        if entry in self.config["entries"]:
            await evt.reply(self.config["entries"][entry])
        else:
            await evt.reply("I don't know anything about {}".format(entry))
