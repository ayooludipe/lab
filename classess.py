class Television:
    """
    Class showing details for a remote control object
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor that creates the initial state of the tv remote control object
        sets channel and volume to their minimums and status to off
        :return: None
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        This is the method that sets the tv on or off
        :return: None
        """
        if self.__tv_status == False:
            self.__tv_status = True
        elif self.__tv_status == True:
            self.__tv_status = False

    def channel_up(self) -> None:
        """
        Method to go up the channel of the TV object by one
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to go down the channel of the TV object by one
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase the volume of the TV object by one
        :return: None
        """
        if self.__tv_status == True:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume of the TV object by one
        :return: None
        """
        if self.__tv_status == True:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def get_channel(self) -> int:
        """
        Method to gets channel value
        :return: Channel (int)
        """
        return self.__channel

    def get_volume(self) -> int:
        """
        Method to get volume value
        :return: Volume (int)
        """
        return self.__volume

    def __str__(self) -> str:
        """
        This Method returns the current state of the TV object
        :return: The status, channel, and volume of the TV object
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
