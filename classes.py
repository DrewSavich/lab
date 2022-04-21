class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default variables of the class
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> Boolean:
        """
        Method that sets 'power' to on or off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def channel_up(self):
        """
        Method used to increase the channel. Resets to 'MIN_CHANNEL'
        if the value goes above 'MAX_CHANNEL'.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method used to decrease the channel. Resets to 'MAX_CHANNEL'
        if the value goes below 'MIN_CHANNEL'.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method used to increase the volume. Does not go above
        'MAX_VOLUME'.
        """
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Method used to decrease the volume. Does not go above
        'MIN_VOLUME'.
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Method used to display the status of all variables in
        the class.
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
