from gi.repository import Gtk
from lutris.gui.dialogs import Dialog
from lutris.gui.widgets.log_text_view import LogTextView


class LogDialog(Dialog):
    def __init__(self, title=None, buffer=None, parent=None):
        # XXX Setting the parent attribute makes the log window stick to the
        # main window, while this doesn't happen with other types of dialogs.
        super().__init__(title, None, 0, ("_OK", Gtk.ResponseType.OK))
        self.set_size_request(640, 480)
        self.grid = Gtk.Grid()
        self.buffer = buffer
        self.logtextview = LogTextView(self.buffer)

        scrolledwindow = Gtk.ScrolledWindow(
            hexpand=True, vexpand=True, child=self.logtextview
        )
        self.vbox.add(scrolledwindow)
        self.show_all()
