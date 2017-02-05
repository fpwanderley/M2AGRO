# -*- coding: utf-8 -*-


class CustomExceptions(Exception):

    def __repr__(self):
        return (self.message)


class InvalidMonthORYear(CustomExceptions):

    def __init__(self, *args, **kwargs):

        ERROR_MESSAGE = "Número de Mês ou Ano inválido."

        super(InvalidMonthORYear, self).__init__(ERROR_MESSAGE)
