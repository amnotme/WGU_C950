class ColorPrinter:
    """
    A utility class for printing text with colored formatting in the console.

    The `ColorPrinter` class provides a set of color codes and formatting options
    to print text in various colors and styles. It uses ANSI escape sequences to
    apply the desired formatting in the console.

    Example usage:

    printer = ColorPrinter()
    printer.print_color("This is a red text", ColorPrinter.RED)
    printer.print_color("This is a bold blue text", ColorPrinter.BLUE + ColorPrinter.BOLD)
    printer.print_color("This is a yellow text", ColorPrinter.YELLOW)
    printer.print_color("This is an underlined green text", ColorPrinter.GREEN + ColorPrinter.UNDERLINE)
    printer.reset_color()  # Reset the formatting to default

    Note:
    - The color codes and formatting options provided by this class may not be supported
      in all terminal emulators or operating systems.

    """
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    YELLOW = "\033[1;33m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

    # Flag to enable ANSI colors. Ensure your system supports them before enabling it.
    USE_ANSI_COLORS = False

    def print_color(self, text: str, color_code: str, terminate_color: bool = True):
        """
        Prints the specified text with the provided color code.

        Args:
            text (str): The text to be printed.
            color_code (str): The color code to apply to the text.
            terminate_color (bool): Flag denoting if you would like to reset to original color
                NOTE: setting terminate to False will require that you terminate color explicitly.
        """
        if self.USE_ANSI_COLORS:
            if terminate_color:
                print(color_code + text + ColorPrinter.END)
            else:
                print(color_code + text)
        else:
            print(text)

    def reset_color(self):
        """
        Resets the text formatting to the default color.

        """
        if self.USE_ANSI_COLORS:
            print(ColorPrinter.END)
        else:
            pass
