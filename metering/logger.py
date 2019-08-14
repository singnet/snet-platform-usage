import logging.config


def setup_logger():
    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            }

            # "info_file_handler": {
            #     "class": "logging.handlers.RotatingFileHandler",
            #     "level": "INFO",
            #     "formatter": "simple",
            #     "filename": "info.log",
            # },
            #
            # "error_file_handler": {
            #     "class": "logging.handlers.RotatingFileHandler",
            #     "level": "ERROR",
            #     "formatter": "simple",
            #     "filename": "error.log",
            #     "encoding": "utf8"
            # }
        },

        "loggers": {
            "sqlalchemy": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": "no"
            },
            "freecall_handler": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": "no"
            },
            "": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": "no"
            }
        },

        "root": {
            "level": "ERROR",
            "handlers": ["console"]
        }
    })
