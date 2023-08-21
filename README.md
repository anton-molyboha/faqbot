FAQ bot replies with a long answer when prompted with a short topic name. This helps users quickly answer
some frequently asked questions, by issuing a short command, like `!faq topic-in-question`.

Installation
=====

This is a [maubot](https://github.com/maubot/maubot) plugin. You will need to [install maubot](https://docs.mau.fi/maubot/usage/setup/index.html) first, then follow the instructions for [uploading plugins](https://docs.mau.fi/maubot/usage/basic.html#uploading-plugins).
You will find the packaged version of FAQ bot, `faqbot.mbp`, among the artifacts of the latest release.

Configuration
=====

A sample configuration is available in `base-config.yaml`. The configuration has two top-level parameters:
 - `command_prefix` defines the prefix that the bot will react to. By default, the prefix is "faq", so that the bot
   will reply to queries starting with `!faq `. 
 - `entries` defines a map of topic names to their long descriptions. 
   The sample config has an entry for topic "faq", that explains the role of this faqbot. Use it as an example to add
   as many topics as you want.

See also
=====

Other plugins may also do the job of an FAQ bot.
 - [reactbot](https://github.com/maubot/reactbot) responds to messages that match predefined rules.
 - [gifme](https://github.com/williamkray/maubot-gifme) saves gifs, memes, or optionally anything else someone has posted, associate tags with it, and then return it when those tags are called. 
 - See the [FAQ bot discussion](https://github.com/maubot/plugin-wishlist/issues/20) on the maubot plugin wishlist.