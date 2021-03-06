import logging
import coloredlogs
from .handlers import slack


class Gytrash(logging.Logger):
    def __init__(self, name):
        super(Gytrash, self).__init__(name)

    def setup_logging(
        self,
        *,
        log_level: int = 10,
        log_from_botocore: bool = False,
        log_to_slack: bool = False,
        slack_log_channel: str = None,
        slack_log_level: int = 20,
    ) -> None:
        """ Create the Logging handler for the CLI. This setups a log handler that support logging in color.

        Args:
            log: Root logging object.
            log_level: int - (keyword) console streamhandler log level
            log_from_botocore: bool - (keyword) Add botocore Logger if using boto
            log_to_slack: bool - (keyword) Add custom streamhandler to log to slack channel
            slack_log_channel: str - (keyword) Name of the slack channel to send logs
            slack_log_level: inf - (keyword) slack streamhandler log level
        Returns:
            None
        """

        log_format = (
            "%(asctime)s %(name)s[%(process)d] %(module)s: %(levelname)s %(message)s"
        )

        generic_formatter = logging.Formatter(log_format)

        coloredlogs.install(level=log_level, logger=self, fmt=log_format)
        self.debug(f"runway log level: {self.getEffectiveLevel()}")

        if log_from_botocore:
            self.debug("Tapping Botocore logger.")
            coloredlogs.install(
                level=log_level, logger=logging.getLogger("botocore"), fmt=log_format
            )

        if log_to_slack:
            sh = slack.SlackHandler(slack_log_channel)
            sh.setFormatter(generic_formatter)
            sh.setLevel(slack_log_level)
            self.addHandler(sh)

